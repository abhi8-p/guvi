import os.path
import json
import re

##### CHECKING IF FILE EXISTS IF NOT CREATE A NEW FILE ####
if os.path.isfile('credentials.json'):
    print("file exists")
    pass

else:
    print("creatng new file")
    with open('credentials.json',"w") as fw:
        json.dump({"email":'password'},fw)
        pass

def validator(email,password):
    email_regex='^[A-Za-z0-9]+.*[A-Za-z0-9]+@[A-Za-z]+\.(com|in)$'
    pass_regex='^(?=.{5,16}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
    if(re.search(email_regex,email) == None or re.search(pass_regex,password) == None):
        return False
    else:
        return True

def forgot_password(email):
    with open ('credentials.json','r') as fr:
        data=json.load(fr)
    if email in data.keys():
        print("Your password is: ",data[email])
    else:
        print("Please enter a valid email")
    return True

def register():
    data={}
    val=False
    forgot=False
    email=input("Please Enter you EMAIL ID: ").strip().lower()
    password=input("Please Enter you PASSWORD: ").strip()
    isFileEmpty=False
    final_validator=validator(email,password)
    if(final_validator == False):
        print("Please Enter a valid EMAIL ID and PASSWORD")
        val=True
    else:
        with open("credentials.json","r") as fr:
            try:
                data=json.load(fr)
                print(data)
            except:
                isFileEmpty=True
        if not isFileEmpty:
            if email in data.keys():
                print("You already have an existing account")
                fp=input("If you want to recover your password Please enter 'Y': ").strip().lower()
                if(fp == 'y'):
                    forgot=forgot_password(email)
            else:
                data.update({email:password})
                with open ('credentials.json',"w") as fw:
                    json.dump(data,fw)
        else:
            data.update({email:password})
            with open ('credentials.json',"w") as fw:
                json.dump(data,fw)
    if(forgot):
        choice()
    elif val:
        pass
    else:
        print("Registration Sucessfull")


def login():
    forgot=False
    email=input("Please Enter you EMAIL ID: ").strip().lower()
    password=input("Please Enter you PASSWORD: ").strip()
    with open('credentials.json',"r") as fr:
        try:
            data=json.load(fr)
        except:
            pass
    if email in data.keys():
        if(password==data[email]):
            print("You are logging in...")
        else:
            print("You have entered wrong password")
            fp=input("If you want to recover your password Please enter 'Y': ").strip().lower()
            if(fp == 'y'):
                forgot=forgot_password(email)
    else:
        print("You are not registered with us")
        f=input("Press 'Y' if you would like to register: ").strip().lower()
        if f=='y':
            register()


def choice():
    log=input("Please enter 1 if you want to login, 2 if you want to Register, 3 for forgot password or 'N' to quit: ").strip()
    if(log=='1'):
        login()
    elif(log=='2'):
        register()
    elif(log=='3'):
        email=input("Please Enter your email: ").strip().lower()
        forgot_password(email)
    elif(log.lower()=='n'  ):
        print("Exiting....")
        pass
    else:
        print("Please enter a valid choice")

choice()