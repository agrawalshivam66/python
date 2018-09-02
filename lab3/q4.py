def sum_digit(x):
    sum=0
    while x>=1:
        y=x%10
        sum+=(y**2)
        x//=10
    return sum


def magic():
    sum=0
    for i in range(1,1000):
       sum=i
       while sum>=10:
           sum= sum_digit(sum)
       if sum==1:
         print(i)
       
magic()
