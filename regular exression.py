#                                              REGULAR EXPRESSION
# DEF::   TO FIND THE PATTERN FROM THE STRING IS KNOWN AS RE
#           IN-BUILT FUNCTION CAN BE IMPORT FROM RE MODULE

###  compile() ::   re module contains compile() function to compile a pattern into RegexObject

# import re
# a=re.compile("bmm")
# print(a)
# print(type(a))

# finditer  ::


# import re
# count=0
# pattern=re.compile("ab")
# m=pattern.finditer('ab','abaababa')
# for i in m:
#     count+=1
#     print(i.start(),'....',i.end(),'.....',i.group())
# print("the number of occurence:",count)

# we can pass pattern directly as argument to findetr() function

# import re
# count=0
# matcher=re.finditer('a','abaababa')
# for i in matcher:
#     count+=1
#     print(i.start(),'....',i.end(),'.....',i.group())
# print("the number of occurence:",count)


# Character classes:

# We can use character classes to search a group of characters
# 1. [abc]===>Either a or b or c
# 2. [^abc] ===>Except a and b and c
# 3. [a-z]==>Any Lower case alphabet symbol
# 4. [A-Z]===>Any upper case alphabet symbol
# 5. [a-zA-Z]==>Any alphabet symbol
# 6. [0-9] Any digit from 0 to 9
# 7. [a-zA-Z0-9]==>Any alphanumeric character
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)


# import re
# matcher=re.finditer("[^A-Za-z0-9]","a7b@k9Z")
# for i in matcher:
#     print(i.start(),'...',i.group())

# Pre defined Character classes:

# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .  Any character including special characters

# import re
# matcher=re.finditer("\s","a7b @k9 Z")
# for i in matcher:
#     print(i.start(),'...',i.group())


# Qunatifiers:

# We can use quantifiers to specify the number of occurrences to match.
# a  Exactly one 'a'
# a+  Atleast one 'a'
# a*  Any number of a's including zero number
# a?  Atmost one 'a' ie either zero number or one number
# a{m}  Exactly m number of a's
# a{m,n}  Minimum m number of a's and Maximum n number of a's


# import re
# x="a"
# matcher=re.finditer(x,"aaabbaaabaaaaaaaaa")
# for i in matcher:
#     print(i.start(),'...',i.group())

# #Important functions of re module:
# 1. match()
# 2. fullmatch()
# 3. search()
# 4.findall()
# 5.finditer()
# 6. sub()
# 7.subn()
# 8. split()
# 9. compile()

# 1 match() ::  We can use match function to check the given pattern at beginning of target string.

## eg
# import re
# s=input("enter some string:")
# m=re.match(s,"aaabbaaabaaaaaaaaa")
# if m!=None:
#     print("match is avaialable at the begining of the string")
#     print("start index",m.start(),"end index",m.end())
# else:
#     print("match is not avaialable at the begining of the string")

# 2 fullmatch()  :: We can use fullmatch() function to match a pattern to all of target string. i.e complete string
#                    should be matched according to given pattern.

##eg
# import re
# s=input("enter some string:")
# m=re.fullmatch(s,"aabb")
# if m!=None:
#     print("string is matched")
# else:
#     print("string is not matched")

#3 search()  ::  We can use search() function to search the given pattern in the target string

##eg
# import re
# s=input("enter some string:")
# m=re.search(s,"aabb")
# if m!=None:
#     print("pattern is available")
# else:
#     print("pattern is not available")

## 4 findall()  ::  To find all occurrences of the match.
#                 This function returns a list object which contains all occurrences.

# import re
# f=re.findall('[a-z0-9]',"sdfsc7jhj9DD")
# print(f)

## 5 finditer()  ::  Returns the iterator yielding a match object for each match.
#                     On each match object we can call start(), end() and group() functions

# import re
# matcher=re.finditer("[a-z]","a7b@k9DDZ")
# for i in matcher:
#     print(i.start(),'...',i.end(),'...',i.group())


## 6 sub()  :: sub means substitution or replacement
#              In the target string every matched pattern will be replaced with provided replacement.

#           syntax :: re.sub(regex,replacement,targetstring)

# import re
# f=re.sub('[a-z]','%',"sdfsc7jhj9DhD")
# print(f)


## 7 subn() ::  It is exactly same as sub except it can also returns the number of replacements.
#                This function returns a tuple where first element is result string and second element is number of
#                replacements.
##          syntax:: (resultstring, number of replacements)

# import re
# f=re.subn('[a-z]','%',"sdfsc7jhj9DhD")
# print(f)

## 8 split() :: If we want to split the given target string according to a particular pattern then we should go for
#                split() function.
#                This function returns list of all tokens.


# import re
# f = re.split('%', "sdf%sc7jhj9D%hD")
# print(f)

# import re
# f=re.split('%',"sdf%sc7jhj9D%hD")
# print(f)
# for i in f:
#     print(i)

#^ symbol::  We can use ^ symbol to check whether the given target string starts with our provided pattern or not.

# import re
# s="baswaraj marotirao malge"
# res=re.search("^bas",s)
# if res!=None:
#     print("target string starts with with bas")
# else:
#     print("target string  not starts with with bas")


#$ symbol:  We can use $ symbol to check whether the given target string ends with our provided pattern or not



# import re
# s="baswaraj marotirao malge"
# res=re.search("mal",s)
# if res!=None:
#     print("target string ends with with mal")
# else:
#     print("target string  not ends with with mal")

## Note: If we want to ignore case then we have to pass 3rd argument re.IGNORECASE for search() function.

# import re
# s="BASWARAJ MALGE"
# res=re.search("mal",s,re.IGNORECASE)
# if res!=None:
#     print("target string ends with with mal")
# else:
#     print("target string  not ends with with mal")

########################################################################################################
#                                              PROGRAM
###########################################################################################################

# 1: Write a Python Program to check whether the given number is valid mobile number or not?


# import re
# n=input("Enter number:")
# m=re.fullmatch("[7-9][0-9]{9}",n)
# if m!= None:
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")

#Q.2 Write a Python Program to check whether the given mail id is valid gmail id or not?

# import re
# s=input("Enter Mail id:")
# m=re.fullmatch("[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#  print("Valid Mail Id");
# else:
#  print("Invalid Mail id")


#hii bashu
