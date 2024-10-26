from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.termination.default import DefaultSingleObjectiveTermination, DefaultMultiObjectiveTermination
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions


                           

class NSGAPymoo(Problem):
    def __init__(self,init_benchmark,population=300, generations=100):
        
        self.init_benchmark=init_benchmark
        xl = np.full(2,-5)
        xu = np.full(2,5)
        self.DTLZ1=DTLZ1(self.init_benchmark)
        
       
        
        super(). __init__(n_var=2, n_obj=4, n_ieq_constr=2, xl=xl, xu=xu)



    def build_NSGA2_G(self,generations):
        fo_out_g=[]
        for i,indice in enumerate(generations):
            G = self.DTLZ1.F_G(indice[self.init_benchmark.get_M():])
            fo_out_g.append(G)
        return np.array(fo_out_g)


    def _evaluate(self, x, out, *args, **kwargs):
        F1 = (x[:, 0] - 0.5) ** 2 + 0.7 * x[:, 0] * \
            x[:, 1] + 1.2 * (x[:, 1] + 0.7) ** 2

        F2 = 1.1 * (x[:, 0] + 1.5) ** 2 + 0.8 * x[:, 0] * \
            x[:, 1] + 1.3 * (x[:, 1] - 1.7) ** 2
        
        F3 = 1.1 * (x[:, 0] + 1.5) ** 2 + 0.8 * x[:, 0] * \
            x[:, 1] + 1.3 * (x[:, 1] - 1.7) ** 2
        
        F4 = 1.1 * (x[:, 0] + 1.5) ** 2 + 0.8 * x[:, 0] * \
            x[:, 1] + 1.3 * (x[:, 1] - 1.7) ** 2

        out["F"] = np.column_stack([F1, F2, F3, F4])

        G1 = x[:, 0] ** 2 + (x[:, 1] - 1) ** 2 - 9
        G2 = - (x[:, 0] + 0.5) ** 2 - (x[:, 1] - 1) ** 2 + 2

        out["G"] = np.column_stack([G1, G2])

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", 4, n_partitions=15)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        nsga3 = NSGA3(ref_dirs, pop_size=popsize)
        
        

        NGEN=300
        SEED=12
        
        
        res_NSGA = minimize(
            NSGAPymoo(self.init_benchmark),
            nsga3,
            ('n_gen', 150),
            seed=SEED,
            save_history=True,
            verbose=False
            )
        
        
        print("Objetivos:", res_NSGA.F)
       
        
        
        return res_NSGA


        
        



    





        

