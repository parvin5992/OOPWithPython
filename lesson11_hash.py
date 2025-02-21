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
    
    def __hash__(self) -> int:
        return hash(self.__name)+hash(self.__age)
    
    def __str__(self):
        return f"{self.__name}\t\t{self.__age}"
    
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1=Person("mehdi",34)
person2=Person("ali",43)
person3=Person("mehdi",34)
person4=Person("ali",23)
m1=MyClass("ali",23)

if person1==person3:
    print("yes")

else:
    print("No")




if person4==m1:
    print("yes")

else:
    print("No")

print(hash(person1))

set1={person1,person2,person3,person4}
for person in set1:
    print(person)