                                # FILE HANDLING#
# file is collection of datawhich is stored in program , whenever want use it & edit it.

# Types of files: there are two types of file

# 1 Text files
# usually we can use text file to store chracter data
# eg:abc.txt

# 2 binary files
# usually we can use b
# inary file to store binary dta like images,video files,audio files etc...

# Opening file

# f=open(filename,mode)

# the allowed mode in python are

# 1 r:: open an existing file for READ operation

# 2 w:: open an existing file for WRITE operation

# 3 a:: open an existing file for APPEND operation

# 4 r+:: read and writre data in to the file

# 5 w+:: to write and read the data

# 6 a+:: to append and read data from the file

# 7 x:: to open file in exclusive creation mode for write operation if the file already exists then we will get file text error

# closing file:

# f.close()


# various properties of file object

# name:: name of append file
# mode:: mode in which the file is opend
# closed:: returns boolean value indicates that file closed or not
# readable:: returns boolean value indicates that wheter file is readable or not
# writeable:: returns boolean value indicates that wheter file is writable or not

# f=open("baswaraj.txt",'w')
# print("file name:",f.name)
# print("file mode:",f.mode)
# print("is file readable:",f.readable())
# print("is five writable:",f.writable())
# print("is file closed:",f.closed)
# f.close()
# print("is file closed:",f.closed)
# -------------------------------------------------------------------------------------------------------
# writing data to text files:

# we can write chracter data to the text files by using the following 2 methods

# write(str)
# writelines(list of lines)

 # eg1
# f=open("abcd1.txt",'w')
# f.write("baswaHHraj1 marotirao malge\n")
# f.write("JHJ\n")
# f.write("SUREJSH1\n")
# print("data written to the file sucessfully")
# f.close()
# f=open("abcd1.txt",'r+')
# f=open("abcd.txt","a")
#
# f=open("abcd.txt","a")
# list={"baswaraj\n","sadashiv\n","sunil\n","naman\n"}
# f.writelines(list)
# print("list of line written sucesfually")
# f.close()
# -----------------------------------------------------------------------------------------------------
# Reading character data from the text file :
# we can read character data from text file by using the following read mehods

# 1-read():: to read total data from the file
# 2-read(n):: to read "n" character from the file
# 3-readline():: to read only one line
# 4-readlines():: to read all line into the

# eg1 : read()
# f=open("abcd.txt",'r')
# print(f.read())
# f.close()

# eg2::  read(n)

# f=open("abcd.txt",'r')
# print(f.read(10))
# f.close()

# eg3:: readline():: to read data line by line

# f=open("abcd.txt","r")
# print(f.readline())
# f.close()

# eg4:: readlines():: to read all line into list

# f=open("abcd.txt",'r')
# print(f.readlines())
# f.close()

# eg5

# f=open("abcd.txt",'r')
# print(f.read(5))
# print(f.readline())
# print(f.read(4))
# print("remaining data")
# print(f.read())

# -----------------------------------------------------------------------------------
#                                            WITH STATEMENT
# ------------------------------------------------------------------------------------------
# THE WITH STATEMENT : using "with"  keyword file is open but dont worry to close file

# with open("abcd.txt",'w') as f:
#     f.write("baswaraj\n")
#     f.write("marotirao\n")
#     f.write("malge\n")
    # print("is file closed:",f.closed)
# print("is file closed:",f.closed)

# --------------------------------------------------------------------------------------------------
                                    # THE SEEK() AND TELL() METHODS:
# ---------------------------------------------------------------------------------------------

# tell()::     we can use tell methood to retun cureent position of the curoser from begining of thje file.

# f=open("abcd.txt",'r')
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(6))
# print(f.tell())

# seek()::   WE CAN USE SEEK METHOD TO MOVE CURSOER TO SPECIFIED LOCATION .

# in w+,r+,a+ mode data can be read using seek method only

### EG 1
# f=open("f1.txt","r+")
# f.write("good morning")
# f.seek(0)
# print(f.read())
# f.close()

# data="all students are stupids"
# f=open("abc.txt",'w')
# f.write(data)
# with open("abc.txt",'a+') as f:
#     print(f.read())
#     print("the current curser position",f.seek(1))
#     f.write("kk")
#     print(f.read())
#     f.seek(17)
#     print("the current curser position",f.tell())
#     f.write("gems!")
#     f.seek(0)
#     print("data after modification")
#     print(f.read())


#############################################################################################################


# HOW TO CHECK GIVEN FILE EXIT OR NOT EXIT

# SYNTAX:::   os.path.isfile(fname)

# import os,sys
# fname=input("enter file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,'r')
# else:
#     print("file not exists:",fname)
#     sys.exit(0)
# print(f.read())

# eg  2

# import os,sys
# fname=input("enter file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,'r+')
# else:
#     print("file not exists:",fname)
#     sys.exit(0)
# # f=open('abcd.txt','r+')                                     #for check
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# # f.seek(0)
# # print(f.read())
# print("the number of lines:",lcount)
# print("the number of words:",wcount)
# print("the number of characters:",ccount)


#################################################################################################################
                                   # HANDLING CSV FILES::
###############################################################################################################

# CSV--COMMA SEPERATED VALUES

# python provide csv module to handle csv file

# WRITITING DATA IN CSV FILE::

# if you are not use "newline" attribute you get blanked line in csv file

# eg1
# import csv
# with open("emp.csv",'w') as f:
#     w=csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n=int(input("enter number of employes:"))
#     for i in range(n):
#         eno=int(input("enter employ number:"))
#         ename=input("enter employ name:")
#         esal=float(input("enter employ salary:"))
#         eaddr=input("enter employ address:")
#         w.writerow([eno,ename,esal,eaddr])
# print("total employ data writen to csv file sucessfully")

# eg2:;
# import csv
# with open("emp.csv",'w',newline="") as f:
#     w=csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n=int(input("enter number of employes:"))
#     for i in range(n):
#         eno=int(input("enter employ number:"))
#         ename=input("enter employ name:")
#         esal=float(input("enter employ salary:"))
#         eaddr=input("enter employ address:")
#         w.writerow([eno,ename,esal,eaddr])
# print("total employ data writen to csv file sucessfully")

# READING DATA IN CSV FILE::

# import csv
# f=open("emp.csv",'r')
# r=csv.reader(f)
# for line in r:
#     print(line)

###########################################################################################################
                                   # ZIPPING AND UNZIPPING FILES:
##############################################################################################################

# ADVANTAGES

# 1 memory utilization will be improved
# 2 transport time reduced
# 3 improve perfomance

# to create ZIP FILE::

# WRITE METHOD ::

# SYNTAX ::  f=ZipFile("files.zip","w","ZIP_DEFLATED")
#             f.write(filename)

# from zipfile import*
# f=ZipFile("file1.zip",'w',ZIP_DEFLATED)
# f.write("abcd.txt")
# f.write("abcd1.txt")
# f.write("abc.txt")
# f.close()

# READ METHOD::
#  SYNTAX ::   f=ZipFile("files.zip","r","ZIP_STORED")
#             names=f.namelist()


# from zipfile import*
# f=ZipFile("file1.zip",'r',ZIP_STORED)
# names=f.namelist()
# for i in names:
#     print("File Name:",i)
#     f1=open(i,'r')
#     print(f1.read())

############################################################################################################
                                        # WORKING WITH DIRECTIORES
#########################################################################################################
# #Q1   [to know the cwd]
# import os
# print(os.getcwd())

# #Q2    [inside cwd, create dir]
# import os
# print(os.mkdir("msp1"))

# #Q3  [inside dir, create sub-dir]
# import os
# print(os.mkdir("msp1/msp2"))

# #Q4  [multiple sub-dirs create]
# import os
# print(os.makedirs("msp1/sub1/sub2/sub3"))

# #Q5  [remove sub-dir]
# import os
# print(os.rmdir("msp1/msp2"))

# #Q6 [remove all-Multiple-dir]
# import os
# print(os.removedirs("msp1/sub1/sub2/sub3"))


# #Q7  [rename dir]
# import os
# print(os.rename("SUB","SUB1"))

# #Q8  [show list of all directiores]
# import os
# print(os.listdir("."))

# ##Q9 [content dir including sub dir]
# import os
# for dirpath,dirnames,filenames in os.walk("."):
#     print("current dir path",dirpath)
#     print("dir",dirnames)
#     print("files",filenames)

# import os
# print(os.walk("inspectionProfiles"))
##########################################################################################################
                             # GET INFORMATION ABOUT FILE
###########################################################################################################

# import os
# stats=os.stat("abcd.txt")
# print(stats)
#
#
# import os
# from datetime import *
# stats=os.stat("abcd1.txt")
# print('file size in bytes',stats.st_size)
# print('file MODE',stats.st_mode)
# print('file inode no.',stats.st_ino)
# print('file device',stats.st_dev)
# print('file no of hard links',stats.st_nlink)
# print('file user id of owner',stats.st_uid)
# print('file group id of owner',stats.st_gid)
# print('file last accesed time:',datetime.fromtimestamp(stats.st_atime))
# print('file last modified time',datetime.fromtimestamp(stats.st_mtime))
# print('file last data change',datetime.fromtimestamp(stats.st_ctime))