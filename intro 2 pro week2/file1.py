print("Enter your numbers.")

AllNums = []
message = ["Please enter a number",
           "asdasd",
                       "fadf"]
currentIndex = 0


#loops for continously input
while True:
    InputValue = input().lower().is
    if InputValue == "s":
        break
    try:
        a = float(InputValue)
        AllNums.append(a)

    except ValueError:
        print("please enter a valid number")
        continue
if AllNums:
    if len(AllNums) == 1:
        print("The smallest number and the largest number are literally the same:",AllNums(0))
    else:
        print("The largest number is:", max(AllNums))
        print("The smallest number is:", min(AllNums))
else:
    print("not thing yet!")