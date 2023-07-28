#guess the number
#in this game, the computer has thought of a secret number, and the user (us) has to guess the secret number

#making the computer generate a random number

# computer thinks of a random number and we try to guess it

import random

x = random.randint(2, 20)

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x} : "))
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")
        
    print(f"Yay, congrays. You have guessed the number {random_number} correctly")

guess(x)

#we come up with a secret number and this time, we make the computer guess the number

# we think of a random number and computer tries to guess it

y = random.randint(1, 15)

def computer_guess(y):
    low = 1
    high = y #13
    print(y)
    feedback = ''
    while feedback != 'c': # c = correct
        guess2 = random.randint(low, high)
        feedback = (input(f'is {guess2} too high (H), too low (L), or correct (C)? ')).lower()
        if feedback == 'h': 
            high = y - (y - guess2)  
            print(high)
        elif feedback == 'l': 
            low = low + ((guess2+1) - low) 
            print(low)
        
    print(f'the computer guessed your number {guess2}, correctly')

computer_guess(y)