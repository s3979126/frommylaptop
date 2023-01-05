# ex1
import os
filename=input("Enter a filename:")
foldername ="file"
os.makedirs(foldername,exist_ok=True)
filepath = foldername +os.sep+filename+ ".txt"

def print_100(message):
    print((message+"\n")*100)


print_100("haha")
filename="message.txt"
filename.


# w:write
# r:read
# x:created
# a:append
f=open(filename, "w")

# ex3
filepath="folder\\text.txt"
filepath_arr=filepath.split("\\")
filename=filepath_arr[-1]
#change the file name in the filepath_arr
filepath_arr[-1]="new"+filepath_arr[-1]
new_filepath="\\".join(filepath_arr)

with open(new_filepath, "w") as outfile:
    with open(filepath, "r") as infile:
        lines = infile.readlines()
        print(lines)
        number=1
        for line in lines:
            new_line= str(number)+ lines
            number+=1
            outfile.write(new_line)




def generate_new_file():
    """
    param in_filepath
    param out_filepath
    :return
    """


def generate_new_file_with_numbers(infile_path,out_filepath):
    """

    :param infile_path:
    :param out_filepath:
    :return:
    """
    #out_file=open(out_filepath, "w")


#ex4
