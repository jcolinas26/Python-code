students = [
    {"name": "Hermione", "house": "Gryfindor"},
    {"name": "Harry", "house": "Gryfindor"},
    {"name": "Ron", "house": "Gryfindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()#set will eliminate duplicates by its own
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)