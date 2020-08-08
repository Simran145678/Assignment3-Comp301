
print(f"Employee no\t| Employee Name\t\t| Hours worked")
print("")

f=open("data.txt","r")
for lines in f.readlines():
    substr=lines.split(",")
    print(f"{substr[0]}\t\t|{substr[1]} {substr[2]}\t\t|{substr[3]}")


f.close()

