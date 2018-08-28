a,b,c=eval(input("Enter the sides "))
s=(a+b+c)/2
import math
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area = ", area)
a1=2*area/a
print("Three altitude of given triangle:", a1,end=",")
a2=2*area/b
print(a2,end=",")
a3=2*area/c
print(a3)
