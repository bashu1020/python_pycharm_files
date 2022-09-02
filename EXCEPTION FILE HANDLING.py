                                         # exception file handling

# DEF:: the unwanted and unexpected event that distrub normal flow of program is called exception.
# exception handling is only for runtime error not for syntax error.
# exception handling does not repair exception but to continue rest of program.

# in any programming language there are two types of error possible
# 1 syntax error
# 2 runtime error


# 1 syntax error
### eg1
# x=10
# if x=10
#   print("hello")        #SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# eg2
# print"hello"            # syntax error:parentheses in call to 'print


# 2 runtime error/exception::
# type of  RUNTIME  error::

# 1 zerodivisionerror
# 2 typeerror
# 3 valueerror
# 4 filenotfounderror
# 5 eoferror
# 6 sleepingerror
# 7 typepuncturerror

## eg 1
# print(10/0)           #ZeroDivisionError: division by zero

## eg2
# print(10/"ten")       #TypeError: unsupported operand type(s) for /: 'int' and 'str'

## eg3
# x=int(input("enter number:"))
# print(x)                              # ValueError: invalid literal for int() with base 10: 'ten'


# TRY-EXCEPT

# try:
#     risky code
# except xxx:
    # handling code/alternative code

# without try-except

# print("stmt-1")
# print(10/0)
# print("stmt-3")

# with try-xcept

# # print("stmt-1")
# try:
#      print(10/0)
# # except ZeroDivisionError:
# except Exception as abc:
#     print(abc)
#     print(10/2)
# print("stmt-3")

#########   with exception as mesg
# print("stmt-1")
# try:
#      print(10/0)
# except Exception as abc:
#     print(abc)
#     print(10/2)
# print("stmt-3")

# how to print exception information

# try:
#   print(10/0)
# except ZeroDivisionError as msg:
#     print("exception raised and its dscrption is:",msg)

# try with multiple except blocks

# try:
#     x=int(input("enter first number:"))
#     y = int(input("enter second number:"))
#     print(x/y)
# except ZeroDivisionError:
#     print("can`t divide with zero")
# except ValueError:
#     print("please provide int value onaly")


# single except block that can handle multiple exception

# eg
# try:
#     x=int(input("enter first number:"))
#     y = int(input("enter second number:"))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#     print("plz provide valid numbers only and prblem is:",msg)


# default except block

## eg
# try:
#     x=int(input("enter first number:"))
#     y = int(input("enter second number:"))
#     print(x/y)
# except ZeroDivisionError:
#     print("can`t divide with zero")
# except:
#     print("default except:plz provide valid input only")

# note:: if try with multiple except block then default block should be last,otherwise we wil get syntax error
# eg
# try:
#     print(10/0)
# except:
#     print("default except")
# except :
#     print("zerodivisionerror")
#
# SyntaxError: default 'except:' must be last

# finally block:

# try:
#     risky code
# except:
#     handling code
# finally:
#     cleanup code

# the speciality of finally block is it will be excuted always whether exception raised or not raised and wheter exception handled or not handled

# case 1:: if there is no excution

# try:
#     print("try")
# except:
#     print("except")
# finally:
#     print("finally")

# case 2:: if there is an exception raised but handled

# try:
#     print("try")
#     print(10/0)
# except ZeroDivisionError:
#     print("except")
# finally:
#     print("finally")

# case 3:: if there is an exception raised but not handled

# try:
#     print("try")
#     print(10/0)
# except ValueError as msg :
#     print("except")
# finally:
#     print("finally")








#####################################################################################
                    # Various possible combinations of try-except-else-finally:
########################################################################################
#1
# try:
#  print("try")               #SyntaxError: expected 'except' or 'finally' block

# 2
# except:
#  print("Hello")             #SyntaxError: invalid syntax

# # 3
# else:
#  print("Hello")            #SyntaxError: invalid syntax

# # 4
# finally:
#  print("finally")          #SyntaxError: invalid syntax

# # 5
# try:
#  print("try")
# except:
#  print("except")

# # 6
# try:
#  print("try")
# finally:
#  print("finally")

# # 7
# try:
#  print("try")
# except:
#  print("except")
# else:
#  print("else")

# # 8
# try:
#  print("try")
# else:
#  print("else")                  #SyntaxError: invalid syntax
#
# # 9
# try:
#  print("try")
# else:
#  print("else")
# finally:
#  print("finally")           #SyntaxError: invalid syntax

## 10
# try:
#  print("try")
#  # print(10/0)
#  print(10/ten)
# except Exception:
#  print("except-1")
# except Exception:
#  print("except-2")

# #11                             #SyntaxError: invalid syntax
# try:
#  print("try")
# except :
#  print("except-1")
# else:
#  print("else")
# else:
#  print("else")

# #12                    # SyntaxError: invalid syntax
# try:
#  print("try")
# except :
#  print("except-1")
# finally:
#  print("finally")
# finally:
#  print("finally")

# 13
# try:
#  print("try")
#  print("Hello")
# except:
#  print("except")

# 14                    #SyntaxError: invalid syntax
# try:
#  print("try")
# except:
#  print("except")
#  print("Hello")
# except:
#  print("except")

# # 15
# try:
#  print("try")
# except:
#  print("except")
#  print("Hello")
# finally:
#  print("finally")
#
## 16                       #SyntaxError: invalid syntax
# try:
#  print("try")
# except:
#  print("except")
# print("Hello")
# else:
#  print("else")
#
# # 17
# try:
#  print("try")
# except:
#  print("except")
# try:
#  print("try")
# except:
#  print("except")
#
# # 18
# try:
#  print("try")
# except:
#  print("except")
# try:
#  print("try")
# finally:
#  print("finally")

# # 19
# try:
#  print("try")
# except:
#  print("except")
# if 10>20:
#  print("if")
# else:
#  print("else")
#
# 20
# try:
#     print("try")
#     try:
#       print("inner try")
#     except:
#       print("inner except block")
#     finally:
#       print("inner finally block")
# except:
#  print("except")


# # 21
# try:
#     print("try")
# except:
#     print("except")
#     try:
#      print("inner try")
#     except:
#      print("inner except block")
#     finally:
#      print("inner finally block")

# # 22
# try:
#  print("try")
# except:
#  print("except")
# finally:
#     try:
#         print("inner try")
#     except:
#         print("inner except block")
#     finally:
#         print("inner finally block")
#
# #23                     SyntaxError: expected 'except' or 'finally' block
# try:
#  print("try")
# except:
#  print("except")
# try:
#  print("try")
# else:
#  print("else")
#
## 24                           SyntaxError: expected 'except' or 'finally' block
# try:
#  print("try")
# try:
#  print("inner try")
# except:
#  print("except")
######################################################################################################

# class TooYoungException(Exception):
#  def __init__(self,arg):
#   self.msg=arg
#
#  class TooOldException(Exception):
#   def __init__(self,arg):
#    self.msg=arg
# age=int(input("Enter Age:"))
# if age>60:
#   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
# elif age<18:
#  raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
# else:
#  print("You will get match details soon by email!!!")


##################################################################################################################
##                         Assertion
#
# def squareIt(x):
#     return x*x
# assert squareIt(2)  #==4,"The square of 2 should be 4"
# assert squareIt(3)  #==9,"The square of 3 should be 9"
# assert squareIt(4)  #==16,"The square of 4 should be 16"
# print(squareIt(2))
# print(squareIt(3))
# print(squareIt(4))

# Exception Handling vs Assertions:
# Assertions concept can be used to alert programmer to resolve development time errors.
# Exception Handling can be used to handle runtime errors.