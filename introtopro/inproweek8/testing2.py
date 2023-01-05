# define a function recur_least_letters
# this function will take a list as input argument
ans=""
def recur_least_letters(l):
    # use ans string
    global ans
    # if length of the list is 0
    if (len(l) == 0):
        # return ans
        return ans
        # if length of the list is 1
    elif (len(l) == 1):
        # check if string is empty
        if (len(l[0]) == 0):
            # return ans
            return ans
        # otherwise
        else:
            # sort the string
            temp = sorted(l[0])
            # add the smallest letter in ans
            ans = ans + temp[0]
            # and return the ans
            return ans
    # if length of the string is more than
    else:
        # if length of first string is 0
    # if len(l[0]) != 0:
        # sort the string
        temp = sorted(l[0])
        # add the smallest letter in ans
        ans = ans + temp[0]
        # call the recur_least_letters recursively with remaining list(exclude the first string)
        return recur_least_letters(l[1:len(l)])


# create a list
l = ["today", "is", "saturday"]

# call the recur_least_letters function
print("Output:", recur_least_letters(l))