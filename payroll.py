#format for printing the record
print(f"Employee no\t| Employee Name\t\t| Hours worked")
print("")

#opening file in readable format
f=open("data.txt","r")
for lines in f.readlines():

    #using split function to split the string
    substr=lines.split(",")
    print(f"{substr[0]}\t\t|{substr[1]} {substr[2]}\t\t|{substr[3]}")


f.close()

