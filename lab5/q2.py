def remove_dup():
    a=eval(input("Enter the sequence of numbers "))
    count=0
    b=list()
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
remove_dup()
