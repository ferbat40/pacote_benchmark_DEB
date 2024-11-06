from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation

                           

class SPEAPymoo(Problem):
    def __init__(self,benchmark,partitions=15, generations=300,seed=15,pop_size=100):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        self.pop_size=pop_size
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)

  
    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.DTLZ.calc_g(x)
        F=self.DTLZ.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.DTLZ.constraits(F,0.55)
        out["G"]=f_c
        

    def exec(self):

        mutation = PolynomialMutation(prob=0.1, eta=15)
        crossover = SBX(prob=0.9, eta=15)
        spea2 = SPEA2(pop_size=300,
            
            crossover=crossover,
            mutation=mutation
                      
                      
                      
                      )
            
        res_SPEA = minimize(
            SPEAPymoo(self.benchmark, pop_size=self.pop_size),
            spea2,
            ('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )      
        
        return np.column_stack([res_SPEA.F])
