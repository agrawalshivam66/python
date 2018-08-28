for i in range(1,9001):
    sum=0
    for j in range(1,(i//2)+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i," is a perfect number")
    elif sum>i:
        print(i," is a abundant number")
    elif sum<i:
        print(i," is a deficient number")
    else:
        print(i," is a Unknown number")
