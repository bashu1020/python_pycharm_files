############  Q 1:: factorial of number with & without recursie function

##                # with recursive function
# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(4))
# print(fact(5))
#
# ##        # WITHOUT RECURSIVE FUNCTION
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# print(fact(5))
# for i in range(1,5):
#     print(fact(i))

# ------------------------------------------------------------------------------------------------------------------
######  Q2: Check Armstrong Number or Not:

# n=int(input("enter number"))
# s=n
# sum1=0
# while n!=0:
#     r=n%10
#     sum1=sum1+(r*r*r)
#     n=n//10
# if s==sum1:
#     print("the given number is",s,"is a amstrong number")
# else:
#     print("the given number is",s,"is not amstrong number")

##### OR

# num=int(input("enter no."))   #153
# l1=list(str(num))
# pow=len(l1)
# sum=0
# for i in l1:
#     sum=sum+int(i)**pow
# if (num)==sum:
#     print(num,'is armstrong no.')
# else:
#     print(num,"not an armstrong no.")
# --------------------------------------------------------------------------------------------------------------------
### Q3 to find prime number in an interval

# lower=int(input('enter a lower value='))
# upper=int(input('enter a upper value='))
# for num in range (lower,upper+1):
#     if num>1:
#         for i in range (2,num):
#             if (num%i)==0:
#                 break
#         else:
#                 print(num)


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
# ---------------------------------------------------------------------------------------------------------------------
#### Q4  fibacconi series

# def fib():
#     a,b=1,2
#     while a<30:
#         yield a
#         a,b=(b,a+b)
#
# for i in fib():
#     print(i)

# ----------------------------------------------------------------------------------------------------------------
### Q5:: sum of array in multiple ways

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

# ----------------------------------------------------------------------------------------------------------------





############ Q: Check Palindrom or Not

# s="naman"
# s1=s[::-1]
# if s==s1:
#     print('yes')
# else:
#     print('no')

# eg 14
# l=[1,2,3,4,5,6,7,8,9]
# print(len(l))

# eg 20
# s=[10,30,40,50,60]
# sum=0
# for x in s:
#     sum=sum+x;
# print("the sum=",sum)

# eg 20
# s=[2,3,4]
# multi=1
# for x in s:
#     multi=multi*x;
# print("the multipy=",multi)



# eg 25
# s=[12,23,45,66,78]
# for x in s:
#     if (x%2==0):
#         print(x)

# eg 26
# s=[12,23,45,66,78]
# for x in s:
#     if (x%2!=0):
#         print(x)

# eg 27
# for x in range(20):
#     if x%2!=0:
#         print(x)

# eg 28
# for x in range(20):
#     if x%2==0:
#         print(x)

# eg 30
# s=[2,-4,5,-7,8,9,-3]
# for x in s:
#     if x>0:
#         print(x)

# eg 31
# s=[2,-4,5,-7,8,9,-3]
# for x in s:
#     if x<0:
#         print(x)

# eg 32
# for x in range(-10,10):
#     if x>0:
#         print(x)

# # eg 33
# for x in range(-10,10):
#     if x<0:
#         print(x)

# eg 29
# s=[12,23,45,66,78]
# count_odd=0
# count_even=0
# for x in s:
#     if (x%2==0):
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1
# print("even",count_even)
# print("odd",count_odd)


# # eg 34
# s=[12,-23,-45,66,-78]
# count_positive=0
# count_negative=0
# for x in s:
#     if (x>0):
#         count_positive=count_positive+1
#     else:
#         count_negative=count_negative+1
# print("positive",count_positive)
# print("negative",count_negative)

# s=[1,65,76,9]
# b=min(s)
# print(b)

# s=[2,6,1,8,9]
# min=s[0]
# for i in s:
#     if i<min:
#         min=i
#         print(i)

# eg
# s="baswarajmalge"
# i=1
# print("character present at odd/even position:")
# while i<len(s):
#     print(i,s[i])
#     i=i+2
#
# s="baswarajmalge"
# i=2
# print(" character at even position")
# for x in s:
#     if i%2==0:
#         print(i,s[i])
#
#         i=i+2

# s="baswarajmalge"
# i=2
# for x in s:
#     if i%2==0:
#         print(i,s[i])
#         i=i+2




# import keyword
# print(keyword.kwlist)


#

























