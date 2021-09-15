# checks if the pin is correct, else it reruns the function (recursion)
def check_pin(pin):
    try:
        imported_pin = int(input())
        if imported_pin == pin:
            pass
        # reruns the function everytime the user puts the wrong password
        else:
            print("Wrong PIN")
            check_pin(pin)
    except:
        print("You didn't enter a valid pin boss")
        check_pin(pin)