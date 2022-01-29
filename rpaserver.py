from distutils.log import ERROR
from fileinput import filename
import json
from fastapi import FastAPI, Request, Response
from typing import List, Optional
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

# @app.get("/runrpa/")
# async def run_rpa():
#     logFile = open('mylog.txt', 'w') 
#     robot.run("tmp.robot",stdout=logFile)
#     return None


#### checks the json and run the robot
@app.post("/dp/")
async def get_body(request: Request):
    with open('tmp.yaml', 'w') as f:
        fileName = ""
        ### converts to json to string
        try:
            jsonString = json.dumps(await request.json())
            ### Converts json to dict  
            jsonDict = json.loads(jsonString)
        except:
            return {"message" : "probably no proper json"}
        ### will remove the fileName before creating the YAML file 
        ### yaml file for executing robot variable need to be at the top level
        ### if the file name in not in the original json a below msg is returned
        try:
            fileName = jsonDict['FileName']
            del jsonDict['FileName']
            # print(jsonDict)
        except:
            return {"message" : "robot file name not found"}
        try:
            ### write yaml to tmp file
            yaml.dump(jsonDict, f)
        except:
            return {"message" : "Not able create the YAML file"}
        
        ### call the run rpa bot
        f.close()
        try:
            # print("running robot ... ")
            robotresponse = await run_rpabot(fileName)
            # print(robotresponse)
            ### raises error if cannot run robot
            if robotresponse['message'] == "ERROR": 
                raise Exception(".. cannot run ... ")
            with open('output.xml', 'r') as xml:
                data = xml.read()
                # print(data)
                xml.close()
                return Response(content=data, media_type="application/xml")
        except:
            return {"message" : "not able to run robot"}

        # try:
        #     with open('output.xml', 'r') as xml:
        #         data = xml.read()
        #         # print(data)
        #         xml.close()
        #         return Response(content=data, media_type="application/xml")

        # except:
        #     return {"message" : "cannot read XML"}
    return {"message" : "something went wrong perhaps ... "}

@app.get("/favicon.ico")
def favicon():
    return None


### dummy class for testing
def runrobot():
    robot.run("tmp.robot")
    return None

### read the yaml file
async def read_yaml():
    ### read the yaml file 
    with open('tmp.yaml', 'r') as r:
        ylist= yaml.load(r, Loader=yaml.FullLoader)
        print(ylist)

### run the robot        
async def run_rpabot(filename):
    try:
        robot.run_cli(['-Vtmp.yaml', filename], exit=True)
    except:
        return {"message" : "ERROR"}
    return None