data = input("enter your password\n")
fl = False ; fa = False ; fs = False ; fn = False
l = len(data)
if(l >= 5 and not(data.isspace())):
    fl = True
if(data.upper() != data and data.lower() != data):
    fa = True
for var in range(l):
    fs = not(data[var].isalpha()) and not(data[var].isnumeric())
    if(fs == True):
        break
for var in range(l):
    fn = data[var].isnumeric()
    if(fn == True):
        break
if(fl and fa and fs and fn):
    print("passwor is valid")
else:
    print("password is not valid")