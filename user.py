import random
import string
import pyperclip as pc


class User:
    """class"""

    userList = []


def __init__(self, username, password):

    " magic  constructor method "

    self.username = username
    self.password = password

    self.isLoggedin = False


def CreateUser(username, password):
    """method"""

    newUser = User(username, password)
    return newUser


def login(self):
    print("logged in successfully")


def saveUser(self, username, password):
    "method"

    User.userList.append(self)


@classmethod
def displayUser(cls):
    return cls.userList


def deleteUser(self):
    User.userList.remove(self)


class Info:

    info_list = []

    @classmethod
    def verify_user(cls, username, password):

        aUser = ""
        for user in User.userList:
            if (user.username == username and user.password == password):
                aUser == user.username
                return aUser

    def __init__(self, account, username, password):
        """
        info to be stored
        """
        self.account = account
        self.username = username  #sjsjsj
        self.password = password

    def save_details(self):

        Info.info_list.append(self)

    def delete_info(self):

        Info.info_list.remove(self)

    @classmethod
    def createInfo(account,username, password):
        "creates new info"
        newInfo = Info(username, password)
        return newInfo

    def save_info(account,username, password):
        "save info in the list"
        return Info.display_info()

    def find_info(cls, account):
        "method that takes class name and returns the account name info"
        for info in cls.info_list:
            if info.account == account:
                return info
        print("Account not found")

    @classmethod
    def copy_password(cls, account):
        found_info = Info.find_info(account)
        pyperclip.copy(found_info.password)

    @classmethod
    def infoExist(cls, account):

        "checks if the info exists from the list"

        for info in cls.info_list:
            if info.account == account:
                return True
        return False

    @classmethod
    def display_info(cls):
        "returns all info in the list"
        return cls.info_list

    def generatePassword(stringLength=8):
        "generates a random password "

        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#"
        return ''.join(random.choice(password) for i in range(stringLength))

    def copypassword(parameter_list):
        """
        method that allows copying of password to keyboard
        """
        pass


def main():

    isTrue = True

    print(
        "Welcome to password Locker where you can manage your passwords and even generate new passwords."
    )
    while isTrue == True:
       
        print(
            "Please enter one to proceed:\n\n 1. ca for Create new Account\n 2. lg for login\n 3. ex for Exit"
        )
        shortCode = input("").lower().strip()
        if shortCode == "ca":
            print("Sign Up Account")
            print("*" * 20)
            print("Username:")
            username = input()
            while True:
                print(
                    "1. Type Tp to type your own password:\n  or \n 2. Gp for generating random password"
                )
                passwordOption = input().lower().strip()

                if passwordOption == 'tp':
                    print("Enter Your Password")
                    password = input("password\n")

                    break
                elif passwordOption == 'gp':
                     password = Info.generatePassword()
                     break
                else:
                    print("invalid pasword")

                User.CreateUser(username, password)
                User.saveUser(username, password)
                print("\n")

            print(
                f"Hello {username}, your account has been created successfully! \n Your password is: {password}"
            )

        elif shortCode == 'lg':
            print("*" * 50)
            print("Enter your username and password")
            print("*" * 50)

            print("Username")
            username = input()
            print("password")
            password = input()

            for user in User.userList:
                if username == user.username:
                    if user.password == password:
                        print(user.login())
                        
                else:
                        User.CreateUser(username, password)
                        User.saveUser(username, password)
                        print("\n")

                        print(
                                f"Hello {username}, your account has logged in successfully! \n Your password is: {password}"
                                )
            else:
                print("Create Account")
                break
                

    

    while True:
        print(
            "what do you want to do?\n  1. cc for create new info \n 2. ds for Display existing Info\n 3. fc for find a info \n 4. dc for Delete an existing info \n 5. ex-Exit application"
        )
        shortCode = input().lower().strip()

        if shortCode == 'cc':
            print("New info account")
            print("\n")

            print("Account Name example facebook")
            account = input().lower()

            print("Account username: ")
            username = input()

            print("password")
            password=input()
            Info.save_info(account,username,password)
            print('/n')
            print(
                f"Account info for: {account} - username: {username} - password:{password} created successfully"
               )
            print("/n")

           

        elif shortCode == "ds":
                print("Your info include: \n")
                for info in Info.info_list:
                    account = account
                    username = username
                    password = password
                    print(
                        f"Account name: {account}\n Account username: {username}\n Account password: {password}\n"
                    )
                else:
                    print("You have no saved info\n")

        elif shortCode == "fc":
            print("Enter the Account Name you want to search for")
            account = input().lower().strip()
            if Info.infoExist(account):
                searchAccount = Info.find_info(cls, account)
                print(
                    f"Account name: {searchAccount} password :{searchAccount.password}"
                )
            else:
                print("info does not exist\n")

        elif shortCode == 'dc':
            print("Account name you would like to delete?")
            account= input().lower().strip()
            if Info.infoExist(account):
                Info.deleteInfo(account)
                print("Account  deleted")

            else:
                print("Account doesnt exist")

        elif shortCode == 'ex':
            print("Goodbye...!")
            isTrue = False

        else:
            print("invalid")


main()