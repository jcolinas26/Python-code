
#name = input("What's your name? ") #to get inputs from user showing a message at the same time and save it into a variable

#name = name.strip() #removes blanc spaces from string
#name = name.capitalize() #capitalize user´s input
#name = name.title() #capitalize the first letter of every word on user´s input

#name = name.strip().title() #methods can be used together
#name = input("What's your name? ").strip().title() #all in only 1 line
#first, last = name.split(" ") #split user´s input in 2

#print ("hello, " + name)
#print ("hello,", name) #same behaviour as above
#print (f"hello, {first}") #same behaviour as above, f is the way to tell python that it needs to interpretate special features on the line


#create functions
def hello(to): #this is a function; it needs to be defined in the code before it is used
    print("Hello, ", to)

def hello2(to="world"): #it is possible to assign a value by default to the function variable in case the call to the function has no parameter no parameter
    print("Hello, ", to)

name = input("What's your name? ")
hello2(name)

###### good practise to use functions is use main() for the main code of the program and then we can create functions on any point of the code

def main():
    name = input("What's your name? ")
    hello(name)    

def hello(to): 
    print("Hello, ", to)

main() #need to call main for the code to work

