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
        xl = np.full(self.init_benchmark.get_Nvar(),-5)
        xu = np.full(self.init_benchmark.get_Nvar(),5)
        self.DTLZ1=DTLZ1(self.init_benchmark)
        
       
        
        super(). __init__(n_var=6, n_obj=3, n_ieq_constr=0, xl=xl, xu=xu)



    
    def calc_f(self,x):
        

        prod_xm1=np.prod(x[:,:self.init_benchmark.get_M()-1])

        print("até xm-1",x[:,:self.init_benchmark.get_M()-1],prod_xm1)
        print("até xm-2",x[:,:self.init_benchmark.get_M()-2])

        
    
    def calc_g(self,x):
         g_xm=100*((self.init_benchmark.get_K()*x.shape[0])+np.sum([((xi_em-0.5)**2)-(np.cos(20*np.pi*(xi_em-0.5))) for xi_em in x[:,self.init_benchmark.get_M()-1:]]))
         
         print("xm",x[:,self.init_benchmark.get_M()-1:],g_xm)

        


    


    def _evaluate(self, x, out, *args, **kwargs):

        F1 = x[:,1]
        F2 = x[:,1]
        F3 = x[:,2]
        self.calc_f(x)
        self.calc_g(x)
        #print("F1",F1,"F2",F2,"F3")
        print("x",x)
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=1)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        nsga3 = NSGA3(ref_dirs, pop_size=popsize)
        
        

        
        SEED=0
        
        
        res_NSGA = minimize(
            NSGAPymoo(self.init_benchmark),
            nsga3,
            ('n_gen', 2),
            seed=SEED,
            save_history=True,
            verbose=False
            )
        
        
        print("Objetivos:", res_NSGA.F)
       
        
        
        return res_NSGA


        
        



    





        

