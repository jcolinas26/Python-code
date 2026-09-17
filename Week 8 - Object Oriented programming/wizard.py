class Wizard:
     def __init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

class Student(Wizard): #student inherits from wizard
    def __init__(self, name, house):
        super().__init__(name)#calling the super class from which this inherits with the parameter
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
            super().__init__(name)#calling the super class from which this inherits with the parameter
            self.subject = subject

wizar = Wizard("Albus")
student = Student("Harry", "Griffindor")
professor = Professor("Severus", "Defense against the dark arts")