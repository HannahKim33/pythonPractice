class Student:
    def __init__(self,id,name,major,grade,credits):
        self.__id=id
        self.__name=name
        self.__major=major
        self.__grade=grade
        self.__credits=credits
    def setId(self,id):
        self.__id=id
    def setName(self,name):
        self.__name=name
    def setMajor(self,major):
        self.__major=major
    def setGrade(self,grade):
        self.__grade=grade
    def setCredits(self,credits):
        self.__credits=credits

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getMajor(self):
        return self.__major
    def getGrade(self):
        return self.__grade
    def getCredits(self):
        return self.__credits

    def __str__(self):
        return "id:{}, name:{}, major:{}, grade:{}, credits:{}".format(self.__id, self.__name, self.__major, self.__grade, self.__credits)

class UnderGraduate(Student):
    def __init__(self,id,name,major,grade,credits,club):
        Student.__init__(self,id,name,major,grade,credits)
        self.__club=club
    def setClub(self,club):
        self.__club=club
    def getClub(self):
        return self.__club

    def __str__(self):
        # return "id:{}, name:{}, major:{}, grade:{}, credits:{}, club:{}".format(self.getId(), self.getName(), self.getMajor(), self.getGrade(), self.getCredits(), self.__club)
        return "{}, club:{}".format(Student.__str__(self), self.__club)
class Graduate(Student):
    def __init__(self,id,name,major,grade,credits,assi,scholar):
        Student.__init__(self,id,name,major,grade,credits)
        self.__assi=assi
        self.__scholar=scholar

    def setAssi(self,assi):
        self.__assi=assi
    def setScholar(self,scholar):
        self.__scholar=scholar

    def getAssi(self):
        return self.__assi
    def getScholar(self):
        return self.__scholar

    def __str__(self):
        # return "id:{}, name:{}, major:{}, grade:{}, credits:{}, assi:{}, scholar:{}".format(self.getId(), self.getName(), self.getMajor(), self.getGrade(), self.getCredits(), self.__assi, self.__scholar)
        return "{}, assi:{}, scholar:{}".format(Student.__str__(self), self.__assi, self.__scholar)