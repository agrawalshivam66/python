sideA,sideB,sideC=eval(input("Enter three sides "))
if(sideA<sideB+sideC and sideB<sideA+sideC and sideC<sideB+sideA):
    print("The triangle is valid ",end="")

    if(sideA**2==sideB**2+sideC**2) or (sideB**2==sideA**2+sideC**2) or (sideC**2==sideB**2+sideA**2):
        print("and form a Pythagorean Triplet")
    else:
        print("but do not form a pythagorean Triplet")

else:
    print("Not a valid triangle")
