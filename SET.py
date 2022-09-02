# CREATION OF SET OF OBJECT:
#
# s={10,20,30,40}
# print(s)
# print(type(s))

# s=set(any sequence):
#
# l=[10,20,30,40,50]
# s=set(l)
# print(s)
#
# s=set(range(5))
# print(s)
#
# s={}
# print(s)
# print(type(s))
#
# s=set()
# print(s)
# print(type(s))

# IMPORTANT FUNCTION OF SET:

# 1 add():

# s={10,20,30}
# s.add(40)
# print(s)

# 2 update():
#
# s={10,20,30}
# l=[40,50,60,70]
# s.update(l)
# print(s)

# 3 copy():

# s={10,20,30}
# s1=s.copy()
# print(s1)
#
# # 4 pop():
#
# s={40,10,20,30}
# print(s)
# print(s.pop())

# 5 remove():

# s={40,10,20,30}
# s.remove(30)
# print(s)
# s.remove(50)

# 6 discard():

# s={10,30,20}
# s.discard(10)
# print(s)
# s.discard(50)
# print(s)

# # 7 cler():
#
# s={10,20,30}
# print(s)
# s.clear()
# print(s)

# MATHEMATICAL OPERATION ON THE SET:

# 1 union():

# x.union(y) or x|y

# x={10,20,30,40}
# y={50,60,70,80}
# print(x.union(y))
# print(x|y)

# 2 intersection():

# x.intersection(y)  or x&y
#
# x={10,20,30,40}
# y={20,30,50,60}
# print(x.intersection(y))
# print(x&y)

# 3 difference():

# x.difference(y)  or x-y

# x={10,20,30,40}
# y={30,40,50,60}
# print(x.difference(y))
# print(x-y)
# print(y-x)

# 4 symmetric difference():

# x.symmetric_difference(y)   or x^y
#
# x={10,20,30,40}
# y={30,40,50,60}
# print(x.symmetric_difference(y))
# print(x^y)

# SET COMPREHENSION:
#
# s={x*x for x in range(5)}
# print(s)
#
# s={2**x for x in range(2,10,2)}
# print(s)

# s={1,2,3,4}
#
#  print(type(s))