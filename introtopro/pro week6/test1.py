for i in range(0,13):
    if i==0:
        """
        print the first line
        """
        print("x".rjust(4), end=" ")
        for k in range(0, 13):
            print(k.__str__().rjust(4), end=" ")
    print("")
    print(i.__str__().rjust(4), end=" ")

    for j in range(0,13):
        print((j*i).__str__().rjust(4),end=" ")


