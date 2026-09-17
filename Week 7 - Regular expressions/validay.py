import re

email = input("What´s your email?: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #[a-zA-Z0-9_] == \w | IGNORECASE will ignore if the input is lower or upper case | the expresion in () and following ? means that it is optional
    print("Valid")
else:
    print("Invalid")