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
     


    def const_gmx(self,fjx,N,M):
        gmx_arr=[]
        for f, (fjx_ind, fix_ind) in enumerate(zip(fjx[:,:M],N[:,:M]) , start = 1):
            sum_fj_fi=[]
            for item, (fjx_item, fix_item) in enumerate(zip (fjx_ind,fix_ind), start = 1):
                if item < M:
                    sum_fj_fi.append(fjx_item+fix_item)
                if item == M:
                    gmx=2*fjx_item+np.min(sum_fj_fi)-1
                    gmx_arr.append(gmx)
        gmx_arr=np.array(gmx_arr).reshape(N.shape[0],1)
        return gmx_arr
              
          

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
        gmx_const=self.const_gmx(fjx,np.array(self.new_benchmark_obj.get_Point_in_G ()),self.new_benchmark_obj.get_M())
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
       
     
