class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        return self.first+self.second
    def sub(self):
        return self.first-self.second
    def mul(self):
        return self.first*self.second
    def div(self):
        return self.first/self.second

# a=FourCal()
# a.setdata(3,5)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# 클래스 상속하기:     class 클래스 이름(부모클래스):

class MoreFourCal(FourCal):
    def __init__(self,first,second,c):
        FourCal.__init__(self,first,second)
        self.c=c
    def pow(self):
        result=self.first ** self.second
        return result
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
a=MoreFourCal(4,0,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())
