############ overloading
# print("ali")
# print(34)
# x=12.45
# print(x)
# print(x,end=" - ")
# print(len("Ahoura"))
# numlen=len([34,25,65,3654,12.56,89])
# print(numlen)
# print(23+45)
# print(3*" ali")

def sum(a,b):
    return a+b

# def sum(a,b,c):
#     return a+b+c


print(sum(10,20))          #Error midahad zira sum aval az beyn rafte ast
# print(sum(10,20,30))


def sum(a=0,b=0,c=0):
    return a+b+c

print(sum(10,20))         
print(sum(10,20,30))
print(sum(10))         
print(sum())

from multipledispatch import dispatch

@dispatch(int,int)
def sum(a,b):
    return a+b+10000

@dispatch(int,int,int)
def sum(a,b,c):
    return a+b+c


print(sum(10,20))          
print(sum(10,20,30))

# print(sum([2,3,4]))
# ==========================================================================
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def __add__(self,obj2):
        return self.age+obj2.age

    def __mul__(self,obj2):
        return self.age*(obj2.name +" ") 
       
    def __lt__(self,obj2):
        return self.age<obj2.age
    
person1=Person("Parvin",34)
person2=Person("Mostafa",32)

print(person1+person2)
print(person2*person1)
print(person2<person1)

# توابع با ورودی های پویا
def sum(*args):
    s=0
    for item in args:
        s+=item
    return s


print(sum(10,20))
print(sum(10,20,30,56,42.45,50))
print(sum(10))


def sum(datatype,*args):
    if (datatype=='int'):
        s=0
    elif (datatype=='str'):
        s=""
    for item in args:
        s+=item
    return s


print(sum('int',10,20))
print(sum('int',10,20,30,56,42.45,50))
print(sum('str',"Parvin"+" ","Ahoura"+" ","Rashin mehr"+" ","Garoosi"+" "))
print("parvin","Pouneh",340,end=" ")


