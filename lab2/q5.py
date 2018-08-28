a,b,c=eval(input("Enter the sides "))
if a==b and b==c:
    print("Equilateral triangle")
elif a==b!=c or a==c!=b or b==c!=a :
    print("Isosceles triangle")
else:
    print ("Scalene triangle")
