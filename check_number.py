def check_number(number):
    try:
        number = int(number)
    except ValueError:
        print("This was not a number. Try again!\n")
        return False
    
    return True
