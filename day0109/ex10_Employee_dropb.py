class Employee:
    def __init__(self,no,name):
        self.__no = no
        self.__name = name
    def setNo(self,no):
        self.__no = no
    def setName(self,name):
        self.__name=name
    def getNo(self):
        return self.__no
    def getName(self):
        return self.__name
    def computeSalary(self):
        return 0
    def info(self):
        return "사원번호:{},사원이름:{},실수령액:{}".format(self.__no,self.__name,self.computeSalary())


class SalariedEmployee(Employee):
    def __init__(self,no,name,level):
        Employee.__init__(self, no, name)
        self.__level = level

    def computeSalary(self):
        base = 0
        sudang = 0
        salary = 0
        if self.__level == 1:
            base = 2000000
            sudang = 200000
        elif self.__level == 2:
            base = 3000000
            sudang = 300000
        else:
            base = 4000000
            sudang = 400000
        salary = base + sudang
        return  salary


class HourlyEmployee(Employee):
    def __init__(self,no,name,base,time):
        Employee.__init__(self, no, name)
        self.__base = base
        self.__time = time

    def computeSalary(self):
        salary = self.__base * self.__time
        return salary


# kim = SalariedEmployee(10, "김유신", 1)
# lee = HourlyEmployee(20, "이순신", 200000, 15)
# hong = SalariedEmployee(30, " 홍길동", 3)
#
# # print(kim.getNo(), kim.getName(), kim.computeSalary())
# # print(lee.getNo(), lee.getName(), lee.computeSalary())
# # print(hong.getNo(), hong.getName(), hong.computeSalary())
# print(kim.info())
# print(lee.info())
# print(hong.info())

data = []
data.append(SalariedEmployee(10, '김유신', 1))
data.append(HourlyEmployee(20,'홍길동',200000,15))
data.append(SalariedEmployee(30, '이신순',3))
#리스트에 담긴 모든 직원들의 급여를 계산하여 출력 해 봅니다. 완성하면 "1"



