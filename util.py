import time, json, sys, time, random
import savesengine, value

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

def ask_restart(): print(value.plsrestart)
def check_pin(pin : int) -> None:
    inputpin=-1;

    while inputpin == -1:
        try: inputpin = int(input(value.pincodeprompt.replace("%PINCODE%", str(pin)))) # .replace("%PINCODE%", pin) is doing the placeholder
        except Exception: print(value.pincodenotint)

    if inputpin != pin:
        print(value.pincodeswrong)
        sys.exit(pin-1)
def sleepforawhile() -> None:
    time.sleep(random.randrange(0, 2))

# this is a method overload. check it out in google.
def sleepforawhile(max : int) -> None: 
    time.sleep(random.randrange(0, max))


def percentual(max : int) -> int:
    """
    The Max value that you want to use should be the limit that is included\n
    Example: I want to do a probability within `1` and `100`, `100` included, so I write that `max` is `100`
    """
    #global perc # NEVER DO THAT. NEVER.
    return random.randrange(1, max+1)

def fancyPrint(out: str) -> None:
    listt = list(out)
    for i in listt:
        print(i, end="")
        time.sleep(random.uniform(0, 0.05))
    print()