from base.individual import Individual
import numpy as np





class Population:
    
    def __init__(self, pop_size = 100, parameters_bounds=[[-1, 1], [1, 2], [3, 12], [-3, -1]]):
        self.pop_size = pop_size
        self.parameters_size = len(parameters_bounds)
        self.upper_bounds = np.array([x[1] for x in parameters_bounds])
        self.lower_bounds = np.array([x[0] for x in parameters_bounds])
        self.population = []
    
    
    
    def initialize(self):
        
        random_parameters = np.random.rand(self.pop_size, self.parameters_size)*(self.upper_bounds-self.lower_bounds)+self.lower_bounds
    
        for i in range(self.pop_size):
            self.population.append(Individual(params=random_parameters))
    

    def avg_fitness(self):
        avg_fit = 0
        best_fit = 0
        best_individual = self.population[0]

        for i in self.population:
            avg_fit += i.fitness
            if i.fitness > best_fit:
                best_fit = i.fitness
                best_individual = i
                
        return avg_fit/self.pop_size
    
    
    def get_best_individuals(self, num_of_bests):
        
    
    
    
    
    
if __name__ == "__main__":

    pop = Population()
    
    pop.initialize()
    