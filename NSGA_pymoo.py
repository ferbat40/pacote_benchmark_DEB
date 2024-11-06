from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions

                           

class NSGAPymoo(Problem):
    def __init__(self,init_benchmark,population=100, generations=300):
        
        self.init_benchmark=init_benchmark
        xl = np.full(self.init_benchmark.get_Nvar(),0)
        xu = np.full(self.init_benchmark.get_Nvar(),1)
        self.DTLZ1=DTLZ1(self.init_benchmark)    
        self.generations=generations
        super(). __init__(n_var=self.init_benchmark.get_Nvar(), n_obj=self.init_benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)

   
    def constraits(self,f,f_c=[]):
        f_constraits=np.array(f)
        f_c = np.array([np.sum([ f_c  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-0.6 for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c.reshape(f_constraits.shape[0],1)
    
    
    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.DTLZ1.calc_g(x)
        F=self.DTLZ1.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.constraits(F)
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.init_benchmark.get_M(), n_partitions=15)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        nsga3 = NSGA3(ref_dirs, pop_size=popsize)
            
        SEED=15
            
        res_NSGA = minimize(
            NSGAPymoo(self.init_benchmark),
            nsga3,
            ('n_gen', self.generations),
            seed=SEED,
            save_history=True,
            verbose=False
            )      
        
        return np.column_stack([res_NSGA.F])


        
        



    





        

