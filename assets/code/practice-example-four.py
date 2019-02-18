"""
Practice File 4
Created by David Story

Description: Some nice examples of things you can do with functions from the following libraries:
    - sys
    - os
    - time
    - datetime
"""

import sys
import os
import time
import datetime

# get the time
print(time.time())

# get the current date
print(datetime.date.today())

# prints the current working directory
print(os.getcwd())

# saves your current working directory
your_working_directory = os.getcwd()

# changes directory to the C:\\ drive
os.chdir("C:\\")

# prints the current working directory
print(os.getcwd())

# change to the original current working directory
os.chdir(your_working_directory)

# prints the directory
print(os.getcwd())

# gets number of cores on your cpu
computer_cpu_count = os.cpu_count()

print("This computer has this many CPU cores:", computer_cpu_count)

seconds = 2
time_1 = time.time()
time.sleep(seconds)
time_2 = time.time()

print("The sleep operation took this many seconds:", (time_2-time_1))