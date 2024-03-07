# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!


# Solution
var1 = 84
var2 = 541
var3 = 99

def max(var1,var2,var3):
    if var1 > var2:
        if var1 > var3:
            return var1
    if var2 > var3:
        if var2 > var1:
            return var2
    if var3 > var2:
        if var3 > var1:
            return var3
    
print(max(var1,var2,var3))

############## Solution 1 from website###############
def max_of_three(a,b,c):
     max_3=0
     if a>b:
         #max_3=a
         if a>c:
             max_3=a #changed from max_3 = c
         else:
             max_3=c #changed from max_3 = a
     else:
          if b>c:
             max_3=b
          else:
             max_3=c
     return max_3

