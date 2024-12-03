import numpy as np

class DTLZ9:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj
 

    
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
         print(fjx)
      



