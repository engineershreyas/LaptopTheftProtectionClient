token = None
option = None
import networking

while option is not "1" or option is not "2":
    option = raw_input("Choose 1 for Login and 2 for Register, Press anything else to quit")
    if option is "1":
        localLogin()
    elif option is "2":
        localRegister()
    else:
        break

def localLogin():
    number = raw_input("What is your 10 digit phone number?")
    number = "+1" + number
    password = raw_input("What is your password?")
    token = networking.login(number, password)
    if token is not None:
        while True:
            status = networking.ping(number,token)
            if status is "alert" or status is "error":
                break
    else:
        print("Invalid Login")
        option = None

def localRegister():
    number = raw_input("What is your 10 digit phone number?")
    number = "+1" + number
    firstname = raw_input("What is your first name")
    lastname = raw_input("What is your last name")
    password = "x"
    confirm = "y"
    while password is not confirm:
        password = raw_input("What do you want your password to be?")
        confirm = raw_input("Confirm your password")
        if password is not confirm:
            print("Please enter matching passwords")
    success = networking.register(number, password, firstname, lastname)
    if success:
        localLogin()
    else:
        print("Register failed, please try again")
        localRegister()
