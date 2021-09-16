import json
import os
import re
import util

# dict is a json data

# actually, you dont have to place ; in the end of every statement,
# that's just mine habbit. But that is useful if you want to learn
# another languages.

#CONFIG
saveFileName = "save_%ID%" # saveFileName MUST include %ID%
saveFileDir  = "saves"
saveFileExt  = "json" # that doesn't really matter

def retrieveSaves() -> list[str]:
    if "%ID%" not in saveFileName: raise Exception("saveFileName MUST include %ID%!")
    savePattern = re.compile(saveFileName.replace("%ID%", "\d+")+f".{saveFileExt}")
    saves = []
    for root, dirs, files in os.walk(saveFileDir):
        for i in files:
            saves.append(savePattern.findall(i))
    return saves
        

def getSave(id : int) -> dict:
    fn = saveFileName.replace("%ID%", str(id)); 
    pathtosave = f"{saveFileDir}/{fn}"+f".{saveFileExt}"; 

    if "%ID%" not in saveFileName: raise Exception("saveFileName MUST include %ID%!")
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
    if validateSave(jsonData) == False:              # then check if the save is valid
        raise Exception("Save is not valid!")        # 
    if jsonData["gameVersion"] < 0.1:                # and check if the save version is supported
        raise Exception("Unsupported game version")  # 
    return jsonData;                                 # and after all of this, return the value! ^=^
    
def emptySave() -> dict:
    """Returns empty save data. Check the code for details."""
    if "%ID%" not in saveFileName: raise Exception("saveFileName MUST include %ID%!")
    return {
        "gameVersion": 0.1,
        "name": "",
        "xp": 0,
        "saveName": "$ej_k236",
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
        "lastTimeVisit": util.getTimeStamp()
    }

def writeSave(save : dict, id : int) -> bool:
    """### Save your save data.\n
    ---\n
    Returns `True` if save saved successfully.\n
    Otherwise, you will get `False`."""

    if "%ID%" not in saveFileName: raise Exception("saveFileName MUST include %ID%!")
    if validateSave(save) == False:
        raise Exception("Save is not valid!")

    fn = saveFileName.replace("%ID%", str(id)); 
    pathtosave = f"{saveFileDir}/{fn}"+f".{saveFileExt}"; 
    util.eraseFileContents(pathtosave)
    f = open(pathtosave, 'w')
    save["lastTimeVisit"] = util.getTimeStamp()
    
    try:
        f.write(json.dumps(save, indent=3))
    except Exception:
        f.close()
        return False; 
    f.close()
    return True; 

def validateSave(save: dict) -> bool:
    """Checks if save is valid"""
    if "%ID%" not in saveFileName: raise Exception("saveFileName MUST include %ID%!")
    check1 = "gameVersion" in save and "name" in save and "xp" in save and "settings" in save and "gameData" in save and "lastTimeVisit" in save; 
    return check1