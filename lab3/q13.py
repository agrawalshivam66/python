def raman():
    n=eval(input("enter a number "))
    for i in range(1,n+1):
        for j in range(1,int((i**(1/3)))+1):
            for k in range(j,int((i**(1/3)))+1):
                if (j**3)+(k**3)==i:
                    for l in range(j+1,int((i**(1/3)))+1):
                        for m in range(l,int((i**(1/3)))+1):
                            if i==(l**3)+(m**3):
                                print(i)
raman()

