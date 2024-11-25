import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj



    def calc_gjx(self,fjx,M):
        fjx_cp=np.copy(fjx)
        fmx=np.array(fjx_cp[:,M-1]).reshape(fjx_cp.shape[0],1)
        fj=np.array(fjx_cp[:,:M-1])
        gjx = True if np.all((fmx+4*fj-1)>=1) else False

        print("fjx",fjx)
        ff = np.array([fmx+4*fj-1])
        print(ff)
        


    def calc_f(self,i,N,M):
        fjx_arr=[]
        for fxi in i:
            sum_xi= np.array(np.sum(fxi, axis=1)).reshape(i.shape[0],1)
            fjx=(1/(N/M))*sum_xi
            fjx_arr.append(np.hstack(fjx))
        return np.array(fjx_arr)
        
    
    def calc_m_const(self,N,M,P):
        fj=M
        #print(P,"P")
        i_part=[]

        for fji,j in enumerate(range(0,fj), start = 1):
            i=[P[:,NPart].reshape(P.shape[0],1) for NPart in range(int(((fji-1)*(N/M))),int(((fji)*(N/M))))]
            i_part.append(np.hstack(np.array(i)))
        return np.array(i_part)
          
        

    def minimize_DTLZ(self):

        fix=self.calc_m_const(self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M(),self.new_benchmark_obj.get_Point_in_G ())
        fjx=self.calc_f(fix,self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M())
        constraits_gjx=self.calc_gjx(fjx,self.new_benchmark_obj.get_M())
        #print("fix",fix,"fjx",fjx)
     
