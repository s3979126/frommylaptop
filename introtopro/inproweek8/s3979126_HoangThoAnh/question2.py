# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: HoangThoAnh(s3979126)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
"""Question 2
Write a program that takes a string where each of the words are separated by comma as
an input from a user. The program prints all the words input from the user in a list. Then
filter the words that do not start with vowel alphabets and print each of the filtered words
(which do not start with vowel alphabets) in separate lines.
The output of the program must be as in the example given below:
Example:  Input:  Enter the words separated by comma: Hi,I,am,Python,And,who,is,He
Output:   ['Hi', 'I', 'am', 'Python', 'And', 'who', 'is', 'He']
Hi
Python
who
He """

def requirements(L):
    """
    :param L:
    :return:
    """
    vowel=["u","e","o","a","i"]
    print(L)
    #print words not start with vowels
    for i in L:
        if i[0].lower() not in vowel:
             print(i)
#main
List = input("Enter the words separated by comma: ").split(',')
requirements(List)
