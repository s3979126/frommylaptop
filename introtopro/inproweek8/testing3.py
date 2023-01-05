l=["A","asd","asda","fd","long"]
# Python3 code to demonstrate working of
# Longest String in list
# using loop

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Longest String in list
# using loop
def way1():
    max_len = -1
    longest=[]
    for ele in l:
        if len(ele) >= max_len:
            max_len = len(ele)
            longest.append(ele)

# printing result
ele=[]
maxi=(len(max(l,key=len)))
for i in l:
    if 	len(i) == maxi:
	    ele.append(i)

print("Maximum length string is : " + ele[-1])
