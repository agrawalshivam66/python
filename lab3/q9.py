def sum_digit(x):
    sum=0
    while x>=1:
        y=x%10
        sum+=y
        x//=10
    print( sum)
sum_digit(19) 
def magic():
    a,b=eval(input("Enter the range start,end "))
    for i in range(a,b+1):
       sum1= sum_digit(i)
       sum2=sum_digit(sum1)
       if sum1==sum2:
        print(i)
       
#magic()
