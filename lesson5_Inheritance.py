#*******************************single inheritance*************************************
class A:
    def __init__(self):
        print("run init of A class")

    def showA(self):
        print("AAAAA")

# ---------------------------------------------------------------
class B(A):
    def __init__(self):
        A.__init__(self)
        print("run init of B class")
        
    def showB(self):
        print("BBBBB")
# ---------------------------------------------------------------
b=B()
# b.showA()
# b.showB()
# #================================================================================================
# *********************************multiple inheritance***********************************

# class A:
#     def __init__(self):
#         print("run init of A class")

#     def showA(self):
#         print("AAAAA")

# # ---------------------------------------------------------------
# class B:
#     def __init__(self):
#         print("run init of B class")
        
#     def showB(self):
#         print("BBBBB")
# # ---------------------------------------------------------------
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("run init of C class")
        
#     def showC(self):
#         print("CCCCC")
# # ---------------------------------------------------------------
# c=C()
# c.showA()
# c.showB()
# c.showC()
#================================================================================================
# *********************************multi level inheritance***********************************
# class A:
#     def __init__(self):
#         print("run init of A class")

#     def showA(self):
#         print("AAAAA")

# # ---------------------------------------------------------------
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         print("run init of B class")
        
#     def showB(self):
#         print("BBBBB")
# # ---------------------------------------------------------------
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         print("run init of C class")
        
#     def showC(self):
#         print("CCCCC")
# # ---------------------------------------------------------------

# f=C()
# f.showA()
# f.showB()
# f.showC()
# #================================================================================================
# *********************************hierachical inheritance***********************************
# class A:
#     def __init__(self):
#         print("run init of A class")

#     def showA(self):
#         print("AAAAA")

# # ---------------------------------------------------------------
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         print("run init of B class")
        
#     def showB(self):
#         print("BBBBB")
# # ---------------------------------------------------------------
# class C(A):
#     def __init__(self):
#         # A.__init__(self)
#         print("run init of C class")
        
#     def showC(self):
#         print("CCCCC")
# # ---------------------------------------------------------------
# b=B()
# c=C()
# b.showA()
# b.showB()
# # c.showA()
# c.showC()
# ================================================================================================
# *********************************Hybrid inheritance***********************************
# class A:
#     def __init__(self):
#         print("run init of A class")

#     def showA(self):
#         print("AAAAA")

# # ---------------------------------------------------------------
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         print("run init of B class")
        
#     def showB(self):
#         print("BBBBB")
# # ---------------------------------------------------------------
# class C(A):
#     def __init__(self):
#         A.__init__(self)
#         print("run init of C class")
        
#     def showC(self):
#         print("CCCCC")
#  # ---------------------------------------------------------------
# class D(B,C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("run init of D class")
        
#     def showD(self):
#         print("DDDDD")       
# # ---------------------------------------------------------------
# d=D()
# d.showA()
# d.showC()
# d.showB()
# d.showD()