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
