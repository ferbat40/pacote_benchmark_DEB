import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def const_gjx(self,fjx,m):
        gjx_const=[]
        for col_end,col_begin in enumerate(range(0,m-1), start=1):
            gjx=fjx[:,m-1:m]+4*fjx[:,col_begin:col_end]-1
            gjx_const.append(gjx)
        return np.hstack(np.array(gjx_const))



    def const_gmx(self,fjx,fix,m):
        gmx_const=[]
        for index, (fjx_aux,fix_aux) in enumerate(zip(fjx,fix)):
            sum_xi_M=[]
            for xi in fix_aux[:m]:
                sum_xi_M.append(np.sum(xi))
            gmx=2*fjx_aux[m-1:m]+(np.min(fjx_aux[:m-1])+np.min(sum_xi_M))-1
            gmx_const.append(gmx)
        return np.array(gmx_const)



    def calc_i(self,x,n,m):
       m_part=[]
       fjx=np.zeros((x.shape[0],m))
       fix=np.zeros((x.shape[0],m) , dtype=object)
       for fj,index in enumerate(range(0,m), start=1):
           m_part=x[:,int(((fj-1)*(n/m))):int((fj*(n/m)))]
           for row,index in enumerate(range(0,m_part.shape[0]) , start=1):
               fjx[row-1][fj-1]=(1/(n/m))*np.sum(x[index:row,int(((fj-1)*(n/m))):int((fj*(n/m)))])
               fix[row-1][fj-1]=x[index:row,int(((fj-1)*(n/m))):int((fj*(n/m)))]
       return fjx,fix
          
        

    def minimize_DTLZ(self):
        fjx,fix=self.calc_i(self.new_benchmark_obj.get_Point_in_G (),self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M())
        gmx_const=self.const_gmx(fjx,fix,self.new_benchmark_obj.get_M())
        gjx_const=self.const_gjx(fjx,self.new_benchmark_obj.get_M())
        constraits=np.column_stack([gjx_const,gmx_const])
        condition=np.all(constraits>=0, axis=1)
        constraits_valid=fjx[condition]
        dc_constraits = {
            "Minimization of G"  : constraits_valid                          
        }  
        return dc_constraits
    


    def maximize_DTLZ(self):
        fjx,fix=self.calc_i(self.new_benchmark_obj.get_Point_in_G (),self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M())
        dc_constraits = {
            "Minimization of G"  : fjx                          
        }  
        return dc_constraits
       
     
