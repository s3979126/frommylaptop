# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 2
# Author: HoangThoAnh(s3979126)
# Created date: 17/12/2022
# Last modified date: 17/12/2022

times=1``
1   def recur_representative(n):
    """
    :param n:
    :return:
    """
    global times
    if n ==1:
        return 1
    times = n + recur_representative(n-1)
    return times
#main
students=int(input("Enter the number of students:"))
print("Therse are",recur_representative(students),"way(s) to select a representative board from ", students," students. ")
def combination(n):
  """
  Recursively calculate number of combination of student
  parameter n: input number of students
  return: number of combination of n students
  """
  if n == 1:
    return 2
  return combination(n-1)*2

#Step 2: Main program
num = int(input("Enter the number of students: "))
print("There are", combination(num) - 1, end="")
print("way(s) to select a representative board from", num, "student(s).")
