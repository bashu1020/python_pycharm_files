#Logging-By using this logging to track the error or exception or information. also for debugging purpose.

## defn:: logging is python module in standard library that provide the facility to work with the framework for
##         releasining log messages from the python programs

# 5-Levels of logging; debug(10),info(20),warning(30),error(40),critical(50).  extra 6-NotSet(0)
# 5-basicConfig- level,filename,filemode,format,style.


# #Q1: by default warning to run

# from logging import*
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

#  ##Q2:     1-Debug level set
# from logging import*
# basicConfig(level=DEBUG)         ## for level set
# debug("im debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

# #Q3:  2-level+filename(if file name create before filemode by default append happens)
# from logging import*
# basicConfig(filename='log3.txt',level=DEBUG)
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

# #Q4: 3-[Level+FileName+FileMode]- (if file name create then take filemode take W then override)
# from logging import*
# basicConfig(filename='log3.txt',level=DEBUG,filemode='w')
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

# #Q5: 4-[Level+FileName+FileMode+format]  [format-'%(asctime)s,%(message)s,%(lineno)d,%(name)s'] s=string, d=decimal
# from logging import*
# basicConfig(filename='logfile6.txt',level=DEBUG,filemode='w',format='%(asctime)s %(message)s %(lineno)d %(name)s %(levelname)s')
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")


# #Q6: 4-[Level+FileName+FileMode+format]   format sequence order comma no need
# from logging import*
# basicConfig(filename='logfile6.txt',level=DEBUG,filemode='w',format='%(lineno)d **#1 %(name)s **##1 %(asctime)s **#1 %(message)s')
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

# #Q7: 5-[Level+FileName+FileMode+format+Style]   if style curly bracket use then no need-(% & data type)
# from logging import*
# basicConfig(filename='logfile6.txt',level=DEBUG,filemode='w',style='{',format='{lineno} ** {name} ** {asctime} ** {message}')
# debug("im aa debug")
# info("im info")
# warning("im warning")
# error("im error")
# critical("im critical")

# #Q8: 5-[Level+FileName+FileMode+format+Style]   we pass parameter(username) name
# from logging import*
# basicConfig(filename='logfile6.txt',level=DEBUG,filemode='w',style='{',format='{lineno} ** {name} ** {asctime} ** {message}')
#
# logger=getLogger("Suresh")
#
# logger.debug("im aa debug")
# logger.info("im info")
# logger.warning("im warning")
# logger.error("im error")
# logger.critical("im critical")

# #Q9: 5-[Level+FileName+FileMode+format+Style]   ##if parameter not pass(empty) then bydefault username(root) came
# from logging import*
# basicConfig(filename='logfile6.txt',level=DEBUG,filemode='w',style='{',format='{lineno} ** {name} ** {asctime} ** {message}')
#
# logger=getLogger()                                   ##if parameter not pass then bydefault username(root) came
#
# logger.debug("im aa debug")
# logger.info("im info")
# logger.warning("im warning")
# logger.error("im error")
# logger.critical("im critical")

# #Q10: 5-[Level+FileName+FileMode+format+Style]   ## add adminlog() how to run check
# from logging import*
# basicConfig(filename='logfile6.txt',filemode='w',level=DEBUG,style='{',format='{lineno} ** {name} ** {asctime} ** {message}')
#
# logger=getLogger()
# logger.debug("im aa debug")
# logger.info("im info")
# ## adminlog()                        ##don't know, how to run
# logger.warning("im warning")
# logger.error("im error")
# logger.critical("im critical")



########################################    [END]    ##########################################################
# import logging
# from logging import*
# basicConfig(level=DEBUG,filename='log5.txt')
# a=5
# b=0
# try:
#     c=a/b
# except Exception as e:
#     print('error occured')
#     logging.debug('exception occcure',exc_info=True)

