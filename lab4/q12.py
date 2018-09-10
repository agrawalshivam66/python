def polite_num(n):
    a=[]
    count=0
    for i in range(1,(n//2)+1):
        sum=0
        for j in range(i,(n//2)+1):
            a.append(j)
            sum+=j
            if sum>n:
                a.clear()
                break
            elif sum==n:
                print(a)
                count+=1
    if count==0:
        print(n,"is impolite number")
polite_num(32)           
            
            
            
