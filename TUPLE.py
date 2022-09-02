# TUPLE
# tuple is collection of objects which is ordered,unchangable,hetrogenous,duplicates
# tuple is immutable

# acessing elements of tuple:

# 1 by using index:

# t=(10,20,30,40,50,60)
# print(t[0])
# print(t[-1])
# print(t[100])

# by using slice operator:

# t=(10,20,30,40,50,60)
# print(t[2:5])
# print(t[2:100])
# print(t[::2])

# tuple vs immutability:

# t=(10,20,30,40)
# t[1]=70

# mathematical operators for tuple:

# 1 concatenation oprator(+):
#
# t1=(10,20,30)
# t2=(40,50,60)
# t3=t1+t2
# print(t3)

# 2 multipication oprator:

# t1=(10,20,30)
# t2=t1*2
# print(t2)

# important function of tuple:

# 1 len():

# t=(10,20,30,40)
# print(len(t))

# 2 count():

# t=(10,20,30,40)
# print(t.count(10))

# 3 index():

# t=(10,20,30)
# print(t.index(10))

# 4 sorted():

# t=(40,10,30,20)
# t1=sorted(t)
# print(t1)
# print(t)

# 5 min() and max():

# t=(10,40,20,30)
# print(min(t))
# print(max(t))

# 6 cmpare cmp(): is available in python 2 but not in 3

# t1=(10,20,30)
# t2=(40,50,60)
# t3=(10,20,30)
# print(cmp(t1,t2))#-1 first tuple is less than second tuple
# print(cmp(t1,t3))#0 if both tuple are equal
# print(cmp(t2,t3))# +1 if first tuple is greATER than second tuple

# TUPLE PACKING AND UNPACKING:

# PACKING TUPLE:
#
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)

# UNPACING TUPLE:

# t=(10,20,30,40)
# a,b,c,d=t
# print("a=",a,"b=",b,"c=",c,"d=",d)

# TUPLE COMPREHENSION:
#
# t=(x**2 for x in range(1,6))
# print(type(t))
# for x in t:
#     print(x)

