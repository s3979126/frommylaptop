print("Enter your numbers.")
CurrentmaxNum = "Nothing yet!"
OnetimeValue = True

#loops for continously input
while True:
    input_value = input().lower()
    if input_value == "s":
        break
    try:
        a = float(input_value)
        print(a)
        # one-time use lines:
        if OnetimeValue and type(a) == float:
            CurrentmaxNum = a
            OnetimeValue = False
        try:
            if a > CurrentmaxNum:
                CurrentmaxNum = a

        except:
            pass

    except ValueError:
        print("please enter a valid number")
        pass

print("The largest number is:", CurrentmaxNum)
