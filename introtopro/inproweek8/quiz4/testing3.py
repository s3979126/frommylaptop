my_name = "Edgar Allan Poe"
name_list = my_name.split()
init = ""
for name in name_list:
    init = init + name[0]
print(init)