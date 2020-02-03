class Box:
    def __init__(self):
        self.w=5
        self.h=5
        self.d=5
    def volume(self):
        print("Width=" ,self.w)
        print("Height=",self.h)
        print("Depth=",self.d)
        return self.w*self.h*self.d
c1 = Box()
print("Volume of Box= ",c1.volume())
