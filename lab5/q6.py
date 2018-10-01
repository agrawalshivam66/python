def suffle():
    a=list(input("Enter the numbers ").split(","))
    l=len(a)
    a1=a[0:l//2]
    a2=a[l//2:l+1]
    a.clear()
    print(a1)
    print(a2)
    f=0
    x=0
    y=0
    
    for i in range(1,l+1):
        if i%2==0:
            print(x)
            a.append(a1[x])
            x+=1
            f=1
        else:
            print(y)
            a.append(a2[y])
            y+=1
            f=0
        print(a)
suffle()
