import numpy as np

class DTLZ5:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj


    def constraits(self,f,parameter,f_c=[]):
        f_constraits=np.array(f)
        f_c = np.array([np.sum([ f_c**2  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-parameter for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c.reshape(f_constraits.shape[0],1)
    

    def aval_constraits(self,f,f_c=[]):
        const_in=[]
        const_out=[]
        M_constraits=self.constraits(f,self.new_benchmark_obj.get_constraits_default())
        for index,(fc,fo) in zip( range(M_constraits.shape[0]) ,  zip(M_constraits,f)):
            if fc == 0.0000000000:
                const_in.append(fo)
            if fc != 0.0000000000:
                const_out.append(fo)   
        return np.array(const_in),np.array(const_out)

    def calc_prod(self,theta):
        return np.array(np.prod(theta,axis=1)).reshape(theta.shape[0],1)
        

    def calc_theta_until(self,Gxm,x1=[],x_until=[]):
        theta_until=x_until.copy()
        theta_until=(np.pi/(4*(1+Gxm)))*(1+2*Gxm*theta_until)
        theta_x1=x1.copy()
        theta_x1=theta_x1*np.pi/2
        theta=np.concatenate((theta_x1,theta_until), axis=1)
        return theta
    
    def param_f(self,param_1,param_2,param_3,param_4,param_5,param_6,param_7,f_index,f_size):
        
        parameter = {
            (0,0) : (1+param_1)*param_2*param_3,
            (1,1) : (1+param_1)*param_2*param_4,
            (2,f_size-2) : (1+param_1)*param_5*param_6,
            (f_size-1,f_size-1) : (1+param_1)*param_7
            }
#f= [self.param_f(Gxm,theta_x1_xm2_cos,theta_xm1_cos,theta_xm1_sin,theta_x1_xm3_cos,theta_xm2_sin,theta_x1_sin,i,len(F_index)) for i in F_index]
      

        for index,value in parameter.items():  
            if index[0] <= f_index <= index[1]:
                return value
        return f_index
    
    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)  
        theta_x1_xm2_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x[:,0:1],x[:,1:self.new_benchmark_obj.get_M()-2])))))
        theta_xm1_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1])))))
        theta_xm1_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1])))))
        theta_x1_xm3_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x[:,0:1],x[:,1:self.new_benchmark_obj.get_M()-3])))))
        theta_xm2_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x[:,self.new_benchmark_obj.get_M()-3:self.new_benchmark_obj.get_M()-2])))))
        theta_x1_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x[:,0:1])))))
       
        f= [self.param_f(Gxm,theta_x1_xm2_cos,theta_xm1_cos,theta_xm1_sin,theta_x1_xm3_cos,theta_xm2_sin,theta_x1_sin,i,len(F_index)) for i in F_index]
        
        f=np.array(f)
        f=np.concatenate(f, axis = 1)
        
        return f
       
       
         
       
    def calc_g(self,x=[],G=[]):
         Gxm=np.array(x[:,self.new_benchmark_obj.get_M()-1:])
         G = np.array([np.sum((XeXm-0.5)**2 for XeXm in Gxm[row,0:Gxm.shape[1]]) for index, row in enumerate(range(Gxm.shape[0]))])
         return G.reshape((Gxm.shape[0],1))



    def minimize_DTLZ(self):
         x=np.array(self.new_benchmark_obj.get_Point_in_G())
         g=self.calc_g(x)
         f=self.calc_f(x,g)
         constraits=self.aval_constraits(f)
         dc_constraits = {
            "Minimization of G (Function objectives sum same 1.0)"  : constraits[0],
            "Minimization of G (Function objectives sum close 1.0)" : constraits[1]                           
        }      
        
         return dc_constraits
         
       
