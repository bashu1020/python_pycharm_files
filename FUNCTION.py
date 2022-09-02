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
# def even_odd(*num):
#     for i in num:
#      if i%2==0:
#         print(i,"is even num")
#      else:
#         print(i,"is odd num")
# even_odd(10,11,12,13,14,15,16,17,18,19,20)
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
# t1=list(calc(20,10))
# # t3=calc(100,200)
# for i in t,t1,t2:
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
# wish("baswaraj","good night")
# wish(msg="good night","baswaraj") # invalid

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
#     print(x.keys())
#     print(x.values())
# abc(n1=10,n2=20,n3=30)
# abc(rno=100,name="baswaraj",marks=80,subject="python")


# TYPE OF VARIABLE:

# 1 GLOBAL VARIABLE:
# 2 LOCAL VARIABLE:

# 1 GLOBAL VARIABLE

# eg

# a="baswaraj"  #global variable
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
#     a="sadashiv"
#     print(a)
#     a="brainworks"
#
#
# def f2():
#     print(a)

# f1()
# f2()

# eg4
#
# a=10
# b=15  #global variable
# def f1():
#     a=222   #local variable
#     print(a)
#     print(globals()['a'])
#     print(b)
# f1()


# Recursive function:

# a function that calls itself is known as recursive function

# eg:
# factorial(3)=3*factorial(2)
#             =3*2*factorial(1)
#             =3*2*1*factorial(0)
#             =3*2*1*1
#             =6
# factorial(n)=n*factorial(n-1)

# the main advatages of recursive function

# 1 we can reduce length of the code and improves readability
# 2 we can solve complex promblems

# eg

# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# print("factorial of 4 is",factorial(4))
# print("factorial of 5 is",factorial(5))
#
# # eg2        WITHOUT RECURSIVE FUNCTION7988787
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
#
# # for i in range(1,5):
# #     print("the facorial of",i,"is",fact(i))
# a=fact(5)
# print(a)






# lambda function:/anonymous function

# sometimes we can declare a function without any name,such type of nameless function are called anonymous
# function or lambda function

# normal function :

# we can define by using def keyword :

# def squarelet(n):
#     return n*n

# lambda function:

# we can define using lambda keyword :

# lambda n:n*n

# syntax of lambda function :

# lambda argument_list:expression

# eg1

# s=lambda n:[n*n,2*n,3**n,2*n]
# print("the square of 4 is",s(4))
# print("the square of 4 is",s(5))
# eg2
# #
# s=lambda a,b:[a+b,a-b,a*b,a/b,abs(a-b)]
# print("the calc of 10,20 is",s(10,20))
# print("the calc of 100,200 is",s(100,200))

# eg3

# s=lambda a,b:a if a>b else b
# print("the biggest value is 10,20 is:",s(10,20) )
# print("the biggest value of 200,100 is:",s(200,100))

# filter() function:

# we can use filter() function to filter values from the given sequence based on some condition

# filter(function,squence)

# eg1
#
# def even(x):  # without lambda function
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[0,5,10,15,20,25,30]
# l1=list(filter (even,l))
# print(l1)


# l=[0,5,10,15,20,25,30]        # with lambda function
# even=list(filter(lambda x:x%2==0,l))
# print(even)
# odd=list(filter(lambda x:x%2!=0,l))
# print(odd)

# eg2

# mystring="baswaraj marotirao malge"       # without lambda function
# l1=["a","e","i","o","u"]
# def fun(x):
#     if x in l1:
#         return True
#     else:
#         return False
#
# vow=" ,".join(filter(fun,mystring))
# print(vow)

# vow=" ".join(filter(lambda x: x in l1,mystring))                     # with lambda function
# print(vow)

# constants=" ".join(filter(lambda x: x  not in l1,mystring))           # with lambda function
# print(constants)

# map() function:   mp function is can beapplied on each element of sequence and generate anew sequence

# syntax:

# map(function,sequence)

# l=[1,2,3,4,5]              # without lambda function
# def double(x):
#     return 2*x
# l1=list(map(double,l))
# print(l1)

# l=[1,2,3,4,5]                     # with lambda function
# l1=list(map(lambda x:2*x,l))
# print(l1)

# eg2

# s="baswaraj"               # without lambda function
# def double(x):
#     return 3*x
# s1=list(map(double,s))
# print(s1)

# s="baswaraj"             # with lambda function
# s1=list(map(lambda x:x+x,s))
# print(s1)

# eg3
# l=[2,3,4,5,6]
# l1=list(map(lambda x:x*x,l))
# print(l1)

# eg4
# l1=[2,3,4,5,6] # for i in range(0,10)
# l2=[6,7,8,9,8,]
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)

# eg5
# l3=list(map(lambda x,y:x*y,range(5),range(6,11)))
# print(l3)

# reduce() function:  function reduce sequence of element into a single element by using specified functio

# syntax:   reduce(function,sequence)

# eg1
# from functools import*
# l=[10,20,30,40,50]
# r=reduce(lambda x,y:x+y,l)
# print(r)
# # #
# result=reduce(lambda x,y:x*y,l)
# print(result)
#
# # eg2
# from functools import*
# result=reduce(lambda x,y:x+y,range(1,101))
# print(result)


# function aliasing:

# for the existing function we can give anthor name ,which is nothing but function aliasing

# eg1
# def wish(name):
#     print("good morning",name)
# greeting=wish
# print(id(wish))
# print(id(greeting))
#
# wish("baswaraj")
# greeting("kiran")

# eg2
#
# def wish(name):
#     print("good morning",name)
# greeting=wish
#
# greeting("baswaraj")
# wish("kiran")
#
# del wish
# greeting("kiran")
# wish("kiran")       #name error :name wish is not defined



# Nested function

# we can declare a function inside another function ,such type of function are called nested function

# eg1
# def outer():
#     print("outer function strated")
#     def inner():
#         print("inner function exuection")
#     print("outer function calling inner function")
#     inner()
# outer()

# eg2

# def f1():
#     def inner(a,b):
#         print("the sum",a+b)
#         print("the average",(a+b)/2)
#     inner(10,20)
#     inner(20,30)
#     inner(40,50)
#
# f1()

# eg3
# def outer():
#     print("outer function strated")
#     def inner():
#         print("inner function started")
#         def small():
#             print("small is here")
#             def verysmall():
#                 print("verysmall is here")
#             verysmall()
#         small()
#     inner()
# outer()

# eg4

# def outer():
#     print("outrer function strated")
#     def inner():
#         print("inner functin started")
#     print("outer function returing inner function")
#     return inner
# # f1=outer
# f1=outer()
# f1()


# Function decorators:

# eg1
#
# def decor(func):
#     def inner(name):
#         if name=="baswaraj":
#             print("hello baswaraj bad morning")
#         else:
#             func(name)
#     return inner
#
# @decor
# def wish(name):
#     print("hello",name,"goood morning")
# wish("baswaraj")
# wish("kiran")
# wish("swara")
# wish("baswaraj")

# eg2


# def insurances(func):
#     def amt():
#         loan=func()
#         print("after adding insurance your loan is :")
#         return loan+1000
#     return amt
#
# @insurances
# def loan():
#     print("your loan is ",20000)
#     return 20000
# print(loan())

# eg3
# #
# def upper_case(func):
#     def inner():
#         str1=func()
#         return str1.upper()
#     return inner
# #
# def split_words(func):
#     def gather():
#         str2=func()
#         return str2.split()
#     return gather
#
# # @upper_case
# @split_words
# @upper_case
# def words():
#     return "baswaraj marotirao malge"
# print(words())

# eg4

# def out(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
# def out2(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
#
# @out
# @out2
# # @out
# def num():
#     return 10
# print(num())
#
# z=out(out2(num))
# print(z())


# eg5

# def deco_first_stud(func):
#     def james(name,mark):
#         result="full name :{} \tobtained mark:{}"
#         print(result.format(name,mark))
#         return func(name,mark)
#     return james
#
# @deco_first_stud
# def result_system(name,mark):
#     if mark >=35:
#         print("result is pass")
#     else:
#         print("result is fail !")
#
# result_system("baswaraj",40)

# eg5

# def smart_division(func):
#     def inner(a,b):
#         print("we are dividing",a,"with",b)
#         if b==0:
#             print("oopot divide")
#         else:
#             return func(a,b)
#     return inner
#
# @smart_division
# def division(a,b):
#     return a/b
#
# print(division(20,2))
# print(division(10,0))

# eg 6
# def decor(fun):
#     def inner(x,y):
#         fun(x,y)
#         return x+y
#
#     return inner
# @decor
# def wish(x,y):
#     print(x/y)
# print(wish(20,10))
#######################################################################################################33
                                             # Generators:
# generator is a function which is responsible to genrate a sequence of values
# yeild keyword is used return values

# eg1

# def mygen():
#     yield'a'
#     yield'b'
#     yield'c'
#
# g=mygen()
# print(type(g))
#
# print(next(g))
# print(next(g))
# print(next(g))

# eg2
# def mygen():
#      for i in range(0,10,2 ):
#          yield i
# x=mygen()
# print(next(x))
# print(next(x))
# print(next(x))

# eg3
# def my_gen():
#     n=1
#     print("this is printed first and n= :",n)
#     yield n
#     n+=1
#     print("this is printed second and n= :",n)
#     yield n
#     n+=1
#     print("this is printed at last n= :",n)
#     yield n
# a=my_gen()
# next(a)
# next(a)
# next(a)

# eg4
# def countdown(num):
#     while(num>0):
#         yield num
#         num=num-1
# values=countdown(6)
# for x in values:
#     print(x)
# # print(next(values))

# eg5

# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
#
# values=firstn(5)
# print(next(values))
# for x in values:
#     print(x)

# values=firstn(10)
# l1=list(values)
# print(l1)

# eg6

# def fib():
#     a,b=1,2
#     while True:
#         yield a
#         a,b=(b,a+b)
#
# f=fib()
# for f in fib():
#     if f>100:
#         break
#     print(f)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# eg 7

# def fib():
#     a,b=1,2
#     while a<30:
#         yield a
#         a,b=(b,a+b)
# for i in fib():
#     print(i)




# # generators vs normal collection wrt performances:

# import random
# import time
#
#
# names=["baswaraj","sunil","sadashiv","naman"]
# subjects=["math","python","java"]
#
# def people_list(num_people):
#     results=[]
#     for i in range(num_people):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#             }
#         results.append
#     return results
# def people_generator(num_people):
#
#     for i in range(num_people):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#             }
#         yield person
#
# t1 = time.clock()             # AttributeError: module 'time' has no attribute 'clock'
# people=people_generator(10000000)
# t2=time.clock()

# '''t1=time.clock()
# people=people_list(10000000)
# t2=time.clock()'''


# print('took{}'.format(t2-t1))


# def fun(a):
#     if a>10:
#         return True
#     else:
#         return False
# l1=filter(fun,[10,20,11])
# print(tuple(l1))


#



# def decor(wish):
#     def inner(name):
#         if name=="sunny":
#             print("hello bad morning")
#         else:
#             wish(name)
#     return inner
# @decor
# def wish(name):
#     print("hello good morning")
#
# # decorfunction=decor(wish)
#
# wish("baswaraj")
# wish("sunny")
# decorfunction("baswaraj")
# decorfunction("sunny")

# l1=[10,20,30]
# # sum=0
# # for i in l1:
# #     sum=sum+i
# #
# # print(sum)
# def sum():

# l=lambda x,y,z:x if x>y and y>z else z
#
# print(l(30,10,20))
#
# l=[7,6,8,4,5,6]
# def max(x):
#     a=x[0]
#     b=x[0]
#     for i in range(len(x)):
#         if x[i]>a:
#             a=x[i]
#     for i in range(len(x)):
#         if x[i]>b and x[i]!=a:
#             a=x[i]
#     return b
# print (max(l))

# l=[7,6,8,4,5,6]
# def max(x):
#     a=x[0]
#     for i in range(len(x)):
#         if x[i]>a:
#             a=x[i]
#     return a
# print (max(l)

# l=[7,6,8,4,5,6,9]
# a=l[0]
# # b=l[0]
# for i in range(len(l)):
#     if l[i]<a:
#         a=l[i]
# for i in range(len(l)):
#         if l[i]<b and l[i]!=a:
#             b=l[i]
# print(a)

# l=[7,6,8,4,5,6,9]
# a=l[0]
# b=l[0]
# c=l[0]
# for i in range(len(l)):
#     if l[i]>a:
#         a=l[i]
# for i in range(len(l)):
#         if l[i]>b and l[i]!=a:
#             b=l[i]
# for i in range(len(l)):
#     if l[i]>c and l[i]!=a and l[i]!=b:
#         c=l[i]
#
# print(c)


# def fib():
#     a,b=1,2
#     while a<30:
#         yield a
#         a,b=(b,a+b)
# for i in fib():
#     print(i)

# eg 1::  find maximum number without in built function

# l=[4,5,6,9,8,3]
# a=l[0]
# for i in range(len(l)):
#     if l[i]>a:
#         a=l[i]
# print(a)

# eg 1::  find second maximum number without in built function
# l=[4,5,6,9,8,3]
# a=l[0]
# b=l[0]
# for i in range(len(l)):
#     if l[i]>a:
#         a=l[i]
# for i in range(len(l)):
#     if l[i]>b and a!=l[i]:
#         b=l[i]
# print(b)

### eg 1::  find third maximum number without in built function
# l=[4,5,6,9,8,3]
# a=l[0]
# b=l[0]
# c=l[0]
# for i in range(len(l)):
#     if l[i]>a:
#         a=l[i]
# for i in range(len(l)):
#     if l[i]>b and a!=l[i]:
#         b=l[i]
# for i in range(len(l)):
#     if l[i]>c and a!=l[i] and b!=l[i]:
#         c=l[i]
# print(c)

# # eg 1::  find minimum number without in built function
# l=[4,5,6,9,8,3]
# a=l[0]
# for i in range(len(l)):
#     if l[i]<a:
#         a=l[i]
# print(a)
#
# # # eg 1::  find second minimum number without in built function
# l=[4,5,6,9,8,3]
# a=l[0]
# b=l[0]
# for i in range(len(l)):
#     if l[i]<a:
#         a=l[i]
# for i in range(len(l)):
#     if l[i]<b and a!=l[i]:
#         b=l[i]
# print(b)

# # # eg 1::  find third minimum number without in built function
# l=[5,6,9,8,3,4]
# a=l[0]
# b=l[0]
# c=l[0]
# for i in range(len(l)):
#     if l[i]<a:
#         a=l[i]
# for i in range(len(l)):
#     if l[i]<b and a!=l[i]:
#         b=l[i]
# for i in range(len(l)):
#     if l[i]<c and a!=l[i] and b!=l[i]:
#         c=l[i]
# print(c)


