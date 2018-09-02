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
