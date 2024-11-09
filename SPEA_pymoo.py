from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.optimize import minimize
import numpy as np
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from init_algorithm import InitAlgorithm


class SPEAPymoo(InitAlgorithm):
    def __init__(self,benchmark,pop_size=100):
        self.pop_size=pop_size
        super(). __init__(benchmark)
  
    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.DTLZ.calc_g(x)
        F=self.DTLZ.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.DTLZ.constraits(F,self.benchmark.get_constraits_SPEA_2())
        out["G"]=f_c
        

    def exec(self):
        mutation_prob=1/self.benchmark.get_Nvar()
        mutation = PolynomialMutation(prob=mutation_prob, eta=20)
        crossover = SBX(prob=1.0, eta=15)
        spea2 = SPEA2(pop_size=300,crossover=crossover,mutation=mutation)
            
        res_SPEA = minimize(
            SPEAPymoo(self.benchmark, pop_size=self.pop_size),
            spea2,
            ('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )      
        

        SPEA_algorithm={
            "SPEA-2" :np.column_stack([res_SPEA.F])
        }   
        
        return SPEA_algorithm
