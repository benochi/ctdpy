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
