import math

# QUESTION 1
def distance(a):
    dis = math.sqrt((a[0])**2 + (a[1])**2)
    return  round(dis)

def first():
    a=[]
    a.append(0)
    a.append(0)
    move=''
    while move != 'X':
        move = str(input("Enter your movement "))
        mov = move.split()
        if mov[0]=='X':
            break
        elif mov[0]=='UP':
            a[1]+=int(mov[1])
        
        elif mov[0]=='DOWN':
            a[1]-=int(mov[1])
            
        elif mov[0]=='LEFT':
            a[0]-=int(mov[1])
            
        elif mov[0]=='RIGHT':
            a[0]+=int(mov[1])
        
        else: 
            print("Wrong Chocie ")
            
    dis = distance(a)
    print(dis)
first()


# QUESTION 2
def second():
    a=[]
    a.append(0)
    a.append(0)
    move=''
    while move != 'X':
        move = str(input("Enter your movement "))
        mov = move.split()
        if mov[0]=='X':
            break
        elif mov[0]=='UP':
            a[1]+=int(mov[1])
        
        elif mov[0]=='DOWN':
            a[1]-=int(mov[1])
            
        elif mov[0]=='LEFT':
            a[0]-=int(mov[1])
            
        elif mov[0]=='RIGHT':
            a[0]+=int(mov[1])
        
        else: 
            print("Wrong Chocie ")
            
    if a[0]==0 and a[1]==0:
        print('circular')
    else:
        print('not circular')
second()

#QUESTION 3
def third():
    n = int(input("Enter the number "))
    my_dict = {}
    for i in range(1,n+1):
        my_dict[i]=i*i
    print(my_dict)
third()

#QUESTION 4
def forth():
    s1 = str(input("Enter first string "))
    s2 = str(input("Enter second string "))
    if sorted(s1) == sorted(s2): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
forth()

      
