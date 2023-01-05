ori = "without,hello,bag,world"


def ex1(ori):
    templist = ori.split(",")
    templist.sort()
    print(",".join(templist))


def ex2(X, Y):
    '''
    X=int
    Y=int
    '''
    for i in range(X):
        res = [j * i for j in range(Y)]
        print(res)


def ex3():
    bla = [i ** i for i in range(1, 101)]
    print(bla[:-6:-1])

exg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ex4(exg):
    exg = [ne for ne in exg if ne % 2 != 0]
    print(exg)


def ex5(exb):
    exb = [ne ** 2 for ne in exb if ne % 2 == 0]
    print(exb)


def ex6(lines):
    splitted=lines.split(",")
    for i in range (0,len(splitted)):
        splitted[i]=int(splitted[i])
    print(type(splitted[1]))
    splitted=[ne ** 2 for ne in splitted if ne % 2 != 0]
    print(splitted)


lies="1,2,3,4,5,6,7,8"
ex6(lies)