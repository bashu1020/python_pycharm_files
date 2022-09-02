

# import threading
# print("current exucuting code",threading.current_thread().getName())

# creating a thread without using any class

# from threading import *
# def display():
# 	for i in range(1,4):
# 		print("child Thread:")
# t = Thread(target=display)
# t.start()
# for i in range(1,4):
# 	print("main thread")

# creating a thread by extending thread class

# from threading import *
# class MyThread(Thread):
# 	def run(self):
# 		for i in range(1,4):
# 			print("child Thread:")
# t=MyThread()
# t.start()
# for i in range(1,4):
# 	print("main thread")

# creating a thread without extending thread class

# from threading import *
# class test:
# 	def m1(self):
# 		for i in range(1,4):
# 			print("child Thread:")
# t=test()
# t1=Thread(target=t.m1)
# t1.start()
# for i in range(1,4):
# 	print("main thread")

# without multithreading

# from threading import *
# import time
# def doubles(numbers):
# 	for n in numbers:
# 	  time.sleep(1)
# 	  print("Double:",2*n)
# def squares(numbers):
# 	for n in numbers:
# 	  time.sleep(1)
# 	  print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# doubles(numbers)
# squares(numbers)
# print("The total time taken:",time.time()-begintime)

# with multitthreading

# from threading import *
# import time
# def doubles(numbers):
# 	for n in numbers:
# 	  time.sleep(1)
# 	  print("Double:",2*n)
# def squares(numbers):
# 	for n in numbers:
# 	  time.sleep(1)
# 	  print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# t1=Thread(target=doubles,args=(numbers,))
# t2=Thread(target=squares,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The total time taken:",time.time()-begintime)













#Thread identification Number(ident):
# from threading import *
# def info():
# 	print("child Thread:")
# t = Thread(target=info)
# t.start()
#
# print("Main Thread identification number:",current_thread().ident)
# print("Child Thread identification number:",t.ident)






#---------------------------------------------------------------------------------------------------------




# active_count() :: the function retuns the number active threads currently running


# from threading import *
# import time
# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(1)
# 	print(current_thread().name,"ended...")
# print("Current active count:",active_count())
# t1 = Thread(target=info)
# t2 = Thread(target=info)
# t3 = Thread(target=info)
# t1.start()
# t2.start()
# t3.start()
# print("mid)_Current active count:",active_count())
# time.sleep(1)
# print("last_Current active count:",active_count())

#---------------------------------------------------------------------------------------------------------
#enumerate() function:: the function returns list of all the active threads currently running
#
# from threading import *
# import time
# def info():
#      print(current_thread().name,"started....")
#      # time.sleep()
#      print(current_thread().name,"ended...")
# t1=Thread(target=info,name=" thread 1")
# t2=Thread(target=info,name=" thread 2")
# t3=Thread(target=info,name=" thread 3")
# t1.start()
# t2.start()
# t3.start()
# time.sleep(1)
# l=enumerate()
# print(l)
# for t in l:
#   	print("name",t.name)
# l=enumerate()
# print(l)
# for t in l:
#   	print("name",t.name)
# time.sleep(10)
# l=enumerate()
# for t in l:
#   	print("name",t.name)






#---------------------------------------------------------------------------------------------------------





# isAlive():

#
# from threading import *
# import time
# def info():
# 	print(current_thread().name,"started....")
# 	time.sleep(4)
# 	print(current_thread().name,"ended...")
# t1=Thread(target=info,name="child thread 1")
# t2=Thread(target=info,name="child thread 2")
# t3=Thread(target=info,name="child thread 3")
# t1.start()
# t2.start()
# t3.start()
# time.sleep(1)
# print(t1.name,'isAlive:',t1.is_alive())
# print(t2.name,'isAlive:',t2.is_alive())
# print(t3.name,'isAlive:',t3.is_alive())
#





# from threading import *
# import time
# def info():
#     print(current_thread().name,"started....")
#     time.sleep(10)
#     print(current_thread().name,"ended...")
# t1=Thread(target=info,name="child thread 1")
# t2=Thread(target=info,name="child thread 2")
# t1.start()
# t2.start()
# print(t1.name,'is Alive:',t1.is_alive)
# print(t2.name,'is Alive:',t2.is_alive)
# time.sleep(6)
# print(t1.name,'is Alive:',t1.is_alive)
# print(t2.name,'is Alive:',t2.is_alive)
#


#-------------------------------------------------------------------------------------
# join() method:


# from threading import *
# import time
# def info():
#   for i in range(3):
#     print(" A Thread")
#     time.sleep(2)
# def info2():
#   for i in range(5):
#     print(" B Thread")
#     time.sleep(2)
#
# t=Thread(target=info)
# t1=Thread(target=info2)
# t.start()
# # t.join()
# t1.start()
# t1.join(5)
# #
# for i in range(3):
#   print(" B Thread coming ")





#-------------------------------------------------------------------------------------




# Daemon Threads:  the thread which are running in the background are called daemon thread
              # the main objective of daemon thread is



# from threading import *
# print(current_thread().isDaemon())
# current_thread().setDaemon(True)
# print(current_thread().isDaemon())




#--------------------------------------------------------------------------------------------------------




# Default nature:



# from threading import *
# import time
# def job():
#     for i in range(4):
#         print("child thread")
#
# t=Thread(target=job)  # main thread is parent and t child
# t.setDaemon(True)
# t.start()
#
# print(" main thread")

#from threading import *





#######################################################################


# from threading import*
# def test():
#     print("child method")
# t=Thread(target=test)
# t.start()
#
# print("main thread identification number:",current_thread().ident)
# print("child thread identificatin number",t.ident)
# print(current_thread().name)
# print(t.name)



###########################################################################################

# from threading import *
# print("current execution thread:",current_thread().name)

# from threading import *
# def m1():
#     for i in range(10):
#       print("child thread")
# t=Thread(target=m1)
# t.start()
# for i in range(10):
#     print("main thread")


# from threading import *
# class myThread(Thread):
#     def run(self):
#         for i in range(3):
#           print("child thread")
# t=myThread()
# t.start()
# for i in range(3):
#     print("main thread")

# from threading import *
# class A:
#     def m1(self):
#         for i in range(3):
#             print("child thread")
# t=A()
# t1=Thread(target=t.m1)
# t1.start()
# for i in range(3):
#     print("main thread")


# import time
# def m1(number):
#     for i in number:
#         time.sleep(1)
#         print("square",i*i)
# def m2(number):
#     for i in number:
#         time.sleep(1)
#         print("double",2*i)
# begintime=time.time()
# number=[2,3,4,5,6,7]
# m1(number)
# m2(number)
# print("time taken:",time.time()-begintime)

# from threading import *
# import time
# def m1(number):
#     for i in number:
#         time.sleep(1)
#         print("square",i*i)
# def m2(number):
#     for i in number:
#         time.sleep(1)
#         print("double",2*i)
# begintime=time.time()
# number=[2,3,4,5,6,7]
# t1=Thread(target=m1,args=(number,))
# t2=Thread(target=m2,args=(number,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("time taken:",time.time()-begintime)
############################################################################################################
                                         # synchronization
#######################################################################################################3
 # if multiple threads are exeucting simalteanously then there may be a chance of data constiency problem

# from threading import *
# import time
# def m1(name):
#     for i in range(4):
#         print("good evening",end='')
#         time.sleep(2)
#         print(name)
# t1=Thread(target=m1,args=("dhoni",))
# t2=Thread(target=m1,args=("yuvraj",))
# t1.start()
# t2.start()

# to stop this problem we should go for synchronization
# synchronization thread will be executed one by one
# the main application areas of syncronization is
#    1 online reservation system
#    2 fund trasfer from joint account

# in python we can implement synchronization by using following
#  1 lock
#  2 rlock
#  3 semaphore

# 1  lock::

# lock are the most fundamental syncronization mechanism provided by threading module
# we can create lock object as follows
# l=Lock()

# a thread can acquire the lock by using acquire method()
#  l.acquire()
# a thread can release the lock by using release method()
#  l.release()

# from threading import *
# import time
# l=Lock()
# def m1(name):
#     l.acquire()
#     for i in range(4):
#         print("good evening",end='')
#         time.sleep(2)
#         print(name)
#     l.release()
# t1=Thread(target=m1,args=("dhoni",))
# t2=Thread(target=m1,args=("yuvraj",))
# t1.start()
# t2.start()


# 2 RLock()::

# from threading import *
# import time
# l=RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#       result=1
#     else:
#         result=n*factorial(n-1)
#     l.release()
#     return result
# def results(n):
#     print("the factorial of",n,"is",factorial(n))
# t1=Thread(target=results,args=(2,))
# t2=Thread(target=results,args=(3,))
# t3=Thread(target=results,args=(4,))
# t4=Thread(target=results,args=(5,))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# _______________________________________________________________________________________________________
# 3 semaphore()::    semaphore is advanced syncronization mechanism
                     # s=semaphore(counter)

# case 1:  s=semaphore()
# in this case counter value is 1 and at a time only one thread is allowed to acess. it is exactly same as lock concept
# from threading import *
# import time
# s=Semaphore()
# def m1(name):
#     s.acquire()
#     for i in range(4):
#         print("good evening",end='')
#         time.sleep(2)
#         print(name)
#     s.release()
# t1=Thread(target=m1,args=("dhoni",))
# t2=Thread(target=m1,args=("yuvraj",))
# t3=Thread(target=m1,args=("virat",))
# t4=Thread(target=m1,args=("sachin",))
# t1.start()
# t2.start()
# t3.start()
# t4.start()

# case 2:  s=semaphore(3)
# in this case semaphore object can be assecced by threads at a time  the reamaining threads have to wait until
  # realising the semaphore

# from threading import *
# import time
# s=Semaphore(2)
# def m1(name):
#     s.acquire()
#     for i in range(4):
#         print("good evening",end='')
#         time.sleep(1)
#         print(name)
#     s.release()
# t1=Thread(target=m1,args=("dhoni",))
# t2=Thread(target=m1,args=("yuvraj",))
# t3=Thread(target=m1,args=("virat",))
# t4=Thread(target=m1,args=("sachin",))
# t1.start()
# t2.start()
# t3.start()
# t4.start()

# boundsemaphore::

# from threading import*
# s=Semaphore(3)
# s.acquire()
# s.acquire()
# s.acquire()
# s.acquire()
# s.release()
# s.release()
# s.release()
# s.release()
# print("end")

########################################################################################################
#                                        INTER THREAD COMMUNICATION
########################################################################################

# def:: for progamming requirment threads are communicate with each other is known as inter thread communication

# there are three types of inter thread communication

# 1 event
# 2 object
# 3 queue


# 3 queue ::  queue concept is the most enhanced mechanism for interthread communication to share data betn thrads
# we use queue to we should import queue module
import queue

# import Queue
# q=queue.Queue()

# methods of queue::
# 1 put():: put an item into the queue
# 2 get():: remove and retun item from the queue

