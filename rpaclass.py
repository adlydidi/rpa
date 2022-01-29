from ast import arguments, keyword
from typing import List
from xml.etree.ElementInclude import include
from pydantic import BaseModel, json
import robot

class runRPA(BaseModel):
    robotFileName: str
    keyWordList: List[str]


# robot.run("tmp.robot", options=['V tmp.yaml'])
# robot.run('tmp.robot', options=['Vtmp.yaml'])
robot.run_cli(['--rpa -Vtmp.yaml', 'tmp.robot'], exit=False)