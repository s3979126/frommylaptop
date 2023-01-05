a= True
lst=[]
for i in range(1,14):
    for j in range(0,13):
        if a :
            """
            print the first line
            """
            print("x", end=" ")
            for k in range (0,13):
                print(k, end=" ")
            a= False
            print("")
        val=j * (i - 1)
        val=str(val)
        lst.append(val)
        print(val,end=" ")
    print("")
    if i==13:
        break
    print(i,end=" ")

# Split input data by row and then on spaces
rows = [ line.strip().split(' ') for line in lst().split('\n') ]

# Reorganize data by columns
cols = zip(*rows)

# Compute column widths by taking maximum length of values per column
col_widths = [ max(len(value) for value in col) for col in cols ]

# Create a suitable format string
format = ' '.join(['%%%ds' % width for width in col_widths ])

# Print each row using the computed format
for row in rows:
  print (format % tuple(row))