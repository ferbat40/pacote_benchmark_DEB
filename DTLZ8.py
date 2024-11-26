import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj


    def calc_gmx(self,fjx,fix,M):
        fjx_cp=np.copy(fjx)
        fmx=np.array(fjx_cp[:,M-1]).reshape(fjx_cp.shape[0],1)
        fj=np.array(fjx_cp[:,:M-1])
        fix_cp=np.copy(fix)
        fi=np.array(fix_cp[:,:M-1])
        gmx_min=[]

       

        for index,(index_fj,index_fmx) in enumerate(zip (fj,fi)):
            #print("index_f",index_fj)
            for index_aux,i in enumerate(index_fmx,start=1):
                #print("index_fmx",i,index,index_aux,len(index_fj))
                if index_aux==len(index_fj):
                    #print(np.min(index_fj),np.min(index_fmx))
                    gmx_min.append([float(np.min(index_fj)),float(np.min(index_fmx))])
        #print(np.array(gmx_min))
        gmx=2*fmx+(gmx_min[0]+gmx_min[1])-1
        #print("gmx",gmx)
        #print("fjx",fjx_cp)
        condition=np.all(gmx >= 0, axis = 1)
        fjx_constraits=fjx_cp[condition]
        print(fjx)
        #print("fjx_constraits",fjx_constraits)
        return fjx_constraits


    def calc_gjx(self,fjx,M):
        fjx_cp=np.copy(fjx)
        fmx=np.array(fjx_cp[:,M-1]).reshape(fjx_cp.shape[0],1)
        fj=np.array(fjx_cp[:,:M-1])
        condition=np.all(fmx+4*fj-1 >= 0, axis = 1)
        gj_constraits=fjx_cp[condition]
        return gj_constraits
        


    def calc_f(self,i,N,M):
        fjx_arr=[]
        for fxi in range(0,M):
            print(i[fxi])
            fxi_v=np.array(fxi)
            sum_xi= np.array(np.sum(fxi_v, axis=1)).reshape(fxi_v.shape[1],1)
            print(sum_xi)
            #sum_xi= np.array(np.sum(fxi, axis=1)).reshape(i.shape[1],1)
            #print(sum_xi,"sum_xi")
            #fjx=(1/(N/M))*sum_xi
            #fjx_arr.append(np.hstack(fjx))
        #print("fjx_arr",fjx_arr)
        return np.array(fjx_arr)


    
    def calc_m_const(self,N,M,P):
        fj=M
        i_part=[]
        #print(P)

        for fji,j in enumerate(range(0,fj), start = 1):
            i=[P[:,NPart].reshape(P.shape[0],1) for NPart in range(int(((fji-1)*(N/M))),int(((fji)*(N/M))))]
            i_part.append(np.hstack(np.array(i)))
        #print(np.array(i_part))
        return np.array(i_part)
          
        

    def minimize_DTLZ(self):

        fix=self.calc_m_const(self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M(),self.new_benchmark_obj.get_Point_in_G ())
        fjx=self.calc_f(fix,self.new_benchmark_obj.get_Nvar(),self.new_benchmark_obj.get_M())
        #constraits_gjx=self.calc_gjx(fjx,self.new_benchmark_obj.get_M())
        #constraits_gmx=self.calc_gmx(fjx,fix,self.new_benchmark_obj.get_M())
        #print("constraits_gmx",constraits_gmx)
       
     
