from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.rvea import RVEA


class RVEAymoo(Problem):
    def __init__(self,benchmark,partitions=12, generations=300,seed=15,pop_size=100):
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
        f_c=self.DTLZ.constraits(F,self.benchmark.get_constraits_NSGA_3())
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.benchmark.get_M(), n_partitions=self.partitions)
        popsize = (ref_dirs.shape[0] // 4 )*4 #+ ref_dirs.shape[0] % 4
        muttation_prob = 1/self.benchmark.get_Nvar()
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        algorithm_RVEA = RVEA(ref_dirs, pop_size=popsize, crossover=crossover,mutation=muttation)    
         
          

        res_RVEA = minimize(
            RVEAymoo(self.benchmark),
            algorithm_RVEA,
            ('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )  

        RVEA_algorithm={
            "RVEA" :np.column_stack([res_RVEA.F])
        }    
        
        return RVEA_algorithm