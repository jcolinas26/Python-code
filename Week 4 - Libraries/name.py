import sys #module to capture arguments from command line

if len(sys.argv) < 2:
    sys.exit("Too few arguments")#exit, exits the program
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])#argv[1] captures what is typed after python3 name.py -> "python3 name.py Jorge"



#------
for arg in sys.argv[1:]: #-> with this, you tell to start on the element 1 of the list and till the end, it will skip element 0
    print("Hello, my name is", arg)

for arg in sys.argv[1:-1]: #-> it will start on the element 1 and will remove the last element
    print("Hello, my name is", arg)