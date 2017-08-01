token = None
option = None
import networking
import time
import getpass

PING_INTERVAL = 2
VALID_NUMBER_LENGTH = 10

def localLogin():
    number = raw_input("What is your 10 digit phone number?\n")
    if len(number) != VALID_NUMBER_LENGTH:
        print("Invalid Phone Number")
        localLogin()
    number = "+1" + number
    password = getpass.getpass("What is your password?\n")
    token = networking.login(number, password)
    first = True
    success = (token != None)
    if success:
        print("Login successful, press Ctrl + C to exit pinging")
    while success:
        try:
            status = networking.ping(number,first,False,token)
            if first == True:
                first = False
            time.sleep(PING_INTERVAL)
        except KeyboardInterrupt:
            networking.ping(number,False,True,token)
            break
    else:
        print("Invalid Login")
        option = None

def localRegister():
    number = raw_input("What is your 10 digit phone number?\n")
    if len(number) != VALID_NUMBER_LENGTH:
        print("Invalid Phone Number")
        localRegister()
    number = "+1" + number
    password = "x"
    confirm = "y"
    while password != confirm:
        password = getpass.getpass("What do you want your password to be?\n")
        confirm = getpass.getpass("Confirm your password\n")
        if password != confirm:
            print("Please enter matching passwords\n")
    success = networking.register(number, password)
    if success:
        print("Registration successful, please login now\n")
        localLogin()
    else:
        print("Register failed, please try again\n")

while True:
    option = raw_input("Choose 1 for Login and 2 for Register, or press anything else to quit\n")
    if option == "1":
        localLogin()
    elif option == "2":
        localRegister()
    else:
        break
