from fastapi import FastAPI, File, UploadFile
from typing import Optional
import robot
import serverstatus


app = FastAPI()


@app.get("/")
def read_root():
    return {"hello" : "hello RPA"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    print(q)
    return {"item_id": item_id, "q": q}

@app.get("/status/")
async def getStatus():
    # serverstatus.getStats()
    return serverstatus.getStats()


# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}

@app.get("/runrpa/")
async def run_rpa():
    logFile = open('mylog.txt', 'w') 
    robot.run("tmp.robot",stdout=logFile)
    return None

@app.get("/favicon.ico")
def favicon():
    return None