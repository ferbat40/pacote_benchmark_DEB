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
        xl = np.full(self.init_benchmark.get_Nvar(),0)
        xu = np.full(self.init_benchmark.get_Nvar(),1)
        self.DTLZ1=DTLZ1(self.init_benchmark)
        
       
        
        super(). __init__(n_var=self.init_benchmark.get_Nvar(), n_obj=self.init_benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)



    
    def calc_f(self,x,Gxm):
        

        prod_xm1=[]
        xm1_p=x[:,:self.init_benchmark.get_M()-1]
        xm1_p=np.array(xm1_p)


        for index,linha in enumerate(range(xm1_p.shape[0])):
             prod_xm1.append(np.prod(xm1_p[linha,0:xm1_p.shape[1]]))
        prod_xm1=np.array(prod_xm1)
        prod_xm1=prod_xm1.reshape(xm1_p.shape[0],1)
        


        prod_xm2=[]
        xm2_p=x[:,:self.init_benchmark.get_M()-2]
        xm2_p=np.array(xm2_p)



        for index,linha in enumerate(range(xm2_p.shape[0])):
             prod_xm2.append(np.prod(xm2_p[linha,0:xm2_p.shape[1]]))
        prod_xm2=np.array(prod_xm2)
        prod_xm2=prod_xm2.reshape(xm2_p.shape[0],1)


        #print("p1",prod_xm1)
        #print("1",xm1_p)


        #print("p2",prod_xm2)
        #print("2",xm2_p)
        x1=np.array(x[:,0])
        x1=x1.reshape(x.shape[0],1)

        xm1=x[:,1:self.init_benchmark.get_M()-1]



        #print(f'xm1 {xm1}')
        #print(f'prod_xm1 {prod_xm1}')
        #print(f'prod_xm2 {prod_xm2}')
        #print(f'Gxm {Gxm}')
        #print(f'X {x}')
        
        

        f1=1/2*prod_xm1*(1+Gxm)
        f2=1/2*prod_xm2*(1-xm1)*(1+Gxm)
        f3=1/2*(1-x1)*(1+Gxm)



       

        #print(f'f1 {f1}')
        #print(f'f2 {f2}')
        #print(f'f3 {f3}')
        #print(f'gmx {Gxm[0]}')
        return f1,f2,f3
       


        #ff=xm1-1

        #print("até xm-1",x[:,:self.init_benchmark.get_M()-1]+1)
        #print("até xm-1",x[:,:self.init_benchmark.get_M()-1])
        #print("G",Gxm)
        #print("xm-1",x[:,1:self.init_benchmark.get_M()-1])
        #print("até xm-2",x[:,:self.init_benchmark.get_M()-2])

        #print(f'f1 {f1} f2 {f2} f3 {f3} Gxm {Gxm} Xm-1 -1 {ff}')
        
        #print(f'Gxm {Gxm}')

        
    
    def calc_g(self,x):
         #x[:,self.init_benchmark.get_M()-1:]#=0.5
         Gxm=x[:,self.init_benchmark.get_M()-1:]
         Gxm=np.array(Gxm)
         #print("gxm",Gxm)
         
         G=[]
         for index,linha in enumerate(range(Gxm.shape[0])):
             G.append(100*((self.init_benchmark.get_K())+np.sum([((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[linha,0:len(Gxm)]])))
         G=np.array(G)  
         G=G.reshape((Gxm.shape[0],1))
         return G
    
    def constraits(self,f):
        f_constraits=np.array(f)
        f_c=[]
        for index,linha in enumerate(range(f_constraits.shape[0])):
            f_c.append(np.sum([ f_c  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-0.6)
        
        f_c=np.array(f_c)
        f_c=f_c.reshape(f_constraits.shape[0],1)
        #print(f_c)
        #print("all",f_constraits)
        return f_c

        


    


    def _evaluate(self, x, out, *args, **kwargs):

        
        Gxm=self.calc_g(x)
        F=self.calc_f(x,Gxm)
        #x[:,self.init_benchmark.get_M()-1:]=0.5

        #Fg=self.DTLZ1.build_NSGA2_FO(x)
        F_join = np.column_stack([F[0],F[1],F[2]])
        out["F"]=F_join#Fg
        f_c=self.constraits(F_join)
        
        #print("F1",F1,"F2",F2,"F3")
        #print("x",x)
        
        #print("Gxm",Gxm)
        
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


        
        



    





        

