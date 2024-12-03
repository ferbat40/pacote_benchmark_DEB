from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.optimize import minimize
import numpy as np
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem
from pymoo.util.ref_dirs import get_reference_directions

class SPEAPymoo(Problem):
    def __init__(self,benchmark,partitions=13, generations=300,seed=15,pop_size=100):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        self.pop_size=pop_size
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        self.pop_size=pop_size
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), n_ieq_constr=self.benchmark.get_n_ieq_constr(), xl=xl, xu=xu)
  
    def _evaluate(self, x, out, *args, **kwargs):   
        number_DTLZ =  int(str(type(self.benchmark.get_DTLZ()).__name__)[4:5])
        if number_DTLZ <=7:
            Gxm=self.DTLZ.calc_g(x)
            F=self.DTLZ.calc_f(x,Gxm)
            out["F"]=F
            if self.benchmark.get_n_ieq_constr()>0:
                f_c=self.DTLZ.constraits(F,self.benchmark.get_constraits_SPEA_2())
                out["G"]=f_c

        elif number_DTLZ==8:
            fjx,fix=self.DTLZ.calc_i(x,self.benchmark.get_Nvar(),self.benchmark.get_M())
            out["F"]=fjx
            gjx_const=self.DTLZ.const_gjx(fjx,self.benchmark.get_M())
            c_fj_fi=self.DTLZ.combinate_fj_fi(self.benchmark.get_M())
            gmx_const=self.DTLZ.const_gmx(fjx,c_fj_fi,self.benchmark.get_M())
            constraits_g=np.column_stack([gjx_const,gmx_const])
            constraits_g_v=constraits_g-1
            out["G"]=-constraits_g_v
        

    def exec(self):
        ref_dirs = get_reference_directions("uniform", self.benchmark.get_M(), n_partitions=self.partitions)
        self.pop_size = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        mutation_prob=1/self.benchmark.get_Nvar()
        mutation = PolynomialMutation(prob=mutation_prob, eta=20)
        crossover = SBX(prob=1.0, eta=15)
        algorithm_spea = SPEA2(ref_dirs=ref_dirs,pop_size=self.pop_size,crossover=crossover,mutation=mutation)
            
        res_SPEA = minimize(
            SPEAPymoo(self.benchmark,self.partitions, self.generations,self.seed, self.pop_size),
            algorithm_spea,
            termination=('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )      
        

        SPEA_algorithm={
            "SPEA-2" :np.column_stack([res_SPEA.F])
        }   
        
        return SPEA_algorithm
