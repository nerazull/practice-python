# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

# Solution
a = [5, 10, 15, 20, 25]

def first_last(a_list):
    new_list = [a_list[0], a_list[-1]]
    print(new_list)

first_last(a)

# OR

def first_last(a_list):
    new_list = [a_list[0], a_list[-1]]
    return new_list

print(first_last(a))


# Solution from website

# def list_ends(a_list):
#     return [a_list[0], a_list[len(a_list)-1]]
