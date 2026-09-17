class Student:
    def __init__(self, name, house):#initialize the contents of an object from a class
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"#this method will return if at other parts of the code the class is called and a string is expected like form example print

    #to prevent that the variable could be changed after the class is called
    #Getter
    @property
    def house(self):
        return self._house
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    

def main():
    student = get_student()
    print(student)

def get_student():
    name =  input("Name: ")
    house = input("House: ")
    return Student(name, house)#creating an object from class

if __name__ == "__main__":
    main()
