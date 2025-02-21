class Person:
    count=0
    def __init__(self,name,family):
        self.name=name
        self.family=family
        Person.count+=1

class Student(Person):
    def __init__(self, name, family):
        super().__init__(name, family)
   

    def __str__(self):
        return   self.name+"\t\t"+self.family
    
    def __del__(self):
        print(self.name+"\t\tthe end......")


person1=Person("Parvin","Rashin mehr")
print(str(person1))
print(Person.count)

person2=Person("Ahoura","Garoosi")
print(str(person2))
print(Person.count)

person1.name="shervin"
print(str(person1))
print(Person.count)

del(person2)


for i in range(1,10):
    print("hello")


person1=Person("Parvin","rashin mehr")
person2=Person("Ahoura","Garoosi")
person3=Student("Mostafa","Rad")
print(person1.count)
print(person2.count)
print(Person.count)
print(person3.__str__)

print("=========================================================")
person1=Person("Ali","Abdi")
person2=Person("maryam","mohammadi")
person1.count=30
Person.count=999
print(person1.count)
print(person2.count)
print(Person.count)


