n=eval(input("Enter a number "))
sum=0
for j in range(1,(n//2)+1):
    if n%j==0:
        sum+=j
if sum==n:
    print(n," is a perfect number")
elif sum>n:
    print(n," is a abundant number")
else:
    print(n," is a deficient number")
