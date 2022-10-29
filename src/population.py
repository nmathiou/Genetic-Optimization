from src.base.individual import Individual
import numpy as np





class Population:
    
    def __init__(self, pop_size = 100, mutation_rate=0.01, parameters_bounds=[[-1, 1], [1, 2], [3, 12], [-3, -1]], fitness_function = None):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
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
        arr = np.arange(self.parameters_size)
        # np.random.shuffle(arr)
        num = np.random.randint(int(0.2*self.parameters_size), int(0.8*self.parameters_size))
        genes_parent_1_1 = parent_1.parameters[arr[0:num]]
        genes_parent_1_2 = parent_2.parameters[arr[0:num]]
        genes_parent_2_1 = parent_2.parameters[arr[num:]]
        genes_parent_2_2 = parent_1.parameters[arr[num:]]
        child_1 = Individual(np.append(genes_parent_1_1, genes_parent_2_1))
        child_2 = Individual(np.append(genes_parent_1_2,genes_parent_2_2))
        return child_1, child_2

    def mutate(self):
        for ind in self.population:
            ind.mutate(self.mutation_rate, self.upper_bounds, self.lower_bounds)


    def sellection(self):

        self.__sort()
        self.parents = self.population[0:int(len(self.population)/2)+1]
        return self.parents

    def advance_generation(self):
        next_gen = []
        self.calculate_fitness()
        parents = self.sellection()
        # np.random.shuffle(np.array(parents))
        for p in range(0, len(parents)-1):
            child_1, child_2 = self.crossover(parents[p], parents[p+1])
            child_1.mutate(self.mutation_rate, self.upper_bounds, self.lower_bounds)
            child_2.mutate(self.mutation_rate, self.upper_bounds, self.lower_bounds)

            next_gen.append(child_1)
            next_gen.append(child_2)

        self.population = next_gen
        print(len(self.population))
        self.calculate_fitness()


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
    