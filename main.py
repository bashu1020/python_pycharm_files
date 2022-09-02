# for i in range(10):
#       for j in range(0,10):
#                   print("i=",i):
#           print("j=",i*j):
#
#
#
# # a=10

# a=10
# b=20
# if(a>b):
#     print("a is greater ta
# #
# x=int(input("enter first number"))
# y=int(input("enter second number"))
# print("the sum",x+y)
# #
# a,b,c=[int(x) for x in input("3 numbers").split(",")]
# print('the product is',a*b*c)
# n=int(input("enter number"))
# if n>=1 and n<=10:
#     print("baswaraj")
# else:
#     print("malge")
# a="baswaraj malge"
# for x in a:
#     print(x)

# a="baswaraj"
# count=0
# for i in a:
#     print("no",count)
#     count+=1
#
# s=input("baswaraj")
# i=0
# for x in s:
#     print("the character present at",i,"index is:",x)
#     i+=1
#
# for x in range(10):
#     print("baswaraj")

# for x in range(11):
#     print(x)

# for x in range(100):
#     if (x%2!=0):
#         print(x)
# x=[]
# for x in range(100):
#     if (x%2==0):
#         print(x)

# for x in range (100,1,-1):
#     print(x)
#
# for i in range(1,10):
#     print("i=",i)
#     for j in range(1,11 ):
#         print("j=",j*(i))

# list=[10,20,30,40,50]
# sum=0
# for x in list:
#     sum=sum+x
# print(sum)

# x=1
# while x<=10:
#     print(x)
#     x=x+1


# n=int(input('enter number:'))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("the sum of first",n,"number is",sum)
# l1=[1,2,3,4]
# l2=[1,4,3,5]
# l3=l1+l2
# print(l3)
# #
# list=eval(input("enter two string"))
# sum=0
# for x in list:
#     sum+=x
# print("the sum=",sum)


# x=0
# while x<=10:
#     print(x)
#     x+=1

# n=int(input("enter number"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print("the sum of first",n,'number is',sum)

# name=""
# while name!='baswaraj':
#     name=input("enter name")
# print('malge')
# name=""
# pwd=""
# while (name!="baswaraj") or (pwd!="malge"):
#     name=input('enter name:')
#     pwd=input('enter password:')
# print("vinod")

# i=0
# while False:
#     i=i+1
#     print("hello",i)

# for i in range(4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j))




















# for i in range(4):
#     for j in range(4):
#         print("i=",i,"j=",j)
# print("baswaraj*10")
#
#
# n=int(input("enter number of rows:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()



# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     print("*"*i)

# for i in range(1,1+n):
#     print(""*(i-1),end="")
#     for j in range(65,66+n-i):
#         print(chr(j),end="")
#     print()n=int(input("enter number of rows;"))
#




# n=int(input("enter number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("* "*i)
#

# s="baswaraj"
# for i in range (str(s)):
#     print(s)

# for s in range(10):

#       if(s%2==0)
#        print(s)

# n=int(input("enter number of rows"))
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n+2-i):
#         print(j,end="")
#     for k in range(2,n+2-i):
#         print(n+k-i,end="")
#     print()


# n=int(input("enter no of rows:"))
# for i in range(n):
#     for j in range(i,n):
#         print("",end="")
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(i):
#         print("*",end="")
#     print



# for i in range(100):
#     if i%9==0:
#         print(i)
#     else:pass

# String
# access character of string

# 1 by using index
# 2 by using slices operator

# 1 by using index

# s="baswaraj"
# print (s[0])
# print(s[5])
# print(s[-1])
# print(s[-4])
# print(s[10])

# 2 by using slice operator


# s="baswaraj malge"# print(s[5:])
# print(s[:5])
# print(s[:])
# print(s[::])
# print(s[1:5:2])
# print(s[-10:-15:-1])
# print(s[5::-1])
# print(s[::-1])

# mathematical operator for string
# 1 + for concatenation
# 2 * for repetition
#
# s="baswaraj malge"
# print("baswaraj"+"malge")
# print("baswaraj"*2)

# len function

# s="baswaraj"
# print(len(s))

# checking membership

# s="baswaraj"
# print('d' in s)
# print('w' in s)

#
# s=input('enter main string')
# subs=input('enter sub string')
# if subs in s:
#     print(subs,'is found in main string')
# else:
#     print(subs,'is not found in main string')

# comparison of string

# s1=input("enter first string")
# s2=input("enter second string")
# if s1==s2:
#     print("both are equal")
# elif s1<s2:
#     print("first string is less than second string")
# else:
#     print("first string is greater than second string")


# finding substrings

# for forward direction

# 1 find
# 2 index

# for backward direction

# 1 rfind
# 2 rindex
#
# s="baswaraj malge"
# print(s.find("a",4,7))
# print(s.index("a"))
# print(s.rfind("a"))
# print(s.rindex("a"))

# counting substring in the given string

# count

# s="basawaraj"
# print(s.count("a"))
# print(s.count("a",2,6))

# replacing string with another string

# replace(oldstring,newstring)


# splitting of string

# s="baswaraj:: malge"
# print(s.split(":"))

# s="baswaraj malge"
# l=s.split()
# for x in l:
#     print(x)

# changing case of string

#
# 1 lower
# 2 upper
# 3 swapcaselower
# 4 title
# 5 capitalize
#
# s="Baswaraj malge "
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# checking starting and ending part of the string

# 1 startswith
# 2 endswith

# s="baswaraj malge"
# print(s.startswith("b"))
# print(s.endswith("e"))

# to check type of characters present in the string

# 1 isalnum: (A to Z,a to z,0 to 9)
# 2 isalpha: (A to Z,a to z)
# 3 isdigit:(0 to 9)
# 4 islower
# 5 isupper
# 6 istitle
# 7 isspace

# s=input("enter any character")
# if s.isalnum():
#     print("alpha numeric chracter")
#     if s.isalpha():
#         print("alpha charcter")
#         if s.islower():
#             print("lower case")
#         else:
#             print("upper case")
#     else:
#          print("it is a digit")
# elif s.isspace():
#     print("it is a sapace charcter")
# else:
#     print("non space special charcter")

# formatting the string

# name="baswaraj"
# salary=10000
# age=26
# print("{} salary is {} and his age is {}".format(name,salary,age))
# print("{0} salary is {1} and his age is {2}".format(name,salary,age))
# print("{x} salary is{y} and his age is {z}".format(z=age,y=salary,x=name))


 # List

# acessing element of list

# 1 by using index

# l=[10,20,30,40]
# print(l[1])
# print(l[3])
# print(l[-2])

# 2 by using slice operator

# l=[1,2,3,4,5,6,7,8,9]
# print(l[::])


# list vs mutability

# l=[10,20,30,40]
# print(l)
# l[1]=100
# print(l)

# IMPORTANT FUNCTION OF LIST:

# 1 TO GET INFORMATION ABOUT LIST:

# (1) len:

# l=[1,2,3,4,5,6]
# print(len(l))

# (2) count:

# l=[1,2,2,2,3,3,4,5]
# print(l.count(2))

# (3) index:

# l=[1,2,2,2,2,3,4]
# print(l.index(2))

# 2 manipulating elements of list:

# 1 append function

# l=['D','E',"F"]
# l.append('A')
# l.append('B')
# l.append('C')
# print(l)

# l=[]
# for i in range(101):
#     if i%10==0:
#         l.append(i)
# print(l)

# 2 insert function:
#
# l=[1,2,3,4,5]
# l.insert(1,55)
# l.insert(10,888)
# l.insert(-10,999)
# print(l)

# 3 extend function:

# l1=["baswaraj","sadashiv","naman"]
# l2=["malge","sarwad","jagtap"]
# l1.extend(l2)
# print(l1)

# l=["baswaraj",'sadashiv']
# l.extend("naman")
# print(l)

# 4 remove function:

# l=[10,20,30,10]
# l.remove(10)
# l.remove(20)
# print(l)

# 5 pop function:

# l=[10,20,30,40]
# l.pop()
# l.pop()
# print(l)

# 3 ordering elments of list:

# 1 reverse function:

# l=[10,20,30,40]
# l.reverse()
# print(l)

# 2 sort function

# l=[20,5,15,10,0]
# l.sort()
# print(l)
#
# l=["b","g",'t','h','k']
# l.sort()
# print(l)

# i="python language"
# for s in i:
#     for a in i:
#         if a==" ":
#             break
