print("Enter your numbers.")

AllNums = []

ErrorMessages = ["Please enter a number",
                 "Hey, don't you know I can't do the caculating yet?So only number!",
                 "And only one number at a time",
                 "N-U-M-B-E-R!",
                 "Like, pretty please my almighty master?",
                 "After all that said, why do you stil..."
                 "Why why why why why why why????",
                 "NUMBERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
                 "I swear, if you do it one more time.....",
                 "That's it, that's the last straw, I'm done"

                 ]
ErrorMessagesNums = 0

# loops for continously input
while True:
    input_value = input().lower().strip()
    if input_value == "s":
        break
    try:
        a = float(input_value)
        AllNums.append(a)
    # When user enter an invalid variable
    except ValueError:
        print(ErrorMessages[ErrorMessagesNums])
        ErrorMessagesNums += 1
        if ErrorMessagesNums == len(ErrorMessages):
            quit("AND BAD-BYE TO YOU!")
        continue
if AllNums:
    if len(AllNums) == 1:
        print("The smallest number and the largest number are literally the same:", AllNums[0])
    else:
        print("The largest number is:", max(AllNums))
        print("The smallest number is:", min(AllNums))
else:
    print("not thing yet!")
