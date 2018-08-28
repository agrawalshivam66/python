n=eval(input("Enter a number "))
nc=n
sum=0
while nc>=0.1:
    d=nc%10
    nc=nc//10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
if sum==n:
    print(n," is a Strong number")
for i in range(1,30000):
    nc=i
    sum=0
    while nc>=0.1:
        d=nc%10
        nc=nc//10
        fact=1
        for j in range(1,d+1):
            fact*=j
        sum+=fact
    if sum==i:
        print(i," is a Strong number")
