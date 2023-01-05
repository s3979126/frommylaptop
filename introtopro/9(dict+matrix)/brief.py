import numpy as np

"""
DICTIONARY
MATRIX
COUNT APPEAR TIMES OF A LETTER IN STRING
"""
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}


def biggist_dict():
    dict_for_compare = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': -1}
    biggist = 0
    b2 = 0
    print(dict_for_compare.get("a"))
    for i in dict_for_compare:
        biggist = [dict_for_compare.get(i)  if dict_for_compare[i] >= biggist]
    for i in dict_for_compare:
        if dict_for_compare.get(i) >= b2:
            b2 = dict_for_compare.get(i)
    print(b2)

    print(biggist)
    # list(dict_for_compare.values()).index(biggist))
    """trace back the key from value"""
    print([k for k,v in dict_for_compare.items() if v== max(dict_for_compare.values())][0])
    '''this is equal: print(list[0])'''

biggist_dict()



def biggest_dic2():
    a = max(dict_for_compare)
    b = max(dict_for_compare, key=dict_for_compare.get)
    print(a)
    print(b)
def dict_count_times_a_letter_appear_in_a_string():
    str="w3re  so  urce"
    str= str.replace(" ","")
    dictstr={}
    for i in str:
        dictstr[i]=dictstr.get(i,0)+1
    print(dictstr)
