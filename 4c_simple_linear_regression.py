#!/usr/bin/python

import matplotlib.pyplot as plt

# trainings (x, y) pairs
trainings = [[1,2], [3,6], [7,14], [2,4], [4,8]]
print("trainings:", trainings)

trainings_X = [row[0] for row in trainings]
trainings_Y = [row[1] for row in trainings]

import random
import time

# hypothesis: y = ax + b
while True:
    a = random.uniform(0, 10)
    b = random.uniform(0, 10)

    err = 0

    for i, t_x in enumerate(trainings_X):
        y = a * t_x + b  # hypothesis
        t_y = trainings_Y[i]  # labels
        err += abs(y - t_y)  # cost
    print("a=", a, "b=", b, "err=", err)
    time.sleep(1)
