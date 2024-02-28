# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


# Solution
number = int(input('Please enter a number: '))

if number % 2 == 0 and number % 4 != 0:
    print(f'{number} is an even number')
elif number % 4 == 0:
    print(f'{number} is a multiple of 4')
else:
    print(f'{number} is an odd number')

num = int(input('Please enter a number to check: '))
check = int(input('Please enter a number to divide by: '))

if num % check == 0:
    print(f'{check} divides evenly into {num}')
else:
    print(f'{check} does not divide evenly into {num}')


# Solution from website for main exercise (added conversion)    
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("You picked an odd number.")
# else:
#     print("You picked an even number.")

# # Solution from website for whole exercise
    
# num = int(input("give me a number to check: "))
# check = int(input("give me a number to divide by: "))

# if num % 4 == 0:
#     print(num, "is a multiple of 4")
# elif num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")

# if num % check == 0:
#     print(num, "divides evenly by", check)
# else:
#     print(num, "does not divide evenly by", check)