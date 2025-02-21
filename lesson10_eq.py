class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showPersonInfo(self):
        print(self.__name)
        print(self.__age)

    def __eq__(self,obj2):
        if not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self.__age==obj2.__age
    
    def __str__(self):
        return f"{self.__name}\t\t{self.__age}"
    
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1=Person("ahmad",23)
person1.showPersonInfo()
person2=Person("ali",43)
person3=Person("ahmad",23)
 
if person1==person3:
    print("yes")

else:
    print("No")

m1=MyClass("ahmad",23)
if person1==m1:
    print("yes")

else:
    print("No")

print(str(person1))
print(person1)
print(person1.__str__)

