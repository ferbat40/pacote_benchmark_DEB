import numpy as np

class DTLZ2:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj


    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)   
        xm2_p=np.array(x[:,:self.new_benchmark_obj.get_M()-2])
        prod_xm2=np.array([np.prod(np.cos(xm2_p[linha,0:xm2_p.shape[1]])*np.pi/2)  for index,linha in enumerate(range(xm2_p.shape[0]))])
        
        print("x",x)
        print("xm2_p",xm2_p)
        print("prod_xm2",prod_xm2)


    def calc_g(self,x=[],G=[]):
         Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
         G = np.array([np.sum((XeXm-0.5)**2 for XeXm in Gxm[row,0:Gxm.shape[1]]) for index, row in enumerate(range(Gxm.shape[0]))])
         return G.reshape((Gxm.shape[0],1))

              
         


    def minimize_DTLZ(self):
         x=np.array(self.new_benchmark_obj.get_Point_in_G())
         g=self.calc_g(x)
         f=self.calc_f(x,g)
         
         