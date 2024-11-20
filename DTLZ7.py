import numpy as np

class DTLZ7:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_h(self,x,f,g):
        #print("x",x)
        #print("f",f)
        #print("g",g)
        #print("g h",g)
        h=np.hstack([np.array(f[:,col:col+1]/1+g*(1+np.sin(3*np.pi*f[:,col:col+1]))) for col in range(0,f.shape[1])])
        h_sum= np.array(np.sum(h,axis=1)).reshape(h.shape[0],1)
        #print("h",h)
        #print("h_sum",h_sum)
        h_m=self.new_benchmark_obj.get_M()-1-h_sum
        #print("h_m",h_m)

          
        
               

        #xi=np.array(x[0:,:self.new_benchmark_obj.get_M()-1])
        #h_c = np.hstack([x[:,col:index]/1+G*(1+np.sin(3*np.pi*x[:,col:index])) for index,col in enumerate(range(0,xi.shape[1]),start=1)])
        #print("x",x)
        #print("h",h)
        #h_sum = np.array(np.sum(h_c,axis=1))
        #h=self.new_benchmark_obj.get_M()-h_sum
        #h_sum_v = h_sum.reshape(h.shape[0],1)
        return h_m



    def calc_Fm(self,f,x,Gxm):
        h=self.calc_h(x,f,Gxm)
        #print("h",h)
        #print("g",Gxm)
        Fm=(1+Gxm)*h
        #print("Fm",Fm)
        return Fm


    def calc_f(self,x,Gxm):
        fx=[np.array(x[:,i]).reshape(x.shape[0],1)  for index,i in enumerate(range(0,self.new_benchmark_obj.get_M()-1),start=1)]
        f=np.array(np.hstack(fx))
        #if index != self.new_benchmark_obj.get_M() else self.calc_Fm(np.array(x[:,i]).reshape(x.shape[0],1),x,Gxm)
        Fm=self.calc_Fm(f,x,Gxm)
        #print("f",f)
        #print("Fm",Fm)
        Fxi=np.concatenate((f,Fm),axis=1)
        #print("Fxi",Fxi)
        return Fxi



    def calc_g(self,x=[],G=[]):
        Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
        g_sum = np.array([ (np.sum(np.abs(Gxm[row, :])))  for row in range(Gxm.shape[0])]).reshape(Gxm.shape[0],1)
        g = np.where(g_sum > 0, 1+9/self.new_benchmark_obj.get_K()*g_sum , 1)
        #print("g",g)
        #g=g+1
        #print("g",Gxm)
        #print("g_sum",g)
        return g
     
    def minimize_DTLZ(self):
        x=np.array(self.new_benchmark_obj.get_Point_in_G())
        g=self.calc_g(x)
        f=self.calc_f(x,g)
        #print("f f",f)
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
       
         