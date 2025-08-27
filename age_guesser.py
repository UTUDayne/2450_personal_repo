import random

def greet():
        print("Hello, I am Chat-not-gpt and I am going to guess your age")
        name = input("What be yer name? ")
        correctness = "\0"
        i = 0
        initial_check = input("Are you between 15 and 30 years old?")
        if initial_check[0].lower() != 'y':
            print("Age out of range")
            return
        while correctness[0].lower() != "y" or i > 50:
            guess = random.randrange(15, 30)
            print(guess)
            correctness = input("Is this correct?")
            i += 1
            if correctness[0].lower() != "y":
                print("Rats!")
        print(name + " is " + str(guess) + " years old.")


greet()
        
            
