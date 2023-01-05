def ab(a,b):
    if b==1:
        return  a

    return a + ab(a,b-1)
def vladimir(n)
    if n==1:
        return 1
    return vladimir(n-1) + vladimir(n-2)

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
.input().i4