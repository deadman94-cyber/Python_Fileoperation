import os
from os import path
import shell
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    #make duplicate of existing file
    #if path.exists("myfile.txt"):
     #   src = path.realpath("myfile.txt")
      #  dst = src+".bak"

        #shutil.copy(src,dst)
    #now of you want the modification time
        #shutil.copystat(src,dst) 


    #rename the original file
        #os.rename("myfile.txt","newfile.txt")


    with ZipFile("opswithfile.zip","w") as opswith:
        opswith.write("opwithfile.py")
        opswith.write("path.py")
        opswith.write("shell.py")


if __name__=="__main__":
    main()   