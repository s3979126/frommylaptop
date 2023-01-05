def dict_count_times_a_letter_appear_in_a_string():
    str="w3re  so  urce"
    str= str.replace(" ","")
    dictstr={}
    for i in str:
        dictstr[i]=dictstr.get(i,0)+1
    print(dictstr)
#ex2
def filter_dict_based_on_value():
    not_filtered_dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    filtered_dict=not_filtered_dict.copy()
    for i in not_filtered_dict:
        if not_filtered_dict.get(i)<170:
            del filtered_dict[i]
    print(filtered_dict)
def filter_dict_based_on_value2():
    not_filtered_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    results={key:value for key,value in not_filtered_dict.items() if value>175}
    return  results
def biggest_dic2():
    dict_for_compare = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100, "z": 0}
    a = max(dict_for_compare.values())
    b = max(dict_for_compare, key=dict_for_compare.get)
    print("max value is",a,"at",b)
not_filtered_dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print(dict(filter(lambda ele: ele>175,not_filtered_dict)))