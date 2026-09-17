class Student:
    def __init__(self, name, house, patronus):#initialize the contents of an object from a class
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"#this method will return if at other parts of the code the class is called and a string is expected like form example print

    def charm(self):#it is possible to create bespoke methods
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _: #any different input
                return "🪄"
        


def main():
    student = get_student()
    #print(student)
    print("Expecto Patronum")
    print(student.charm())

def get_student():
    name =  input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    #return (name, house) #returning a tuple of 2 values
    return Student(name, house, patronus)#creating an object from class

if __name__ == "__main__":
    main()
