# # oops--------------------------------------------------------------->
# # class Student:
# #     college_name="SIMS"  #Class attribute
#     # default constructor
#     # def __init__(self):
#     #     pass
#     #     parameterised conustructor
#     # def __init__(self,name,marks):
#     #     self.name =name #obj attr.> class atr.
#     #     self.marks=marks
#         # print(name)
#         # print(marks)
#         # print(self)
#         # print("adding new student")
#     # def welcome(self):
#     #     print("Welcome students",self.name)
#     # def getmarks(self):
#         # print()
# #         return  f"{self.name}'s marks are {self.marks}"
# #
# #
# # s1 = Student("Chintu",97)
# # print(s1.name,s1.marks,s1.college_name)
# # s1.welcome()
# # print(s1.getmarks())
# #
# # s2 = Student("Karn",66)
# # print(s2.name,s2.marks,s2.college_name)
# from CONSTRUCTOR_TASK1 import student
#
#
# # OOPS CONCEPT PART-2------------------------------------------------------------------------>
#
#
# # use of del keyword
#
# # class students:
# #     def __init__(self,name):
# #         self.name=name
# #         print(self.name)
# #
# # s1=students("Chintu")
# #
# # del s1.name
# # print(s1.name)
#
#
# # use of private concept...
# # class account:
# #     def __init__(self,acc,pas):
# #         self.acc=acc
# #         self.__pas=pas
# #     def __risk(self,id):
# #         self.id=id
# #         print(self.id)
# #
# # user=account("12345","54321")
# # print(user.acc)
# # print(user.pas)
# # user.__risk(123)
# # user.risk(123)
#
#
# # INHERITANCE------------------------------------------------------------>
#
#
# # multi-level inheritance & the use of super()......................
#
#
# # class car:
# #     colour="RED"
# #     def __init__(self,type):
# #         self.type = type
# #     @staticmethod
# #     def start():
# #         print("car starting")
# #     @staticmethod
# #     def stop():
# #        print("car stopped")
# # class Toyota(car):
# #     def __init__(self,name,type):
# #         super().__init__(type)
# #         self.name = name
# #         super().start()
#
# # class Fortuner(Toyota):
# #     def __init__(self,type):
# #         super().__init__(type)
# #         self.type=type
# #         super.start
#
#
# # car1=Toyota("prieus","electric")
# # print(car1.type)
# # print(car1.type)
#
#
#
#
# # MULTIPLE INHERITANCE---------------------------------------------->
#
# # class A:
# #     varA="Welcome to class A"
# # class B:
# #     varB="Welcome to class B"
# #
# # class C(A,B):
# #     varC="Welcome to class C"
# #
# # c1 = C()
# # print(c1.varA)
# # print(c1.varB)
# # print(c1.varC)
#
#
# # CLASS METHOD--------------------------------------------------------->

# class Person:
#     name="anonymous"
#     def changeName(self,name):
#         self.name=name
#         Person.name = name
#         self.__class__.name=name
#
#     @classmethod
#     def changename(cls,name):       #here, we are changing  directly class attribute.
#         cls.name=name
#
# s1=Person()
# s1.changename("Himanshu")
# print(s1.name)
# print(Person.name)
#
#
# # property decorator---------------------------------------------->
# #
# from CONSTRUCTOR_TASK1 import student


# class Students:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
        # self.percentage = str((self.phy+self.che+self.math)/3) + "%"

    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.che + self.math) / 3) + "%"
    #     print(self.percentage + ",Your percentage")

    # @property
    # def percentage(self):
    #     return str((self.phy + self.che + self.math) / 3) + "%"

# user=Students(36,48,39)
# print(user.percentage)

# user.phy=63
# print(user.phy)
# print(user.percentage)
# user.calcpercentage()
# print(user.calcpercentage())

