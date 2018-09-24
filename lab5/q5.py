def mode_num():
    a=eval(input("Enter the number "))
    max=0
    for i in a:
        if a.count(i)>max:
            max=a.count(i)
    print("the mode of list is ",max)
mode_num()
