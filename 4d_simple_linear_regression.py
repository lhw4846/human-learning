#!/usr/bin/python

import matplotlib.pyplot as plt

# trainings (x, y) pairs
trainings = [[1,2], [3,6], [7,14], [2,4], [4,8]]
print("trainings:", trainings)

trainings_X = [row[0] for row in trainings]
trainings_Y = [row[1] for row in trainings]

import random
import time

MAX = 1000
best_a = -MAX
best_b = -MAX
err_min = MAX^3
count = 0

# hypothesis: y = ax + b
while True:
    a = random.uniform(-MAX, MAX)
    b = random.uniform(-MAX, MAX)

    err = 0
    count += 1

    for i, t_x in enumerate(trainings_X):
        y = a * t_x + b  # hypothesis
        t_y = trainings_Y[i]  # labels
        err += abs(y - t_y)  # cost

    if err < err_min:
        err_min = err
        best_a = a
        best_b = b

    if count % 10000 == 0:
        print("a=", a, "b=", b, "err=", err)
        print(" ", "best_a=", best_a, "best_b=", best_b, "err_min=", err_min)


    #time.sleep(0.01)
