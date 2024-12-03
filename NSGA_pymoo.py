from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem


class NSGAPymoo(Problem):
    def __init__(self,benchmark,partitions=15, generations=300,seed=15,pop_size=100):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        self.pop_size=pop_size
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), n_ieq_constr=self.benchmark.get_n_ieq_constr(), xl=xl, xu=xu)

        
    def _evaluate(self, x, out, *args, **kwargs):   
        number_DTLZ =  int(str(type(self.benchmark.get_DTLZ()).__name__)[4:5])
        if number_DTLZ <=7:
            Gxm=self.DTLZ.calc_g(x)
            F=self.DTLZ.calc_f(x,Gxm)
            out["F"]=F
            if self.benchmark.get_n_ieq_constr()>0:
                f_c=self.DTLZ.constraits(F,self.benchmark.get_constraits_NSGA_3())
                out["G"]=f_c
  


        elif number_DTLZ==8:
            fjx,fix=self.DTLZ.calc_i(x,self.benchmark.get_Nvar(),self.benchmark.get_M())
            out["F"]=fjx
            gjx_const=self.DTLZ.const_gjx(fjx,self.benchmark.get_M())
            gmx_const=self.DTLZ.const_gmx(fjx,self.benchmark.get_c_fj_fi(),self.benchmark.get_M())
            constraits_g=np.column_stack([gjx_const,gmx_const])
            out["G"]=-constraits_g

       
    def exec(self):
        ref_dirs = get_reference_directions("uniform", self.benchmark.get_M(), n_partitions=self.partitions)
        self.pop_size = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        muttation_prob = 1/self.benchmark.get_Nvar()
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        nsga3 = NSGA3(ref_dirs=ref_dirs, pop_size=self.pop_size, crossover=crossover,mutation=muttation)      

        res_NSGA = minimize(
            NSGAPymoo(self.benchmark,self.partitions, self.generations,self.seed, self.pop_size),
            nsga3,
            termination=('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )  

        NSGA_algorithm={
            "NSGA-3" :np.column_stack([res_NSGA.F])
        }    
        
        return NSGA_algorithm