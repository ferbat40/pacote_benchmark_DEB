import numpy as np
from deap import base, creator, tools
from DTLZ1 import DTLZ1

                           

class NSGA_benchmark(DTLZ1):
    def __init__(self,init_benchmark,population=300, generations=100):
        self.init_benchmark=init_benchmark
        self.population=population
        self.generations=generations
        self.n=init_benchmark.get_Nvar()
        super(). __init__(self.init_benchmark)
       

    def creator_NSGA(self):
        creator.create("FitnessMin",base.Fitness, weights=(-0.5,)*self.init_benchmark.get_M())
        creator.create("Individual",list,fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_float", np.random.uniform, 0, 1)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_float, n=self.n)  
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate",self.build_NSGA2)
        self.toolbox.register("mate", tools.cxSimulatedBinary, eta=15)
        #self.toolbox.register("mutate", tools.mutPolynomialBounded, low=0.0, up=1.0, eta=20, indpb=1/self.n)
        self.toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=1/self.n)
        
        self.toolbox.register("select", tools.selNSGA2)


    def run_NSGA(self):
        population=self.toolbox.population(n=self.population)


        for gen in range(0,self.generations):
            fits=list(map(self.toolbox.evaluate, population))
            for fit, ind in zip(fits,population):
                ind.fitness.values=fit
                
            offspring = self.toolbox.select(population,len(population))
            offspring = list(map(self.toolbox.clone,offspring))


            for child1, child2 in zip(offspring[::2],offspring[1::2]):
                self.toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values
                
                    
            for mutant in offspring:
                if np.random.rand() < (1/self.n):
                    self.toolbox.mutate(mutant)
                    del mutant.fitness.values
                                 
                    
            fits = list(map(self.toolbox.evaluate, offspring))
            for fit, ind in zip (fits,offspring):
                ind.fitness.values=fit


            population[:]=offspring

        FOP = np.array([ind.fitness.values   for ind in population])
        return FOP
       

    


        

        
        





       
        
        




        


