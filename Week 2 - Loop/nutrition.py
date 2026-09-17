#The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”
#In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

fruits = [ 
    {"fruit": "Apple", "calories": "130"},
    {"fruit": "Avocado", "calories": "50"},
    {"fruit": "Banana", "calories": "110"},
    {"fruit": "Cantaloupe", "calories": "50"},
    {"fruit": "Grapefruit", "calories": "60"},
    {"fruit": "Grapes", "calories": "90"},
    {"fruit": "Honeydew Melon", "calories": "50"},
    {"fruit": "Kiwifruit", "calories": "90"},
    {"fruit": "Lemon", "calories": "15"},
    {"fruit": "Lime", "calories": "20"},
    {"fruit": "Nectarine", "calories": "60"},
    {"fruit": "Orange", "calories": "80"},
    {"fruit": "Peach", "calories": "60"},
    {"fruit": "Pear", "calories": "100"},
    {"fruit": "Pineapple", "calories": "50"},
    {"fruit": "Plums", "calories": "70"},
    {"fruit": "Strawberries", "calories": "50"},
    {"fruit": "Tangerine", "calories": "50"},
    {"fruit": "Watermelon", "calories": "80"},
]

f = input("Item: ")
f = f.lower()

for fruit in fruits:
    if fruit["fruit"].lower() == f:
        print("Calories: ", fruit["calories"])
        break