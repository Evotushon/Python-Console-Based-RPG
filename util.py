import time, json, sys, time, random, os, datetime
import savesengine, value, constant

# timestamps
def getTimeStamp() -> float:
    """
    Gets you current timestamp\n
    Note: timestamp is amount of seconds since Epoch\n
    ---
    Epoch was in `1 Jan 1970 00:00`
    """
    return time.time(); 
def getTimeStampNS() -> float:
    """
    Gets you current timestamp in nano seconds\n
    Note: timestamp is amount of seconds since Epoch\n
    ---
    Epoch was in `1 Jan 1970 00:00`\n
    A nanosecond is `one billionth of a second`.
    """
    return time.time_ns(); 

def saveAndExit(save : dict):
    """
    Saves a save and exits immediately.\n
    If save went wrong somewhy, it will ask user\n
    for further actions.
    """
    if savesengine.validateSave(save):
        result = savesengine.writeSave(save)
        if result: exit(0)
        if result==False:
            print("Save wasn't saved somewhy, exit anyway? (Y/n)")
            prompt = userChoice("", ["y", "n"])
            if prompt == "y": exit(0)
            if prompt == "n":
                print("Print json-formatted save so you can save it manually? (Y/n)")
                prompt = userChoice("", ["y", "n"])
                if prompt == "y": print(str(save).replace("\'", "\""))
                exit();

def eraseFileContents(path: str = ""):
    """Erase file contents that is determinied in `path` argument."""
    if path == "": raise Exception("It looks like you forgot to give me the path")
    open(path, "w").close()

def ask_restart():
    """Prints `value.plsrestart`"""
    print(value.plsrestart)
def check_pin(pin : int) -> None:
    """Check pin"""
    inputpin=-1;

    while inputpin == -1:
        try: inputpin = int(input(value.pincodeprompt.replace("%PINCODE%", str(pin)))) # .replace("%PINCODE%", pin) is doing the placeholder
        except Exception: print(value.pincodenotint)

    if inputpin != pin:
        print(value.pincodeswrong)
        sys.exit(pin-1)

def sleepforawhile(max : int = 2) -> None: 
    """Sleep for a while for making it more human-like"""
    time.sleep(random.randrange(0, max))


def percentual(max : int) -> int:
    """
    The Max value that you want to use should be the limit that is included\n
    Example: I want to do a probability within `1` and `100`, `100` included, so I write that `max` is `100`
    """
    #global perc # NEVER DO THAT. NEVER.
    return random.randrange(1, max+1)

def fancyPrint(out: str, end="\n", speed=0.05) -> None:
    """
    Prints a value to console, with a little delay between each letter\n
    Except space and `\\n`.
    """
    listt = list(out)
    for i in listt:
        print(i, end="")
        if i != "\n" or i != " ":
            time.sleep(random.uniform(0, speed))
    print(end=end)

def fastFancyPrint(out: str, end="\n") -> None:
    """
    Same as fancyPrint but faster.
    """
    listt = list(out)
    for i in listt:
        print(i, end="")
        if i != "\n" or i != " ":
            time.sleep(random.uniform(0, 0.01))
    print(end=end)


def userInput(prompt: str = "") -> str:
    """Get user input and then lowercase it"""
    return input(str).lower()

def dinput(fprint: bool = False) -> str:
    """Default user input(with fancy priny)"""
    fastFancyPrint(value.defaultprompt, end="")
    return userInput()

def userChoice(msg: str, choices: list, wrongchoice=value.wrongchoice) -> str:
    """
    Provides fast user choice interface.\n
    `msg` is the message you want the user to see,\n
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
    """
    `isint("abc")` -> `False`\n
    `isint("one23")` -> `False`\n
    `isint("123")` -> `True`\n
    `isint("З")` -> `False` (because its a cyrillic letter instead of number)
    """
    try:
        int(string); 
        return True; 
    except Exception:
        return False; 

def cls() -> None:
    """Runs `cls` cmd command if you are using windows nt."""
    if os.name == 'nt':
        os.system('cls')





def gamelogo():
    """Prints a game logo that determines in values.py"""
    cls()
    for i in value.logo.split("\n"):
        fancyPrint(i, speed=0.00001)
    print("                                    ", end="")
    time.sleep(0.75)
    fancyPrint("RPGame studios (C)", speed=0.3)
    time.sleep(5)
    cls()

def verbose(msg: str, msgend: str = "\n", saveLog: bool = True, cmdPrint: bool = False, fprint: bool = False):
    """
    msg = Message to write to verbose. Cannot be an empty str.\n
    msgend = End of the message. Used by both file and print.\n
    saveLog = save to log file.\n
    cmdPrint = if you want to print your message to console.\n
    fprint = use `fancyPrint` if true.\n
    """
    if msg == "": raise Exception("Message must contain data!")
    if saveLog:
        # Check if file name contains placeholder
        if ("%TIME%" in constant.LOGFILENAME) == False:
            raise Exception("constant.LOGFILENAME must contain %TIME%\n    constant.LOGFILENAME = " + constant.LOGFILENAME)

        # Generate time string & replace placeholder
        now = datetime.datetime.now()
        timestr = f"{now.hour}:{now.second}_{now.month}.{now.day}.{now.year}"
        fname = constant.LOGFILENAME.replace("%TIME%", timestr)
        fp = f"{constant.LOGFILESDIR}/{fname}.{constant.LOGFILEEXTN}"

        # Do file magic
        f = open(fp, "r", encoding="utf-8")
        buffer = f.read()
        f.close()
        f = open(fp, "w+", encoding="utf-8")
        f.write(buffer+msgend+msg)
        f.close()
        f=None # clean memory
    if cmdPrint:
        task_completed = False
        if fprint:
            fancyPrint(msg, end=msgend)
            task_completed = True
        if task_completed is False:
            print(msg)
            task_completed = True
