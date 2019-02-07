data = {100:['navneet',1234,1000,"sav"],101:['suraj',15734,1460,"cur"]}
#         V      V       V    V    V 
print("neme ",data[100][0],"\nbal ",data[100][2],"\ntyp ",data[100][3])
data[103]=['shubham',4321,500,'sav'] # adding a new a/c
print(data)
while(1):
    x=int(input("enter your a/c\n"))
    if(x in data.keys()):
        print("a/c exist")
        break
    else:
        print("a/c not found")    
print("welcone ",data[x][0])
while(1):
    y=int(input("enter pin\n"))
    if(y == data[x][1]):
        print("avl",data[x][2])
        break
    else:
        print("worng pin")
while(1):
    z=int(input("enter amt to withdrawl\n"))
    if(z <= data[x][2]):
        print("transaction is sucessful")
        data[x][2] = data[x][2] - z
        print("avl ", data[x][2])
        break
    else:
        print("unsufficient bal")
