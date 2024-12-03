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
     


    def const_gmx(self,fjx,c_fj_fi,M):
        fj=[]
        fi=[]
        s_fj_fi=[]
        gmx_arr=[]
        
        for end,begin in enumerate(range(0,c_fj_fi.shape[1]), start=1):
            f_first=int(c_fj_fi[:,begin:end][0][0])
            f_second=int(c_fj_fi[:,begin:end][1][0])
            fj.append(fjx[:,f_first-1:f_first])
            fi.append(fjx[:,f_second-1:f_second])
            s_fj_fi.append(fjx[:,f_first-1:f_first]+fjx[:,f_second-1:f_second])
        fj=np.array(fj)
        fi=np.array(fi)
        s_fj_fi=np.array(np.hstack(s_fj_fi))
        for fjx_ind,s_fj_fi_ind in zip(fjx,s_fj_fi):
            for end, fm in enumerate(fjx_ind, start=1):
                if end == M:
                    gmx=2*fm+np.min(s_fj_fi_ind)-1
                    gmx_arr.append(gmx)             
        gmx_arr=np.array(gmx_arr).reshape(fjx.shape[0],1)
        return gmx_arr



    def combinate_fj_fi(self,M):
        combination=[]
        exists=[]
        for fj in range(1,(M+1)-1):
            for fi in range(1,(M+1)-1):
                if fj != fi:
                     combination.append([[fj],[fi]])
        combination=np.array(np.hstack(combination))
        for fj_end, fj_begin in enumerate(range(0,combination.shape[1]), start = 1):
            for f_end, f_begin in enumerate(range(0,fj_end), start = 1):
                if (combination[:,fj_begin:fj_end][0][0] == combination[:,f_begin:f_end][1][0]) and (combination[:,fj_begin:fj_end][1][0] == combination[:,f_begin:f_end][0][0]):
                    exists.append(combination[:,fj_begin:fj_end])
                    break
        exists=np.array(np.hstack(exists))
        combination_valid=np.copy(combination)
        for end,begin in enumerate(range(0,exists.shape[1]), start=1):
            res= np.where(np.all(combination_valid==exists[:,begin:end], axis=0))
            combination_valid=np.delete(combination_valid,np.array(res), axis=1)
        return combination_valid
           
           

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
        c_fj_fi=self.combinate_fj_fi(self.new_benchmark_obj.get_M())
        gmx_const=self.const_gmx(fjx,c_fj_fi,self.new_benchmark_obj.get_M())
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
       
     
