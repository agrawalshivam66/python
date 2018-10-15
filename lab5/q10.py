def lucky():
    a=[]
    for i in range(1,201):
        a.append(i)
    del a[1::2]
    i=1
    while(a[i]<len(a)):   
        del a[a[i]-1::a[i]]
        i+=1
    return a

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=lucky()
for i in a:
    if is_prime(i):
        print(i,end=',')
