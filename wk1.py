# windows
# python -m venv .venv
# source .venv/Scripts/activate
# code .
#
# MAC / Linux: python3 -m venv .venv
# source .venv/bin/activate
# code .

# deactivate

name = "Jazmine"
age = 28
height = 5.8

is_student= True
balance = 1000.75
first_name = "Charlie"
number_of_days = 7

print(type(balance))

num_str = "42"
num_int = int(num_str)
num_float = float(num_int)
num_str_again = str(num_float)

is_empty = not bool("") #Like asking is not a bool(arg)
is_non_zero = bool(5)

age = 30
try:
    message = "I am " + age + " years old."  # This will raise a TypeError
    print(message)
except Exception as e:
    print(f"Error: {e}")

age = 30
message = "I am " + str(age) + " years old." #correct.
print(message)

#Implicit Vs Explicit - implied, vs forced type
# Implicit conversion
result = 3 + 2.5  # 5.5 (float, because Python converts the integer to float)

# Explicit conversion
result = int(2.8) + 3  # 5 (integer, because we explicitly converted the float to int)

# Arithmetic
result = 10 + 5  # 15
remainder = 9 % 4  # 1 
print(result)
print(remainder)

# Comparison
print(5 > 3)  # True
# Logical
print(True and False)  # False

print(8 // 3) #int vs float division
print(8 / 3) #float



# + (addition): 3 + 2 → 5
# - (subtraction): 5 - 3 → 2
# * (multiplication): 4 * 2 → 8
# / (division): 9 / 3 → 3.0
# // (integer division): 9 // 3 → 3
# % (modulus, remainder): 7 % 3 → 1
# ** (exponentiation): 2 ** 3 → 8
# Comparison Operators: Compare two values and return a Boolean (True or False)

# == (equal to): 5 == 5 → True
# != (not equal to): 5 != 4 → True
# < (less than): 3 < 4 → True
# > (greater than): 10 > 5 → True
# <= (less than or equal to): 5 <= 5 → True
# >= (greater than or equal to): 7 >= 3 → True
# Logical Operators: Used to combine conditional statements

# and: True and False → False
# or: True or False → True
# not: not True → False

def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")


# def check_number(num):if num > 0:  # This will raise an error because it's not indented properly
#     print("Positive number")


def check_number(num):
    if num > 0:  
        print("Check number function: ","Positive number")
check_number(5)

#Loops
for i in range(3):
    print("Loop iteration:", i)


#Control flow. 
age = 20

if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")

#nested conditionals:
score = 85

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        print("C")

# Looping through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Using range to loop a specific number of times
#For loop
for i in range(3):
    print("Loop iteration:", i)

#while loop
count = 0

while count < 3:
    print("Count is:", count)
    count += 1

#break loop:
for num in range(10):
    if num == 5:
        break
    print(num)

#skip iteration:
for num in range(5):
    if num == 2:
        continue
    print(num)

#functions: 
def greet():
    print("Hello, world!")
greet()

#single param
def greet(name):
    print("Hello, " + name + "!")
    
greet("Jazmine")

# multiple params
def add(a, b):
    print(a + b)

add(3, 5)

#return:
def square(number):
    return number * number

result = square(4)
print(result)

def greet(name="stranger"):
    print("Hello, " + name + "!")

greet()            # Output: Hello, stranger!
greet("Luis") # Output: Hello, Luis!

# any number of args
# Use *args when the exact number of arguments isn't known beforehand.
# The collected arguments are treated as a tuple. ()
def add_numbers(*args):
    print("args shape: ", args)
    return sum(args)

print(add_numbers(1, 2, 3, 4))

# kwargs allows a function to accept any number of keyword arguments, 
# which are collected into a dictionary. {}
# Use **kwargs when you expect dynamic named parameters.
# The collected arguments are treated as a dictionary.
def print_info(**kwargs):
    print("Kwargs shape: ", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Janet", role="Developer", age=25)

def mixed_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_function(1, 2, 3, name="Janet", role="Developer")

def mixed_function_2(*args, a_value="default"):
    print(f"args are {args} and a_value is {a_value}")

mixed_function_2(1, 2, 3, a_value="override")

#variable local scope example:
# def set_name():
#     name="James"

# set_name()
# print(name)

name = "Hima"

def set_name():
    name="James"

set_name()
print(name) # Prints "Hima"

def set_name_2(name):
    name = "Nguyen"

# set_name_2() #needs and arg
print(name) # Prints "Hima

def print_global_name():
    print(name) # Prints "Hima

this_list=[0,1] # a global
def change_list():
    this_list[1]=17 # Does change this_list[1] for the this_list global

# print debugging.
def multiply(a, b):
    result = a * b
    print("Result is: ", result)  # Print to check the result
    return result

multiply(3, 5)

# Logging Levels

#* DEBUG: Detailed information, typically useful only for debugging.
#* INFO: Confirmation that things are working as expected.
#* WARNING: An indication that something unexpected happened, or indicative of future problems.
#! ERROR: A serious problem that prevented some part of the code from running.

# Step 1
import logging

# Step 2
logging.basicConfig(level=logging.DEBUG)

# Step 3
def multiply(a, b):
    logging.debug(f"Multiplying {a} and {b}")
    result = a * b
    logging.info(f"Result is: {result}")
    return result

multiply(3, 5)

# Error handling
try:
    result = 10 / 0 # divide by zero error. 
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    num = int(input("Enter a number: "))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Success! The result is {result}.")

try:
    file = open("example.txt", "r") # Make sure you close files, with open will close automatically
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()
    print("File closed.")