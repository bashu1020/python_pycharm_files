# class Student:
#
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#
#     def talk(self):
#         print("hello my name is",self.name)
#         print("my rollno is",self.rollno)
#         print("my marks is",self.marks)
#
# s1=Student("baswaraj",100,96)
# s1.talk()
# s2=Student("suresh",101,98)
# s2.talk()

#
# s2=Student("sunil",101,98)
# s2.talk()

# class Test:
#     def __init__(self):
#         self.a=10
#     def m1(self):
#         self.a=777
#         self.b=888
# t=Test()
# t.m1()
# t.b=333
# t.c=555
# print(t.__dict__)

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
# t1=Test()
# t1.a=333
# t2=Test()
# t2.b=444
# print(t1.a,t1.b)
# print(t2.a,t2.b)


# class test:
#     a=10
#     def __init__(self):
#         test.e=50
#     @classmethod
#     def m2(cls):
#         cls.a=70
#         test.c=80
#     @staticmethod
#     def m3():
#         test.d=90
#         test.a=75
#         print(test.a)
#     def m4(self):
#         print(test.a)
# print(test.a)
# t=test()
# print(test.e)
# test.m2()
# print(test)
# print(test.c)
# test.m3()
# t.m4()
# t1=test()
# t2=test()
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(t1.__dict__)
# print(t2.__dict__)
# print(test.a,test.b)

# class student:
#     def  __init__(self,rollno,marks):
#         self.rollno=rollno
#         self.marks=marks
#     def talk(self):
#         print(self.rollno)
#         print(self.marks)
# s1=student(101,65)
# s1.talk()
# s2=student(202,55)
# s2.talk()


### 1-inside of constructor by using self variable
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
# e=test()
# print(e.__dict__)


### 2-inside of Instance method by using self variable
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def method(self):
#         self.c=30
# e=test()
# e.method()
# print(e.__dict__)

### 3-outside of class by using a object ref variable
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def method(self):
#         self.c=30
# e=test()
# e.method()
# e.d=40
# print(e.__dict__)



## Access  instance varible
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         # self.c=30
#     def method(self):
        # print("Method bkmmsx")
        # print(self.a)
        # print(self.b)
    # def method2(self):
    #     print(self.c)
# e=test()
# e.method()
# e.method2()
# e.c=30
# print(e.__dict__)
# print(e.a,e.b,e.c)


##  Delete

# class test:
#     def __init__(self):
#
#         self.a=10
#         self.b=20
#         self.c=30
#     def method(self):
#
#         del self.b
#         print(self.a)
#         print(self.c)
# e=test()
# e.method()
# del e.c
# print(e.__dict__)

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.r=40
#         del self.a
#     def method(self):
#         del self.b
# e=test()
# e.method()
# del e.c
# print(e.__dict__)


##  Change
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def method(self):
#          self.c=30
#
# e1=test()
# e1.method()
# e1.c=50
# e1.b=55
# e2=test()
# e2.method()
# print(e1.__dict__)
# print(e2.__dict__)


####################################################### Static Variable  #################

# class test:
#     a=10
#     def __init__(self):
#         self.b=20
#         test.c=55
#     def m1(self):            ## Instance method
#         test.d=30  # Static variable
#         self.e=65  # instance variable
#     @classmethod
#     def m2(cls):             ## Class Method
#         cls.f1=40
#         test.f2=50
#     @staticmethod
#     def m3():                ## Static method
#         test.g=60
#
#
# t=test()
# t.m1()
# t.m2()
# t.m3()
# t.h=70              ## Outside class instance variable
# test.i=80           ## outside class static variable
#
# print(t.a,t.b,t.c,t.d,t.e,t.f1,t.f2,t.g,t.h,t.i)



######################################################### 3-Local Variable #####################

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c = 30
#
#     def m1(self):
#         self.c=60
#         print(self.c)
#     def m2(self):
#         print(self.c)
#         del self.c
# t=test()
# t.m1()
# t.m2()
# t.c=40
# del t.c
# t.d=50
# print(t.__dict__)

######################  ststic
# class test:
#     a=10
#     c=55
#     def __init__(self):
#         self.c=555
#         test.b=20
#     def m1(self):
#         test.c=30
#     @classmethod
#     def m2(cls):
#         test.d=40
#     @staticmethod
#     def m3():
#         test.e=50
# print(test.c)
# t=test()
# print(t.c)
# print(t.a)
# print(t.b)
# t.m1()
# print(test.c)
# t.m2()
# print(test.d)
# t.m3()
# print(test.e)
# test.f=70
# del test.f
# print(test.f)


# class test:
#     # a=10
#     def __init__(self):
#           pass
#         # self.a=20
#         # self.b=30
#     def m(self):
#         self.a=111
#         self.b=222
#
#     @classmethod
#     def m1(cls):
#         cls.a=40
#         cls.b=50
#     @staticmethod
#     def m2():
#         test.a=60
#         test.b=70
#
# t1=test()
# t2=test()
# t2.m()
# print(t2.a,t2.b)
# t1.m()
#
#
# print(test.a,test.b)
# # t2.m()
# # print(t2.a,t2.b)

# class baswaraj:
#     a=10
#     b=20
#     @staticmethod
#     def add(x,y):
#         baswaraj.a
#         baswaraj.b
#         print(baswaraj.a-baswaraj.b)
#         print("the sum",x+y)
#
# baswaraj.add(10,20)


####################
# class animal:
#     # legs=4
#     @classmethod
#     def walk(cls,name,legs):
#         cls.legs=legs
#
#         print('{}walks with {} legs'.format(name,cls.legs))
# a=animal()
# a.walk('dog',4)
# a.walk('cat',3)
# animal.walk('dog',4)
# animal.walk('cat',3)

######################   method overloading
# class Test:
#   def m1(self):
#      print('no-arg method')
#   def m1(self,a):
#      print('one-arg method')
#   def m1(self,a,b):
#       print('two-arg method')
#
# t=Test()
# # t.m1()
# # t.m1(10)
# t.m1(10,20)


# class duck:
#     def talk(self):
#         print('quck...')


