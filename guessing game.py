import random
print("Welcome to our guessing game!")

for _ in range(5):
    try:
        user_number = input("Please guess a number: ")
        random_number = random.randint(1,10)
        if int(user_number) == random_number:
            print("You are a genius!")
        else:
            print("You are wrong!")
    except:
        print("Sorry, that's not a number.")
        
