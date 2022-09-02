#####  1-Single Level Inheritance:
# inherits the properties from one class to another class.(parent~child)
## Eg.

# class A:
#     def m1(self):
#         print("Im Parent-A")
# class B(A):
#     def m2(self):
#         print("Im Chaild-B")
# t=B()
# t.m2()
# t.m1()

###### 2- Multi level inheritance:
# inherits the properties from multiple to single class.(grand~ Parent~child)
#Eg.

# class A:
#     def m1(self):
#         print("Im Parent-A")
#
# class B(A):
#     def m2(self):
#         print("Im Chaild-B")
# class C(B):
#     def m3(self):
#         print("Im Sub-child-c")
# t=C()
# t.m1()
# t.m2()
# t.m3()


###### 3- Hierarchical inheritance:
# inherits the properties from single to multiple class.(Parent~2-child)
#Eg.

# class A:
#     def m1(self):
#         print("Im Parent-A")
#
# class B(A):
#     def m2(self):
#         print("Im Chaild-1")
# class C(A):
#     def m3(self):
#         print("Im child-2")
# t1=B()
# t1.m1()
# t1.m2()
#
# t2=C()
# t2.m3()
# t2.m1()



##### 4- Multiple inheritance:
## inherits the properties from Multiple to Single class. (2-Parent~1-child)
##Eg.

# class A:
#     def m1(self):
#         print("Im Parent-1")
# class B:
#     def m1(self):
#         print("Im PArent-2")
# class C(A,B):
#     def m2(self):
#         print("Im child-2")
# t1=C()
# t1.m2()
# t1.m1()

### 5-Hybrid Inheritance:
### combination of single,multi,hierarchical and multiple inheritance is called.


### 6-Cyclic Inheritance:
### inherits the properties from one class to another class in cyclic way is called.
## in python would not support cyclic inheritance.






#######################################          [MRO]      ##############################################
## MRO-method resolution Order. (depth first run from left to right)

# class A:
#     def m1(self):
#         print("A-Class Method")
# class B:
#     def m1(self):
#         print("B-Class Method")
# class C:
#     def m1(self):
#         print("C-Class Method")
#
# class D(A,B):
#     def m1(self):
#         print("D-Class Method")
# class E(B,C):
#     def m1(self):
#         print("E-Class Method")
# class F(E,D):
#     def m1(self):
#         print("F-Class Method")
#
# # t=()
# # t.m1()
# print(D.mro())


# class a:
#     def m1(self):
#         print('a class method')
# class b:
#     def m1(self):
#         print('b class method')
# class c:
#     def m1(self):
#         print('c class method')
# class x(a,b):
#     def m1(self):
#         print('x class method')
# class y(b,c):
#     def m1(self):
#         print('y class method')
# class p(x,y,c):
#     def m1(self):
#         print('p class method')
#
# print(p.mro())
# print(y.mro())