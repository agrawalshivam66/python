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

