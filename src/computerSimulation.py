#Copyright (C), 2023-2024, bl33h
#FileName: computerSimulation
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 14/11/2023
#Last modification: 14/11/2023

import time
import random

def sumIntegers(a, b):
    return a + b

# number of repetitions
N = 100000

# initialize total time
totalTime = 0

# simulation and time measurement
for _ in range(N):
    # generate random values for a and b (ints)
    a = random.randint(1000000000, 9000000000)
    b = random.randint(1000000000, 9000000000)

    startTime = time.time()

    # function call for integer addition
    result = sumIntegers(a, b)

    endTime = time.time()

    # time accumulation
    totalTime += endTime - startTime

# calculate average time
averageTime = totalTime / N

print(f"addition result: {result}")
print(f"total time: {totalTime} seconds")
print(f"average time per operation: {averageTime} seconds")