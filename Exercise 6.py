# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


# Solution
user_string = input('Please enter a string: ').lower() # Expanded on solution and added .lower() to ignore upper/lower case
backward_string = user_string[-1:-len(user_string)-1:-1]

if user_string[0:len(user_string)] == backward_string:
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')


# Solution from website no1
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')


# Solution from website no2
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")