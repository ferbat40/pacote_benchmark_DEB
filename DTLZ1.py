import numpy as np


class DTLZ1:

    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj

                
    def constraits(self,f,parameter,f_c=[]):
        f_constraits=np.array(f)
        f_c = np.array([np.sum([ f_c  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-parameter for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c.reshape(f_constraits.shape[0],1)
    
    def aval_constraits(self,f,f_c=[]):
        const_in=[]
        const_out=[]
        M_constraits=self.constraits(f,self.new_benchmark_obj.get_constraits_default())
        for index,(fc,fo) in zip( range(M_constraits.shape[0]) ,  zip(M_constraits,f)):
            if fc == 0.0:
                const_in.append(fo)
            if fc != 0.0:
                const_out.append(fo)   
        return np.array(const_in),np.array(const_out)
        
    def param_f(self,param_1,param_2,param_3,param_4,param_5,param_6,f_index,f_size):
        
         parameter = {
            (0,0) : param_1*(1+param_2),
            (1,1) : param_3*(1-param_4)*(1+param_2),
            (2,f_size-2) : param_5*(1-param_6)*(1+param_2),
            (f_size-1,f_size-1) : (1-param_5)*(1+param_2)
         }
         for index,value in parameter.items():  
            if index[0] <= f_index <= index[1]:
                return 1/2*value
         return f_index
    
    
    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)   
       
        xm1_p=np.array(x[:,:self.new_benchmark_obj.get_M()-1])
        prod_xm1 = np.array([ np.prod(xm1_p[row,0:xm1_p.shape[1]]) for index,row in enumerate(range(xm1_p.shape[0]))])
        prod_xm1=prod_xm1.reshape(xm1_p.shape[0],1)
        
        xm2_p=np.array(x[:,:self.new_benchmark_obj.get_M()-2])
        prod_xm2=np.array([np.prod(xm2_p[linha,0:xm2_p.shape[1]])  for index,linha in enumerate(range(xm2_p.shape[0]))])
        prod_xm2=prod_xm2.reshape(xm2_p.shape[0],1)
  
        x1=np.array(x[:,0])
        x1=x1.reshape(x.shape[0],1)

        x2=np.array(x[:,1])
        x2=x2.reshape(x.shape[0],1) 

        xm1=x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1]
        
        f= [self.param_f(prod_xm1,Gxm,prod_xm2,xm1,x1,x2,i,len(F_index)) for i in F_index]
       
      
        f=np.array(f)
        f=np.concatenate(f, axis = 1)
       
        return f
    

    def calc_g(self,x=[],G=[]):
         Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
         G = np.array([ 100* ((self.new_benchmark_obj.get_K())+np.sum(((XeXm-0.5)**2)-(np.cos(20*np.pi*(XeXm-0.5))) for XeXm in Gxm[row,0:Gxm.shape[1]]))  for index,row in enumerate(range(Gxm.shape[0]))  ])
         return G.reshape((Gxm.shape[0],1))
    

    def minimize_DTLZ(self):
        x=np.array(self.new_benchmark_obj.get_Point_in_G())
        g=self.calc_g(x)
        f=self.calc_f(x,g)
        constraits=self.aval_constraits(f)
        dc_constraits = {
            "Minimization of G (Function objectives sum same 0.5)"  : constraits[0],
            "Minimization of G (Function objectives sum close 0.5)" : constraits[1]                           
        }      
        return dc_constraits
    

    def maximize_DTLZ(self):
        x=np.array(self.new_benchmark_obj.get_Point_out_G())
        g=self.calc_g(x)
        f=self.calc_f(x,g)
        constraits=self.aval_constraits(f)
        dc_constraits = {
            "Minimization of G (Function objectives sum same 0.5)"       : constraits[0],
            "Maximization of G (Function objectives sum far way of 0.5)" : constraits[1]                           
        }
        return dc_constraits
    
    

    
                            

       


    



        

