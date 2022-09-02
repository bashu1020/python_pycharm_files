
# eg :: for counting no of line in file

# fname=input("enter file name")
# f=open(fname)
# lcount=ccount=wcount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("the no of lines",lcount)
# print("the no of words",wcount)
# print("the no of character",ccount)

# eg2
# f=open('abcd1.txt','r')
# f1=f.read()
# for i in f1:
#     print(i)

# # eg3   first way ans
# f=open('abcd1.txt','r')
# m=f.readlines()
# for i in m:
#     word=i.split()
#     for w in word:
#       print(w)
#######################  [OR]
# eg3  second way ans
# f=open('abcd1.txt','r')
# for i in f:
#     word=i.split()
#     for w in word:
#       print(W)

# import time
# print(time.ctime())