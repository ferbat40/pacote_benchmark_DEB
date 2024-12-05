from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from metrics import Metrics
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.moead import MOEAD


class MOEADpymoo(Problem):
    def __init__(self,benchmark,partitions=13, generations=300,seed=15):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), xl=xl, xu=xu)

        
    def _evaluate(self, x, out, *args, **kwargs):   
        number_DTLZ =  int(str(type(self.benchmark.get_DTLZ()).__name__)[4:5])
        if number_DTLZ <=7:
            Gxm=self.DTLZ.calc_g(x)
            F=self.DTLZ.calc_f(x,Gxm)
            out["F"]=F

        
        elif number_DTLZ==8:
            fjx,fix=self.DTLZ.calc_i(x,self.benchmark.get_Nvar(),self.benchmark.get_M())
            out["F"]=fjx

        
        elif number_DTLZ==9:
            fjx,fix=self.DTLZ.calc_i(x,self.benchmark.get_Nvar(),self.benchmark.get_M())
            out["F"]=fjx
             

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.benchmark.get_M(), n_partitions=self.partitions)
        muttation_prob = 1/self.benchmark.get_Nvar()
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        algorithm_MOEAD = MOEAD(ref_dirs, crossover=crossover,mutation=muttation)      

        res_MOEAD = minimize(
            MOEADpymoo(self.benchmark),
            algorithm_MOEAD,
            termination=('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )  

        MOEAD_algorithm={
            "MOEAD" :np.column_stack([res_MOEAD.F])
        }    
        
        return MOEAD_algorithm