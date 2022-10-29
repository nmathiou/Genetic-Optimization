
import numpy as np






class Individual:
    
    def __init__(self, params):
        self.parameters = params
        self.fitness = 0
    
    def mutate(self, mutation_rate, upper_bounds, lower_bounds):
        
        for i in range(len(self.parameters)):
            propability = np.random.rand()
            if propability < mutation_rate:
                self.parameters[i] = np.random.rand()*(upper_bounds[i]-lower_bounds[i])+lower_bounds[i]


    
    
    
    
    
    
    
if __name__ == "__main__":
    
    ind = Individual()