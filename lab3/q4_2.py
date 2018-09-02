def sum_digit(x):
    sum=x
    while sum>=10 or sum==7:
        sum=0
        while x>=1:
            y=x%10
            sum+=(y**2)
            x//=10
            if sum==1:
                return True
            else:
               sum= sum_digit(sum)
    return False   
    

def happy():
    a=list()
    sum=0
    for i in range(1,1000):
        t= sum_digit(i)
        if t==True:
         print(i)
happy()
