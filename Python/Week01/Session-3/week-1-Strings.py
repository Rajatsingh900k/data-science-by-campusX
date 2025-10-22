# Strings are sequence of unicode characters not ASCII characters.
# ASCII is 8 bit
# Unicode is 16 bit 

# string creation
s='hi'
s="hi"
# multi line strings
s='''hi'''
s="""hi"""
str('hello')

# Indexing
#  012345678910
s='hello world'
print(s[0])

# Negative indexing
#  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  
s='hello world'
print(s[-1])

# Slicing

s="Hello world"
print(s[0:5]) # end point is exclusive
print(s[0:]) # prints whole string
print(s[:5])
print(s[0:5:2]) # third argument is step size are in for loop
# if step size if negative then start>end as the string will be print in reverse order.
print(s[::-1])

###################################################################################################

# Editing and deleting in strings

s="Hello world" # string are immutable
# s[0]="R" throws error.

# deleting a string
del s
