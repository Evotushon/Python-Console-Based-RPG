import time, json, sys, time, random, os
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

def fancyPrint(out: str, end="\n", speed=0.05) -> None:
    listt = list(out)
    for i in listt:
        print(i, end="")
        if i != "\n" or i != " ":
            time.sleep(random.uniform(0, speed))
    print(end=end)

def fastFancyPrint(out: str, end="\n") -> None:
    listt = list(out)
    for i in listt:
        print(i, end="")
        if i != "\n" or i != " ":
            time.sleep(random.uniform(0, 0.01))
    print(end=end)


def userInput(prompt: str) -> str:
    return input(str).lower()

def userInput() -> str:
    return input().lower()

def dinput() -> str:
    fastFancyPrint(value.defaultprompt, end="")
    return userInput()

def userChoice(msg: str, choices: list, wrongchoice=value.wrongchoice) -> str:
    """
    Provides fast user choice. `msg` is the message you want the user to see,\n
    and the `choices` is the list of possible choices.
    """
    fastFancyPrint(msg)
    while True:
        ans = dinput()
        for i in choices:
            if ans == str(i):
                return ans;
        print(wrongchoice)

def isint(string: str) -> bool:
    try:
        int(string); 
        return True; 
    except Exception:
        return False; 

def cls() -> None:
    if os.name == 'nt':
        os.system('cls')





def gamelogo():
    cls()
    for i in value.logo.split("\n"):
        fancyPrint(i, speed=0.00001)
    print("                                    ", end="")
    time.sleep(0.75)
    fancyPrint("RPGame studios (C)", speed=0.3)
    time.sleep(5)
    cls()