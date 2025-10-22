print("Hello world")
print(1,2,3,4,5,sep='//') # 1//2//3//4//5


print(123, end='-')
print(234,end='a')
print(1111) # 123-234a1111

# Data Types or Data Structure in python

# 1. List: lists are like array in cpp but a little bit different, [1,2,3,4,5]
# 2. Integers: python can handle upto 1e309
# 3. Double(Float): Python can handle 1.7e309
# 4. Tuples: (1,2,3,4,5)
# 5. Boolean: True or False
# 6. Sets: {1,2,3,4}, always distinct
# 7. Dictionary: these are key-value pairs, {"name":"John Doe", "age":"23"}
# 8. Complex Number: 2+3j


# type function
# returns the data type print(type(12))

# Python is dynamically types language and dynamic binding is present in python

# Assign multiple variables
a,b,c=1,2,3
print(a,b,c,sep=",")

# Assign multiple variables with same value
x=y=z=5
print(x,y,z,sep=",")

# Keywords & Identifiers
# Keywords are predefined set od words which are reserved for python. In python there are 32 keywords.
# Identifiers are names which helps to identify variables, function to prgrammers
# ex- name01="John", def reverseMe(name), etc

# User Input
name = input("Enter your name")
age = int(input("Enter your age"))# this is type conversion
print(f"Your name is {name} and age is {age-1}")
# Type conversion: There are implicit and explicit type conversions in python

# Literals: the value that is stored in varibale is called literal
a=0b1010 # binary literal
b=100 # Decimal literal
c= 0o310 # octal literal
d= 0x12c # Hexadecimal Literal

# float literal

x=10.2
y=1.5e2
z=2.5e-3

# complex literals

num = 3.5j

# string = 'This is Python'
# strings = "This is Python"
# char = "C"
# multiline_str="""Hi this is multiline string"""
# unicode = u"\U0001f600\U0001F606\U0001F92"
# raw_str = r"raw \n string"
# print(unicode)

# none is special lieral that means nothing.