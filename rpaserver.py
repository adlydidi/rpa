from datetime import datetime
from getpass import getuser
from importlib.resources import path
import json, aiofiles, robot, yaml, uvicorn, sqlite3, sqldb as db, os
from socket import timeout
from fastapi import FastAPI, Request, Response,  HTTPException, File, UploadFile


app = FastAPI()


#### start service

@app.get("/")
async def read_root():
    return {"hello" : "hello RPA"}


#### 

# @app.get("/runrpa/")
# async def run_rpa():
#     logFile = open('mylog.txt', 'w') 
#     robot.run("tmp.robot",stdout=logFile)
#     return None


#### checks the json and run the robot
@app.post("/dp/")
async def get_body(request: Request):
    rpaStartTime = datetime.timestamp(datetime.now())
    with open('tmp.yaml', 'w') as f:
        fileName = ""
        ### converts to json to string
        try:
            jsonString = json.dumps(await request.json())
            ### Converts json to dict  
            jsonDict = json.loads(jsonString)
            hash_value = hash(jsonString)
            # print(hash_value)
            # print(jsonDict)
        except:
            raise HTTPException(status_code=404, detail="Not proper json")
        ### will remove the fileName before creating the YAML file 
        ### yaml file for executing robot variable need to be at the top level
        ### if the file name in not in the original json a below msg is returned
        # try:
        fileName = jsonDict['FileName']
        del jsonDict['FileName']
        # vigetUserfromDB(fileName)
        dbresult = db.read_data_from_db()
        print(dbresult[0][2])
        jsonDict['Username'] = dbresult[0][1]
        jsonDict['Password'] = dbresult[0][2]

        # print(robotUserName, robotPassword)
        # print(jsonDict)
        # except:
        #     raise HTTPException(status_code=404, detail="robot file not found")
        try:
            ### write yaml to tmp file
            yaml.dump(jsonDict, f)
        except:
            raise HTTPException(status_code=404, detail="Not able to create YAML")
        
        ### call the run rpa bot
        f.close()
        try:
            # print("running robot ... ")
            ### get the timestamp before rpa call
            rpaCallTime= datetime.timestamp(datetime.now())
            await run_rpabot(fileName, hash_value)

            # # print(rpaCallTime)
            # ### get the output.xml files timestamp from os
            # timesOutputXML = os.path.getmtime('output.xml')
            # # print(timesOutputXML)

            # ### raises error if cannot run robot
            # ### if rpa call time is greater than the output.xml --> the file was created from another run
            # if rpaCallTime > timesOutputXML: 
            #     raise Exception(".. cannot run ... ")

            with open((str(hash_value)+'.xml'), 'r') as xml:
                data = xml.read()
                # print(data)
                xml.close()
                return Response(content=data, media_type="application/xml")
        except:
            raise HTTPException(status_code=404, detail="cannot run robot")

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
async def run_rpabot(filename, filehash): 
    robotfilename = "./robotscripts/" + filename 
    filehash = str(filehash) + '.xml' 
    try:
        # robot.run_cli(['-Vtmp.yaml', filename], exit=False)
        robot.run(robotfilename, variablefile='tmp.yaml', output=filehash)
        try:
            os.remove('tmp.yaml')
        except:
            return {"Result" : "error"}
    except:
        raise HTTPException(status_code=404, detail="ERROR - cannot run robot")
    return None


# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


@app.post("/uploadfile/")
async def post_endpoint(in_file: UploadFile=File(...)):
    # ...
    async with aiofiles.open("./robotscripts/" + in_file.filename, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write

    return {"Result": "OK"}

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8881, timeout_keep_alive=300)