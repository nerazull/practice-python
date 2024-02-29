# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a,'\n',b)

# Solution
overlap_list = []

for value in a:
    if value in b and value not in overlap_list:
        overlap_list.append(value)
print(overlap_list)

# Solution for Extra 1
from random import randint

rand_list1 = []
rand_list2 = []

for value in range(10):
    rand_list1.append(randint(0,50))
    rand_list2.append(randint(0,50))
print(rand_list1)
print(rand_list2)

for value in rand_list1:
    if value in rand_list2 and value not in overlap_list:
        overlap_list.append(value)
print(overlap_list)

# Solution for Extra 3
overlap_list = [value for value in rand_list1 if value in rand_list2 and value not in overlap_list]
print(overlap_list)



