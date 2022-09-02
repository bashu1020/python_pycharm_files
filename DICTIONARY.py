# CREATE DICTIONARY:
#
# d={}  or d=dict()      d={key:value,key:value}
######### for just change
# d={}
# d[100]="baswaraj"
# d[200]="sadashiv"
# d[300]="naman"
# print(d)

# ACESS DATA FROM THE DICTIONARY:

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d[100])
# print(d[200])

# update dictionary:

# d[key]=value

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# a={10:"suresh",150:"ram"}
# d.update(a)
# print(d)
# d[400]="swara"
# print(d)
# d[100]="kiran"
# print(d)

# important function of dictionary:

# 1  dict():
#
# d=dict()
# d=dict({100:"baswaraj",200:"sadashiv"})
# print(d)
# d=dict([(100,"baswaraj"),(200,"sadashiv"),(300,"naman")])
# print(d)

# 2 ien()

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(len(d))

# 3 clear():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.clear())

# 4 get():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d[100])
# print([400])
# print(d.get(100))
# print(d.get(400))
# print(d.get(100,"kiran"))
# print(d.get(400,"kiran"))

# 5 pop():
#
# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.pop(100))
# print(d)
# print(d.pop(400))

# 6 popitem():

# d={100:"baswaraj",200:"sadashiv",300:"naman","a":25}
# print(d)
# print(d.popitem())

# 5 keys():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.keys())
# for k in d.keys():
#     print(k)

# 6 values():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.values())
# for v in d.values():
#     print(v)

# 7 items():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.items())
# for k,v in d.items():
#     print(k,v)

# 8 copy():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# d1=d.copy()
# print(d1)

# 9 setdefualt():

# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.setdefault(400,"kiran"))
# print(d)
# print(d.setdefault(100,"swara"))
# print(d)

# 10 update():
#
# d={100:"baswaraj",200:"sadashiv",300:"naman"}
# print(d.update())

# dictionary comprehension

# d={x:x*x for x in range(1,6)}
# print(d)
