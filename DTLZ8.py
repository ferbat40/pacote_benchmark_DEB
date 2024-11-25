import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj
       
    
    def calc_f(self,N,M,P):
        fj=M
        print(P)
        i_part=[]

        for fji,j in enumerate(range(0,fj), start = 1):
            i=[P[:,NPart].reshape(P.shape[0],1) for NPart in range(int(((fji-1)*(N/M))),int(((fji)*(N/M))))]
            i_part.append(np.hstack(np.array(i)))
        return np.array(i_part)
        
        

    def minimize_DTLZ(self):

        i=self.calc_f(self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M(),self.new_benchmark_obj.get_Point_in_G ())
        print(i)
     
