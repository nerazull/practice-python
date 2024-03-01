# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


# Solution (expanding on Exercise 4)
def is_prime(text = "Enter a number: "):
    number = int(input(text))

    divisor_candidates = range(1,number+1)
    divisors = [divisor for divisor in divisor_candidates if number % divisor == 0]

    if divisors == [1, number]:
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')
        
is_prime()


############ Solution 1 from website ##############################
# import sys
# number = input("Please enter a number" + "\n" + ">>>")
# number = int(number)
# prime = False #initiate boolean for true false, default false

# if number > 0:
#     for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
#         if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
#             continue 
#         elif number % x == 0: #If number is evenly divisible by x, it can't be prime
#             sys.exit("The number is not prime.")
#     sys.exit("The number is prime.") #number wasn't evenly divisible by any x, so it's prime
# elif number == 0:
#     sys.exit("The number is not prime.") #According to the Google, 0 is not prime
# else:#if number is less than 0, the number is not prime (according to the Google).
#     sys.exit("The number is not prime.")


############ Solution 3 from website ##############################
# num = int(raw_input('Insert a number: '))
# a = [x for x in range(2, num) if num % x == 0]

# def is_prime(n):
# 	if num > 1:
# 		if len(a) == 0:
# 			print 'prime'
# 		else:
# 			print 'NOT prime'
# 	else:
# 		print 'NOT prime'
	
# is_prime(num)