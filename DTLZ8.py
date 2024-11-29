import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def const_gjx(self,fjx,m):
        gjx_const=[]
        for col_end,col_begin in enumerate(range(0,m-1), start=1):
            gjx_const.append(fjx[:,m-1:m]+4*fjx[:,col_begin:col_end]-1)
        gjx_const_valid=np.hstack(np.array(gjx_const))
        #condition=np.all(gjx_const_valid>=0, axis=1)
        #gjx_const_valid=fjx[condition]
        #print(gjx_const_valid.shape)
        return np.array(gjx_const_valid)



    def const_gmx(self,fjx,fix,m):
        gmx_const=[]
        for index, (fjx_aux,fix_aux) in enumerate(zip(fjx,fix)):
            sum_xi=[]
            for ff in fix_aux[:m-1]:
                sum_xi.append(np.sum(ff))
            gmx=2*fjx_aux[m-1:m]+(np.min(fjx_aux[:m-1])+np.min(sum_xi))-1
            #if gmx < 0:
            gmx_const.append(gmx)
        #print(gmx_const)
        gjx_const=self.const_gjx(fjx,m)    
        gmx_const_gjx_const=np.column_stack([gjx_const,gmx_const])
        #print("pingdf",gmx_const_gjx_const)

        return np.array(gmx_const_gjx_const)



    def calc_i(self,x,n,m):
        m_part=[]
        fjx=np.zeros((x.shape[0],m))
        fix=np.zeros((x.shape[0],m) , dtype=object)
        for fj,index in enumerate(range(0,m), start=1):
            m_part=x[:,int(((fj-1)*(n/m))):int((fj*(n/m)))]
            for row,index in enumerate(range(0,m_part.shape[0]) , start=1):
                fjx[row-1][fj-1]=(1/(n/m))*np.sum(x[index:row,int(((fj-1)*(n/m))):int((fj*(n/m)))])
                fix[row-1][fj-1]=np.array(x[index:row,int(((fj-1)*(n/m))):int((fj*(n/m)))])
        return fjx,fix
          
        

    def minimize_DTLZ(self):
        fjx,fix=self.calc_i(self.new_benchmark_obj.get_Point_in_G (),self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M())
        gmx_const=self.const_gmx(fjx,fix,self.new_benchmark_obj.get_M())
        try:
           fjx_valid = np.delete(fjx,gmx_const, axis = 0)
        except Exception as e:
           fjx_valid=fjx
        gjx_const=self.const_gjx(fjx_valid,self.new_benchmark_obj.get_M())

        dc_constraits = {
            "G Constraits Allowed"  : gjx_const                          
        }  
        return dc_constraits
       
     
