import math
a,b,c=eval(input("Enter the coefficients "))
d=(b*b)-(4*a*c)
if a!=0:
    x1=(-b+ math.sqrt(d))/(2*a)
    x2=(-b- math.sqrt(d))/(2*a)
    if d>0:
        print("Real Roots")
        print("The first root " + str(x1))
        print("The second root " + str(x2))
    elif d==0:
        print("Single Root")
        print("Repeated Roots= " + str(x1))
    else:
        print(f"Complex Roots {a}+i{b}")
else:
    print("Invalid input")
    
    
