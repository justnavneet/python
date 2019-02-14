#Program to check whether the year is leap year or not
def leap():
    year = int(input("Enter the year you want to check : "))   #enter the year 
    if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print(year,"is a leap year")    
                else:
                    print(year,"is not a leap year")    
            else:
                print(year,"is a leap year")     
    else:
        print(year,"is not a leap year")  

print("Program to check whether the year is leap year or not")
while(True):
    otp = int(input("enter 1 to continue 0 to exit \n"))      #want to check for more 
    if(otp==1):
        leap()
    else:
        break