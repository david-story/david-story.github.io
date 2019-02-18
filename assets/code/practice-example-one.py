"""
Practice File 1
Created by David Story

Description: Basics of Python including variables, datatypes, arithmetic, and functions.
"""

# This is how you print to the console
print("Hello, World!")

# we can create an integer called x with integer value 1
x = 1

# we can create an integer called y with integer value -1
y = -1

# we can print both values
print("x:", x, "|y:", y)

# We can add those two variables into a new variable z
z = x + y

# this is the value of z
print("z =", z)

# We can make a variable string that is a string
string = "This is a string"

# we create another string
other_string = "The value of z is: "

# we can make the current value of z a string
z = str(z)

# Here are some more data types!

one = 1
boolean = bool(one)
floatingpoint = float(1)
anotherfloat = floatingpoint + 0.111111
newinteger = int(anotherfloat)

print("An integer:", one)
print("A boolean:", boolean)
print("A floating point:", floatingpoint)
print("Another floating point:", anotherfloat)
print("A float converted to an integeer:", newinteger)

# we can add strings!
other_string = other_string + z
print(other_string)

# this is how we define a function!
# it has an input, z
def this_is_a_function(parameter):
    # it prints the parameter
    print("We were passed parameter:", parameter)
    # it returns parameter
    return z

# this is how we tell python to execute a function, with its parameter = z
this_is_a_function(z)

# Here is a list of examples of different operations in Python
# e = 2, f = 2
e, f = 2, 2
odd = 3
even = 2

multiplied = e*f
powerofvariable = e**f
remainder = 3 % 2
plus = odd + even
minus = odd - even

# this is how we import libraries
import math

pi = math.pi
print("Pi is:", pi)

# We can even calculate the area of a circle
# area of a circle = pi multiplied by the radius squared
radius = 2
area = (radius**2) * pi
print("The area of circle of radius", radius, "is:", area)

# Now lets make it so the user can make a function where they can specify the radius
# It has no input as a parameter
def circleRadius():
    userinput = input("Pick a number for tha radius of the circle so we can calculate the area: ")

    # Note! when you use the input() command, it returns a string! so we must make this a float or an int,
    # lets make a float for more precision. We will use a try-except to make sure we don't cause any errors
    # if the user passes an invalid input (such as a character or bad string)

    try:
        radius = float(userinput)
        area = math.pi * (radius**2)
        print("The area of the circle of radius", radius, "is:", area)
        return area
    except:
        print("Bad input! Try again...")
        return None

# we will now call this function, and its output will be sent to a variable called 'functionOutput'

functionOutput = circleRadius()
print("Our function output was:", functionOutput)