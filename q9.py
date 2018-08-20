a,b,c=eval(input("Enter the numbers "))
if a==(b+c)/2 :
     print(a," is the mean of ",b," and ",c)
elif b==(a+c)/2:
     print(b," is the mean of ",a," and ",c)
elif c==(a+b)/2:
     print(c," is the mean of ",a," and ",b)
else:
    print("No number is mean of the other two")
