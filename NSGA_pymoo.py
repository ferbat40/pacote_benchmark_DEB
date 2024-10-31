from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions


                           

class NSGAPymoo(Problem):
    def __init__(self,init_benchmark,population=100, generations=300):
        
        self.init_benchmark=init_benchmark
        xl = np.full(self.init_benchmark.get_Nvar(),0)
        xu = np.full(self.init_benchmark.get_Nvar(),1)
        self.DTLZ1=DTLZ1(self.init_benchmark)    
        self.generations=generations
        super(). __init__(n_var=self.init_benchmark.get_Nvar(), n_obj=self.init_benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)


    def param_f(self,param_1,param_2,param_3,param_4,param_5,param_6,f_index):
        parameter = {
            (0,0) : param_1*(1+param_2),
            (1,1) : param_3*(1-param_4)*(1+param_2),
            (2,2) : (1-param_5)*(1+param_2)
        }

        for index,value in parameter.items():
            if index[0] <= f_index <= index[1]:
                return 1/2*value
        return f_index
      
    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
       
        xm1_p=np.array(x[:,:self.init_benchmark.get_M()-1])
        prod_xm1 = np.array([ np.prod(xm1_p[row,0:xm1_p.shape[1]]) for index,row in enumerate(range(xm1_p.shape[0]))])
        prod_xm1=prod_xm1.reshape(xm1_p.shape[0],1)
        

        xm2_p=np.array(x[:,:self.init_benchmark.get_M()-2])
        prod_xm2=np.array([np.prod(xm2_p[linha,0:xm2_p.shape[1]])  for index,linha in enumerate(range(xm2_p.shape[0]))])
        prod_xm2=prod_xm2.reshape(xm2_p.shape[0],1)

        
        x1=np.array(x[:,0])
        x1=x1.reshape(x.shape[0],1)

        x2=np.array(x[:,1])
        x2=x2.reshape(x.shape[0],1)

        xm1=x[:,1:self.init_benchmark.get_M()-1]
        f= [self.param_f(prod_xm1,Gxm,prod_xm2,xm1,x1,x2,i) for i in range(self.init_benchmark.get_M())] 
        
        f=np.array(f)
        f=np.concatenate(f, axis = 1)
        return f
    
    def calc_g(self,x,G=[]):
         Gxm=np.array(x[:,self.init_benchmark.get_M()-1:])
         G = np.array([ 100* ((self.init_benchmark.get_K())+np.sum(((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[row,0:Gxm.shape[1]]))  for index,row in enumerate(range(Gxm.shape[0]))  ])
         return G.reshape((Gxm.shape[0],1))
    
    def constraits(self,f,f_c=[]):
        f_constraits=np.array(f)
        f_c = np.array([np.sum([ f_c  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-0.6 for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c.reshape(f_constraits.shape[0],1)
    


    def _evaluate(self, x, out, *args, **kwargs):   
        Gxm=self.calc_g(x)
        F=self.calc_f(x,Gxm)
        out["F"]=F
        f_c=self.constraits(F)
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", self.init_benchmark.get_M(), n_partitions=30)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        nsga3 = NSGA3(ref_dirs, pop_size=popsize)
            
        SEED=15
            
        res_NSGA = minimize(
            NSGAPymoo(self.init_benchmark),
            nsga3,
            ('n_gen', self.generations),
            seed=SEED,
            save_history=True,
            verbose=False
            )      
        
        return np.column_stack([res_NSGA.F])


        
        



    





        

