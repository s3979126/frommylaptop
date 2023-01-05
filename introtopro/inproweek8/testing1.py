# ex4
a= ["laa", "u;a;a", "hanoi", "elder"]
def ex4_but_simpler():
    # take the smallest charecter inside each string
    list=[min(i) for i in a]
    # print the requirement
    print(",".join(list))

ans_lst=""
def fucking_rec(l):
    global  ans_lst
    # take out the case the list empty
    if len(l)==0:
        return ans_lst
    # take the case tto stop recur
    elif len(l)==1:
            #take the smallest letter
            ans_lst+=min(l[0])
            return ans_lst
    else:
        # if len(l[0])!=0:
        #take the smalest letter
        ans_lst +=min(l[0])
        return fucking_rec(l[1:len(l)])

l = [" ","today"," ", "is", "saturday"]


# create an empty string ans
ans = ""


# define a function recur_least_letters
# this function will take a list as input argument
# def recur_least_letters(l):
#     # use ans string
#     global ans
#     # if length of the list is 0
#     if (len(l) == 0):
#         # return ans
#         return ans
#         # if length of the list is 1
#     elif (len(l) == 1):
#         # check if string is empty
#         if (len(l[0]) == 0):
#             # return ans
#             return ans
#         # otherwise
#         else:
#             # sort the string
#             temp = sorted(l[0])
#             # add the smallest letter in ans
#             ans = ans + temp[0]
#             # and return the ans
#             return ans
#     # if length of the string is more than
#     else:
#         # if length of first string is 0
#         if (len(l[0]) != 0):
#             # sort the string
#             temp = sorted(l[0])
#             # add the smallest letter in ans
#             ans = ans + temp[0]
#         # call the recur_least_letters recursively with remaining list(exclude the first string)
#         return recur_least_letters(l[1:len(l)])


# create a list


# call the recur_least_letters function
# print("Output:", recur_least_letters(l))
print(fucking_rec(l))
