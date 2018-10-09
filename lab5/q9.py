a=[]
n = eval(input("Enter the number "))
for i in range(1,n+1):
    a.append(i)
del a[1::2]
i=1
while(a[i]<len(a)):   
    del a[a[i]-1::a[i]]
    i+=1
print(a)        
    
