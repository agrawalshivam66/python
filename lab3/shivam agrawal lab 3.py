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

#Question 2
def armstrong():
    n=eval(input("Enter the number "))
    nc=n
    a=nc%10
    nc//=10
    b=nc%10
    nc//=10
    c=nc%10
    sum=(a**3)+(b**3)+(c**3)
    if sum==n:
        print(n," is an armstrong number")
    else:
        print(n," is not an armstrong number")
        
    for i in range (100,1000):
        nc=i
        a=nc%10
        nc//=10
        b=nc%10
        nc//=10
        c=nc%10
        sum=(a**3)+(b**3)+(c**3)
        if sum==i:
            print(i," is an armstrong number")
        #else:
            #print(i," is not an armstrong number")
armstrong()

#question 3
def strong():
    n=eval(input("Enter a number "))
    nc=n
    sum=0
    while nc>=0.1:
        d=nc%10
        nc=nc//10
        fact=1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
    if sum==n:
        print(n," is a Strong number")
    for i in range(1,30000):
        nc=i
        sum=0
        while nc>=0.1:
            d=nc%10
            nc=nc//10
            fact=1
            for j in range(1,d+1):
                fact*=j
            sum+=fact
        if sum==i:
            print(i," is a Strong number")

#question 4
def four(n):
    store=[]
    while n!=1:
        temp=n
        sum=0
        while temp!=0:
            sum+=(temp%10)**2
            temp//=10
        n=sum
        if n in store:
            return False
        store.append(n)
    return True

print("Happy number from 1 - 1000 are: ")
count=0
for i in range(1,1001,1):
    check=four(i)
    if(check == True):
        count+=1
        print(i,end=", ")
print(count)

#question 5
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

#question 6
def fib_range(x):
    print("First fibonacci numbers in range 1-1000 are") 
    a=0
    b=1
    c=0
    while c<x:
        print(c,end=', ')
        c=a+b
        a=b
        b=c

def fib_first():
    print("First 25 fibonacci numbers are") 
    a=0
    b=1
    c=0
    count=0
    while count<25:
        print(c,end=', ')
        c=a+b
        a=b
        b=c
        count+=1
        
fib_range(1000)
fib_first()

#question 7
import math
def perfect_square(x):
    
    y=math.sqrt(x)
    y=int(y)
    if  y*y==x:
        return 1
    else:
        return 0

def square_free():
    count=0
    i=2
    print(1,end=',')
    while count<19:
     ps2=perfect_square(i)
     if ps2!=1:    
       for j in range(2,i//2+1):
           if i%j==0:
               ps=perfect_square(j)
               if ps == 1:
                break
       else:
         print(i,end=',')
         count+=1
     i+=1  
square_free()

#question 8
def sum_digit(x):
    sum=0
    while x>=1:
        y=x%10
        sum+=y
        x//=10
    return sum


def digital_root():
    a=eval(input("Enter the number "))
    count=0
    sum=a
    while sum>=10:
        sum= sum_digit(sum)
        count+=1
    print ("digital root is ",sum," number of step is ",count)
digital_root()

#question 9
def sum_digit(x):
    sum=0
    while x>=1:
        y=x%10
        sum+=y
        x//=10
    return sum


def magic():
    a,b=eval(input("Enter the range start,end "))
    sum=0
    for i in range(a,b+1):
       sum=i
       while sum>=10:
           sum= sum_digit(sum)
       if sum==1:
         print(i)
       
magic()

#question 10
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

 #question 11
def a(n):
    print("a")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(j,end=' ')
        print('')

def b(n):
    print("b")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(i,end=' ')
        print('')
        
def c(n):
    print("c")
    for i in range(1,n+1):
        for j in range (1,n+1-i):
            print(end=' ')
        for k in range(1,i+1):
            print("*",end='')
        print('')
        
def d(n):
    print("d")
    for i in range(n,0,-1):
        for j in range (1,n+1-i):
            print(end=' ')
        for k in range(1,i+1):
            print("*",end='')
        print('')

def e(n):
    print("e")
    count=1
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(count,end=' ')
            count+=1
        print('')

def f(n):
    print("f")
    for i in range(1,n+1):
        for j in range (i,0,-1):
            print(j,end=' ')
        print('')

def g(n):
    print("g")
    c=1
    for i in range(1,n+1):
        for j in range (1,i+1):
           print(c,end=' ')
           if c==0:
               c=1
           else:
               c=0
        print('')

def h(n):
    print("h")
    for i in range(1,n+1):
        z=4
        sum=i
        for j in range (1,i+1):
            print(sum,end=' ')
            sum=sum+z
            z-=1
        print('')

def i(n):
    print("i")
    for i in range(1,n+1):
        sum=1
        while sum<=i:
            print(sum,end=' ')
            sum=sum+1
        sum=i-1
        while sum>=1:
            print(sum,end=' ')
            sum=sum-1    
        print('')
        
def j(n):
    print("j")
    for i in range(1,n+1):
        for j in range (i,0,-1):
            sum=i+i-j
            print(sum,end=' ')
        sum=0
        print('')


def k(n):
    print("k")
    d=0
    for i in range(1,n+1):
        for j in range (1,i+1):
            a=0
            b=1
            c=1
            for x in range(1,d+1):
                c=a+b
                a=b
                b=c
            print(c,end=' ')
            d+=1
        print('')
        
def m(n):
    print("m")
    for i in range(1,n+1):
        for j in range (1,i+1):
            print("*",end=' ')
        print('')
    for i in range(n-1,0,-1):
        for k in range (i+1,1,-1):
            print("*",end=' ')
        print('')


#question 12
def first(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i*i)
    print(sum)

def second(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=j
    print(sum)

def third(n):
    sum=0
    sum1=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum1*=j
        sum+=sum1
        sum1=1
    print(sum)

def forth(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i**i)
    print(sum)

def fifth(n):
    sum=0
    sum1=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum1*=j
        sum+=(sum1//i)
        sum1=1
    print(sum)
    
import math
def sixth(n):
    x=float(input(" Enter the value for x : "))
    x=(x*math.pi)/180
    term=x
    sum=x
    i=2
    while abs(term) >= 0.000001: 
        term *= (-x*x)/((2*i-2)*(2*i-1))
        sum=sum+term
        i+=1
    print("The value of Sin(x) = ",sum)
    

#Question 13
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





