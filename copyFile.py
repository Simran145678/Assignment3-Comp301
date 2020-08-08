
import shutil
#prompting user to enter file path that has to be copied
print('Enter the path of file that you want to copy')
source=input()

#prompting user to enter filepath where he wishes to copy
print('Enter the path of file where you want to copy')
destination=input()


from shutil import copyfile
#function to copy the file
copyfile(source,destination)

#to check contents of file
print("After copying the contents of destination file are")
f=open(destination,"r")
print(f.read())