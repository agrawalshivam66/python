a=[]
n = eval(input("Enter the number of elements "))
for i in range(0,n):
    x = eval(input("Enter the number "))
    a.append(x)
max_diff=max(a)-min(a)
print(max_diff)
    
