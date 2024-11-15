import numpy as np

class DTLZ5:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj


    def ret_theta(self,row,thetax,Gxm):
         for colum,xi in enumerate(thetax[0:thetax.shape[0],0:thetax.shape[1]]):
                if colum==0:
                    return float(xi*np.pi/2)
                else:
                    return float(np.pi/(4*(1+Gxm))*(1+2*Gxm*xi))
                   

    def calc_theta(self,x,Gxm):
        thetax = np.array(x[:,:self.new_benchmark_obj.get_M()-1])
        valid_theta=[float(xi*np.pi/2) if colum==0 else float(np.pi/(4*(1+Gxm))*(1+2*Gxm*xi)) for colum,xi in enumerate(thetax[0:thetax.shape[0],0:thetax.shape[1]])]
        print(valid_theta)
        #print ("theta",thetax_valid)
           

          
            
            

        
        
        #print("cuz",xm2_p)
        print("x",x)




    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)   



    def calc_g(self,x=[],G=[]):
         Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
         G = np.array([np.sum((XeXm-0.5)**2 for XeXm in Gxm[row,0:Gxm.shape[1]]) for index, row in enumerate(range(Gxm.shape[0]))])
         return G.reshape((Gxm.shape[0],1))



    def minimize_DTLZ(self):
         x=np.array(self.new_benchmark_obj.get_Point_in_G())
         g=self.calc_g(x)
         theta=self.calc_theta(x,g)
         #f=self.calc_f(x,g)
         
       
