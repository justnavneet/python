"""encrypted permanent database :-- 'database.dir',sing in,sing up,delete account,log will save with real time and date"""
import pickle,getpass
from datetime import datetime
file= open('database.dir', 'rb')      
data= pickle.load(file) 
file.close() 
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
def start():
    
    while(True):# main function
        otp=int(input("enter option as per choice\n1\tsing in\n2\tsing up\n3\texit\n"))
        if(otp==1):
            singin()
        elif(otp==2):
            singup()
        elif(otp==3):
            break
        else:
            print("worng choice")
def singup():
    while(True):
        x=(input("choose your username "))
        if not (x in data.keys()):
            print("username is selected")
            break
        else:
            print("username is already taken try another one")
    print("choose your password having at lest at least 5 characters with nospace\nand at least one upper case ,lower case and a spical char")
    while(True):
        password=getpass.getpass("enter password: ")
        if(checkPass(password)):
            print("password is valid")
            temp=getpass.getpass("confirm password: ")
            if(password==temp):
                print("your account is successful created !")
                t=str(datetime.time(datetime.now()))
                d=str(datetime.date(datetime.now()))
                data[x]={'password': password, 'logs': [{'date':d,'time':t,'text':'I am successful created my account'}]}
                return None
        else:
            print("password is not valid retry")
            continue
def singin():
    pass
start()
database = open('database.dir', 'wb') 
pickle.dump(data,database)                      
database.close()