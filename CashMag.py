note =[2000,500,200,100,50,20,10,5,2,1]
num=[1,4,5,6,0,0,0,0,0,0]
def checkAmt():
    total=0
    for i in range(10):
        total = total + note[i]*num[i]
    return total
def pay(x):
    total=0
    for i in range(10):
        if((note[i]<=x)and(num[i] is not 0)):
                req=x//note[i]
                if(req<=num[i]):
                        x=x%note[i]
                        num[i]=num[i]-req
                        total=total+note[i]*req
                        print(note[i],"--> ",req)
                else:
                        print(note[i],"--> ",num[i])
                        total=total+note[i]*num[i]
                        x=x-num[i]*note[i]
                        num[i]=0
    if(total<x):
        print("appropriate change is not avl")

def start():
    data=int (input("enter amt "))
    if(data<=checkAmt()):
        pay(data)
    else:
        print("unsufficient bal")
    print(num)    
start()