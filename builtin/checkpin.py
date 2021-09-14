# checks if the pin is correct, else it reruns the function (recursion)
def checkpin(pin):
    imported_pin = int(input())
    if imported_pin == pin:
        pass
    # reruns the program everytime the user puts the wrong password
    else:
        print("Wrong PIN! Rerun the Program!")
        checkpin()
