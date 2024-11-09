from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from init_algorithm import InitAlgorithm
from metrics import Metrics


class NSGAPymoo(InitAlgorithm):
    def __init__(self,benchmark):
        super(). __init__(benchmark)
        
    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.DTLZ.calc_g(x)
        F=self.DTLZ.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.DTLZ.constraits(F,self.benchmark.get_constraits_NSGA_3())
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.benchmark.get_M(), n_partitions=self.partitions)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        muttation_prob = 1/self.benchmark.get_Nvar()
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        nsga3 = NSGA3(ref_dirs, pop_size=popsize, crossover=crossover,mutation=muttation)      

        res_NSGA = minimize(
            NSGAPymoo(self.benchmark),
            nsga3,
            ('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )  

        NSGA_algorithm={
            "NSGA-3" :np.column_stack([res_NSGA.F])
        }    
        
        return NSGA_algorithm
    


        
        



    





        

