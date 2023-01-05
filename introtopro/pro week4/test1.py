n=5
for i in range (1,11,1):
    if i>=5:
        for k in range (0,n):
            print(k, end=" ")
        n+=1
        print()
    else:
        for j in range (n,0,-1):
            print(j,end=" ")
        n-=1
        print()

