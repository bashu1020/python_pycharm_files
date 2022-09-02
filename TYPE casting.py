# TYPE CASTING ::

# we can convert one type value to another type this coversion is called type casting

# the following are various inbult function
# 1 int()
# 2 float()
# 3 complex()
# 4 bool()
# 5 str()

# 1 int():::   we can use int() function to convert other values to int type

# print(int(123.45))
# print(int(10+5j))  #type error :can convert complex to int
# print(int(True))
# print(int(False))
# print(int("10"))
# print(int("10.5"))      #ValueError: invalid literal for int() with base 10: '10.5'
# print(int("ten"))         #ValueError: invalid literal for int() with base 10: 'ten'

# 2 float()::       we can use float() function to convert other values to float() type

# print(float(123.45))
# # print(int(10+5j))  #type error :can convert complex to int
# print(float(True))
# print(float(False))
# print(float("10"))
# print(float("10.5"))
# print(float("ten"))         #ValueError: invalid literal for int() with base 10: 'ten'

# 3 complex::         we can use complex() function to convert other values to complex() type

# print(complex(123))
# print(complex(10+5j))
# print(complex(True))
# print(complex(False))
# print(complex("10"))
# print(complex("10.5"))
# print(complex("ten"))            #ValueError: complex() arg is a malformed string

# 4 bool()::           we can use bool() function to convert other values to bool() type

# print(bool(123))
# print(bool(10+5j))
# print(bool(True))
# print(bool(False))
# print(bool("10"))
# print(bool("10.5"))
# print(bool("ten"))

# 5 string()::             # we can use bool() function to convert other values to bool() type

# print(str(123))
# print(str(10+5j))
# print(str(True))
# print(str(False))
# print(str("10"))
# print(str("10.5"))
# print(str("ten"))


# m=[1,5,6,5,7,5,8,4,6,5]
# print(set(str(m)))
# # for i in m:
# #     if i==5:
# #         print(i)
