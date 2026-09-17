class Student:
    def __init__(self, name, house):#initialize the contents of an object from a class
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"#this method will return if at other parts of the code the class is called and a string is expected like form example print
        
    @classmethod
    def get(cls):
        name =  input("Name: ")
        house = input("House: ")
        
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
