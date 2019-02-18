"""
Practice File 2
Created by David Story

Description: This has refreshers on logic, loops, and lists
"""

# With logic we can make decisions.
# An if statement lets us test 'if' our value is true, and then do something

# We make x = 1
x = 1

def logic(x):
    # if it is equal to 1, then we do something
    if x == 1:
        print("Do something")

    # else if (elif) x is not equal to 1 (!=), we do something else
    elif x != 1:
        print("Do something else")

    # else, if none of the above was true, we have this final case
    else:
        print("Do the last thing")

logic(1)
logic(2)
logic(3)

# We can define basic loops, one that needs a condition to stop (While loop) and one that has a
# specified range (for loop)

# while x == 1 is true, then we continue looping
y = 1
while y == 1:
    y = y + 1
    print("Current value of y:", y)

# always make sure you have an achieveable exit condition or you will be stuck in the loop infinitely!

# We can also define loops with ranges!

# For the range of 0 to 2, or 3 iterations...
for i in range(3):
    # we will print the current value of i
    print(i)

# this is a list, it contains multiple elements!
list = ["David Story", "Story David", "DaViD StOrY", "yrotS divaD"]

# we can make for loops iterate over the range of just a list!
# or, we can say we want to iterate for every element in a list like this:

for name in list:
    # we will now print each element
    print(name)

# this is an empty list!
empty = []

# we can add things to lists like such
for j in range(5):
    empty.append(j)

# lets see whats in our list!
print(empty)

# not so empty anymore, lets print out each element individually

for item in empty:
    print(item)

# lets get the last item from the list
lastitem = empty.pop()

# Lets see what that item was and what our list looks like now!
print("Item popped:", lastitem)
print("Our list:", empty)