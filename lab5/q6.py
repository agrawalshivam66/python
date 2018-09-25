def suffle():
    a=list(input("Enter the number "))
    l=len(a)
    a1=a[0:l//2]
    a2=a[l//2:l]
    a.clear()
    f=0
    x=0
    y=0
    for i in range(0,l):
        if f==0:
            a.append(a1[x])
            x+=1
            f=1
        else:
            a.append(a2[y])
            y+=1
            f=0
    print(a)
suffle()
