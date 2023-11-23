from matplotlib import pyplot as plt
import numpy as np
x = 3.567

a = np.arange(3.5, 25.5, 0.75)
print(a)
y = ((np.cos(x) / np.sin(x))**3) + 2.24 * a * x
print(y)

max = y.max()
min = y.min()
avg = y.mean()
count = y.size
print(max)
print(min)
print(avg)
print(count)
y.argsort()
print(y)
plt.plot(a, y, color='green', marker='o', markersize=7)
y = a + avg - a
plt.plot(a, y)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('График функции A')
plt.yscale(value='log')
plt.show()