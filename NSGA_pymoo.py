from DTLZ1 import DTLZ1
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions


                           

class NSGAPymoo(Problem):
    def __init__(self,init_benchmark,population=300, generations=100):
        
        self.init_benchmark=init_benchmark
        xl = np.full(self.init_benchmark.get_Nvar(),0)
        xu = np.full(self.init_benchmark.get_Nvar(),1)
        self.DTLZ1=DTLZ1(self.init_benchmark)    
        super(). __init__(n_var=self.init_benchmark.get_Nvar(), n_obj=self.init_benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)



    
    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
       
        xm1_p=np.array(x[:,:self.init_benchmark.get_M()-1])
        prod_xm1 = np.array([ np.prod(xm1_p[row,0:xm1_p.shape[1]]) for index,row in enumerate(range(xm1_p.shape[0]))])
        prod_xm1=prod_xm1.reshape(xm1_p.shape[0],1)
        

        xm2_p=np.array(x[:,:self.init_benchmark.get_M()-2])
        prod_xm2=np.array([np.prod(xm2_p[linha,0:xm2_p.shape[1]])  for index,linha in enumerate(range(xm2_p.shape[0]))])
        prod_xm2=prod_xm2.reshape(xm2_p.shape[0],1)


        
        x1=np.array(x[:,0])
        x1=x1.reshape(x.shape[0],1)

        xm1=x[:,1:self.init_benchmark.get_M()-1]
        

        f1=1/2*prod_xm1*(1+Gxm)
        f2=1/2*prod_xm2*(1-xm1)*(1+Gxm)
        f3=1/2*(1-x1)*(1+Gxm)
        return f1,f2,f3
       
        
    
    def calc_g(self,x,G=[]):
         Gxm=np.array(x[:,self.init_benchmark.get_M()-1:])
         #for index,linha in enumerate(range(Gxm.shape[0])):
            # G.append(100*((self.init_benchmark.get_K())+np.sum([((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[linha,0:len(Gxm)]])))
         #G=np.array(G)  
         #G=G.reshape((Gxm.shape[0],1))
         #print("shap",Gxm.shape)


         #G = np.array(100*((self.init_benchmark.get_K())+np.sum((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[row,0:Gxm.shape[1]]) for index,row in enumerate(range(Gxm.shape[0]))))
         #G=G.reshape((Gxm.shape[0],1))
         G = np.array([ 100* ((self.init_benchmark.get_K())+np.sum(((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[row,0:Gxm.shape[1]]))  for index,row in enumerate(range(Gxm.shape[0]))  ])
         #G=G.reshape((Gxm.shape[0],1))
        


         





         return G.reshape((Gxm.shape[0],1))
    
    def constraits(self,f):
        f_constraits=np.array(f)
        f_c=[]
        for index,linha in enumerate(range(f_constraits.shape[0])):
            f_c.append(np.sum([ f_c  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-0.6)
        
        f_c=np.array(f_c)
        f_c=f_c.reshape(f_constraits.shape[0],1)
        return f_c
    


    def _evaluate(self, x, out, *args, **kwargs):

        
        Gxm=self.calc_g(x)
        F=self.calc_f(x,Gxm)
        F_join = np.column_stack([F[0],F[1],F[2]])
        out["F"]=F_join#Fg
        f_c=self.constraits(F_join)
        out["G"]=f_c
        

    def exec(self):
        ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=30)
        popsize = ref_dirs.shape[0] + ref_dirs.shape[0] % 4
        nsga3 = NSGA3(ref_dirs, pop_size=popsize)
            
        SEED=15
            
        res_NSGA = minimize(
            NSGAPymoo(self.init_benchmark),
            nsga3,
            ('n_gen', 300),
            seed=SEED,
            save_history=True,
            verbose=False
            )      
        
        fo=np.column_stack([res_NSGA.F])
        
        return fo


        
        



    





        

