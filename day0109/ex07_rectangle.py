class Rectangle:
    def __init__(self,width=0,length=0):
        self.width=width
        self.length=length
    def calcArea(self):
        return self.width*self.length
    def setWidth(self,width):
        self.width=width
    def setLength(self,length):
        self.length=length

r1=Rectangle(3,5)
print(r1.calcArea())
r2=Rectangle()
print(r2.calcArea())
r2.setWidth(9)
r2.setLength(8)
print(r2.calcArea())



class Plane:
    planes = 0
    def __init__(self,maker='undefined',model='undefined',max=0):
        self.__maker=maker
        self.__model=model
        self.__max=max
        Plane.planes+=1
    def setMaker(self, maker):
        self.__maker=maker
    def setModel(self, model):
        self.__model=model
    def setMax(self, max):
        self.__max=max

    def getMaker(self):
        return self.__maker
    def getModel(self):
        return self.__model
    def getMax(self):
        return self.__max

    def getPlanes(self):
        return Plane.planes

p1=Plane('에어버스','A380',500)

print(p1.getMaker(), p1.getModel(), p1.getMax())
print(p1.getPlanes())
print(Plane.planes)