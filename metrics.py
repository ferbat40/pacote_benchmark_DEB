from pymoo.indicators.gd import GD
from pymoo.indicators.gd_plus import GDPlus
from pymoo.indicators.hv import HV
import numpy as np
from init_metrics import InitMetrics

class Metrics(InitMetrics):
   
        
    def identify_algorithm(self,obj,index_obj):
        for index,value in obj.items():
             if index_obj in index:
                  return value
        return []
    
        
                
    def param_obj(self,obj):
        array_algo=[]
        param={
            "NSGA" : [],
            "SPEA" : []           
        }

        self.metric = [
                self.M_GD,
                self.M_GD_plus
        ]

        for c,func in enumerate(self.metric):
             print(func)
             for index,value in param.items():
                 for i in obj:
                      if isinstance(i,dict): 
                        point_algorithm=[]
                        point_algorithm=self.identify_algorithm(i,index)
                        if len(point_algorithm) != 0 and len(value) == 0:
                            #param[index]=self.M_GD(np.array(point_algorithm))
                              if callable(func):
                                  print("no if",func)
                                  param[index]=func(np.array(point_algorithm))
                              else:
                                   print(f"Erro: self.metric[{i}] não é uma função.")
             array_algo.append(param)
    
        return array_algo
    

    def param_point(self,obj):
        param={
            "Minimization" : [],      
        }

       
        for index,value in param.items():
                 for i in obj:
                      if isinstance(i,dict): 
                        point_algorithm=[]
                        point_algorithm=self.identify_algorithm(i,index)
                        if len(point_algorithm) != 0 and len(value) == 0:
                             param[index]=np.array(point_algorithm)
        return param
               


    def get_obj(self):
            POF=list(self.param_point(self).values())
            self.POF=POF[0]
            #print("point",self.POF)
            algorit=self.param_obj(self)
            
        
            
            print(algorit)

        

    def M_GD(self,algorithm):
        ind = GD(self.POF)
        D_ind = {

           "Generational Distance (GD)" : float(ind(algorithm))

        }
        return D_ind
    
    def M_GD_plus(self,algorithm):
        ind = GDPlus(self.POF)
        D_ind = {

           "Generational Distance PLUS (GD+)" : float(ind(algorithm))

        }
        return D_ind
    
    def M_hypervolume(self):
        ref_point = [ 1.5  for i in range(self.POF.shape[1])]
        ind = HV(ref_point=ref_point)
        D_ind = {

           "Hypervolume" : ind(self.algorithm)

        }
        return D_ind
    







    
