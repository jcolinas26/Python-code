i = 0
while i < 3:
    print("meow1")
    i += 1



for i in [0,1,2]: #-> [0,1,2] is a list
    print("meow2")

for i in range(3): #-> range returns the number of values in the parenthesis
    print("meow3")

for _ in range(3): #-> if the i is not going to be used anymore than counting, it can be used a _ instead
    print("meow3")


print("meow4\n" * 3, end="") #same result as above

while True:
    n = int(input("What´s n: "))

    if n > 0:
        break

for _ in range(n):
    print("meow5")