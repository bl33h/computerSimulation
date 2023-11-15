#Copyright (C), 2023-2024, bl33h
#FileName: computerSimulation
#Author: Sara Echeverria, Melissa Perez, Alejandro Ortega
#Version: I
#Creation: 14/11/2023
#Last modification: 15/11/2023

import time
import random

def sumIntegers(a, b):
    return a / b

# number of repetitions
N = int(10E5)

# initialize total time
totalTime = 0

# store individual times for each operation
operationTimes = []

# simulation and time measurement
for _ in range(N):
    # generate random values for a and b (ints)
    a = random.randint(10000, 99999)
    b = random.randint(10000, 99999)

    startTime = time.time()

    # function call for integer addition
    result = sumIntegers(a, b)

    endTime = time.time()

    # time accumulation
    totalTime += endTime - startTime

    # store individual time for the operation
    operationTimes.append(endTime - startTime)

# calculate average time
averageTime = totalTime / N

print(f"division result: {result}")
print(f"total time: {totalTime} seconds")
print(f"average time per operation: {averageTime} seconds")