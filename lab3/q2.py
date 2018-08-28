n=eval(input("Enter the number "))
nc=n
a=nc%10
nc//=10
b=nc%10
nc//=10
c=nc%10
sum=(a**3)+(b**3)+(c**3)
if sum==n:
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")
    
for i in range (100,1000):
    nc=i
    a=nc%10
    nc//=10
    b=nc%10
    nc//=10
    c=nc%10
    sum=(a**3)+(b**3)+(c**3)
    if sum==i:
        print(i," is an armstrong number")
    #else:
        #print(i," is not an armstrong number")
