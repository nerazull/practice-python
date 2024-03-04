# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. 
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


# Initial start of flawed attempt
with open("D:/Programming/Training_01.txt", 'r') as open_file:
    all_text = open_file.read().split()
    darth = all_text.count('Darth')
    lea = all_text.count('Lea')
    luke = all_text.count('Luke')    
    print(darth)
    print(lea)
    print(luke)

with open("D:/Programming/Training_02.txt", 'r') as open_file:
    line = open_file.readline()
    for line in open_file:
        result = line.split('/')
        print(result[2])
        
# Solution from website for main exercise        
# counter_dict = {}
# with open("D:/Programming/Training_01.txt", 'r') as open_file:
#     line = open_file.readline()
#     while line:
#         line = line.strip()
#         if line in counter_dict:
#             counter_dict[line] += 1
#         else:
#             counter_dict[line] = 1
#         line = open_file.readline()

# print(counter_dict)

# Solution for Extra
new_dict = {}
with open("D:/Programming/Training_02.txt", 'r') as open_file:
    line = open_file.readline()
    while line:
        result = line.split('/')
        if result[2] in new_dict:
            new_dict[result[2]] += 1
        else:
            new_dict[result[2]] = 1
        line = open_file.readline()

print(new_dict)