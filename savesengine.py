import json
from sys import path
from util import *

# dict is a json data

# actually, you dont have to place ; in the end of every statement,
# that's just mine habbit. But that is useful if you want to learn
# another languages.

#CONFIG
saveFileName = "save_%ID%"
saveFileDir  = "saves"

def getSave(id : int) -> dict:
    fn = saveFileName.replace("%ID%", id); 
    pathtosave = f"{saveFileDir}/{fn}"; 

    isempty = True; 
    isjson = False; 
    f = open(pathtosave);   # open the file
    fileData = f.read();    # i reccomend to load the file data only once, and then close
    f.close();              # just for security reasons
    if fileData != "": isempty = False; 

    try: json.loads(fileData); isjson = True; 
    except Exception: 0  # you can use "0" not "pass"

    if isempty:
        f = open(pathtosave)
        f.write(emptySave())
        f.close()
    
    if isjson == False:
        f = open(pathtosave)
        f.write(emptySave())
        f.close()
        fileData = json.dumps(emptySave())

    jsonData = json.loads(fileData);                 # convert string json to dict json
    if jsonData["gameVersion"] < 0.1:                # check if save version is supported
        raise Exception("Unsupported game version")  # 
    if validateSave(jsonData) == False:              # check if save is valid
        raise Exception("Save is not valid!")        # 
    return jsonData;                                 # and then return the value! ^=^

def emptySave() -> dict:
    """Returns empty save data. Check the code for details."""
    return {
        "gameVersion": 0.1,
        "name": "",
        "xp": 0,
        "settings": {
            #no settings
        },
        "gameData": {
            "locationData": {
                "currentLocation": "non-existance",
                "step": -1,
                "timeEnter": -1
            },
            "money": 150,
            "xp": 5,
            "health": 100
        },
        "lastTimeVisit": getTimeStamp()
    }

def writeSave(save : dict, id : int) -> bool:
    """### Save your save data.\n
    ---\n
    Returns `True` if save saved successfully.\n
    Otherwise, you will get `False`."""

    if validateSave(save) == False:
        raise Exception("Save is not valid!")

    fn = saveFileName.replace("%ID%", id); 
    pathtosave = f"{saveFileDir}/{fn}";
    eraseFileContents(pathtosave)
    f = open(pathtosave)
    save["lastTimeVisit"] = getTimeStamp()
    
    try:
        f.write(save)
    except Exception:
        return False; 
    return True; 

def validateSave(save: dict) -> bool:
    """Checks if save is valid"""
    check1 = "gameVersion" in save and "name" in save and "xp" in save and "settings" in save and "gameData" in save and "lastTimeVisit" in save; 
    check2=False;check3=False;check4=False; 
    try:
        check2 = save["gameData"] is dict and save["settings"] is dict; 
        check3 = save["gameData"]["locationData"] is dict; 
        check4 = save["lastTimeVisit"] is float and save["gameVersion"] is float; 
    except Exception:
        return False; 
    return check1 and check2 and check3 and check4; 
