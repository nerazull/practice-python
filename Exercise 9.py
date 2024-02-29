# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.


# Solution
from random import randint
from sys import exit

tries = []
guess = 0
rand_number = 0

while True:

    if guess == rand_number:
        random_number = rand_number = randint(1,9)
        
    user_input = input('Guess the number: ')
    check_list = list(range(1,10))

    if user_input == 'exit':
        print(sum(tries))
        exit()

    if not user_input or user_input.isspace() or user_input not in str(check_list).replace(',', '') or int(user_input) not in check_list:
        print('Invalid value. Please enter a number between 1 and 9.')
        continue

    if int(user_input) > random_number:
        print('Too high')
    elif int(user_input) < random_number:
        print('Too low')
    else:
        print('You guessed the number!')

    if user_input:
        tries.append(1)
        guess = int(user_input)



############## Solution 1 from website ##########################################
# import random

# rd = random.randint(1,9)
# guess = 0
# c = 0
# while guess != rd and guess != "exit":
#     guess = input("Enter a guess between 1 to 9")

#     if guess == "exit":
#         break

#     guess = int(guess)
#     c += 1

#     if guess < rd:
#         print("Too low")
#     elif guess > rd:
#         print("Too high")
#     else:
#         print("Right!")
#         print("You took only", c, "tries!")
# input()



############## Solution 2 from website ##########################################
# import random

# # Awroken

# MINIMUM = 1
# MAXIMUM = 9
# NUMBER = random.randint(MINIMUM, MAXIMUM)
# GUESS = None
# ANOTHER = None
# TRY = 0
# RUNNING = True

# print("Alright...")

# while RUNNING:
#     GUESS = input("What is your lucky number? ")
#     if int(GUESS) < NUMBER:
#         print("Wrong, too low.")
#     elif int(GUESS) > NUMBER:
#         print("Wrong, too high.")
#     elif GUESS.lower() == "exit":
#         print("Better luck next time.")
#     elif int(GUESS) == NUMBER:
#         print("Yes, that's the one, %s." % str(NUMBER))
#         if TRY < 2:
#             print("Impressive, only %s tries." % str(TRY))
#         elif TRY > 2 and TRY < 10:
#             print("Pretty good, %s tries." % str(TRY))
#         else:
#             print("Bad, %s tries." % str(TRY))
#         RUNNING = False
#     TRY += 1