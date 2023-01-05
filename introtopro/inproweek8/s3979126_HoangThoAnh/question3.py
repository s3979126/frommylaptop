# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 2
# Author: HoangThoAnh(s3979126)
# Created date: 17/12/2022
# Last modified date: 17/12/2022
"""
Question 3
Write a program that takes a sequence of numbers separated by space as an input from
a user. Find and display the maximum value and all their positions in the input sequence.
Example:     Input:   Enter a sequence of numbers:  15 17.2 7 -8.8 9.2 17.2 -3.5
          Output:  The maximum value is 17.2 at position(s) 1, 5 """

def max_value_and_index(in_num_list):
    """

    :param in_num_list:
    :return:
    """
    num_list=in_num_list.split(" ")
    print(num_list)
    m=max(num_list,key=lambda x:float(x))
    index_posi=[i for i, j in enumerate(num_list) if j == m]
    print(max(num_list,key=lambda x:float(x)) ,"at", end=" ")
    for k in index_posi:
        print(k,end=" ")

user_type=input(" Enter a sequence of numbers:")
max_value_and_index(user_type)