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
          
    def K_validate(self):
        assert self.N-self.M+1 > 0, "this value of 'k' is not valid, it must be greater than 0" 
        return True
    
    def M_validate(self):
        assert self.M >= 3, "this value of 'M' is not valid, it must be greater or equal than 3" 
        return True
        
    def call_DTLZ1(self):
        if self.K_validate() == True and self.M_validate() == True:
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
        all_data_pandas.reset_index(drop=True, inplace=True)
        return all_data_pandas

    def call_plot_PF_M(self,pt1=[],pt2=[],pt3=[]):
        if self.K_validate() == True and self.M_validate() == True:
            plot = PlotFP_M(self.get_M(),pt1,pt2,pt3)
     

#bk = CreateBenchmark(1, 100,7,4)
#bk.call_benchmark()
#var1=bk.get_DTLZ().build_in_G()
#var2=bk.get_DTLZ().build_out_G()


#pt1=bk.const_in_g(var1)



#pt2=bk.const_close_g(var1)



#pt3=bk.const_out_g(var2)


#pd_fo=bk.create_dataframe(pt1,pt2,pt3)
#bk.call_plot_PF_M(pt1,pt2,pt3)
#plot.plot_FP_M("Objetivo_1","Objetivo_2","Objetivo_3")





