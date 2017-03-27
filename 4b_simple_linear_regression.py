#!/usr/bin/python

import matplotlib.pyplot as plt

# trainings (x, y) pairs
trainings = [[1,2], [3,6], [7,14], [2,4], [4,8]]
print("trainings:", trainings)

trainings_X = [[row[0] for row in trainings]]
trainings_Y = [[row[1] for row in trainings]]

#plt.plot(trainings, "o")
plt.plot(trainings_X, trainings_Y, "o")
plt.axis([0,20,0,20])
plt.show()