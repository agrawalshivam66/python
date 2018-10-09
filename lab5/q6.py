def suffle():
    a=list(input("Enter the numbers ").split(","))
    l=len(a)
    a1=a[0:l//2]
    a2=a[l//2:l+1]
    a.clear()
    x=0
    y=0
    for i in range(0,l):
        if i%2==0:
            a.append(a1[x])
            x+=1
            
        else:
            a.append(a2[y])
            y+=1
    print(a)    
suffle()
