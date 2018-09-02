def prime(x):
    if x==1:
        return 1
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    else:
        return 1
    
def prime_range():
    print("The prime numbers in range 100-200")
    for i in range (100,201):
        if prime(i)==1:
            print(i)

def first_prime():
    print("First 25 prime numbers are")
    c=0
    i=1
    while(c<25):
        if prime(i)==1:
            print(i)
            c+=1
        i+=1

prime_range()
first_prime()
