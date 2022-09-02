#################################  INSTANCE VARIABLE  ##########################

## i. inside constructor by using self keyword.
# #Q1.
# class Test:
#     z=666
#     def __init__(self):
#         self.a=10
#         self.b=20
# t=Test()
# print(t.a,t.b)
# print(t.__dict__)
# print(Test.z)
# print(t.z,t.a,t.b)
##print(Test.a)      ## Self Keyword Print by using ClassName not possible.


## ii. inside instance method by using self keyword.
#Q1.
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def method(self):
#         self.c=30
# t=Test()
# t.method()
# print(t.a,t.b,t.c)
# print(t.__dict__)

# #Q2.
# class Test:
#     a=555
#     g=666
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.b=30
#         self.c=40
#         self.d=50
#     def m2(self):
#         self.a=60
#         self.c=70
#         self.e=80
# t1=Test()
# print(t1.a,t1.b)
# print(t1.__dict__)
# t1.m1()
# t2=Test()
# t2.m2()
# print(t1.__dict__)
# print(t2.__dict__)
# print(t1.b,t1.c,t1.d)
# print(t2.a,t2.c,t2.e)

## iii. outside of class by using object ref.variable.
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def method(self):
#         self.c=30
# t=Test()
# t.d=40
# print(t.__dict__)

## Q2.
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t=Test()
# t.d=40
# t.m1()
# print(t.__dict__)
# print(t.a,t.b,t.c,t.d)

############## Access
##Q1.
# class Test:
#     a=455
#     f=555
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
#     def m1(self):
#         print("Method Run")
#         print(self.a)
#         print(self.b)
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# print(t.a,t.b,t.c,t.d)


################## Delete

## Q1.
# class Test:
#     a=555
#     k=666
#     p=777
#     del p
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
#         del self.c
#     def m1(self):
#         self.e=50
#         self.f=60
#         del self.b
#         del self.e
#         self.g=70
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.a
# del t.f
# print(t.__dict__)


###################  Change
# ##Q1.
# class Test:
#     a=555
#     k=666
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def m1(self):
#         self.a=40
#         self.b=50
#         self.d=60
# t1=Test()
# t1.b=200
# print(t1.__dict__)
# t1.m1()
# # t1.b=200
# t1.d=600
#
# t2=Test()
# t2.m1()
# print(t1.__dict__)
# print(t2.__dict__)


######################################### [ STATIC VARIABLE ] ####################################
##Q1.
# class test:
#     a=555
#     def __init__(self):
#         test.a=1
#         test.b=2
#     def m1(self):
#         test.a=10
#         test.b=20
#     @classmethod
#     def m2(cls):
#         test.a=30
#         cls.b=40
#     @staticmethod
#     def m3():
#         test.a=50
#         test.b=60
# t1=test()
# t1.m2()
# print(t1.a,t1.b)
# t1.m3()
# print(t1.a,t1.b)
# t1.m1()
# print(t1.a,t1.b)
# t1.m3()
# print(t1.a,t1.b)

###Q2.
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         test.a=1
#         test.b=2
#     def m1(self):
#         test.a=10
#         test.b=20
#     @classmethod
#     def m2(cls):
#         test.a=30
#         cls.b=40
#     @staticmethod
#     def m3():
#         test.a=50
#         test.b=60
# t1=test()
# print(test.a)
# print(t1.__dict__)
# t1.m1()
# print(t1.a,t1.b)
# print(t1.__dict__)
# t1.m2()
# print(t1.a,t1.b)
# t1.m3()
# print(t1.a,t1.b)
# print(test.z)
# print(test.a)
# print(t1.__dict__)



########### Miscellaneous [Instance variable + Static Variable] #########

###### General
## Q1.
# class Test:
#     a=15
#     def __init__(self):
#         self.b=20
#
# t1=Test()
# print(t1.a,t1.b)
# print(Test.a)

### Q2
# class Test:
#     a=15
#     def __init__(self):
#         self.b=20
#         self.a=10
#
# t1=Test()
# print(t1.a,t1.b)
# print(Test.a)


# ### Q3.
# class Test:
#     a=15
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         self.b=30
#     def m2(self):
#         self.b=40
#         self.a=50
# t1=Test()
# print(t1.a,t1.b)
# print(Test.a)
#
# t1.m1()
# print(t1.a,t1.b)
# print(Test.a)
#
# t1.m2()
# print(t1.a,t1.b)
# print(Test.a)


## Q4
# class test:
#     def __init__(self):
#         pass
#     def m1(self):     ## Instance Method= when this mehod run below all same instance value come when if below are class & Static mehod avilable then.
#         self.a=10
#         self.b=20
#     @classmethod    ## class Method= i:if above instance method & constructor not run then same class method value come.
#     def m2(cls):    ##               ii:if above first instance method run then class method run then instance method value come.
#         cls.a=30    ##               iii:if above first constructor run then class method run then constuctor value come.
#         test.b=40
#     @staticmethod   ## Same as class mehod only i: fist here static value come.
#     def m3():
#         test.a=50
#         test.b=60



# ### Q1
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         self.a=1
#         self.b=2
#         test.c=3
#     def m1(self):
#         pass
#     @classmethod
#     def m2(cls):
#         cls.a=30
#         test.b=40
#         test.c=50
#         test.d=60
#     @staticmethod
#     def m3():
#         test.a=70
#         test.b=80
#         test.c=90
#         test.e=100
# t1=test()
# print(t1.__dict__)
# t1.m2()
# print(t1.a,t1.b,t1.c,t1.d)
# t1.m3()
# print(t1.a,t1.b,t1.c,t1.e)
# print(t1.__dict__)



# ## Q2
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         pass
#     def m1(self):
#         self.a=10
#         test.b=20
#         self.g=25
#     @classmethod
#     def m2(cls):
#         cls.a=30
#         test.b=40
#         test.c=50
#     @staticmethod
#     def m3():
#         test.a=60
#         test.b=70
#         test.c=80
# t1=test()
# print(t1.__dict__)
# t1.m2()
# print(t1.a,t1.b,t1.c)
# t1.m3()
# print(t1.a,t1.b,t1.c)
# t1.m1()
# print(t1.a,t1.b,t1.g)
# t1.m2()
# print(t1.a,t1.b,t1.c)
# t1.m3()
# print(t1.a,t1.b,t1.c)
# print(t1.__dict__)


# ### Q3
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         self.a=1
#         self.b=2
#         test.c=3
#     def m1(self):
#         self.a=10
#         self.b=20
#         test.c=25
#     @classmethod
#     def m2(cls):
#         cls.a=30
#         test.b=40
#         test.c=50
#     @staticmethod
#     def m3():
#         test.a=60
#         test.b=70
#         test.c=80
# t1=test()
# print(t1.__dict__)
# t1.m2()
# print(t1.a,t1.b,t1.c)
# t1.m3()
# print(t1.a,t1.b,t1.c)
# t1.m1()
# print(t1.a,t1.b,t1.c)
# t1.m3()
# print(t1.a,t1.b,t1.c)
# t1.m2()
# print(t1.a,t1.b,t1.c)
# print(t1.__dict__)



# #### Q4
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def m1(self):
#         self.a=10
#         self.b=20
#     def m2(self):
#         self.a=30
#         self.b=40
#     @classmethod
#     def m3(cls):
#         cls.a=50
#         test.b=60
#     @staticmethod
#     def m4():
#         test.a=70
#         test.b=80
# t1=test()
# print(t1.__dict__)
# t1.m1()
# print(t1.a,t1.b)
# t1.m2()
# print(t1.a,t1.b)
# t1.m3()
# print(t1.a,t1.b)
# t1.m4()
# print(t1.a,t1.b)
# print(t1.__dict__)



# #### Q5.
# class test:
#     a=555
#     z=666
#     def __init__(self):
#         self.a=1
#         self.b=2
#         test.c=3
#         test.e=4
#     def m1(self):
#         self.a=10
#         self.b=20
#         test.c=25
#     def m2(self):
#         self.a=30
#         self.b=40
#         test.c=45
#         test.e=46
#     @classmethod
#     def m3(cls):
#         cls.a=50
#         test.b=60
#         test.e=65
#     @staticmethod
#     def m4():
#         test.a=70
#         test.b=80
# t1=test()
# print(test.a)
# ##print(text.b)      ## self keyword if print(test.b) then error
# print(test.c)
#
# print("M1m1m1m1m1m1m1m")
# t1.m1()
# print(test.a)
# ##print(text.b)      ## self keyword if print(test.b) then error
# print(test.c)
#
# print("m2m2m2m2m2m2m2m2m2m")
# t1.m2()
# print(test.a)
# ##print(text.b)      ## self keyword if print(test.b) then error
# print(test.c)   ##if print(test.b) then error
#
# print("m3m3m3m3m3m3m3m3m3m3")
# t1.m3()
# print(test.a)
# print(test.b)
# print(test.c)
# print(test.e)
#
# print("m4m4m4m4m4m4m4m4m4")
# t1.m4()
# print(test.a)
# print(test.b)
# print(test.c)
# print(test.e)


################################# Modify / Change

# ### Q1
# class Test:
#     a=15
#     def __init__(self):
#         self.b=20

# t1=Test()
# t2=Test()
# t1.b=999
# Test.a=888
# print(t1.a,t1.b)
# print(t2.a,t2.b)


# ### Q2
# class Test:
#     a=15
#     def __init__(self):
#         self.b=20
#         Test.c=30
#         self.d=40
#
# t1=Test()
# t2=Test()
# print(t1.c)
# t1.b=999
# Test.a=888
# Test.c=333
# Test.d=444     ## consider as newly add
# print(t1.a,t1.b,t1.c,t1.d)
# print(Test.c)
# print(Test.d)   ## Newly added taken
# print(t2.a,t2.b,t2.c,t2.d)
#

# ## Q3
# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(SELF):
#         SELF.a=888
#         SELF.b=999
# t1=Test()
# t2=Test()
# print(t2.a,t2.b)
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(Test.a)


### Q4
# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
#     @classmethod
#     def m1(cls):
#         cls.a=888
#         cls.b=999
# t1=Test()
# t2=Test()
# print(t2.a,t2.b)
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(Test.a,Test.b)

################## General

##################### Delete

# ## Q1
# class Test:
#     a=10
#     pass
#
# t1=Test()
# # del t1.a
# print(t1.a)
# del Test.a
# print(Test.a)

# ## Q2
# class test:
#     a=1
#     def __init__(self):
#         test.a=5
#         test.b=6
#         del test.a
#     def m1(self):
#         test.c=10
#         test.d=20
#         del test.b
#     @classmethod
#     def m2(cls):
#         cls.e=30
#         cls.f=40
#         del test.c
# t1=test()
# t1.m1()
# t1.m2()
# print(t1.__dict__)
# print(t1.d,t1.e,t1.f)
# #print(test.a)          ### this are deleted
# #print(t1.a,t1.b,t1.c)  ### this are deleted


####################################################### [ 3: LOCAL VARIABLE ] #############################

# ##Q1.
# class test:
#     def m1(self):
#         a=10
#         print(a)
#     def m2(self):
#         b=20
#         print(b)
# t=test()
# t.m1()
# t.m2()


# ##Q2.
# class test:
#     def m1(self):
#         a=10
#         c=20
#         print(a)
#     def m2(self):
#         b=30
#         print(b)
#      ## print(c)   ## Error because inside method not call any (self or className)
# t=test()
# t.m1()
# ##print(t.c)    ## Error because inside method not call any (self or className)
# t.m2()




############################################################################################################
#                  [ TYPES OF METHODS ]
#                    1-Instance Method
#                    2-Class Method
#                    3-Static Method

##############  1-Instance Method:

# #Q1:
# class Student:
#     def __init__(self,name,marks):
#         self.a=name
#         self.b=marks
#     def display(self):
#         print(self.a)
#         print(self.b)
#     def grade(self):
#         if self.b>=60:
#             print("First Class")
#         elif self.b>=50:
#             print("Second Class")
#         elif self.b>=35:
#             print("Third Class")
#         else:
#             print("Failed Exam")
#
# n=int(input("Enter Number of Students :"))
# for i in range(n):
#     a=input("Enter Name :")
#     b=int(input("Enter Marks :"))
#     print()
#     t=Student(a,b)
#     t.display()
#     t.grade()


# #Q2:
# class Student:
#     def __init__(self,name,marks):
#         self.Name=name
#         self.Marks=marks
#     def display(self):
#         print("Hii :",self.Name)
#         print("Your Marks :",self.Marks)
#     def grade(self):
#         if self.Marks>=60:
#             print("First Class")
#         elif self.Marks>=50:
#             print("Second Class")
#         elif self.Marks>=35:
#             print("Third Class")
#         else:
#             print("Failed Exam")
#
# n=int(input("Enter Number of Students :"))
# for i in range(n):
#     Name=input("Enter Student Name :")
#     Marks=int(input("Enter Student Marks :"))
#     #print()                 ## No need print all ready available in display
#     t=Student(Name,Marks)
#     t.display()
#     t.grade()


# #Q3:
# class Student:
#     def __init__(self,name,marks):
#         self.Name=name
#         self.Marks=marks
#     def display(self):
#         print("Student Sequnce No.:", i + 1)
#         print("Hii :",self.Name)
#         print("Your Marks :",self.Marks)
#     def grade(self):
#         if self.Marks>=60:
#             print("First Class")
#         elif self.Marks>=50:
#             print("Second Class")
#         elif self.Marks>=35:
#             print("Third Class")
#         else:
#             print("Failed Exam")
#
# n=int(input("Enter Number of Students"))
# for i in range(n):
#     Name=input("Enter Name")
#     Marks=int(input("Enter Marks"))
#     #print()                 ## No need print allredy available in display
#     t=Student(Name,Marks)
#     t.display()
#     t.grade()

########## SETTER & GETTER

# # ## Q1.
# class Student:
#     def setmethod1(self,name):
#         self.a=name
#     def getmethod1(self):
#         return self.a
#     def setmethod2(self,marks):
#         self.b=marks
#     def getmethod2(self):
#         return self.b
# n=int(input("Enter No.of Students :"))
# for i in range(n):
#     a=input("Enter Student Name :")
#     b=int(input("Enter Student Marks :"))
#
#     t=Student()
#     t.setmethod1(a)
#     t.setmethod2(b)
#     print("Hii I'm :",a)
#     print("My Marks :",b)
#   ##### or both are execute
#     print("I'm :",t.a)
#     print("My % :",t.b)


# ## Q2.
# class Student:
#     def setmethod1(self,name):
#         self.a=name
#     def getmethod1(self):
#         return self.a
#     def setmethod2(self,marks):
#         self.b=marks
#     def getmethod2(self):
#         return self.b
# n=int(input("Enter No.of Students :"))
# for i in range(n):
#     name=input("Enter Student Name :")
#     marks=int(input("Enter Student Marks :"))
#
#     t=Student()
#     t.setmethod1(name)
#     t.setmethod2(marks)
#     print("Hii I'm :",name)
#     print("My Marks :",marks)
#     #####       Or both are execute
#     print("I'm :",t.a)
#     print("My % :",t.b)


# ## Q3.
# class Student:
#     def setmethod1(self,name,marks):
#         self.a=name
#         self.b = marks
#     def getmethod1(self):
#         return self.a, self.b
#         ###  Or both are possible
#         # return self.a
#         # return self.b
#
# n=int(input("Enter No.of Students :"))
# for i in range(n):
#     name=input("Enter Student Name :")
#     marks=int(input("Enter Student Marks :"))
#
#     t=Student()           ## HERE VALUE PASSING IS NOT POSSIBLE
#     t.setmethod1(name,marks)
#     print("Hii I'm :",name)
#     print("My Marks :",marks)
#   #### or both are execute
#     print("i'm :",t.a)
#     print("my % :",t.b)



############################   [ CLASS METHOD ]

# ##Q1.
# class animal:
#     leg=4
#     @classmethod
#     def walk(animal,name):
#         print("{}: walks with {} :legs".format(name,animal.leg))
#
# animal.walk("Dog")
# animal.walk("Cat")
#  ##OR
# t=animal()
# t.walk("Deer")
# t.walk("Rabbit")


# ##Q2.
# class animal:
#     leg=4
#     #legs=2
#     @classmethod
#     def walk(cls,name):
#         print("{}: walks with {} :legs".format(name,cls.leg))
#
#     @classmethod
#     def walks(cls,name):
#         legs = 2
#         print("{}: walks with {} :legs".format(name,legs))
#         #print("{}: walks with {} :legs".format(name,cls.legs))
# animal.walk("Dog")
# animal.walks("Chim")
# ## or
# t=animal()
# t.walk("CAt")
# t.walks("Peacoak")



##########################################  [ STATIC METHOD ]

# ## Q1.
# class Math:
#     @staticmethod
#     def add(x,y):
#         print("add:",x+y)
#     @staticmethod
#     def mul(x,y):
#         print("mul:",x*y)
#     @staticmethod
#     def average(x,y):
#         print("average:",(x+y)/2)
# t=Math()
# t.add(2,3)
# t.mul(4,5)
# t.average(6,7)
# ## OR
# print("Other Mehod answer")
# Math.add(10,20)
# Math.mul(10,20)
# Math.average(10,20)


## Passing member one class to another class:

# class A:    ## PASSING MEMBER ONE CLASS TO ANOTHER CLASS
#     def __init__(self,number,name,salary):
#         self.a=number
#         self.b=name
#         self.c=salary
#     def display(self):
#         print("Employee Number :",self.a)
#         print("Employee Name :",self.b)
#         print("Employee Salary :",self.c)
# class B:
#     def modify(emp):
#         emp.c=emp.c+100     ##emp=className & v=variable
#         emp.display()
# t=A(25,"RAJ",85)
# B.modify(t)


## Inner Class: CLASS INSIDE CLASS

# ## Q1
# class Outer:
#     def __init__(self):
#         print("Outer class")
#     class Inner:
#         def __init__(self):
#             print("Inner class-c")
#         def m1(self):
#             print("inner class-m")
# t=Outer()
# i=t.Inner()
# i.m1()
#  ## OR
# i=Outer().Inner()
# i.m1()
#  ## OR
# Outer().Inner().m1()

# ## Q2.
# class Human:
#     def __init__(self):
#         self.a="RAJ"
#         self.b=self.DOB()         ## This line is use only for 2nd condition is possible,for 1st condition is G.C.
#     def display(self):
#         print("My Name is :",self.a)
#
#     class DOB:
#         def __init__(self):
#             self.dd=15
#             self.mm=8
#             self.yr=1947
#         def display1(self):
#             print("{}\{}\{}=Day,Month,Year".format(self.dd,self.mm,self.yr))
# t=Human()
# t.display()
# i=t.DOB()
# i.display1()
# # ## OR
# t=Human()
# t.display()
# i=t.b
# i.display1()


# ## Q3.
# class Human:
#     def __init__(self):
#         self.name="Sunny"
#         self.brain=self.Brain()
#         self.head=self.Head()
#         # self.brain.think()
#         # self.head.talk()
#     def display(self):
#         print("Hello :",self.name)
#         # self.brain.think()
#         # self.head.talk()
#
#     class Head:
#         def talk(self):
#             print("Talking")
#     class Brain:
#         def think(self):
#             print("Thinking")
# t=Human()
# t.display()
# Human().Head().talk()
# Human().Brain().think()


# ## Q4.
# class Human:
#     def __init__(self):
#         self.name="Sunny"
#         self.brain=self.Brain()
#         self.head=self.Head()
#         self.head.talk()
#         self.brain.think()
#     def display(self):
#         print("Hello :",self.name)
#         self.head.talk()
#         self.brain.think()
#
#     class Head:
#         def talk(self):
#             print("Talking")
#     class Brain:
#         def think(self):
#             print("Thinking")
# t=Human()
# print("For Next Type Answer")
# ## or
#
# t=Human()
# t.display()



# ## Q5
# class Test:
#     def m1(self):
#         a,b=5,10
#         print("First Step------------------------")
#         print("Addition :",a+b)
#         print("Substraction :",a-b)
#         print("product :",a*b)
#
#         a,b=11,12
#         print("Second Step--------------------------")
#         print("Addition :",a+b)
#         print("Substraction :",a-b)
#         print("product :",a*b)
#
#         a,b=15,20
#         print("Third Step------------------------")
#         print("Addition :",a+b)
#         print("Substraction :",a-b)
#         print("product :",a*b)
# t=Test()
# t.m1()



# ## Q6.
# class Test:
#     def m1(self,a,b):        ## self parameter taken i.e print no need to take ClassName
#         print("Addition :",a+b)
#         print("Substraction :",a-b)
#         print("product :",a*b)
# t=Test()
# print("First Step------------------------")
# t.m1(5,6)                                     ## self parameter taken i.e print no need to take ClassName
# print("Second Step------------------------")
# t.m1(11,12)                                  ## self parameter taken i.e print no need to take ClassName
# print("Third Step------------------------")
# t.m1(15,20)                                 ## self parameter taken i.e print no need to take ClassName

# ## Q7.
# class Test:
#     def m1(a,b):               ## self parameter not taken i.e print by using ClassName
#         print("Addition :",a+b)
#         print("Substraction :",a-b)
#         print("product :",a*b)
#
#
# print("First Step------------------------")
# Test.m1(5,10)                           ## self parameter not taken i.e print by using ClassName
# print("Second Step------------------------")
# Test.m1(11,12)                          ## self parameter not taken i.e print by using ClassName
# print("Third Step------------------------")
# Test.m1(15,20)                          ## self parameter not taken i.e print by using ClassName



# ## Q8.
# class Test:
#     def m1(self):
#         def cal(a,b):
#             print("Addition :",a+b)
#             print("Substraction :",a-b)
#             print("product :",a*b)
#
#         print("First Step------------------------")
#         cal(5,10)
#         print("Second Step------------------------")
#         cal(11,12)
#         print("Third Step------------------------")
#         cal(15,20)
# t=Test()
# t.m1()


################################## [ Garbage Collector ] #########################
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())
