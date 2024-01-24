name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)
birth_year = 2023 - age

print(f"Hey {name}, you are {age} years old and born in {birth_year}")
#f string
print("Hey",name, ", you are" ,age, " years old and born in ",birth_year)