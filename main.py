"""
author: Jana Cápíková
email: capikovajana@gmail.com
"""

import random
import time 

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

while True:
    secret_number = str(random.randint(1000, 9999))
    if len(set(secret_number)) == len(secret_number):
       break

secret_number_length = len(secret_number)
attempts = 0
start = time.time()

while True:
    user_number = input("Enter a number: ")
    attempts += 1
    if len(user_number) != secret_number_length:
        print(f"Please enter a {secret_number_length}-digit number.")
        continue
    if not user_number.isdigit():
        print("Only numeric characters are allowed.") 
        continue
    if user_number[0] == "0":
        print("Please enter a number that does not begin with 0.") 
        continue
    if len(set(user_number)) != len(user_number):
        print("The number must not contain any repeated digits.")
        continue
    bulls = 0
    cows = 0    
    for i in range(len(secret_number)):
        if secret_number[i] == user_number[i]:
            bulls += 1
        elif secret_number[i] != user_number[i] and user_number[i] in secret_number:
            cows += 1

    if bulls <= 1:
        unit_bull = "bull"
    else:
        unit_bull = "bulls"
    
    if cows <= 1:
        unit_cow = "cow"
    else:
        unit_cow = "cows"

    print(f"{bulls} {unit_bull}, {cows} {unit_cow}")
    print("-" * 47)

    if bulls == secret_number_length:
        end = time.time()
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
        print(f"Time: {round(end - start, 2)} seconds")
        print("-" * 47)
        print("That's amazing!")
        break

