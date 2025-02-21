class Person:
    __x=None
    _y=None
    z=None

    def __init__(self,name,family,age):
        self.__name=self.__toPascalCase(name)
        self.__family=self.__toPascalCase(family)
        self.__age=(age)
        print(f"x:  {self.__x}\t\ty: {self._y}\t\tz:  {self.z}")

#     # def __toPascalCase(self,str1):
#     #     strList=list(str1)
#     #     strList[0]=chr(ord(strList[0])-32)
#     #     self.__x=2550
#     #     return ''.join(strList)
#     # ********or************
    def __toPascalCase(self,Str1):
        listStr1=list(Str1)
        sum=ord(listStr1[0])
        if sum>=65 and sum<=96:
            listStr1[0]= listStr1[0]
            return ''.join(listStr1)
        elif sum>=97 and sum<=129:
           listStr1[0]=chr(ord(listStr1[0])-32)
           return ''.join(listStr1)
        else:
            return "Error"
        
    


    def _showPersonInfo(self):
        print(f"Name: {self.__name}")
        print(f"family:  {self.__family}")
        print(f"Age:  {self.__age}")
        self.__x=4500
        self._y=100
        self.z=5
        print(f"x:  {self.__x}\t\ty: {self._y}\t\tz:  {self.z}")
        

    def _getFullLenght(self):
        return len(self.__name)+len(self.__family)
        

# # =====================================================================================

class Student(Person):
    def __init__(self,name,family,age,studentId):
        super().__init__(name,family,age)
        self.__studentId=studentId

    def showStudentInfo(self):
        self._showPersonInfo()
        self.z=2000
        self._y="bbbb"
        print(f"Student Id :  {self.__studentId}")
        print(f"lenght:  {self._getFullLenght()}")
        print(f"y: {self._y}\t\tz:  {self.z}")

# # ==================================================================================

class Teacher(Person):
    def __init__(self,name,family,age,teacherCode):
        super().__init__(name,family,age)
        self.__teacherCode=teacherCode

    def showTeacherInfo(self):
        self._showPersonInfo()
        self._y="cccccc"
        self.z=6542
        print(f"Teacher Code : {self.__teacherCode}")
        print(f"lenght:  {self._getFullLenght()}")
        print(f"y: {self._y}\t\tz:  {self.z}")
  
# # ======================================================================================
person1=Person("parvin","Rashin mehr",37)
person1._showPersonInfo()


stu1=Student("Ahoura", "Garoosi", 34,1000)
stu1.showStudentInfo()

Te1=Teacher("Parmis","Rad",36,2562)
Te1.showTeacherInfo()

