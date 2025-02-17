class Person:
    id=None
    _name=None
    __family=None
    def __init__(self,id,name,family):
        self.id=id
        self._name=name
        self.__family=family

    def getFamily(self):
        return self.__family
    

    def setFamily(self,newFamily):
        self.__family=newFamily

    def showPersonInfo(self):
        print(f"ID : {self.id}\t\t NAME  : {self._name}\t\t FAMILY  :{self.__family}")
        


class Student(Person):
    __studentId=None
    def __init__(self,studentId,id,name,family):
        self.__studentId=studentId
        super().__init__(id,name,family)

    def showStudentInfo(self):
        print(self.__studentId)
        self.showPersonInfo()

student1=Student(1345,1,"parvin","rashin")
person1=Person(1,"Ahoura","garoosi")
print(person1.id)
print(person1._name)
# print(person1.__family)
print(person1.getFamily())
print("***************************************************")
person1.setFamily("winselt")
print(person1.getFamily())
print("***************************************************")
print(f"ID : {person1.id}\t\t NAME  : {person1._name}\t\t FAMILY  :{person1.getFamily()}")
person1.showPersonInfo()
print("***************************************************")
student1.showStudentInfo()




