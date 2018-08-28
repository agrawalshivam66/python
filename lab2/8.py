sal=eval(input("Enter the salary in lakhs "))
sal*=100000
if sal>=0 and sal<=250000:
    amt=sal
elif sal>250000 and sal<=500000:
    amt=sal*0.05
elif sal>500000 and sal<1000000:
    amt=(250000*0.05)+(sal-500000)*0.2
else:
    amt=250000*0.05+(500000*0.2)+(sal-1000000)*0.3
print("Amount =" + str(amt/100000)+" lakhs")
