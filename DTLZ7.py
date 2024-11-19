import numpy as np

class DTLZ7:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_h(self,x,G):
        xi=np.array(x[0:,:self.new_benchmark_obj.get_M()-1])
        h_c = np.hstack([x[:,col:index]/1+G*(1+np.sin(3*np.pi*x[:,col:index])) for index,col in enumerate(range(0,xi.shape[1]),start=1)])
        #print("x",x)
        #print("h",h)
        h_sum = np.array(np.sum(h_c,axis=1))
        h=self.new_benchmark_obj.get_M()-h_sum
        h_sum_v = h_sum.reshape(h.shape[0],1)
        return h_sum_v 



    def calc_Fm(self,Fm,x,Gxm):
        h=self.calc_h(x,Gxm)
        Fm=(1+Gxm)*h
        return Fm


    def calc_f(self,x,Gxm):
        fx=[np.array(x[:,i]).reshape(x.shape[0],1) if index != self.new_benchmark_obj.get_M() else self.calc_Fm(np.array(x[:,i]).reshape(x.shape[0],1),x,Gxm) for index,i in enumerate(range(0,self.new_benchmark_obj.get_M()),start=1)]
        fx_col=np.array(np.hstack(fx))
        return fx_col



    def calc_g(self,x=[],G=[]):
        Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
        g_sum = np.array([ (np.sum(np.abs(Gxm[row, :])))  for row in range(Gxm.shape[0])]).reshape(Gxm.shape[0],1)
        g = np.where(g_sum>0,9/self.new_benchmark_obj.get_K()*g_sum,g_sum)
        g=g+1
        #print("g",g)
        return g
     
    def minimize_DTLZ(self):
        x=np.array(self.new_benchmark_obj.get_Point_in_G())
        g=self.calc_g(x)
        f=self.calc_f(x,g)
        dc_constraits = {
             "Minimization of G"  : f                           
        }  
        return dc_constraits
    

    def maximize_DTLZ(self):
        x=np.array(self.new_benchmark_obj.get_Point_out_G())
        g=self.calc_g(x)
        f=self.calc_f(x,g)
        dc_constraits = {
             "Maximization of G"  : f                           
        }  
        return dc_constraits
       
         