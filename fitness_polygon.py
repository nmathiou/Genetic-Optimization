
import numpy as np


import matplotlib.pyplot as plt





def fitness_func_polygon(params):
    a = 0
    points = []
    sides = []
    for i in range(0, len(params), 2):
        points.append([params[i], params[i+1]])



    for p in range(len(points)-1):
        sides.append(np.sqrt((points[p+1][1] - points[p][1])**2 + (points[p+1][0] - points[p][0])**2))
    sides.append(np.sqrt((points[0][1] - points[-1][1])**2 + (points[0][0] - points[-1][0])**2))

    perimeter = sum(sides)

    for p in range(len(points)-1):
        a += points[p][0]*points[p+1][1] - points[p+1][0]*points[p][1]
    a += points[-1][0]*points[0][1] - points[-1][0]*points[0][1]


    area = 0.5*np.abs(a)

    return (area)/(perimeter)

