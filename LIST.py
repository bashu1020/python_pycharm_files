 # List

# acessing element of list

# 1 by using index

# l=[10,20,30,40]
# print(l[1])
# print(l[3])
# print(l[-2])

# 2 by using slice operator

# l=[1,2,3,4,5,6,7,8,9]
# print(l[::-1])


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
# l.insert(3,888)
# l.insert(-10,999)
# print(l)

# 3 extend function:

# l1=["baswaraj","sadashiv","naman"]
# l2=["malge","sarwad","jagtap"]
# l1.extend(l2)
# print(l1)

# l=["baswaraj",'sadashiv']
# l.extend('naman')
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

# using mathematical operators for list object

# 1 concatenation operator (+):

# a=[10,20,30]
# b=[40,50,60]
# c=a+b
# print(c)

# 2 repetition operator (*):

# a=[10,20,30]
# b=a*2
# print(b)

# comparing list object:
#
# a=["baswaraj","sadashiv","naman"]
# b=["baswaraj","sadashiv","naman"]
# c=["BASWARAJ","SADASHIV","NAMAN"]
# print(a==b)
# print(a==c)
# print(a!=c)

# clear() function:

# l=[10,20,30,40]
# print(l)
# l.clear()
# print(l)

# nested list

# l=[10,20,[30,40]]
# print(l[0])
# print(l[2][0])
# print(l[2])
# print(l[2][1])

# list comprehensions:
# a=[x*x for x in range(1,6)]
# print(a)

# a=[2**x for x in range(1,6)]
# print(a)


# for x,y in enumerate([1,2,3,4]):
#     print(x,y)

l1=[2,4,5,6]

print(l1.pop(1))