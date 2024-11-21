import json

global currentGamblerAccount

def createAccount(newAccount):
    with open("gamblerAccounts.json", "r+") as file:
        file_data = json.load(file)
        file_data["gambler_accounts"].append(newAccount)
        file.seek(0)
        json.dump(file_data, file, indent = 4)


with open("gamblerAccounts.json", "r") as file:
    file_data = json.load(file)
    gamblerAccounts = file_data["gambler_accounts"]

def accountRegistration():
    registrationAttempt = "ongoing"
    while registrationAttempt != "success":
        registrationAttempt = "ongoing"
        accountUserReg = input("Please choose an account username ")
        accountPassReg = input("Please create an account password ")
        accountPassRegConfirm = input("Please re-enter your account password ")

        for i in range(len(gamblerAccounts)):
            while registrationAttempt == "ongoing":
                if gamblerAccounts[i]["account_username"] != accountUserReg:
                    if accountPassReg == accountPassRegConfirm:
                        print("Account has been made. Your username is", accountUserReg, "and your password is", accountPassReg)
                        print("Due to reasons im not working out rn, you have to end the program and start it again for the login to actually work with a just-made account")
                        registrationAttempt = "success"    
                    else:
                        print("Your passwords do not match, please try again")
                        registrationAttempt = "fail"
                        
                else:
                    print("This username is already taken, please try another")
                    registrationAttempt = "fail"

    if registrationAttempt == "success":
        accountInfo = {
        "account_username": accountUserReg,
        "account_password": accountPassReg,
        "balance": 20000
    }
    createAccount(accountInfo)


def accountLogin():
    loginAttempt = "ongoing"
    while loginAttempt != "success":
        loginAttempt = "ongoing"
        accountUserLogin = input("What is your account username? ")
        accountPassLogin = input("What is your account password? ")
        while loginAttempt == "ongoing":
            for i in range(len(gamblerAccounts)):
                if gamblerAccounts[i]["account_username"] == accountUserLogin:
                    if gamblerAccounts[i]["account_password"] == accountPassLogin:
                        global gamblerBalance
                        gamblerBalance = gamblerAccounts[i]["balance"]
                        global currentGamblerAccount
                        currentGamblerAccount = gamblerAccounts[i]["account_username"]
                        global accountArrayLocation
                        accountArrayLocation = i
                        print("Welcome back", accountUserLogin)
                        loginAttempt = "success"
                        break
                    else:
                        print("Incorrect Password")
                        loginAttempt = "fail"
                else:
                    print("Invalid Username")
                    loginAttempt = "fail"