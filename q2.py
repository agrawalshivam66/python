a,b,c=eval(input("Enter three numbers "))
if a>b and a<c:
    print("the second largest number is ",a)
elif a>c and a<b:
    print("the second largest number is ",a)
elif b>a and b<c:
    print("the second largest number is ",b)
elif b>c and b<a:
    print("the second largest number is ",b)
elif c>a and c<b:
    print("the second largest number is ",c)
elif c>b and c<a:
    print("the second largest number is ",c)
else:
    print("Wrong input")
