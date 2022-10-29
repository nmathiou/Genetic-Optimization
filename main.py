from src.base.individual import Individual
from src.population import Population
import numpy as np
import matplotlib.pyplot as plt

from fitness_polygon import fitness_func_polygon

def fitness_func(params):
    
    point_1 = [params[0], params[1]]
    point_2 = [params[2], params[3]]
    point_3 = [params[4], params[5]]
    point_4 = [params[6], params[7]]

    x1 = point_1[0]
    y1 = point_1[1]

    x2 = point_2[0]
    y2 = point_2[1]
    
    x3 = point_3[0]
    y3 = point_3[1]
    
    x4 = point_4[0]
    y4 = point_4[1]

    side_1 = np.sqrt((point_2[1] - point_1[1])**2 + (point_2[0] - point_1[0])**2)
    side_2 = np.sqrt((point_3[1] - point_2[1])**2 + (point_3[0] - point_2[0])**2)
    side_3 = np.sqrt((point_4[1] - point_3[1])**2 + (point_4[0] - point_3[0])**2)
    side_4 = np.sqrt((point_1[1] - point_4[1])**2 + (point_1[0] - point_4[0])**2)
    area = 0.5*np.abs((x1*y2 - x2*y1) + (x2*y3-x3*y2) + (x3*y4 - x4*y3) + (x4*y1-x1*y4))
    perimeter = side_1 + side_2 + side_3 + side_4
    return perimeter - area

# def fitness_func(params):
    
#     point_1 = [params[0], params[1]]
#     point_2 = [params[2], params[3]]
#     point_3 = [params[4], params[5]]
#     # point_4 = [params[6], params[7]]

#     x1 = point_1[0]
#     y1 = point_1[1]

#     x2 = point_2[0]
#     y2 = point_2[1]
    
#     x3 = point_3[0]
#     y3 = point_3[1]
    
#     # x4 = point_4[0]
#     # y4 = point_4[1]

#     side_1 = np.sqrt((point_2[1] - point_1[1])**2 + (point_2[0] - point_1[0])**2)
#     side_2 = np.sqrt((point_3[1] - point_2[1])**2 + (point_3[0] - point_2[0])**2)
#     side_3 = np.sqrt((point_1[1] - point_3[1])**2 + (point_1[0] - point_3[0])**2)
#     # side_4 = np.sqrt((point_1[1] - point_4[1])**2 + (point_1[0] - point_4[0])**2)
#     area = 0.5*np.abs((x1*y2 - x2*y1) + (x2*y3-x3*y2) + (x3*y1 - x1*y3))
#     return area


if __name__ == "__main__":
    pop = Population(mutation_rate = 0.05, pop_size = 100, parameters_bounds=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]], fitness_function=fitness_func_polygon)
    # pop = Population(mutation_rate = 0.1, pop_size = 100, parameters_bounds=[ [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]], fitness_function=fitness_func)

    pop.initialize()
    generations = 1000
    avg_fit = []
    best_fit = []
    for i in range(generations):
        pop.advance_generation()
        print(f"--------------------Generation: {i}------------------------")
        print(f"Average fitness: {pop.avg_fitness()}")
        print(f"Best fitness: {pop.get_best_individuals()[0].fitness}\n")
        avg_fit.append(pop.avg_fitness())
        best_fit.append(pop.get_best_individuals()[0].fitness)

    ################################################################
    params = pop.get_best_individuals()[0].parameters
    borders_x = [0, 1, 1, 0, 0]
    borders_y = [0, 0, 1, 1, 0]
    xx = [params[x] for x in range(0, len(params), 2)]
    xx.append(params[0])
    yy = [params[x] for x in range(1, len(params), 2)]
    yy.append(params[1])

    # point_1 = [params[0], params[1]]
    # point_2 = [params[2], params[3]]
    # point_3 = [params[4], params[5]]
    # point_4 = [params[6], params[7]]
    plt.cla()
    plt.plot(borders_x, borders_y, 'g.')
    plt.plot(xx, yy, "b")
    plt.plot(xx, yy, "r*")
    # plt.draw()
    # plt.pause(0.001)

        
    # plt.cla()
    # plt.plot(np.arange(generations), avg_fit, "b")
    # plt.plot(np.arange(generations), best_fit, "r")
    # plt.grid()
    plt.show()