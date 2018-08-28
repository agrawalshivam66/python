n=int(input("Enter a number "))
if n%2==0:
    if n>0:
        n/=2
    else:
        n*=2
else:
     if n>0:
        n-=1
     else:
        n+=1
print("The value of number is ",n)
