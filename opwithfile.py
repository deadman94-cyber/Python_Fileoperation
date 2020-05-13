#def main():
    #open a file for writing and create a file if it doesnot exists

#f = open("myfile.txt", "w+")

#open a file to append data 

#f = open("myfile.txt","a")

#read the file

f = open("myfile.txt","r")

#if f.mode=='r':
 #   content=f.read()
  #  print(content)


# read one line at a time

if f.mode == 'r':
    fl = f.readlines()
    for x in fl:
        print(x)
    #write data to file
#for i in range (19):
 #   f.write("This is a line"  + "\r\n")
    
#f.close()


