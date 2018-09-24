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
