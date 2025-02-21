from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def showInfo(self):
       pass
    
# =======================================================================================
    
class Student(Person):
    def __init__(self,name,age,studentId):
        super().__init__(name,age)
        self.__studentId=studentId

    def showInfo(self):
        print(f"Name: {self.name}\t\tAge: {self.age}\t\tStudent Id :  {self.__studentId}")
       

# ==================================================================================

class Teacher(Person):
    def __init__(self,name,age,teacherCode):
        super().__init__(name,age)
        self.__teacherCode=teacherCode

    def showInfo(self):
        print(f"Name: {self.name}\t\tAge: {self.age}\t\tteacher Id :  {self.__teacherCode}")
       

st1=Student("mehdi",34,10)
te2=Teacher("ali",43,100)
st1.showInfo()
print("===========================================")
te2.showInfo()