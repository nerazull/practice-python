# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
#  And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

# Solution
def find_overlap(primes,happy):
    overlap = []
    for number in primenumbers:
        if number in happynumbers:
            overlap.append(number)
    return overlap

primenumbers = []
happynumbers = []

with open('D:/Programming/primenumbers.txt', 'r') as open_file:
    primenumbers = open_file.read().split('\n')
    
with open('D:/Programming/happynumbers.txt', 'r') as open_file:
    happynumbers = open_file.read().split('\n')

print(find_overlap(primenumbers, happynumbers))


########################### Happy numbers algorithm copied from recommended wiki page in order to understand the topic
# def pdi_function(number, base: int = 10):
#     """Perfect digital invariant function."""
#     total = 0
#     while number > 0:
#         total += pow(number % base, 2)
#         number = number // base
#     return total

# def is_happy(number: int) -> bool:
#     """Determine if the specified number is a happy number."""
#     seen_numbers = set()
#     while number > 1 and number not in seen_numbers:
#         seen_numbers.add(number)
#         number = pdi_function(number)
#     return number == 1

########################### Solution 1 from website ###############################
# primeslist = []
# with open('primenumbers.txt') as primesfile:
# 	line = primesfile.readline()
# 	while line:
# 		primeslist.append(int(line))
# 		line = primesfile.readline()

# happieslist = []
# with open('happynumbers.txt') as happiesfile:
# 	line = happiesfile.readline()
# 	while line:
# 		happieslist.append(int(line))
# 		line = happiesfile.readline()

# overlaplist = []
# for elem in primeslist:
# 	if elem in happieslist:
# 		overlaplist.append(elem)
		
# print(overlaplist)

########################### Solution 2 from website ###############################
# def filetolistofints(filename):
# 	list_to_return = []
# 	with open(filename) as f:
# 		line = f.readline()
# 		while line:
# 			list_to_return.append(int(line))
# 			line = f.readline()
# 	return list_to_return

# primeslist = filetolistofints('primenumbers.txt')
# happieslist = filetolistofints('happynumbers.txt')

# overlaplist = [elem for elem in primeslist if elem in happieslist]
# print(overlaplist)

