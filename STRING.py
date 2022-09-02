 # String   :: string is sequence of chractrers enclosed in single or double quote

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
# str1 = 'braj malge'
# print(str1.replace('braj','bswaraj'))

# splitting of string

# s="bas:waraj: mal:ge"
# print(s.split("a"))

# list1 = ['BASWARAJ','MAROTIRAO','MALGE']
# str1= ' '.join(list1)
# print(str1)

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
# s="bAswaraj maLge "
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


# REMOVING space from the string

# 1 rstrip()
# 2 lstrip()
#  3 strip()
#
# s=" baswaraj "
# print("before strip opration:",s)
# print("after strip opration:",s.strip())
# print(s.rstrip())
# print(s.lstrip())


# palindrome::


# s=input("any string:")
# if s==s[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")



# s="baswaraj"
# print(max(s))
# print(min(s))
# print(sorted(s))
# print(sorted(s,reverse=True))