import shutil

print("Enter file")
source=input()

print("Enter file")
destination=input()

from shutil import copyfile
copyfile(source,destination)


