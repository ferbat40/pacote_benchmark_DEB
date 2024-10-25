import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class DTLZ1:

    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj
                

    def FOP_in_g(self,F):
        sum_xm=np.sum(i  for i in F[0:len(F)] )
        sum_xm_aval = [(sum_xm) for i in range(0,1) ]
        #BETWEEN hyperplane
        bt_hyper = [0, *[ c == 0.50 for c in sum_xm_aval ]]
        return bt_hyper
    

    def FOP_out_g(self,F):
        sum_xm=np.sum(i  for i in F[0:len(F)] )
        sum_xm_aval = [(sum_xm) for i in range(0,1) ]
        #OUTSIDE the hyperplane
        out_hyper= [0, *[ c >= 0.50 for c in sum_xm_aval ]]
        return out_hyper
    


    def FO_PARM(self,index_v_f,param_1,param_2,param_3,param_4,param_5,param_6,param_7,size_f):
        PARAM = {
          (0,0) : param_1*param_3,
          (1,1) : param_2*param_4*param_3,
          (2,size_f-2) : param_7*param_5*param_3,
          (size_f-1,size_f-1) : param_6*param_3
        }
        for P_FO,V_FO in PARAM.items():
            if P_FO[0] <= index_v_f <= P_FO[1]:
                return 1/2*V_FO
        return index_v_f
    
    
    
    def FO(self,G,X):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)
        param_1 = np.prod(X[1:(self.new_benchmark_obj.get_M()-1+1)])
        param_2 = np.prod(X[1:(self.new_benchmark_obj.get_M()-1)])
        param_3 = (1+G)
        param_4 = (1-X[self.new_benchmark_obj.get_M()-1])
        param_5 = (1-X[2])
        param_6 = (1-X[1])
        param_7 = (X[1])
        F_O=[self.FO_PARM(i,param_1,param_2,param_3,param_4,param_5,param_6,param_7,len(F_index)) for i in F_index]
        return F_O
    
    def F_G(self,Xm):
        G_Xm=[self.new_benchmark_obj.get_K()+np.sum([((xi-0.5)**2)-np.cos(20*np.pi*(xi-0.5)) for xi in Xm])]
        return 100*G_Xm[0]

        
    def build_in_G(self):
        fo_in=[]
        fo_out=[]
        for i in self.new_benchmark_obj.get_Point_in_G():
            G = self.F_G(i[self.new_benchmark_obj.get_M():])
            F= self.FO(G,i)
            FOP_in_g_=self.FOP_in_g(F)
            FOP_in_g_aval=list(filter(lambda v: v == False, FOP_in_g_[1:] ))
            if len(FOP_in_g_aval) == 0:
                fo_in+=[F]
            else:
                fo_out+=[F]
        return fo_in,fo_out
       


    def build_out_G(self):
        fo_out_g=[]
        for i in self.new_benchmark_obj.get_Point_out_G():
            G = self.F_G(i[self.new_benchmark_obj.get_M():])
            F= self.FO(G,i)
            FOP_out_g_=self.FOP_out_g(F)
            FOP_out_g_aval=list(filter(lambda v: v == False, FOP_out_g_[1:] ))
            if len(FOP_out_g_aval) == 0:
                fo_out_g += [F]
        return fo_out_g 
    

    def build_NSGA2(self,generations):
        fo_NSGA2=[]
        G = self.F_G(generations[self.new_benchmark_obj.get_M():])
        F= self.FO(G,generations)
        fo_NSGA2 += [F]
        fo_NSGA2=np.array(fo_NSGA2)


        return fo_NSGA2[0]

                            

       


    



        

