import numpy as np

class DTLZ7:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_h(self,x,f,g):
        gaux = np.tile(g, (1, self.new_benchmark_obj.get_M()-1))
        #print("gaux",gaux)
        #print("g",g)
        #print("f",f)
        h=np.hstack([f[:,col:col+1]/(1+gaux)*(1+np.sin(3*np.pi*f[:,col:col+1])) for col in range(0,f.shape[1])])
        #h=np.hstack([f[:,col:col+1]/(1+g)*(1+np.sin(3*np.pi*f[:,col:col+1])) for col in range(0,f.shape[1])])
        #print("h normal",h)
        #print("h_aux",h_aux)
        h_sum= np.array(np.sum(h,axis=1)).reshape(h.shape[0],1)
        h_m=self.new_benchmark_obj.get_M()-h_sum
        return h_m



    def calc_Fm(self,f,x,Gxm):
        h=self.calc_h(x,f,Gxm)
        Fm=(1+Gxm)*h  
        return Fm


    def calc_f(self,x,Gxm):
        fx=[np.array(x[:,i]).reshape(x.shape[0],1)  for index,i in enumerate(range(0,self.new_benchmark_obj.get_M()-1),start=1)]
        f=np.array(np.hstack(fx))
        Fm=self.calc_Fm(f,x,Gxm)
        Fxi=np.concatenate((f,Fm),axis=1)
        return Fxi



    def calc_g(self,x=[],G=[]):
        Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
        g_sum = np.array([ (np.sum(Gxm[row, :]))  for row in range(Gxm.shape[0])]).reshape(Gxm.shape[0],1)
        g=1+9/self.new_benchmark_obj.get_K()*g_sum
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
       
         