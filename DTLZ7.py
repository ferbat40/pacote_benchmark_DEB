import numpy as np

class DTLZ7:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_h(self,x,f,g):
        print("x",x)
        print("f",f)
        print("g",g)
        for col in range(0,f.shape[1]-1):
           h= f[:,col]/1+g*(1+np.sin(3*np.pi*f[:,col]))
           print("h",h)
        
               

        #xi=np.array(x[0:,:self.new_benchmark_obj.get_M()-1])
        #h_c = np.hstack([x[:,col:index]/1+G*(1+np.sin(3*np.pi*x[:,col:index])) for index,col in enumerate(range(0,xi.shape[1]),start=1)])
        #print("x",x)
        #print("h",h)
        #h_sum = np.array(np.sum(h_c,axis=1))
        #h=self.new_benchmark_obj.get_M()-h_sum
        #h_sum_v = h_sum.reshape(h.shape[0],1)
        return 1



    def calc_Fm(self,f,x,Gxm):
        h=self.calc_h(x,f,Gxm)
        #Fm=(1+Gxm)*h
        return 1


    def calc_f(self,x,Gxm):
        fx=[np.array(x[:,i]).reshape(x.shape[0],1)  for index,i in enumerate(range(0,self.new_benchmark_obj.get_M()-1),start=1)]
        f=np.array(np.hstack(fx))
        #if index != self.new_benchmark_obj.get_M() else self.calc_Fm(np.array(x[:,i]).reshape(x.shape[0],1),x,Gxm)
        self.calc_Fm(f,x,Gxm)
        return 1



    def calc_g(self,x=[],G=[]):
        Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
        g_sum = np.array([ (np.sum(np.abs(Gxm[row, :])))  for row in range(Gxm.shape[0])]).reshape(Gxm.shape[0],1)
        g = 1+9/self.new_benchmark_obj.get_K()*g_sum
        print("g",g)
        #g=g+1
        #print("g",Gxm)
        #print("g_sum",g)
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
       
         