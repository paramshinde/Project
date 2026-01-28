import os
import random
import datetime
from git import Repo

PROJECTS={
    '1':{
        "name":"Proj-1",
        "path":r"E:\AutoForge"
    },
    '2':{
        "name":"Proj-2",
        "path":r"E:\mindcraft"
    },
    '3':{
        "name":"Proj-3",
        "path":r"E:\Murf-AI"
    }
}
LEVELS={
    "1":("Low",2,3),
    "2":("Medium",5,10),
    "3":("High",10,15)
}