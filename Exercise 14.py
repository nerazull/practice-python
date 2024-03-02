# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# 1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# 2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.

##################### Exercise 5 #####################
### Take two lists, say for example these two:
###
### a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
### b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
### and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
###
### Extras:
###
### 1. Randomly generate two lists to test this
### 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#####################################################


# Solution for main and extra 1
a_list = [1, 1, 2, 3, 4, 3]
another_list = [1, 1, 5, 9, 2, 2]

def remove_duplicates_loop(a_list):
    new_list = []
    for value in a_list:
        if value not in new_list:
            new_list.append(value)
    print(new_list) # or return and call it with print

remove_duplicates_loop(a_list)

def remove_duplicates_set(a_list):
    a_list = set(a_list)
    a_list = list(a_list)
    print(a_list) # or return and call it with print

remove_duplicates_set(a_list)

# Solution for extra 2
def exercise5_remove_set(list1,list2):
    new_list = print(list(set(list1).intersection(set(list2)))) # or return and call it with print

exercise5_remove_set(a_list, another_list)

# OR

import random

def exercise5_remove_set_random():
    list1 = random.sample(range(100), 13)
    list2 = random.sample(range(50), 10)
    new_list = print(list(set(list1).intersection(set(list2)))) # or return and call it with print

    # OR
    
    new_list = print(list(set(random.sample(range(100), 13)).intersection(set(random.sample(range(50), 10))))) # or return and call it with print



################ Solution from website ################
# this one uses a for loop
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(dedupe_v1(a))
print(dedupe_v2(a))


