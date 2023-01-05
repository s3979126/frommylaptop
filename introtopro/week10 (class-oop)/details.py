"""
init-asign value
"""
"#caculate distance"
def cordinate_cac():
    class Cordinate:
        def __init__(me,x,y):
            me.x=x
            me.y=y
        def distanc(self,second):
            sqr_x= (self.x-second.x) **2
            sqr_y= (self.y-second.y) **2
            return (sqr_x+sqr_y)**0.5

    a=Cordinate(3,4)
    b=Cordinate(0,0)
    print(a.distanc(b))

