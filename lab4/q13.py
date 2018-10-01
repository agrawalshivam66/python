def isprime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
    else:
        return 1

def twin_prime():
    for i in range(101,201):
        if isprime(i) and isprime(i+2):
            print("(",i,",",i+2,")",end=', ')

def twin_prime_first():
    c=1
    i=1
    while(c<=50):
        if isprime(i) and isprime(i+2):
            print("(",i,",",i+2,")",end=', ')
            c+=1
        i+=1
twin_prime()   
twin_prime_first()
