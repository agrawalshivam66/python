m=[[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1], [0, 0, 0]]
dis=[[4],[2,4],[2],[0],[6],[4],[4],[2]]

def decision_tree():
    m=[[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 1], [0, 0, 0]]
    dis=[[4],[2,4],[2],[0],[6],[4],[4],[2]]
    #sorting
    for i in range (0,len(m)):
        for j in range(0,i):
            if dis[i]>dis[j]:
                dis[i],dis[j]=dis[j],dis[i]
                m[i],m[j]=m[j],m[i]
    #printing        
    print("Decision tree")
    print("<50\tCOD\tWhole\tDiscount")
    for i in range(0,len(m)):
        for j in range(0,3):
            print(m[i][j],end='\t')
        print(dis[i])

        
def decision_table():
    print()
    print("Decision table")
    print("Enter 1 for yes and 0 for No")
    c1=int(input("Number of units<50 (1/0) "))
    c2=int(input("Cash on delivery (1/0) "))
    c3=int(input("Wholesale outlet (1/0) "))
    n=[c1,c2,c3]
    for i in range(0,len(m)):
        if m[i]==n:
            print("Thee discount rate is ",dis[i])
    print()
decision_table()
decision_tree()
