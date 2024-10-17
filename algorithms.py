from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
import numpy as np

                           

class NSGA_benchmark(ElementwiseProblem):
    def __init__(self,n_var,n_obj,n_constr,xl,xu,F):
        self.F=F
        xl = np.full(2, -5.12)
        xu = np.full(2, 5.12)
        super().__init__(n_var=n_var, n_obj=n_obj, n_ieq_constr=n_constr, xl=xl, xu=xu)
    
    def _evaluate(self, x, out, *args, **kwargs):
        out['F'] = self.F
        
        return super()._evaluate(x, out, *args, **kwargs)




