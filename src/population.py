from src.base.individual import Individual
import numpy as np





class Population:
    
    def __init__(self, pop_size = 100, parameters_bounds=[[-1, 1], [1, 2], [3, 12], [-3, -1]], fitness_function = None):
        self.pop_size = pop_size
        self.parameters_size = len(parameters_bounds)
        self.upper_bounds = np.array([x[1] for x in parameters_bounds])
        self.lower_bounds = np.array([x[0] for x in parameters_bounds])
        self.population = []
        self.is_sorted = False
        self.fitness_function = fitness_function
    

    def initialize(self):
        
        random_parameters = np.random.rand(self.pop_size, self.parameters_size)*(self.upper_bounds-self.lower_bounds)+self.lower_bounds
        for i in range(self.pop_size):
            self.population.append(Individual(params=random_parameters[i]))
    

    def avg_fitness(self):
        avg_fit = 0
        best_fit = 0
        best_individual = self.population[0]

        for i in self.population:
            avg_fit += i.fitness

                
        return avg_fit/self.pop_size
    
    
    def get_best_individuals(self, num_of_bests=1):
        bests = []
        if not(self.is_sorted):
            self.__sort()

        for i in range(num_of_bests):
            bests.append(self.population[i])
        return bests


    def calculate_fitness(self):
        for ind in self.population:
            ind.fitness = self.fitness_function(ind.parameters)


    def crossover(self, parent_1: Individual, parent_2: Individual):
        

    def __sort(self):

        check_is_sorted = 0
        self.is_sorted = False

        while check_is_sorted < len(self.population)-1:
            check_is_sorted = 0
            for i in range(len(self.population)-1):
                check_is_sorted += 1
                if self.population[i].fitness < self.population[i+1].fitness:
                    temp = self.population[i]
                    self.population[i] = self.population[i+1]
                    self.population[i+1] = temp
                    check_is_sorted = 0
        
        self.is_sorted = True






    
if __name__ == "__main__":

    pop = Population()
    
    pop.initialize()
    