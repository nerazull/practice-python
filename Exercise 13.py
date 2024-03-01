# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# Solution
def quantity():
    user_input = int(input('How many Fibonacci numbers do you want to generate?: '))
    return user_input

def fibonacci(quantity):
    a, b = 0, 1
    for i in range(quantity):
        print(a)
        a, b = b, a + b 
        # This works correctly as oppsed to declaring the new a and b on separate lines (e.g. a = b \n b = a + b) because a is getting the old value of b and b is getting the old sum of a and b, 
        # whereas if they were declared on separate lines, a would still get the value of old b but b would take the value of new a instead of old a

fibonacci(quantity())

# Solution 2 from website
# def fibonacci():
#     num = int(input("How many numbers that generates?:"))
#     i = 1
#     if num == 0:
#         fib = []
#     elif num == 1:
#         fib = [1]
#     elif num == 2:
#         fib = [1,1]
#     elif num > 2:
#         fib = [1,1]
#         while i < (num - 1):
#             fib.append(fib[i] + fib[i-1]) # fib[i] = second index in list, fib[i-1] = first index in list
#             i += 1
#     return fib
# print(fibonacci())
# input()

