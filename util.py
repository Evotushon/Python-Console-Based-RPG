import time
import savesengine
import json

# timestamps
def getTimeStamp() -> float:
    return time.time(); 
def getTimeStampNS() -> float:
    return time.time_ns(); 

def saveAndExit(save : dict):
    if savesengine.validateSave(save):
        result = savesengine.writeSave(save)
        if result: exit(0)
        if result==False:
            print("Save wasn't saved somewhy, exit anyway?")
            prompt = input("Y/n: ").lower()
            if prompt == "y": exit(0)
            if prompt == "n":
                print("Print json-formatted save so you can save it manually?")
                prompt = input("Y/n: ").lower()
                if prompt == "y": print(str(save).replace("\'", "\""))
                exit();

def eraseFileContents(path : str):
    open(path, "w").close()