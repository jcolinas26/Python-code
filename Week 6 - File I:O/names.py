name = input("What's your name: ")

#file = open("names.txt", "w")#will open the file in write mode; if file does not exist, it will be created
file = open("names.txt", "a")#a will add new info to the file, w will erase previous info
file.write(f"{name}\n")
file.close()#to save the new data


#######
with open("names.txt", "a") as file:#using this, the file will be opened and closed automatically
    file.write(f"{name}\n")


######

with open("names.txt", "r") as file:#open the file to read it
    lines = file.readlines()#readlines return the text of the file as a list

for line in lines:
    print("hello,", line.rstrip())#rstrip will remove the extra line added when writting in the file

######

with open("names.txt", "r") as file:#same as above but with less lines
    for line in file:
        print("hello,", line.rstrip())

######
names = []

with open("names.txt") as file:#r is the default
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


