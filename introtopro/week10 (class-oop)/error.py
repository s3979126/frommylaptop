#1 : syntax
cass Cordinate
        '''it should be init, not int'''
    def __int__(me,x,y):
        me.x=x
        me.y=y
    def distanc(self,second):
        "where does this self lead to?"
        sqr_x= (self.x-second.x) **2
        sqr_y= (self.y-second.y) **2
        return (sqr_x+sqr_y)**0.5

a=Cordinate(3,4)
b=Cordinate(0,0)
print(a.distanc(b))

"why wont this work?"
# class Animal:
#     life="will die soon"
#     class Cat(Animal):
#         def speak(self):
#             print("meo")
# class waifu:
#     looks="pretty"
