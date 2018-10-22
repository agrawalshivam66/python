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

#question 5
def reverse(a):
    b=''
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b

def fiftha():
    s = str(input("Enter the string "))
    d = int(input("enter digits you want to rotate "))
    x = reverse(s[0:d])
    y = reverse(s[d::])
    rev = reverse(x+y)
    print(rev)
fiftha()

def fifthb():
    s = str(input("Enter the string "))
    d = int(input("enter digits you want to rotate "))
    x = reverse(s[0:len(s)-d])
    y = reverse(s[len(s)-d:len(s)])
    rev = reverse(x+y)
    print(rev)
fifthb()


# question 6
def substring():
    s1 = str(input("Enter the string "))
    s2 = str(input("Enter the string "))
    if s2 in s1:
        print('Substring is in string!')
    else:
        print('Substring not found in string!')
substring()


# question 7
def seventh():
    s = str(input("Enter the string "))
    b=[]
    for i in s:
        x = s[0]
        s=s[1:len(s)]
        s+=x
        if s not in b:
            b.append(s)
            print(s)
seventh()

#question 8
def eight():
    s = str(input("Enter the string "))
    a = s.split()
    b=dict()
    for i in a:
        c = a.count(i)
        b[i]=c
    print(b)
eight()
  

#question 9
def nine():
    s = str(input("Enter the string "))
    b=dict()
    vow = ['a', 'e', 'i', 'o', 'u']
    for i in vow:
        c = s.count(i)
        b[i]=c
    print(b)
nine()  

# question 10
def ten():
    s = str(input("Enter the string "))
    b=dict()
    for i in s:
        c = s.count(i)
        b[i]=c
    print(b)
ten()

# question 11
def eleven():
    s = str(input("Enter the string "))
    import re
    s = re.sub('[^a-zA-Z]',' ', s)#don't remove a-z and A_Z
    print(s)
eleven()

# question 12
def twelve():
    s = str(input("Enter the string "))
    a = s.split()
    sr = sorted(a)
    for i in sr:
        print(i)
twelve()

# question 13
def thirteen():
    s = str(input("Enter the string "))
    b=[]
    for i in s:
        if i not in b:
            c = s.count(i)
            b.append(i)
            print(i,c)
thirteen()    
    