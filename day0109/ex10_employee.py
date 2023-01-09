class Employee:
    def __init__(self,name,id):
        self.__name=name
        self.__id=id
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setId(self,id):
        self.__id=id
    def getId(self):
        return self.__id
    def computeSalary(self):
        return 0
    def info(self):
        return "사원번호:{}, 사원이름:{}".format(self.__id, self.__name)
    def __str__(self):
        return "name:{}, id:{}".format(self.__name, self.__id)

class SalariedEmployee(Employee):
    def __init__(self,name,id,level):
        Employee.__init__(self,name,id)
        # super().__init__(self, name, id)
        self.__level=level
        base = 0
        sudang = 0
        salary = 0

    def computeSalary(self):
        if self.__level==1:
            self.__base=2000000
            self.__sudang=200000
        elif self.__level==2:
            self.__base=3000000
            self.__sudang=300000
        else:
            self.__base=4000000
            self.__sudang=400000
        self.__salary=self.__base+self.__sudang
        return self.__salary
    def __str__(self):
        return "{}, level:{}, salary:{}".format(Employee.__str__(self), self.__level, self.computeSalary())
        # return "id:{}, level:{}, salary:{}".format(self.__id, self.__level, self.computeSalary())

class HourlyEmployee(Employee):
    def __init__(self,name,id,rate,hours):
        Employee.__init__(self,name,id)
        # super().__init__(self,name,id)
        self.__rate=rate
        self.__hours=hours
    def setRate(self,rate):
        self.__rate=rate
    def getRate(self):
        return self.__rate
    def setHours(self,hours):
        self.__hours=hours
    def getHours(self):
        return self.__hours
    def computeSalary(self):
        return self.__rate*self.__hours
    def __str__(self):
        return "{}, rate:{}, hours:{}, salary:{}".format(Employee.__str__(self), self.__rate, self.__hours, self.computeSalary())

kim=SalariedEmployee('김유신',10,1)
lee=HourlyEmployee('이순신',20,200000,15)
hong=SalariedEmployee('홍길동',30,3)

print(kim)
print(lee)
print(hong)
# data=[]
# data.append(SalariedEmployee(10,'김유신',1))
# data.append(HourlyEmployee(20,'홍길동',200000,15))
# data.append(SalariedEmployee(30,'이순신',3))

# for item in data:
#     print(item.computeSalary())

print(type(kim))
print(type(lee))
print(type(hong))
print(type(kim) is SalariedEmployee)    #상속관계는 판별 못함
print(type(lee) is SalariedEmployee)
print(type(hong) is SalariedEmployee)
print('-'*50)
print(isinstance(kim,Employee))     #true. 상속관계에 있는 것도 판별함
print(isinstance(lee,Employee))     #true. 상속관계에 있는 것도 판별함
print(isinstance(hong,Employee))     #true. 상속관계에 있는 것도 판별함
