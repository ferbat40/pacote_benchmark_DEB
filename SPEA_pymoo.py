from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions

                           

class SPEAPymoo(Problem):
    def __init__(self,benchmark,partitions=15, generations=300,seed=15):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)

  
    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.DTLZ.calc_g(x)
        F=self.DTLZ.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.DTLZ.constraits(F,0.60)
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.benchmark.get_M(), n_partitions=self.partitions)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        spea2 = SPEA2(pop_size=popsize)
            
        res_NSGA = minimize(
            SPEAPymoo(self.benchmark),
            spea2,
            ('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )      
        
        return np.column_stack([res_NSGA.F])
