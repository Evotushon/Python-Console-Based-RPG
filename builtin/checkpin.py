# checks if the pin is correct, else it reruns the function (recursion)
def check_pin(pin):
    imported_pin = int(input())
    if imported_pin == pin:
        pass
    # reruns the function everytime the user puts the wrong password
    else:
        print("Wrong PIN! Rerun the Program!")
        check_pin()
