import numpy as np

class DTLZ2:


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

    def param_f(self,param_1,param_2,param_3,param_4,param_5,param_6,param_7,f_index,f_size):
        
        parameter = {
            (0,0) : (1+param_2)*param_1*param_3,
            (1,1) : (1+param_2)*param_1*param_4,
            (2,f_size-2) : (1+param_2)*param_6*param_5,
            (f_size-1,f_size-1) : (1+param_2)*param_7
            }


        for index,value in parameter.items():  
            if index[0] <= f_index <= index[1]:
                return value
        return f_index


    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)   
        xm2_p = np.array(x[:,:self.new_benchmark_obj.get_M()-2])
        prod_xm2 = np.array([np.prod(np.cos(xm2_p[linha,0:xm2_p.shape[1]]*np.pi/2))  for index,linha in enumerate(range(xm2_p.shape[0]))])
        prod_xm2 = prod_xm2.reshape(xm2_p.shape[0],1)

        xm3_p = np.array(x[:,:self.new_benchmark_obj.get_M()-3])
        prod_xm3 = np.array([np.prod(np.cos(xm3_p[linha,0:xm3_p.shape[1]]*np.pi/2))  for index,linha in enumerate(range(xm3_p.shape[0]))])
        prod_xm3 = prod_xm3.reshape(xm3_p.shape[0],1)

        xm1_c=x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1]
        prod_xm1_c = np.array([np.prod(np.cos(xm1_c[linha,0:xm1_c.shape[1]]*np.pi/2))  for index,linha in enumerate(range(xm1_c.shape[0]))])
        prod_xm1_c = prod_xm1_c.reshape(prod_xm1_c.shape[0],1)

        prod_xm1_s = np.array([np.prod(np.sin(xm1_c[linha,0:xm1_c.shape[1]]*np.pi/2))  for index,linha in enumerate(range(xm1_c.shape[0]))])
        prod_xm1_s = prod_xm1_s.reshape(prod_xm1_s.shape[0],1)

        xm2_s=x[:,self.new_benchmark_obj.get_M()-3:self.new_benchmark_obj.get_M()-2]
        prod_xm2_s = np.array([np.prod(np.sin(xm2_s[linha,0:xm2_s.shape[1]]*np.pi/2))  for index,linha in enumerate(range(xm2_s.shape[0]))])
        prod_xm2_s = prod_xm2_s.reshape(prod_xm2_s.shape[0],1)

        x1_s=np.array(np.sin(x[:,0]*np.pi/2))
        x1_s=x1_s.reshape(x.shape[0],1)

        f= [self.param_f(prod_xm2,Gxm,prod_xm1_c,prod_xm1_s,prod_xm2_s,prod_xm3,x1_s,i,len(F_index)) for i in F_index]

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
         
         