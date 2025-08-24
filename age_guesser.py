import random

def greet():
        print("Hello, I am Chat-not-gpt and I am going to guess your age")
        name = input("What be yer name? ")
        correctness = "\0"
        i = 0
        while correctness != "y" or i > 50:
            guess = random.randrange(15, 30)
            print(guess)
            correctness = input("Is this correct?")
            i += 1
            if correctness != "y":
                print("Rats!")
        print(name + " is " + str(guess) + " years old.")

greet()
        
            
