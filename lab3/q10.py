def prime(x):
    if x==1:
        return 1
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    else:
        return 1

def left_trun(n):
    while len(n)>1:
        n=n[1:len(n)]
        print(n)
        x=int(n)
        ck=prime(x)
        if ck==0:
            return 0
    return 1
        
def right_trun(n):
     while len(n)>1:
        n=n[0:len(n)-1]
        print(n)
        x=int(n)
        ck=prime(x)
        if ck==0:
            return 0
     return 1
    
def find():
    n=str(input("Enter the number "))
    pr=prime(int(n))
    lf=left_trun(n)
    rf=right_trun(n)
    if lf==1 and rf==0 and pr==1:
        print("Left truncate")
    elif lf==0 and rf==1 and pr==1:
        print("right truncate")
    elif lf==1 and rf==1 and pr==1:
        print("both right and left truncate")
    else:
        print("none")
  
find()
 
