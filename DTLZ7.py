import numpy as np

class DTLZ7:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_h(self,x,Gxm):
        xi=np.array(x[0:,:self.new_benchmark_obj.get_M()-1])
        #print("x",x)
        #print("xi",xi)
        h_c = np.hstack([x[:,col:index]/1+Gxm*(1+np.sin(3*np.pi*x[:,col:index])) for index,col in enumerate(range(0,xi.shape[1]),start=1)])
        #for index,col in enumerate(range(0,xi.shape[1]),start=1):
           # h_col =x[:,col:index]
           # h=h_col/1+Gxm*(1+np.sin(3*np.pi*h_col))
            
           # print("h",h)
        
       # print("h_c",np.sum(h_c))
        h=self.new_benchmark_obj.get_M()-h_c
        h_sum = np.array(np.sum(h,axis=1))
        h_sum_v = h_sum.reshape(h.shape[0],1)
        #print("h",h)
        #print(h_sum_v)
        #for row in range(0,h.shape[1]):
            # h_c_t=np.sum(h[row,:])
            # print(h_c_t)
           #  j.append(h_c_t)
       # print("sdf",j)
        #hxa=np.hstack(j)
        #print("h",hxa)
       
        return h_sum_v 



    def calc_Fm(self,Fm,x,Gxm):
        Fm=(1+Gxm)*self.calc_h(x,Gxm)
        return Fm


    def calc_f(self,x,Gxm):
        fx=[np.array(x[:,i]).reshape(x.shape[0],1) if index != self.new_benchmark_obj.get_M() else self.calc_Fm(np.array(x[:,i]).reshape(x.shape[0],1),x,Gxm) for index,i in enumerate(range(0,self.new_benchmark_obj.get_M()),start=1)]
        #for index,i in enumerate(fx, start=1):
           # print(f'fx{index}',i)
        #fx=fx.reshape(fx.shape[1],fx.shape[0])
        fx_col=np.array(np.hstack(fx))
        #print("fx",fx_col)
        #print("x",x)
        return fx_col



    def calc_g(self,x=[],G=[]):
        Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
        return np.array([1+9/self.new_benchmark_obj.get_K()*np.sum(i for i in Gxm[row,0:Gxm.shape[1]]) for row in range(0,Gxm.shape[0])]).reshape(Gxm.shape[0],1)
       

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
       
         