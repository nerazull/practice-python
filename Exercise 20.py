# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

# Solution
l = [2, 4, 6, 8, 10]
number = 10

def search(a_list, number):
    if number in a_list:
        print(True)
    else:
        print(False)

search(l, number)

# OR

def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False

print(find(l, number))


#################### Iterative binary search solution from geeksforgeeks , better explained than website ########################
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


#################### Bisect built-in module binary search from geeksforgeeks, just to see other options ########################
import bisect
  
def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
  
  
# Test array
arr = [2, 3, 4, 10, 40]
x = 10
  
# Function call
result = binary_search_bisect(arr, x)
  
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")