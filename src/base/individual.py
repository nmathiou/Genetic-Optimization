






class Individual:
    
    def __init__(self, params):
        self.parameters = params
        self.fitness = self.calculate_fitness()
    
    def mutate(self):
        pass

    
    def calculate_fitness(self):
        return 0
    
    
    
    
    
    
if __name__ == "__main__":
    
    ind = Individual()