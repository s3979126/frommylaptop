# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 2
# Author: HoangThoAnh(s3979126)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
"""
Question 1
Write a program to count all letters, digits, and special symbols from a given string.
Example 1:  Input:   Enter a string: P@#yn26at^&i5ve
          Output:  Letters: 8
Digits: 3
Symbols: 4
Example 2:  Input:   Enter a string:  RRmmmIIIIT 123
          Output:  Letters: 10
Digits: 3
Symbols: 1
"""
input_from_user = input("Please a String : ")

def counter(string):
    """
    :param string:
    :return:
    """
    alphabets = digits = special = 0
    #counting
    for i in range(len(string)):
        if (string[i].isalpha()):
            alphabets = alphabets + 1
        elif (string[i].isdigit()):
            digits = digits + 1
        else:
            special = special + 1
    print("Letters:  ", alphabets)
    print("Digits:  ", digits)
    print("Symbols:  ", special)

#main program

print(counter(input_from_user))