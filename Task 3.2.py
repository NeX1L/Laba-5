import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(0, 2, 10)
y = np.linspace(0, 2, 10)

X, Y = np.meshgrid(x, y)

def Formule1(x,y):
    return np.power(x, 0.25) + np.power(y, 0.25)

def Formule2(x,y):
    return np.power(x, 2) - np.power(y, 2)

def Formule3(x, y):
    return 2*x + 3*y

def Formule4(x, y):
    return np.power(x, 2) + np.power(y, 2)

def Formule5(x, y):
    return 2 + 2*x + 2*y - np.power(x, 2) - np. power(y, 2)

def plot_function(Formule, title):
    Z = Formule(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='magma')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.show()


plot_function(Formule1, 'z=x^(1/4)+y^(1/4)')
plot_function(Formule2, 'z=x^2-y^2')
plot_function(Formule3, 'z=2x+3y')
plot_function(Formule4, 'z=x^2+y^2')
plot_function(Formule5, 'z=2+2x+2y-x^2-y^2')