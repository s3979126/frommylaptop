# # # # # # # # # # # print("Go" * 6)
# # # # # # # # # # # name = "RMIT"
# # # # # # # # # # # print(name * 3)
# # # # # # # # # # # print(name + "Go" * 3)
# # # # # # # # # # # print((name + "Go") * 3)
# # # # # # # # # # # import operator
# # # # # # # # # # A="ASFDASFD"
# # # # # # # # # # print(A[-3:-1])
# # # # # # # # # #
# # # # # # # # # ss = "Hello, World"
# # # # # # # # # print(ss.upper())
# # # # # # # # # tt = ss.lower()
# # # # # # # # # print(tt)
# # # # # # # # ss  = " Hello, World "
# # # # # # # # els = ss.count("l")
# # # # # # # # print(els)
# # # # # # # # print("***" + ss.strip() + "***") # stars added to show bounds
# # # # # # # # print("***" + ss.lstri
# # p() + "***")
# # # # # # # # print("***" + ss.rstrip() + "***")
# # # # # # # # news = ss.replace("o", "***")
# # # # # # # # print(news)
# # # # # # # food = "banana bread"
# # # # # # # print(food.capitalize())
# # # # # # # print("*" + food.center(25) + "*") # stars added to show bounds
# # # # # # # print("*" + food.ljust(25) + "*")
# # # # # # # print("*" + food.rjust(25) + "*")
# # # # # # # print(food.find("a"))
# # # # # # # print(food.find("na"))
# # # # # # # print(food.find("b"))
# # # # # # # print(food.rfind("e"))
# # # # # # # print(food.rfind("na"))
# # # # # # # print(food.rfind("b"))
# # # # # # txt = "Welcome to the jungle, baby!"
# # # # # # # default split at whitespace
# # # # # # print(txt.split())
# # # # # # # specify the delimiter  (where to split)
# # # # # # print(txt.split("to     "))
# # # # # # # join the text
# # # # # # splitted = txt.split()
# # # # # print(" ".join(splitted))
# # # # # # print(". ".join(txt))
# # # # # d="hbjhb"
# # # # # print(d.encode())
# # # #
# # # # print('p' in 'apple')
# # # # print('i' in 'apple')
# # # # print('ap' in 'apple')
# # # # print('pa' in 'apple')
# # # # print('' not in 'apple')
# # # def remove_vowels(s):
# # #     """
# # #     Return a new string created by removing all vowels from string s
# # #     :params: a string
# # #     :return: a new string created by removing all vowels from s
# # #     """
# # #     vowels = "aeiouAEIOU"
# # #     new_str = ""
# # #     for char in s:  # process each  character  of s
# # #        if char not in vowels:
# # #          new_str = new_str + char  # only add char if it's not a vowel
# # #     return new_str
# # # # Main program to test the function
# # # print(remove_vowels("compsci"))
# # # print(remove_vowels("Can you read without vowels?"))
# # import string
# # print(string.ascii_lowercase)
# # print(string.ascii_uppercase)
# # print(string.digits)
# # print(string.punctuation)
# print("String are sequences of charecters"[5])
# print("wonderful">"wonder")
s="ABCDE"
z=2347293
v="0100101"
print(v.isdigit())
a= True
for i in range(1,14):
    for j in range(0,13):
        if a :
            """
            print the first line
            """
            print("x0123456789101112".rjust(4), end=" ")
            for k in range (0,13):
                k=str(k)
                print(k.rjust(4), end=" ")
            a= False
            print("")
            print("0".rjust(4),end=" ")
        val=j * (i - 1)
        val= str(val)
        print(val.rjust(4),end=" ")

    print("")
    if i==13:
        break
    i=str(i)
    print(i.rjust(4),end=" ")

def odd_reverse():
    v=a[-1 if len(a)%2 ==0 ]
