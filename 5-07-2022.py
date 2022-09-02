# FUNCTION
#  A FUNCTION IS A BLOCK OF CODE WHICH ONLY RUNDS WHEN IT IS CALLED

# creating a function:
# IN PYTHON A FUNCTION IS DEFINED USING THE def KEYWORD
# eg
# def abc():
#     print("hello baswaraj")

# calling a function:
# to call function use the function name followed by parenthesis
# eg
# def abc():
#     print("hello baswaraj")
# abc()

# parameters:

# def wish(name):
#     print("hello",name,"good morning")
# wish("baswaraj")
# wish("sadashiv")

# def squarelet(number):
#     print("the square of",number,"is",number*number)
# squarelet(4)
# squarelet(5)

# return statement:

# e
#
#
#
# def add(x,y):
#     return x+y,x-y,x*y,x/y
# result=add(10,20)
# print("the sum is",result)
# print("the sum is",add(10,20))

# eg2
# def f1():
#     print("Hello")
#
# f1()
# print(f1())
#
# eg3
# def even_odd(num):
#     if num%2==0:
#         print(num,"is even num")
#     else:
#         print(num,"is odd num")
# even_odd(10)
# even_odd(15)

# eg4
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# # print(sum_sub(100,50))
# x,y=sum_sub(100,50)
# print(" sum= ",x ,"sub=",y)

# eg5
# def sum_sub_mul_div (a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# print(sum_sub_mul_div(100,50))
# print(list(sum_sub_mul_div(100,50)))
# x,y,z,p=sum_sub_mul_div(100,50)
# print("sum=",x,"sub=",y,"mul=",z,"div=",p)

# eg6
# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# t=set(calc(10,20))
# t1=calc(20,10)
# t3=calc(100,200)
# for i in t,t1,t3:
#     print(i)

# type of arguments


# 1 positional argument:
# 2 keyword argument
# 3 default argument
# 4 variable length argument

# 1 positional arguments:

# def sub(a,b,):
#     print(a-b)
# sub(100,200)
# sub(200,100)

# 2 keyword argument:
#
# def wish(name,msg):
#     print("Hello",name,msg)
# wish(name="baswaraj",msg="good morning")
# wish(msg="good night",name="kiran")
# wish("baswaraj",msg="good night")
# wish(msg="good night","baswaraj")  invalid

# 3 default argument
#
# def wish(name="Guest"):
#     print("hello",name,"good morning")
#
# wish("durga")
# wish()

# varaible length argument:  def f1(*n)

#eg:1
# def sum(*n):
#     total=0
#     for n1 in n:
#         total=total+n1
#     print("the sum",total)
#
# sum()
# sum(10)
# sum(10,20,30)
# sum(10,20,30,40)

# eg2
#
# def f1(n1,*s):
#     print(n1)
#     for s1 in s:
#         print(s1)
# f1(10)
# f1(10,20,30,40)
# f1(10,"a",20,"b")

# def f1(*s,n1):
#     for s1 in s:
#         print(s1)
#     print(n1)
# f1(10,n1=20)
# f1("a","b",n1="c")

# eg3
#
# def abc(**x):
#     for key,value in x.items():
#         print("%s  :  %s" % (key,value))
#
# abc(a="baswaraj",b="sadashiuv")

# another method

# def abc(**x):
#     for k,v in x.items():
#         print(k,"=",v)
# abc(n1=10,n2=20,n3=30)
# abc(rno=100,name="baswaraj",marks=80,subject="python")


# TYPE OF VARIABLE:

# 1 GLOBAL VARIABLE:
# 2 LOCAL VARIABLE:

# 1 GLOBAL VARIABLE

# eg

# a="baswaraj"
# def f1():
#     print(a)
#
#
# def f2():
#     print(a)
#
# f1()
# f2()

# 2 local variable:

# def f1():
#     a=10
#     print(a)
#
# def f2():
#     print(a)  # invalid
#
# f1()
# f2()


# global keyword:
# we can use global keyword for the following 2 purpose:

# 1 to decalre global variable inside function
# 2 to make global variable available to the function so that we can perform required modfication

# eg1
# a="baswaraj"
# def f1():
#     a=10
#     print(a)
# def f2():
#     print(a)
#
# f1()
# f2()

# eg2
# a=10
# def f1():
#     global a
#     a="baswaraj"
#     print(a)
#
# def f2():
#     print(a)
#
# f1()
# f2()
#
# eg3
# def f1():
#     global a
#     a="baswaraj"
#     print(a)
#
# def f2():
#     print(a)
#
# f1()
# f2()

# eg4
#
# a=10
# def f1():
#     a=222
#     print(a)
#     print(globals()['a'])
# f1()
