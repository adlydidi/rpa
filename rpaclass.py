from ast import keyword
from typing import List
from pydantic import BaseModel, json

class runRPA(BaseModel):
    robotFileName: str
    keyWordList: List[str]