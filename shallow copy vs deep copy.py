# l1=[10,20,30,40]
# l2=l1
# print(l1)
# print(l2)

# l1=[10,20,30,40]
# l2=l1
# l2[2]=70
# print(l1)        # [10, 20, 70, 40]
# print(l2)        # [10, 20, 70, 40]


# l1=[10,20,30,40]
# l2=l1.copy()
# l1[2]=70
# print(l1)        # [10, 20, 70, 40]
# print(l2)        # [10, 20, 30, 40]

import copy
# l1=[10,20,[30,40],50]
# l2=copy.copy(l1)
# print(id(l1))
# print(id(l2))

# l1=[10,20,30,40]
# l2=copy.copy(l1)
# l1[2]=888
# print(l1)
# print(id(l1))
# print(l2)
# print(id(l2))

# l1=[10,20,[30,40],50]       #SHALLOW COPY
# l2=copy.copy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)             #[111, 222, [888, 999], 555]
# print(id(l1))
# print(id(l1[2]))
# print(l2)              #[10, 20, [888, 999], 50]
# print(id(l2))
# print(id(l2[2]))


# l1=[10,20,[30,40],50]       #DEEP COPY
# l2=copy.deepcopy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)              #[111, 222, [888, 999], 555]
# print(id(l1))
# print(id(l1[2]))
# print(l2)              #[10, 20, [30, 40], 50]
# print(id(l2))
# print(id(l2[2]))


# l1=[10,20,[30,40],50]
# l2=l1.copy()
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=555
# print(l1)              #[111, 222, [888, 999], 555]
# print(l2)              #[10, 20, [888, 999], 50]


# if origional list does not contain any nested list then we should go for shallow copy/copy
# if origional list  contain any nested list then we should go for deep copy


