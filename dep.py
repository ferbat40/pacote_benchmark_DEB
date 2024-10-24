import numpy as np
from deap import base, creator, tools

                           

class NSGA_benchmark:
    def __init__(self,objectives, FO, constraits=1.0, generations = 300 , population_size=100):
        self.FO = [np.array(i) for i in FO]
        print(self.FO)
        print("fim")
        self.objectives=objectives
        #self.evaluate()
        self.generations=generations
        var_weights = [(-constraits*2)+constraits  if constraits < 0 else constraits+ (-constraits*2)  for _ in range(self.objectives)]
   
        creator.create("FitnessMin", base.Fitness, weights=tuple(var_weights))
        creator.create("Individual", list,fitness=creator.FitnessMin)


        

        self.population = [creator.Individual(obj) for obj in self.FO]
        self.exec_NSGA()
        
   
    def evaluate_param(self,obj):
        sum=np.sum(i for i in obj)
        for b in range(0,self.objectives):
            if (sum < 0.5):
                obj[b]=obj[b]+(0.5)
            else:
                obj[b]=obj[b]+(-0.5)
        
        return obj


    def evaluate(self,individual):
        #penality = [self.evaluate_param(b)
                  #  for   b in self.FO_evaluate          
                 #  ]
        
        objetive_penalitys=individual
        total = sum(objetive_penalitys)
        penality=abs(total-0.5)
        return tuple(objective+penality for objective in objetive_penalitys)
        


        
        

        
        
    def exec_NSGA(self):
        indpb = 0.1 
        for gen in range(self.generations):
            

            for ind in self.population:
                if not ind.fitness.valid:
                    ind.fitness.values=self.evaluate(ind)

            selection = tools.selTournament(self.population, len(self.population), tournsize=3)
            
            for child1, child2 in zip (selection[::2],selection[1::2]):
                if np.random.rand() < 0.7:
                    tools.cxBlend(child1,child2, alpha=0.5)

            
            for mutant in selection:
                if np.random.rand() < 0.2:
                    tools.mutPolynomialBounded(mutant, low = 0, up = 1, eta = 20.0, indpb=indpb)
                    

            self.population[:] = selection
            fitnesses = list(map(lambda ind: ind.fitness.values, self.population))
            fitnesses=np.array(fitnesses)
            print(fitnesses)