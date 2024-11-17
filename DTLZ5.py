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
        theta_p=np.array(np.prod(theta,axis=1)).reshape(theta.shape[0],1)
        return theta_p
    

    def find_in_matrix(self,x=[],x1=[]):
        x1_find=x1.copy()
        x1_find=x1_find.flatten()
        return np.where(np.all(x==x1_find[:,np.newaxis],axis=0))[0][0]

        

    def calc_theta_until(self,Gxm,x,x1=[],x_aux=[]):
        #print("x1",x1)
        try:
            colum_0=x1[:,0]
        except Exception:
            colum_0=x_aux

        colum_0=colum_0.reshape(Gxm.shape[0],1)
        part_1=np.array([])
      
        
        matrix_rest=x1[:,1:]
        part_2=np.array([])
        if len(colum_0)>0:
           if self.find_in_matrix(x,colum_0)==0:   
                #print("colum_0", colum_0)
                part_1=colum_0*np.pi/2
           elif self.find_in_matrix(x,colum_0)!=0:  
                #print("colum_0 pos",colum_0.shape,colum_0)
                part_2=(np.pi/(4*(1+Gxm)))*(1+2*Gxm*colum_0)
                
         
        if len(matrix_rest)>0 and len (part_2)==0:
            #print("matrix_rest",matrix_rest.shape,matrix_rest)
            part_2=(np.pi/(4*(1+Gxm)))*(1+2*Gxm*matrix_rest)
        part_1 = np.array(part_1) if len(part_1) else np.zeros_like(Gxm).reshape((Gxm.shape[0],1))
        part_2 = np.array(part_2) if len(part_2) else np.zeros_like(Gxm).reshape((Gxm.shape[0],1))
        
        

        #print("part_1",part_1)
       #print("part_2",part_2)
        join_matrix=np.concatenate((part_1,part_2), axis=1)
        clean=join_matrix[:,~np.all(join_matrix==0,axis=0)]
        #print("join_matrix",clean)
        return clean
        
       
       


    
    def param_f(self,param_1,param_2,param_3,param_4,param_5,param_6,param_7,f_index,f_size):
        
        parameter = {
            (0,0) : (1+param_1)*param_2*param_3,
            (1,1) : (1+param_1)*param_2*param_4,
            (2,f_size-2) : (1+param_1)*param_5*param_6,
            (f_size-1,f_size-1) : (1+param_1)*param_7
            }
      

        for index,value in parameter.items():  
            if index[0] <= f_index <= index[1]:
                return value
        return f_index
    
    def calc_f(self,x,Gxm,prod_xm1=[],prod_xm2=[]):
        F_index=[]
        for v in range(0,self.new_benchmark_obj.get_M()):
            F_index.append(v)  
        #print("x",x)
       
       # print("theta_x1_xm2_cos")
        theta_x1_xm2_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x,x[:,:self.new_benchmark_obj.get_M()-2])))))
        #print("theta_x1_xm2_cos",theta_x1_xm2_cos)
       
       # print("theta_xm1_cos")
        theta_xm1_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x,x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1])))))
       # print("theta_xm1_cos",theta_xm1_cos)

        #print("theta_xm1_si")
        theta_xm1_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x,x[:,self.new_benchmark_obj.get_M()-2:self.new_benchmark_obj.get_M()-1])))))
       # print("theta_xm1_si",theta_xm1_sin)
        
        #print("theta_x1_xm3_cos")
        theta_x1_xm3_cos=self.calc_prod(np.array(list(map(lambda xi: np.cos(xi), self.calc_theta_until(Gxm,x,x[:,0:self.new_benchmark_obj.get_M()-3],x[:,0])))))
        #print(theta_x1_xm3_cos)

       # print("theta_xm2_sin")
        theta_xm2_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x,x[:,self.new_benchmark_obj.get_M()-3:self.new_benchmark_obj.get_M()-2])))))
        #print(theta_xm2_sin)

        #print("theta_x1_sin")
        theta_x1_sin=self.calc_prod(np.array(list(map(lambda xi: np.sin(xi), self.calc_theta_until(Gxm,x,x[:,0:1])))))
        #print(theta_x1_sin)
       
        
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
         
       
