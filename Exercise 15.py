# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.


# Solution
def reverse_string():
    user_input = input('Please enter a sentence: ').split()
    # list_input = user_input.split()
    reversedstring = " ".join(user_input[::-1])
    print(reversedstring)

reverse_string()

############# Solution from website
def reverseWord(w):
  return ' '.join(w.split()[::-1])


############# Other solutions from website
# method 1: loop through the words and insert each word at the begining of the result list
def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)

# method 2
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])
  
# method 3
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))

# method 4
def reverse_v4(x):
  y = x.split()
  y.reverse()
  return " ".join(y)

# test code
test1 = input("Enter a sentence: ")
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))