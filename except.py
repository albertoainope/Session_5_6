try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("I am sorry, but select an age higher than zero")
except:
    print("Something went wrong")
else:
    print(f"Player 1 is older than player 2 by {res}")
finally:
    print("Thank you for playing")