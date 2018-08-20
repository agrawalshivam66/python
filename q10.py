a,b,c=eval(input("Enter the numbers "))
if a-b==c-a or a-c==b-a:  
     print(a,", ",b,", ",c," are in Arithmetic progression")
elif b-a==c-b or b-c==a-b:  
     print(a,", ",b,", ",c," are in Arithmetic progression")
elif c-a==b-c or c-b==a-c:  
     print(a,", ",b,", ",c," are in Arithmetic progression")     
else:
    print(a,", ",b,", ",c," are not in Arithmetic progression") 
