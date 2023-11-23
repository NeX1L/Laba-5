from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x ** 2
z1 = pow(x, 0.25) + pow(y, 0.25)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z1, label='parametric curve', color='#123456')
plt.title('График функции z1')
plt.show()

z2 = pow(x, 2) - pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z2, label='parametric curve', color='#abcdef')
plt.title('График функции z2')
plt.show()

z3 = 2 * x + 3 * y
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z3, label='parametric curve', color='#aab591')
plt.title('График функции z3')
plt.show()

z4 = pow(x, 2) + pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z4, label='parametric curve', color='#9343ff')
plt.title('График функции z4')
plt.show()

z5 = 2 + 2 * x + 2 * y - pow(x, 2) - pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z5, label='parametric curve', color='#7f3eab')
plt.title('График функции z5')
plt.show()