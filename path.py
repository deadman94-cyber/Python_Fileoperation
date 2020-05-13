import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
#print name of the OS
    print(os.name)    



#check if item exists and is a directory or a file

print("item exists:" + str(path.exists("myfile.txt")))
print("item is a file:" + str(path.isfile("myfile.txt")))
print("item is a directory:"+ str(path.isdir("myfile.txt")))

#work with file path
print("item path:" + str(path.realpath("myfile.txt")))
print("item path and name:" +str(path.split(path.realpath("myfile.txt"))))
print("item path and name:" +str(path.split("myfile.txt")))

#get file modification time 
t = time.ctime(path.getmtime("myfile.txt.bak")) #ctime : to print exact time
print(t)


td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myfile.txt"))
print("it has been"+str(td)+"     "+"since the file is modified")

if __name__=="__main__":
    main()

