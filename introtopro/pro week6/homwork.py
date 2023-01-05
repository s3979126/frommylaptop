# # # # find the last char in a letter
# # # fruit=" fuck you , banana bla bla ,cok weird"
# # # print(fruit.split(","))
# # print("Azzzzzzz"<"a")
# # reverse string not use [](print(a[1::2]))
#
# # # how can i add recursion to this?
# a= "ádfsad"
# # def odd(a):
# #     if len(a)
# #     print(a[1])
# #     return a[len(a)-1]
# encode?
# format/format_map
# "điểm group vs thành viên số lượng"
# '''3'''
# b=123131231
# def int_count(source):
#     print(len(str(source)))
# int_count(b)
# '''4'''
# def string_reverse(input):
#     print(input[-1::-1])
# string_reverse("81923810283asdfasdbf")
#
a="dasds"
# print(a[len(a)-1] )
def recur_reverse(instr):
    print(len(instr)-1)
    if len(instr)==0:
        return ""
    return instr[len(instr)-1] + recur_reverse(instr[:len(instr)-1])

# print(1//2)
# '''5'''

'''
'''
def is_palindrome(sus):
    if len(sus)//2==0:
        return True
    check= sus[0]==sus[len(sus)-1]
    return check and is_palindrome(sus[1:len(sus)-1])

print(is_palindrome("nnonn"))
# def palindrome(sus):
#     re=sus[-1::-1]
#     if re == sus:
#         print(sus + " is palindrome")
#     else:
#         print("nope")
# '''6'''
# def remove(origin,not_this):
#         print(origin.__str__().replace(not_this.__str__(),""))
# remove(1234,12)
def first():
    ss = "Hello, World "
    els = ss.count("l")
    print(els)
    print("***" + ss.strip() + "***")  # stars added to show bounds
    print("***" + ss.lstrip() + "***")
    print("***" + ss.rstrip() + "***")
    news = ss.replace("o", "***")
a="ba nan a"
b=98765
def second():

    size=len(a)-1
    print(size)
    last=a[size]
    print(last)

def third():
    trns=a.maketrans("ba","na")
    print(a.translate(trns))
    print(a.partition())
    print(a.splitlines())

third()