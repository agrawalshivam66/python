#question 1
def perfect():
    n=eval(input("Enter a number "))
    sum=0
    for j in range(1,(n//2)+1):
        if n%j==0:
            sum+=j
    if sum==n:
        print(n," is a perfect number")
    elif sum>n:
        print(n," is a abundant number")
    else:
        print(n," is a deficient number")

def perfect_range():
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
