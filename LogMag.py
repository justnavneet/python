"""encrypted permanent database :-- 'database.dir',sing in,sing up,delete account,log will save with real time and date"""
import pickle,getpass,os
from datetime import datetime
t=str(datetime.time(datetime.now()))
d=str(datetime.date(datetime.now()))
file= open('database.dir', 'rb')
data=pickle.load(file) 
file.close()
def readByDate(date,user):
    for log in data[user]['logs']:
        if log['date']==date:
            print('Time: '+log['time']+'\tlog: '+log['text'])
def pushData():
    database = open('database.dir', 'wb')
    pickle.dump(data,database)
    database.close()
    print("data is pushed !")
def readLog(user):
    while(True):
        otp=int(input("enter option as per choice\n1\tby date\n2\tall\n3\tlast\n4\t exit"))
        if(otp==1):
            readByDate(input("enter date in format like YYYY-MM-DD\n"),user)
        elif(otp==2):
            for log in data[user]['logs']:
                print('Time: '+log['time']+'\tDate: '+log['date']+'\nlog: '+log['text'])
        elif(otp==3):
            temp=len(data[user]['logs'])
            print('Time: '+data[user]['logs'][temp-1]['time']+'\tDate: '+data[user]['logs'][temp-1]['date']+'\nlog: '+data[user]['logs'][temp-1]['text'])
        elif(otp==4):
            os.system("cls")
            return
        else:
            print("worng choice")
def go(user):
    while(True):# main function
        otp=int(input("enter option as per choice\n1\twrite log\n2\tread log\n3\tback\n0\tdelete account\n"))
        if(otp==1):
            text=input("write yor log\n")
            data[user]['logs'].append({'date':d,'time':t,'text':text})
            pushData()
        elif(otp==2):
            readLog(user)
        elif(otp==3 or 'exit()'):
            os.system("cls")
            return 1
        elif(otp==0):
            if('delete'==input("if you want to delete account enter 'delete'\n")):
                del data[user]
                return 1
        else:
            print("worng choice")
def checkPass(data):
    """
    """
    fl = False ; fa = False ; fs = False ; fn = False
    l = len(data)
    if(l >= 5 and not(data.isspace())):
        fl = True
    if(data.upper() != data and data.lower() != data):# check presence of upper case and lower case
        fa = True
    for var in range(l):#  check presence of spicale char
        fs = not(data[var].isalpha()) and not(data[var].isnumeric())
        if(fs == True):
            break
    for var in range(l):
        fn = data[var].isnumeric()
        if(fn == True):
            break
    if(fl and fa and fs and fn):
        return True
    else:
        return False
def start():# main funtion
    
    while(True):
        otp=int(input("enter option as per choice\n1\tsing in\n2\tsing up\n3\texit\n"))
        if(otp==1):
            singin()
        elif(otp==2):
            singup()
        elif(otp==3):
            pushData()
            break
        else:
            print("worng choice")
def singup():
    while(True):
        x=(input("choose your username "))
        if(x=='exit()'):
            return
        if not (x in data.keys()):
            print("username is selected")
            break
        else:
            print("username is already taken try another one")
    print("Choose your password having at lest at least 5 characters with nospace\nAnd at least one upper case ,lower case and a spical char")
    while(True):
        password=getpass.getpass("enter password: ")
        if(password=='exit()'):
            return
        if(checkPass(password)):
            print("password is valid")
            temp=getpass.getpass("confirm password: ")
            if(password==temp):
                print("your account is successful created !")
                data[x]={'password': password, 'logs': [{'date':d,'time':t,'text':'I am successful created my account'}]}
                return None
            else:
                print("password not match !")
                continue
        else:
            print("password is not valid retry")
            continue
        os.system("cls")
        pushData()
def singin():
    while(True):
        user=input("enter your username: ")
        if(user=='exit()'):
            return
        if(user in data.keys()):
            pas=getpass.getpass("enter password: ")
            if(pas==data[user]['password']):
                if(go(user)):
                    break

            else:
                print("Worng password")
        else:
            print("username not exists")
    os.system("cls")
    return None
start()