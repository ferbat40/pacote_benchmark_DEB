import numpy as np
import pandas as pd
from algorithms import NSGA_benchmark
from DTLZ1 import DTLZ1
from init_benchmark import InitBenchmark
from plot_FP_M import PlotFP_M


class CreateBenchmark(InitBenchmark):
    
    def __init__(self,benchmark,P,N,M,DTLZ=None):
        super().__init__(P,N,M,DTLZ)
        self.N=N
        self.M=M
        self.benchmark=benchmark
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
          
    def K_validade(self):
        assert self.N-self.M+1 > 0, "this value of 'k' is not valid, it must be greater than 0" 
        return True
    
    def M_validade(self):
        assert self.M >= 3, "this value of 'M' is not valid, it must be greater or equal than 3" 
        return True
        
    def call_DTLZ1(self):
        if self.K_validade() == True and self.M_validade() == True:
            self.set_DTLZ(DTLZ1(self))

    
    def call_DTLZ2(self):
        print("em construção")


    def call_benchmark(self):
        if self.benchmark in self.PARAM:
           self.PARAM[self.benchmark]()

    def const_in_g(self,vet_out_connstrain):
        assert isinstance(vet_out_connstrain,tuple) and len(vet_out_connstrain)>0, "It is only allowed to vectors with two dimension"
        return vet_out_connstrain[0]

    def const_close_g(self,vet_out_connstrain):
        assert isinstance(vet_out_connstrain,tuple) and len(vet_out_connstrain)>0, "It is only allowed to vectors with two dimension"
        return vet_out_connstrain[1]
    
    def const_out_g(self,vet_out_connstrain):
        assert not isinstance(vet_out_connstrain,tuple) and len(vet_out_connstrain)>0, "It is only allowed to vectors with one dimension"
        return vet_out_connstrain
    
    
           

    def plot_FP(self,vet_0=[],vet_1=[],vet_3=[]):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_0])
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in vet_1])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in vet_3])
        if (len(ff) >0):
            ax.scatter(ff[:,0],ff[:,1],ff[:,2],color='red')
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='gray')
        if (len(cp) >0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2])
        ax.view_init(elev=360, azim=25)
        plt.show()


   

    def transformer_data(self,vet,index):
        self.vet=np.array(vet)
        if len(self.vet)>0:
         data = {
            f'Objetivo_{index+1}':[i for i in self.vet[:,index]],
           
         }
         return data
        
    def choice_dataframe(self,FO_points):
        vet_pandas=[]
        for i in range(0,self.get_M()):
            FO_pandas=pd.DataFrame(self.transformer_data(FO_points,i))
            vet_pandas.append(FO_pandas)
        return vet_pandas

        
    def create_dataframe(self,const_in_g=[],const_close_g=[],const_out_g=[]):
        vet_const=[const_in_g,const_close_g,const_out_g]
        all_data=[]
        for index,value in enumerate(vet_const):
             if len(value)>0:
                 vet_pandas=self.choice_dataframe(value)
                 data_pandas = vet_pandas[0]
                 for i in vet_pandas[1:]:
                     data_pandas=pd.concat([data_pandas,i] , axis = 1)
                 all_data.append(data_pandas)    
        all_data_pandas=all_data[0]
        for n in all_data[1:]:
            all_data_pandas=pd.concat([all_data_pandas,n] , axis = 0)
        return all_data_pandas
    
      

  

#bk = CreateBenchmark(1,10,7,5)
#bk.call_benchmark()
#var1=bk.get_DTLZ().build_in_G()
#var2=bk.get_DTLZ().build_out_G()


#pt1=bk.const_in_g(var1)



#pt2=bk.const_close_g(var1)



#pt3=bk.const_out_g(var2)

#pd_fo=bk.create_dataframe(pt1,pt2,pt3)
#plot = PlotFP_M(pd_fo)
#plot.plot_FP_M("Objetivo_1","Objetivo_2","Objetivo_3")





