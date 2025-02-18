# ---------------------------------------- overriding--------------------------------------
class A:
    def fun1(self):
        print("A class run Fun1")

    def fun2(self):
        print("A class run Fun2")

    def fun3(self):
        print("A class run Fun3")

    def mul(self,a,b):
        print(a+b)

# # #3------------------------------------------------------------------------
class B:
    def fun1(self):
        print("B class run Fun1")

    def fun2(self):
        print("B class run Fun2")

    # def fun3(self,a,b):
    #     return a+b
    
    def mul(self,a,b):
        print((a+b)*1000)
##======================================================================
######model1

a=A()
b=B()

a.fun1()
a.fun2()

b.fun1()
b.fun2()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#######model2
def func(obj):
    obj.fun1()
    obj.fun2()
    obj.mul(30,4)

a=A()
b=B()

func(a)
func(b)
#######################33or or  or or or or or or or###########################
########### model3
a=A()
b=B()
c=A()

for obj in (a,b,c):
    obj.fun1()
    obj.fun2()
    obj.mul(14,4)

# $$$$$$$$$$$$$$$$$$$$$$$$$$11111111111111111111111$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class A:
    def show(self):
        print("AAAAA")

# # ---------------------------------------------------------------
class B(A):     
    def show(self):
        print("BBBBB")
        return A.show(self)
# # ---------------------------------------------------------------
# a=A()
# a.show()

b=B()
b.show()
super(B,b).show()
# ++++++++++++++++++
a=A()
a.show()
b=B()
b.show()
# &&&&&&&&&&&&&&&22222222222222222222222&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
class A:
    def show(self):
        print("AAAAA")

# # ---------------------------------------------------------------
class B:
    def show(self):
        print("BBBBB")
# # ---------------------------------------------------------------
class C(B,A):
    def show(self):
        print("CCCCC")
        return A.show(self)
# # # ---------------------------------------------------------------
c=C()
c.show()
super(C,c).show()
# # &&&&&&&&&&&&&&&&&333333333333333333333333333&&&&&&&&&&&&&&&&&&&&&&&&&
class A:
    def show(self):
        print("AAAAA")

# # ---------------------------------------------------------------
class B(A):    
    def show(self):
        print("BBBBB")
        return A.show(self)
# # ---------------------------------------------------------------
class C(B): 
#  &&&&&&&&&&&&&&&444444444444444444444444&&&&&&&&&&&&&&&&&&&&&&

    def show(self):
        print("AAAAA")

# ---------------------------------------------------------------
class B(A):
        
    def show(self):
        print("BBBBB")
        # return A.show(self)
# ---------------------------------------------------------------
class C(A):
        
    def show(self):
        print("CCCCC")
        return A.show(self)

c=C()
b=B()
b.show()
c.show()
super(C,c).show()
#  &&&&&&&&&&&&&&&5555555555555555555555&&&&&&&&&&&&&&&&&&&&&&
class A:
    def show(self):
        print("AAAAA")

# # ---------------------------------------------------------------
class B(A):
    def show(self):
        print("BBBBB")
        # return A.show(self)
# # ---------------------------------------------------------------
class C(A):
    def show(self):
        print("CCCCC")
        return A.show(self)
#  # ---------------------------------------------------------------
class D(C,B):
    def show(self):
        print("DDDDD") 
        return B.show(self)  
# # ---------------------------------------------------------------
d=D()
d.show()
super(D,d).show()