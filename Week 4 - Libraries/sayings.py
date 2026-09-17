#create our own module

def main(): #just for checking if functions work fine
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__": #to ensure that main is not executed when a function of this module is called from other place
    main()