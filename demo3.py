from random import randint
list=[]
for var in range(100):
    list.append(randint(10,500))
def pro(data):
    from math import log10
    size=len(data)
    data.sort()
    temp_l=data[0]
    temp_u=data[size-1]
    op={}
    val=(temp_u-temp_l)//int(1+3.322*log10(size))
    print(val)
    while(temp_l < temp_u):
        op[f'{temp_l}-{temp_l+val}']=0
        temp_l =temp_l+val
        
    for var in op:
        temp=var.split('-')
        temp[0]=int(temp[0])
        temp[1]=int(temp[1])
        for i in data:
            if(i>=temp[0]and i<temp[1]):
                op[var]=op[var]+1
    return op
list.sort()
print(list,"\n\n\n\n")
print(pro(list))