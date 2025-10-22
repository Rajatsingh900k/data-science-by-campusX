# Operators

# Arithematic Operators:- +, -, *, **, /, //, %
print(1+2)
print(5-6)
print(3*2)
print(6//3) # integer division
print(6/3)
print(2**3) # Power of or exponent
print(5%2)

# Relation Operators:- >, <, ==, !=, >=, <=

# Logical Operators:- and, not and or(in cpp and java it's &&, !, ||)

# Bitwise Operators:- &, |, ~, ^, <<, >>

# Assignent Operators:- =, +=, -=, *=, /=, %= 
# Note in python a++ or ++a in not valid in python.

# Membership Operators:- in, not in
# Note it's case sensitive
print('D' in 'Delhi')
print('R' not in 'Delhi')

###################################################################################################

# Conditional in Python

# if-elif-else
a=1
if a==12:
    print("12")
elif a>12:
    print("Greater than 12")
else:
    print("Smaller than 12")

# Match-case
day_number = 0

match day_number:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:  # Default case
        print("Invalid day number")

###################################################################################################

# Modules:- Modules are like libraries in cpp and packages in java. just the diffrence of name.

# math
# Keywords
# random
# datetime

import math
print(math.sqrt(9))

import keyword
print(keyword.kwlist)

import random
print(random.randint(1,200)) # both inclusive upper and lower limit

import datetime
print(datetime.datetime.now())

# to get to know about modules in python use help('modules')

###################################################################################################

# Loops in Python

# While Loop

# num=int(input("Enter a Number: "))
# i=1
# while i<11:
#     print(i*num)
#     i+=1

# unlike cpp or java, in python we can use else with loops as well

x=1
while x<3:
    print(x)
    x+=1
else:
    print("Limit Reached")

# For Loop: for loop of python can iterate not only on numbers but on other data types as well

for i in range(0,10): # upper limit is exclusive
    print(i)

for x in range(0,101, 5): # third parameter is step size(basicaly third parameter is nothing but inc or dec )
    print(x)

for i in range(10,0,-1):
    print(i)

for i in "Delhi":
    print(i)