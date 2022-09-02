# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(6))

# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# print(fact(6))
#
# n=int(input("number:"))
# l1=list(str(n))
# pow=len(l1)
# sum=0
# for i in l1:
#     sum=sum+int(i)**pow
# if n==sum:
#     print("yes")
# else:
#     print("no")

# lower=int(input('enter a lower value='))
# upper=int(input('enter a upper value='))
# for num in range (lower,upper+1):
#     if num>1:
#         for i in range (2,num):
#             if (num%i)==0:
#                 break
#         else:
#                 print(num)

# a=[1,2,3,4,5]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)
#
# from functools import*
# a=[1,2,3,4,5]
# re=reduce(lambda x,y:x+y,a)
# print(re)

# def sum(array):
#     sum=0
#     for i in array:
#         sum+=i
#     return sum
# array=[1,2,3,4,5]
# print(sum(array))


# a=[6,7,9,4,5]
# b=a[0]
# for i in range(len(a)):
#     if a[i]>b:
#         b=a[i]
# print(b)














# l=int(input("l no."))
# u=int(input("u no."))
# for num in range(l,u+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)



# def fib():
#     a,b=1,2
#     while a<30:
#         yield a
#         a,b=(b,a+b)
#
# for i in fib():
#     print(i)







































# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(5))
#
# def fact(n):
#     result=1
#     while n>1:
#         result=result*n
#         n=n-1
#     return result
# print(fact(4))


# n=int(input('no.'))
# l1=list(str(n))
# pow=len(l1)
# sum=0
# for i in l1:
#     sum=sum+int(i)**pow
# if n==sum:
#     print('yes')
# else:
#     print("n0")





# l=int(input('no'))
# u=int(input('no'))
# for num in range(l,u+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)


# def fib():
#     a,b=1,2
#     while a<30:
#         yield a
#         a,b=(b,a+b)
# f=fib()
# for i in fib():
#     print(i)

# a=[2,3,4,8,1]
# b=a[0]
# for i in range(len(a)):
#     if a[i]>b:
#         b=a[i]
# print(b)


n=int(input("enter number:"))
i=1
count=0
while n>=i:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print('prime number')
else:
    print('not prime number')


