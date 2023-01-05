'''
DICTIONARY
READING FILE
GENERATE FILE
WRITE To FILE
FIND MISSING IN FILE
File mode
'''
# eng2sp = {}
# eng2sp['one']  = 'uno'
# eng2sp['two'] = 'dos'
# eng2sp['three']  = 'tres'
# print(eng2sp)
eng2sp = {'three': 'tres' "normie", 'one': 'uno', 'two': 'dos'}
value = eng2sp['three']
print(value)
file= open("C:\\Users\\hnaoh\\OneDrive\\Documents\\nhật kí IT\\Bugsss.txt", "r")
for line in file:
    print(line)
file.close()