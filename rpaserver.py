from fastapi import FastAPI, File, UploadFile, Request
from typing import Optional
import robot
import serverstatus
import database as db
import yaml


app = FastAPI()



@app.get("/")
async def read_root():
    return {"hello" : "hello RPA"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    print(q)
    return {"item_id": item_id, "q": q}

@app.get("/status/")
async def getStatus():
    # serverstatus.getStats()
    ## get the status of the clients connected to server
    rows = db.selectAllClients()
    connJson = []
    for row in rows:
        ip = db.int2ip(row[1])
        myjson = {  "HostName" : row[0], 
                    "ClientIP" : ip,
                    "ClientStatus" : row[2]}
        connJson.append(myjson)
    return connJson

# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}

@app.get("/runrpa/")
async def run_rpa():
    logFile = open('mylog.txt', 'w') 
    robot.run("tmp.robot",stdout=logFile)
    return None


@app.post("/dp/")
async def get_body(request: Request):
    with open('tmp.yaml', 'w') as f:
        # print(yaml.dump(await request.json(),allow_unicode=True))
        yaml.dump(await request.json(), f)

    return await request.json()

@app.get("/favicon.ico")
def favicon():
    return None