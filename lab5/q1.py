def different():
    a=eval(input("Enter the sequence of numbers "))
    count=0
    for i in a:
        if a.count(i)>1:
           count+=1
    if count==0:
         print("All numbers are distinct from each other")
    else:
         print("All numbers are not distinct from each other")
different()
