class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    

    def showPersonInfo(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def sum(x,y):
        return x+y
    
    @classmethod
    def mul(cls,x,y):
        return cls.sum(x,y)+2000
        

person1=Person("Parvin",40)
person1.showPersonInfo()

print(Person.sum(50,40))

print(Person.mul(50,4))
