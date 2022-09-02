# l=[12,45,65,2,56]
# if l%2==0:
#     print(l)

# x=[10,20,30,40]
# b=bytes(x)
# b[0]=100
# for i in b:
#   print(i)
# output:: TypeError: 'bytes' object does not support item assignment


# x=[10,20,30,40]
# b=bytearray(x)
# b[0]=100
# for i in b:
#   print(i)

# x=[10,255]
# b=bytearray(x)
# for i in b:
#     print(i)

# s=[12,23,45,66,78]
# for x in s:
#     if (x%2!=0):
#         print(x)

# print(bin(15))
# print(oct(0b1111))
# print(hex(15))

#
# t=tuple(range(1,10,2))
# print(t)
# print(type(t))

# mystring="baswaraj"
# i=0
# while i<len(mystring):
#     print(mystring[i])
#     i=i+2




#
# s=input("enter some string")
# d={}
# for x in s:
#     if x in d.keys():
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print("{}={} times".format(k,v))

# s=input("enter some string")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(" ".join(l))

# s=input("enter some string")
# print("chareters at even position",s[0::2])
# print("chareters at odd position",s[1::2])

############################  REMOVE DUPLICATE  #############################
# s="abvzdsfczfshaakhsfcsaxadcxzcxzxdaxac"
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# print(" ".join(l))

# s="abvzdsfczfshaakhsfcsaxadcxzcxzxdaxac"
# a=set(s)
# print(" ".join(a))
# print(a)
########################      COUNT OF SIMILAR LETTER IN STRING  3##############################
# s="abvzdsfczfshaakhsfcsaxadcxzcxzxdaxac"
# d={}
# for x in s:
#     if x in d.keys():
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print("{}={} times".format(k,v))

# eg:::    no of character         # ANOTHER METHOD

# str=input("enter string")
# d={}
# for x in str:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,"occured",v,"times")

#####################     characters prsent at even & ODD position   #################################
# s="abvzdsfczfshaakhsfcsaxadcxzcxzxdaxac"
# i=0
# print("characters prsent at even position")
# while i<len(s):
#     print(i,s[i])
#     i=i+2
#
# s="abvzdsfczfshaakhsfcsaxadcxzcxzxdaxac"
# i=1
# print("characters prsent at odd position")
# while i<len(s):
#     print(i,s[i])
#     i=i+2

#########################################  VOVEL PROGRAM 3####################################
# s="baswarajmalge"
# l=["a","e","i","o","u"]
# print("voels are")
# for x in s:
#     if x   in l:
#         print(x)

# str="baswarajmalge"                    # ANOTHER METHOD
# s=set(str)
# v={"a","e","i","o","u"}
# d=s.intersection(v)
# d=s&v
# d1=s-v
# print("the vovels are:"," ,".join(d))
# print("the constants are:"," ,".join(d1))
##################
# l=[1,2,3,4]
# l[1]=777
# print(l)
# print(len(l))



# l=[1,2,3,4,56,7,87,9,1,2,3,4,5,6,7,87,9]
# print(len(l))
# print(l.count(1))
# print(l.index(5))
# l.reverse()
# print(l)
# l.sort()
# print(l)
# l.clear()
# print(l)


# l=[1,2,3]
# l.append("a")
# l.append("b")
# l.append("c")
# print(l)
#
# l=[]
# for i in range(1,100):
#     if i%10==0:
#         l.append(i)
# print(l)

# l=[1,2,3,4,5,6]
# l.insert(1,777)
# l.insert(0,888)
# l.insert(-10,999)
# print(l)

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l1.extend(l2)
# print(l1)
# l1=["baswaraj","sadashiv"]
# l1.extend("naman")
# print(l1)

# l=[1,2,3,4,5,6,7]
# l.remove(5)
# print(l)
#
# l=[1,2,3,4,5,6,7]
# print(l.pop())
# print(l)

# l=[1,2,3,4,5,6,7,87,9]
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1
# l=[1,2,3,4,5,6,7,87,9]
# for i in l:
#     print(i)


# l1=[10,20,[30,40],50]       #SHALLOW COPY
# l2=copy.copy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)              #[111, 222, [888, 999], 555]
# print(l2)              #[10, 20, [888, 999], 50]

# l1=[10,20,[30,40],50]       #DEEP COPY
# l2=copy.deepcopy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)              #[111, 222, [888, 999], 555]
# print(l2)              #[10, 20, [30, 40], 50]

# l1=[10,20,[30,40],50]
# l2=l1.copy()
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)              #[111, 222, [888, 999], 555]
# print(l2)              #[10, 20, [888, 999], 50]


# l=[x*x for x in range(1,11)]
# print(l)
#
# l1=[2**x for x in range(1,6)]
# print(l1)
#
# l2=[x for x in l if x%2==0]
# print(l2)

# l1=[1,2,3,4,5,6]
# l2=[4,5,6,7,8,9]
# l3=[i for i in l1 if i  in l2]
# print(l3)


# l1=[1,2,3,4,5,6]
# l2=[4,5,6,7,8,9]
# l3=l1+l2
# print(l3)
#
# l1=[1,2,3,4,5,6]
# l2=l1*3
# print(l2)
##############################   TUPLE DATA TYPE  ############################
# t=(1,2,3,4,5,1,1,1,1)
# print(len(t))
# print(t.count(1))
# print(t.index(5))
# t1=sorted(t)
# print(t1)
# print(type(t1))
# print(min(t))
# print(max(t))

# tuple packing and unpacking

# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
#
# t=(10,20,30,40)
# a,b,c,d=t
# print("a=",a,"b=",b,"c=",c,"d=",d)


# t=(x**2 for x in range(1,11) )
# print(t)
# print(id(t))
# for x in t:
#     print(x)

#################################   SET  DATA TYPE   ################################

# s=set()
# print(type(s))

# s={10,20,30,40}
# s.add(70)
# print(s)
#
# s={10,20,30,40}
# l=[50,60,"True"]
# s.update(l,range(1,10),"TRUE")
# print(s)

# s={10,20,30,40}
# s1=s.copy()
# print(s1)

# s={10,20,30,40}
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)

# s={10,20,30,40}
# s.remove(30)
# s.remove(50)                     #KeyError: 50
# print(s)

# s={10,20,30,40}
# s.discard(30)
# s.discard(50)
# print(s)

# s={10,20,30,40}
# s.clear()
# print(s)

# s={10,20,30,40}
# s1={30,40,50,60}
# print(s.union(s1))
# print(s|s1)
#
# print(s.intersection(s1))
# print(s&s1)
#
# print(s.difference(s1))
# print(s-s1)
# print(s1-s)
#
# print(s.symmetric_difference(s1))
# print(s^s1)


# s={x**2 for x in range(5)}
# print(s)
#
# s=[x*x*x for x in range(2,10)]
# print(s)

# l=eval(input("enrer list"))    # remove duplicate
# s=set(l)
# print((s))

# l=eval(input("enrer list"))  ## remove duplicate  another method
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)

# str="baswarajmalge"
# s=set(str)
# v={"a","e","i","o","u"}
# d=s.intersection(v)
# d=s&v
# d1=s-v
# print("the vovels are:",",".join(d))
# print("the constants are:"," ,".join(d1))
#
#
# s={"baswaraj","malge"}
# print(" ".join(s))


# ##############################   DICTIONARY DATA TYPE  ##########################################

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(len(d))
# d.clear()
# print(d)
# print(d.get(400))
# print(d.pop(100))

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.popitem())
# print(d)

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.keys())
# for k in d.keys():
#     print(k)
#
# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.values())
# for v in d.values():
#     print(v)


# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# for k,v in d.items():
#     print(k,"--",v)


# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# d1=d.copy()
# print(d1)

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.setdefault(400,"omkar"))
# print(d)

# eg

# d=eval(input("entrer dictionary"))
# s=sum(d.keys())
# print("sum=",s)

# squares={x:x*x for x in range(1,10)}
# print(squares)
#
# double={x:2*x for x in range(1,10)}
# print(double)

# eg:::    no of character
# str=input("enter string")
# d={}
# for x in str:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k,"occured",v,"times")


 # eg::    noof vovels
# str=input("enter string")
# v={'a','e','i','o','u'}
# d={}
# for x in str:
#     if x in v:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print(k,"occured",v,"times")



# a="nitin"
# b=""
# # for i in a:
# #     b=b+i+"-"
# # print(b)
# print("-".join(a))

# l=[1,5,7,8,3,9,4]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)



# for i in range(1,11):
#     if i==10:
#         break
#     print(i)
# else:
#     print("baswaraj")
# print("i am out of else")
#
# l=[1,3,2,1,2,4,2,5,5,4,4]
# d={}
# count=0
#
# for i in l:
#     if i in d:
#         d[i]=d[i]+[count]
#     if i not in d:
#         d[i]=[count]
#     count=count+1
# d={x:d[x] for x in sorted(d.keys())}
# print(d)



###############  second largest
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
###############  largest
# l=[7,6,8,4,5,6]
# def max(x):
#     a=x[0]
#
#     for i in range(len(x)):
#         if x[i]>a:
#             a=x[i]
#
#     return a
# print (max(l))








# l=[1,2,3,4,5]
# l1=[x**2 for x in l]
# print(l1)

# def name():
#     yield "a"
#     yield "b"
#
# b=name()
# print(next(b))
#
# s="baswaraj"
# if s==s[::-1]:
#     print("it is planindrom")
# else:
#     print("it is not planidrom")


###########################################################################################################
##   FILE HANDLING

# f=open("abc.txt","w")
# f.write("baswaraj\n")
# f.write("suresh")
# f.close()

# f=open("abc.txt","r")
# print(f.read())
# f.close()

# with open("file1.txt",'w') as m:
#      m.write("kiran\n")
#      m.write("swara")
# print("sucess")

# f=open("abc.txt","r")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# f.close()

# mystring="baswaraj marotirao malge"
# l1=['a','e','i','o','u']
# def fun(i):
#     if i in l1:
#         return True
#     else:
#         return False
# vow=list(filter(fun,mystring))
# print(vow)

# vow=list(filter(lambda i :True if i in l1 else False,mystring ))
# print(vow)
# constant=list(filter(lambda x: x not in l1,mystring))
# print(constant)


# l=[2,4,5,6,7,8]
# def square(x):
#     return x*x
# m=list(map(square,l))
# # m=list(map(lambda x: x*x,l))
# print(m)

# l="baswaraj"
# f=list(filter(lambda x:"a" not in x,l))
# print(f)
#
# l="baswaraj"
# m=["a"]
# def abc(x):
#     if x in m:
#         return True
#     else:
#         return False
# f=list(filter(abc,l))
# print(f)


# s="baswaraj"
# m=list(map(lambda x:2*x,s))
# print(m)




# x=[1,2,3,4]
# y=[5,6,7,8]
# m=list(map(lambda x,y:x*y,x,y))
# print(m)

# def decor(func):
#     def inner(name):
#         if name=="kiran":
#             print("bye",name)
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("hello",name)
# wish("baswaraj")
# wish("kiran")


# def mygen(n):
#     i=1
#     while i<n:
#         yield i
#         i=i+1
#
# m=mygen(5)
# print(next(m))
# print(next(m))

# def gen():
#     for i in range(10):
#         yield i
# g=gen()
# print(next(g))
# print(next(g))
# for i in g:
#     print(i)

# def gen(n):
#     while(n>0):
#         yield n
#         n=n-1
# g=gen(6)
# print(next(g))
# for i in g:
#     print(i)


# def fib():
#     a,b=1,2
#     while a<50:
#         yield a
#         a,b=(b,a+b)
# for i in fib():
#     print(i)

#

# n=int(input("number"))
# a=list(str(n))
# l=len(a)
# sum=0
# for i in a:
#     sum=sum+int(i)**l
# if sum==n:
#     print("yes")
# else:
#     print("no")

# from functools import*
# l=[2,3,4,5,6,7]
# l1=reduce(lambda x,y:x+y,l)
# print(l1)


# l=[2,3,4,5,6,7]
# sum=0
# for i in l:
#     sum=sum+i
#
# print("sum:",sum)

# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# print(factorial(5))

l1=[2,3,4,5,6,6]
l={ x:x%2==0 for x in l1 }
print(l)

