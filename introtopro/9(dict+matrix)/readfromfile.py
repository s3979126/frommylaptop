def pirate_translator():
    #create a dictionary from a file
    with open("eng2pirate.txt","r") as file:
        lines = file.readlines()
        p_dict={}
        for line in lines:
            line= line.replace("\n", "").split("\t")
            p_dict[line[0].strip().lower()]=line[-1].strip().lower()
    #translate
    writer="Madam are the boy restroom"
    translating=writer.lower().split(" ")
    after=[]
    for i in translating:
        after.append(p_dict.get(i))
    print(after)
    print(" ".join(after))

pirate_translator()


# e_dict={v:k for k,v in p_dict.items()}

