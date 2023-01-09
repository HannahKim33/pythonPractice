class Family:
    lastname='김'    #클래스 변수. 자바의 static field와 비슷함.
    def __init__(self, firstname):
        self.firstname=firstname
    def info(self):
        print(self.firstname,self.lastname)

#클래스 변수는 객체를 생성하지 않고 사용할 수 있다.
print(Family.lastname)

a=Family('철수')
b=Family('철민')

a.info()
b.info()

Family.lastname='박'

a.info()
b.info()

print(a.lastname)
print(b.lastname)
print(Family.lastname)

'''
    객체를 통해서도 클래스 변수를 사용할 수 있다.
    그런데 객체를 통해 클래스 변수를 변경하면 그 객체의 변수만 변경되고 클래스 변수에는 영향을 끼치지 않는다.
'''

a.lastname='홍'
print(a.lastname)       #홍
print(b.lastname)       #박
print(Family.lastname)  #박