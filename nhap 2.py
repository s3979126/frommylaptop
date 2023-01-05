print("Enter your numbers.")
all_numbers = []
while "s" not in all_numbers:
    input_numbers = input().lower()
    if input_numbers.isnumeric():
        all_numbers.append(input_numbers)
    elif input_numbers == "s":
        all_numbers.append(input_numbers)
    else:
        print("please input a number")
print(all_numbers)
all_numbers.pop()
print(all_numbers)
print("The largest value:", max(all_numbers))
quit("Thanks")