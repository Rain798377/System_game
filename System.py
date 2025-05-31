import time
import sys

#Global Variables
firstTime = True
loggedIn = False
incorrectLogin = True
admin = False
n = 0
n1 = 0
i = 0



#Login Function
def loginAgain():
    loginAgainPrompt = input("Would you like to log in? (Y/n) ")
    if loginAgainPrompt.lower() in ["Y", "y"]:
        login()
    elif loginAgainPrompt.lower() in ["N", "n"]:
        print("Ok.")
        loginAgain()
    else:
        print("Powering off...")
        time.sleep(2)
        powerOn()

#Power on System
def powerOnInit():
    print("                 ▟█▙")
    print("                ▟███▙")
    print("               ▟█████▙")
    print("              ▟███████▙")
    print("             ▂▔▀▜██████▙")
    print("            ▟██▅▂▝▜█████▙")
    print("           ▟█████████████▙")
    print("          ▟███████████████▙")
    print("         ▟█████████████████▙") 
    print("        ▟███████████████████▙") 
    print("        ▟█████████▛▀▀▜████████▙ ") 
    print("       ▟████████▛      ▜███████▙ ") 
    print("      ▟█████████        ████████▙ ") 
    print("     ▟██████████        █████▆▅▄▃▂ ") 
    print("    ▟██████████▛        ▜█████████▙ ") 
    print("   ▟██████▀▀▀              ▀▀██████▙ ") 
    print("  ▟███▀▘                       ▝▀███▙ ") 
    print(" ▟▛▀                               ▀▜▙") 
    listx = ["██ 39%","███ 49%","████ 76%","█████ 89%","██████ 100%","       GENERATE DATA","              GENERATE OBJECT","                           GENERATE FUNCTION","                              COLLECTIONG DATA","                           DOING WORK","                    CONNECTING TO SERVER............","               CONNECTING TO SERVER DONE.............","      -------------------- S Y S T E M   S T A R T E D --------------------"]
    count = 0
    for c in listx:
        if count != len(listx):
            sys.stdout.write('\r' + c)
            time.sleep(1)
            count +=1
            sys.stdout.flush()
    print("\n")
    loginAgain()

def powerOn():
    powerOnPrompt = input("Power on System? (Y/n) ")
    if powerOnPrompt.lower() in ["Y", "y"]:
        powerOnInit()
    elif powerOnPrompt.lower() in ["N", "n"]:
        time.sleep(2)
        powerOn()
    else:
        powerOn()



#Run if logged in function 
def LoggedIn():
    sysInfo = input("1. Who is using the system \n 2. Shutdown \n 3. Is there an admin \n 4. Look at this menu again \n 5. Admin panel \n 6. Set current User as admin \n 7. Log out \n")
    if sysInfo.lower() in ["exit", "Exit", "EXIT"]:
        sys.exit()
    elif sysInfo.lower() in ["sudo -rm -rf", "sudo rm rf", "sudo rm"]:
        time.sleep(1.5)
        print("Deleting root...")
        #easter egg lollllllllllllll
        time.sleep(2)
        print("Done!")
        sys.exit()
    elif sysInfo.lower() == "1":
        print(User)
        LoggedIn()
    elif sysInfo.lower() == "2":
        print("Shutting down...")
        time.sleep(3)
        powerOn()
    elif sysInfo.lower() == "3":
        if admin == True:
            print("The admin on the system is: "+ User_admin)
            LoggedIn()
        else:
            print("There is no admin on the system!")
            LoggedIn()
    elif sysInfo.lower() == "4":
        LoggedIn()
    elif sysInfo.lower() == "5":
        if admin == True:
            askAdmin()
        elif admin == False:
            print(User + " does not have administrative properties!")
            LoggedIn()
        else:
            LoggedIn()
    elif sysInfo.lower() == "6":
        if admin is True:
            print("There is already an admin on the system!")
            LoggedIn()
        elif admin is False:
            adminUser()
    elif sysInfo.lower() == "7":
        print("Signing out...")
        time.sleep(1.2)
        print("Done!")
        time.sleep(1.2)
        loggedIn = False
        loginAgain()
    else:
        LoggedIn()

#cosmetic
print("Please log in")
time.sleep(1)


#login func
def login():
    User_input = input("Please input user: ")
    if User_input == User:
            User_password_input = input("Please input password: ")
            #int(User_password_input)
            if User_password_input == User_password:
                print("Welcome, " + User + "!")
                loggedIn = True
                LoggedIn()
    elif User_password_input != User_password:
        print("Incorrect User or Password!")
        login()
    elif ValueError or SyntaxError:
        print("Error: Please enter something from the ASCII table!")


#ask for admin
def adminUser():
    askAdmin = input("Set "+ User + " as admin? (Y/n) ")
    if askAdmin.lower() in ["Y", "y"]:
        global adminPass
        global admin
        global User_admin
        global n1
        adminPass = input("Please set up a admin password: ")
        print("Setting "+ User + " as admin...")
        time.sleep(1)
        print("Done!")
        User_admin = User
        admin = True
        login()
        n1 += 1
    elif askAdmin.lower() in ["N", "n"]:
        print("Skipping...")
        time.sleep(1)
        print("No admin on system.")
        admin = False
        login()
        n1 += 1



#ask for admin User and pass
def askAdmin():
    global AdminAskUser
    global AdminAskPass
    AdminAskUser = input("Please enter Admin User: ")
    if AdminAskUser == User_admin:
        AdminAskPass = input("Please enter Admin Password: ")
        if AdminAskPass == adminPass:
            print("Welcome to Admin Panel!")
            time.sleep(1.2)
            print("There is nothing to do here yet.")
            time.sleep(0.5)
            LoggedIn()
        elif AdminAskPass != adminPass:
            print("Incorrect Password!")
            time.sleep(1.2)
            askAdmin()
        else:
            askAdmin()
        

if firstTime is True:
    print("Welcome new user!")
    time.sleep(1)
    print("It looks like it's your first time using this program!")
    time.sleep(1.5)
    User = input("Please create a user: ")
    User_password = input("Please create a password: ")
    time.sleep(1)
    adminUser()
    firstTime = False
