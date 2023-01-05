# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(5))
def TowersOfHanoi(n , from_pole, to_pole, aux_pole):
    if n ==1:
        print("Move disk 1 from",from_pole,"to",to_pole)
        return
    TowersOfHanoi(n-1, from_pole, aux_pole, to_pole)
    print("Move disk",n,"from",from_pole,"to",to_pole)
    TowersOfHanoi(n-1, aux_pole, to_pole, from_pole)
for i in range(2):
    TowersOfHanoi(3,"A","B","C")


    