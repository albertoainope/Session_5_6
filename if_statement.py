import random
drinks = ["beer", "wine", "whisky", "rum", "tequila"]

try:
    age = int(input("How old are you? "))
    country = input("In which country do you live? ")
except ValueError:
    print("Input a valid number")
else:
    if age < 0 or age > 130:
        print("Your age is not valid")
    elif age < 21 and country == "US":
        print("You are too young to play this drinking game in US")
    elif age < 18:
        print("You are too young to play this drinking game")
    else:
        drink = random.choice(drinks)
        print(f"Take a shot of {drink}, since you are {age} years old")