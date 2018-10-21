# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:32:29 2018

@author: Shivam-PC
"""
# question 1
def different():
    a=eval(input("Enter the sequence of numbers "))
    count=0
    for i in a:
        if a.count(i)>1:
           count+=1
    if count==0:
         print("All numbers are distinct from each other")
    else:
         print("All numbers are not distinct from each other")
different()

# question 2
def remove_dup():
    a=eval(input("Enter the sequence of numbers "))
    b=list()
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
remove_dup()

# question 3
def is_prime(x):
    for i in range(2,int((x**(1/2))+1)):
        if x%i==0:
            return 1
    return 0

def primes_lessthan(n):
    a=list()
    for i in range(2,n):
        if is_prime(i)==0:
            a.append(i)
    return a

c=eval(input("Enter the number "))
b= primes_lessthan(c)
print(b)

# queation 4
def even_odd():
    a=eval(input("Enter the number "))
    even=list()
    odd=list()
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    a=even+odd
    print(a)
even_odd()

# question 5
def mode_num():
    a=eval(input("Enter the number "))
    max=0
    for i in a:
        if a.count(i)>max:
            max=a.count(i)
    print("the mode of list is ",max)
mode_num()

# question 6
def suffle():
    a=list(input("Enter the numbers ").split(","))
    l=len(a)
    a1=a[0:l//2]
    a2=a[l//2:l+1]
    a.clear()
    x=0
    y=0
    for i in range(0,l):
        if i%2==0:
            a.append(a1[x])
            x+=1
            
        else:
            a.append(a2[y])
            y+=1
    print(a)    
suffle()

# question 7
a=[]
n = eval(input("Enter the number of elements "))
for i in range(0,n):
    x = eval(input("Enter the number "))
    a.append(x)
max_diff=max(a)-min(a)
print(max_diff)

# question 8
def encrypt(text,s): 
    result = "" 
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
    return result 
def eight():
    text = str(input("Enter the string:"))
    s = int(input("How much do you want to shift:"))
    print ("Text  : " + text) 
    print ("Shift : " + str(s)) 
    print ("Cipher: " + encrypt(text,s))
eight()    

# question 9
a=[]
n = eval(input("Enter the number "))
for i in range(1,n+1):
    a.append(i)
del a[1::2]
i=1
while(a[i]<len(a)):   
    del a[a[i]-1::a[i]]
    i+=1
print(a)        
    
# question 10
def lucky():
    a=[]
    for i in range(1,201):
        a.append(i)
    del a[1::2]
    i=1
    while(a[i]<len(a)):   
        del a[a[i]-1::a[i]]
        i+=1
    return a

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=lucky()
for i in a:
    if is_prime(i):
        print(i,end=',')





# question 11
def eleven():
    r=int(input("enter the rows : "))
    c=int(input("enter the columns : "))
    mat=[[0 for x in range(r)] for y in range(c)]
    for i in range(r):
        for j in range(c):
            mat[i][j]=int(input())
    rstart=0
    cstart=0
    rend=r
    cend=c
    while(rstart<rend and cstart<cend):
        for i in range (cstart,cend):
            print(mat[rstart][i],end=" ")
        rstart+=1
        for i in range(rstart,rend):
            print(mat[i][cend-1],end=" ")
        cend-=1
        if (rstart<rend):
            for i in range(cend-1,(cstart-1),-1):
                print(mat[rend-1][i],end=" ")
            rend-=1
        if(cstart<cend):
            for i in range(rend-1,rstart-1,-1):
                print(mat[i][cstart],end=" ")
            cstart+=1

# question 12
def printSpiral(n) :      
    for i in range(0, n) : 
        for j in range(0, n) : 
              
            # Finds minimum of four inputs 
            x = min(min(i, j), min(n - 1 - i, n - 1 - j)) 
              
            # For upper right half 
            if (i <= j) : 
                print((n - 2 * x) * (n - 2 * x) -
                      (i - x)- (j - x), end = "\t") 
  
            # For lower left half 
            else : 
                print(((n - 2 * x - 2) *
                       (n - 2 * x - 2) +
                       (i - x) + (j - x)), end = "\t") 
        print() 
def twelve():
    n = int(input("Enter a number:"))
    printSpiral(n)
twelve()

# question 13
def thirteen(): 
    n=int(input("enter the dimension : "))
    generateSquare(n)       
def generateSquare(n): 
    magicSquare = [[0 for x in range(n)] 
                      for y in range(n)]  
    i = n / 2
    j = n - 1 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:   
            if j == n: 
                j = 0
            if i < 0: 
                i = n - 1
                  
        if magicSquare[int(i)][int(j)]:  
            j = j - 2
            i = i + 1
            continue
        else: 
            magicSquare[int(i)][int(j)] = num 
            num = num + 1
                  
        j = j + 1
        i = i - 1 
    print ("Magic Squre for n =", n) 
    print ("Sum of each row or column",  
            n * (n * n + 1) / 2, "\n") 
      
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (magicSquare[i][j]),  
                                     end = '')  
            if j == n - 1:  
                print() 

# question 14
def fourteenth():
    r=int(input("enter the number of rows"))
    c=int(input("enter the number of columns"))
    mat=[[0 for i in range(r)] for j in range(c)]
    for i in range(r):
        for j in range(c):
            mat[i][j]=int(input())
    for i in range(r):
        min_row=mat[i][0]
        col=0
        for j in range(c):
            if(min_row>mat[i][j]):
                min_row=mat[i][j]
                col=j
        count=0
        for k in range(r):
            if(min_row<mat[k][col]):
                print("No saddle")
                break
            count+=1
        if(count==r):
            print(min_row)
fourteenth()

# question 16
import numpy as np
def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1
def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False
def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return grid
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False
input = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
print(np.array(solveSudoku(input)))

# question 17
import random
WIN_COMBINATIONS = [(1, 2, 3),
                    (4, 5, 6),
                    (7, 8, 9),
                    (1, 4, 7),
                    (2, 5, 8),
                    (3, 6, 9),
                    (1, 5, 9),
                    (3, 5, 7)]
def display_board(board):
    print('''   |   |  
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {} 
   |   |
-----------
   |   |
 {} | {} | {}
   |   |'''.format(*board[1:10]))
def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, Choose O or X to play!').upper()
    if marker == 'X':
        return {'Player 1': 'X', 'Player 2': 'O'}
    else:
        return {'Player 2': 'X', 'Player 1': 'O'}
def win_check (board):
    return any(board[a] != ' ' and board[a] == board[b] == board[c] for a, b, c in WIN_COMBINATIONS)
def choose_first(players):
    random_player = 'Player {}'.format(random.randint(1, 2))
    return random_player, players[random_player]
def full_check (board):
    return all(b != ' ' for b in board)
def player_choice(board):
    while True:
        try:
            position = int(input('Choose number input 1-9'))
            if position in range(1, 10) and board[position] == ' ':
                return position
        except ValueError:
            pass
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
def play():
    board = [' ' for _ in range(10)]
    players = player_input()
    name, player_marker = choose_first(players)
    print('{} with marker {} will go first.'.format(name, player_marker))
    while True:
        position = player_choice(board)
        board[position] = player_marker
        display_board(board)
        if win_check(board):
            print('Congratulations {}! You have won the game!'.format(name))
            break
        if full_check(board):
            print('Congratulations {} and {}! You have a tie!'.format(players.keys()))
            break
        name = 'Player 1' if name == 'Player 2' else 'Player 2'
        player_marker = players[name]
        print(name, player_marker)
print('Welcome to Tic Tac Toe Game!')
while True:
    play()
    if not replay():
        break