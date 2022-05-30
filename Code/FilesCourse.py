import os

# FILE DETECTION

path = "C:\\Users\\Rodrigo\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

#OPEN, READ A FILE

try:
    with open('C:\\Users\\Rodrigo\\Desktop\\test.txt') as file:
            print(file.read())
except FileNotFoundError:
        print("That file was not found :(")

# WRITE A FILE

text = "Have a nice day!\n"

# with open('C:\\Users\\Rodrigo\\Desktop\\test.txt','r') as file:
#     file.write(text)
with open('C:\\Users\\Rodrigo\\Desktop\\test.txt','w') as file:
    file.write(text)
with open('C:\\Users\\Rodrigo\\Desktop\\test.txt','a') as file:
    file.write(text)

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('C:\\Users\\Rodrigo\\Desktop\\test.txt','C:\\Users\\Rodrigo\\Desktop\\copy.txt') #source,destination

# MOVE A FILE


source = "C:\\Users\\User\\Desktop\\source.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

# DELETE A FILE

# import os
# import shutil

path = "test.txt" #file path

try:
    os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    #shutil.rmtree(path)#delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
