from src.base.individual import Individual
from src.population import Population





def fitness_func(params):
    return params[0]**2 - params[1]**3 + params[2]**2 + params[3]**3



if __name__ == "__main__":
    pop = Population(pop_size = 200, parameters_bounds=[[-1, 1], [1, 2], [3, 12], [-3, -1]], fitness_function=fitness_func)

    pop.initialize()

    pop.calculate_fitness()

    print(pop.avg_fitness())
    print(pop.get_best_individuals()[0].fitness)

    print(1 - 1 + 12**2 + -1**3)