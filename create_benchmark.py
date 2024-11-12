import numpy as np
import pandas as pd
from NSGA_pymoo import NSGAPymoo
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo
from metrics import Metrics
from DTLZ1 import DTLZ1
from DTLZ2 import DTLZ2
from init_benchmark import InitBenchmark
from plot_FP_M import PlotFP_M
from itertools import zip_longest


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
        if self.K_validate() == True and self.M_validate() == True:
            self.set_DTLZ(DTLZ2(self))
      


    def call_benchmark(self):
        if self.benchmark in self.PARAM:
           self.PARAM[self.benchmark]()

    def show_points(self,constraits):
        if self.K_validate() == True and self.M_validate() == True:
            assert isinstance(constraits,dict) and len(constraits)>0, "It is only allowed dictionaries"
            for point,value in constraits.items():
                print()
                print(point)
                print()
                print(value)
   
    def transformer_data(self,vet,index):
        self.vet=np.array(vet)
        if len(self.vet)>0:
         data = {
            f'Objective_{index+1}':[i for i in self.vet[:,index]],
           
         }
         return data
        
    def choice_dataframe(self,FO_points):
        vet_pandas=[]
        for i in range(0,self.get_M()):
            FO_pandas=pd.DataFrame(self.transformer_data(FO_points,i))
            vet_pandas.append(FO_pandas)
        return vet_pandas

        
    def create_dataframe(self,const_in_g=[],const_close_g=[],const_out_g=[]):
     if self.K_validate() == True and self.M_validate() == True:
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

    def call_plot_PF_M(self,pt1_dict={},pt2_dict={}):
        vet_pt=[]
        try:
            vet_pt.append(np.array(list(pt1_dict.values())[0]))
        except Exception:
            pass
        try:    
            vet_pt.append(np.array(list(pt1_dict.values())[1]))
        except Exception:
            pass
        try:
            vet_pt.append(np.array(list(pt2_dict.values())[0]))
        except Exception:
            pass
        try:
            vet_pt.append(np.array(list(pt2_dict.values())[1]))
        except Exception:
            pass
       
        vet_pt_valid=[i for i in vet_pt if i.size>0]
        
        assert 0 < len(vet_pt_valid) <= 3, "Number of points allowed is only three, an amount greater than three was received."
        label_1=[]
        label_2=[]
        labels_1 =  {key for key,value in pt1_dict.items() if len(value) > 0 }
        labels_2 =  {key for key,value in pt2_dict.items() if len(value) > 0 }
        for ( labels_1,labels_2) in zip_longest (pt1_dict.items(),pt2_dict.items() , fillvalue=None):
            key_1 = labels_1[0] if labels_1 is not None else None
            key_2 = labels_2[0] if labels_2 is not None else None
            label_1.append(key_1)
            label_2.append(key_2)
        label_1=[i for i in label_1 if i is not None]
        label_2=[i for i in label_2 if i is not None]
        label_valid=label_1+label_2
        
        if self.K_validate() == True and self.M_validate() == True:
         PlotFP_M(self.get_M(),label_valid,vet_pt_valid)


