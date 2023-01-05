while True:
    InputValue = input()
    try:
        a = float(InputValue)
        AllNums.append(a)
    # When user enter an invalid variable
    except ValueError:
        print("PLease enter a number"
              "Do you ưant")

