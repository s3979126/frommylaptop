import random

print("Enter your numbers.")
#all_numbers = []
currentMaxNumber = 0
message = ["Please enter a number",
           "asdasd",
                       "fadf"]
currentIndex = 0

while True:
    input_numbers = input().lower()

    if input_numbers.isnumeric():
        currentMaxNumber = input_numbers
        break
    else:
        if currentIndex >= len(message):
            currentIndex = 0

        print(message[currentIndex])
        currentIndex += 1

        #print(random.choice(message))


while True:
    input_numbers = input().lower()
    if input_numbers != "s":
        if input_numbers.isnumeric():
            if...
            #all_numbers.append(input_numbers)
        else:
            if currentIndex >= len(message):
                currentIndex = 0

            print(message[currentIndex])

            currentIndex += 1

            #print(random.choice(message))


print("The largest number:")
print(currentMaxNumber)
quit("This homework is hard,but thanks")