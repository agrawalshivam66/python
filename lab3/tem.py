def four(n):
    store=[]
    while n!=1:
        temp=n
        sum=0
        while temp!=0:
            sum+=(temp%10)**2
            temp//=10
        n=sum
        if n in store:
            return False
        store.append(n)
    return True

print("Happy number from 1 - 1000 are: ")
for i in range(1,1001,1):
    check=four(i)
    if(check == True):
        print(i,end=", ")
