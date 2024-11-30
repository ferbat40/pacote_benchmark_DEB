import numpy as np
import pandas as pd
from NSGA_pymoo import NSGAPymoo
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo
from metrics import Metrics
from DTLZ1 import DTLZ1
from DTLZ2 import DTLZ2
from DTLZ3 import DTLZ3
from DTLZ4 import DTLZ4
from DTLZ5 import DTLZ5
from DTLZ6 import DTLZ6
from DTLZ7 import DTLZ7
from DTLZ8 import DTLZ8
from init_benchmark import InitBenchmark
from plot_FP_M import PlotFP_M
from itertools import zip_longest
from IPython.display import display,HTML



class CreateBenchmark(InitBenchmark):
    
    def __init__(self,benchmark,P,K_N,M,DTLZ=None):
        super().__init__(P,M,DTLZ)
        self.K_N=K_N
        self.M=M
        self.benchmark=benchmark
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                3:  self.call_DTLZ3,
                4:  self.call_DTLZ4,
                5:  self.call_DTLZ5,
                6:  self.call_DTLZ6,
                7:  self.call_DTLZ7,
                8:  self.call_DTLZ8
                }
        pd.set_option('display.float_format', '{:.15f}'.format)
       
          
    def K_validate(self):
        assert self.K_N > 0, "this value of 'k' is not valid, it must be greater than 0" 
        return True
    
    def M_validate(self):
        assert self.M >= 3, "this value of 'M' is not valid, it must be greater or equal than 3" 
        return True
        
    def call_DTLZ1(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_DTLZ(DTLZ1(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()
            
            

    
    def call_DTLZ2(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_DTLZ(DTLZ2(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()

    
    def call_DTLZ3(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_DTLZ(DTLZ3(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()

    
    def call_DTLZ4(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_DTLZ(DTLZ4(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()


    
    def call_DTLZ5(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_angle(10)
            self.set_DTLZ(DTLZ5(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()
            self.set_Point()
            self.set_POF(0.5)
    
    
    def call_DTLZ6(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.3)
            self.set_angle(10)
            self.set_DTLZ(DTLZ6(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()
            self.set_POF(0.0)
           

    
    def call_DTLZ7(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_n_ieq_constr(0)
            self.set_angle(10)
            self.set_DTLZ(DTLZ7(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()
            self.set_POF(0.0)
           
    

    def call_DTLZ8(self):
        if self.K_validate() == True and self.M_validate() == True:
            self.set_constraits_Default(1.0)
            self.set_constraits_NSGA_3(1.2)
            self.set_constraits_SPEA_2(1.1)
            self.set_n_ieq_constr(3)
            self.set_angle(3)
            self.set_DTLZ(DTLZ8(self))
            self.set_K(self.K_N)
            self.set_NVar()
            self.set_Point()
       
                    
         

    def call_benchmark(self):
        if self.benchmark in self.PARAM:
           self.PARAM[self.benchmark]()

   
    def build_dataframe(self,key,value):
        label=[(f'Objective {i+1}',) for i in range(value.shape[1])]
        column = pd.MultiIndex.from_tuples(label) 
        point_pandas=pd.DataFrame(value, columns=column)  
        point_pandas_valid=point_pandas.reset_index(drop=True)
        point_pandas_valid.index=pd.Index(range(1,len(point_pandas_valid)+1)) 
        display(HTML(f'<h1 style="font-size: 19px;">{key}</h1>'))
        print(key)
        print()
        display(point_pandas_valid)
          
   
    def show_points(self,pt1_dict={}):
     if self.K_validate() == True and self.M_validate() == True:
        assert isinstance(pt1_dict,dict) and len(pt1_dict)>0, "It is only allowed dictionaries"   
        pt1_dict_valid={key: values for key,values in pt1_dict.items() if len(values)>0}
        for key,values in pt1_dict_valid.items():
            self.build_dataframe(key,values) 
        
     
    def valid_points(self,pt1_dict={},pt2_dict={},pt3_dict={}):
        
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
        try:
            vet_pt.append(np.array(list(pt3_dict.values())[0]))
        except Exception:
            pass
        try:
            vet_pt.append(np.array(list(pt3_dict.values())[1]))
        except Exception:
            pass
         
        vet_pt_valid=[i for i in vet_pt if i.size>0]
        assert 0 < len(vet_pt_valid) <= 3, "The number of points allowed is only three; an amount greater than three or equal to zero was received."
        return vet_pt_valid
     


    def call_plot_PF_M(self,pt1_dict={},pt2_dict={},pt3_dict={}):  
        if self.K_validate() == True and self.M_validate() == True:    
            vet_pt_valid=self.valid_points(pt1_dict,pt2_dict,pt3_dict)  
            label_1=[]
            label_2=[]
            label_3=[]
            labels_1 =  {key for key,value in pt1_dict.items() if len(value) > 0 }
            labels_2 =  {key for key,value in pt2_dict.items() if len(value) > 0 }
            labels_3 =  {key for key,value in pt3_dict.items() if len(value) > 0 }
            for ( labels_1,labels_2,labels_3) in zip_longest (pt1_dict.items(),pt2_dict.items(),pt3_dict.items() , fillvalue=None):
                key_1 = f'{labels_1[0]} (Points {len(labels_1[1])})' if labels_1 is not None and len(labels_1[1])>0 else None
                key_2 = f'{labels_2[0]} (Points {len(labels_2[1])})' if labels_2 is not None and len(labels_2[1])>0 else None
                key_3 = f'{labels_3[0]} (Points {len(labels_3[1])})' if labels_3 is not None and len(labels_3[1])>0 else None
                label_1.append(key_1)
                label_2.append(key_2)
                label_3.append(key_3)
            label_1=[i for i in label_1 if i is not None]
            label_2=[i for i in label_2 if i is not None]
            label_3=[i for i in label_3 if i is not None]
            label_valid=label_1+label_2+label_3
            PlotFP_M(self.get_M(),label_valid,vet_pt_valid,self.get_angle())


