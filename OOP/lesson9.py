class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showPersonInfo(self):
        print(self.__name)
        print(self.__age)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age   

    @age.setter
    def age(self,age):
        self.__age=age

person1=Person("Parvin",40)
person1.showPersonInfo()
# print(person1.name)
# print(person1.age)
print("===============================================================")
person1.name="Parmis"
person1.age=20
person1.showPersonInfo()

# print(person1.name)
# print(person1.age)
