from pymoo.indicators.gd import GD
from pymoo.indicators.gd_plus import GDPlus
from pymoo.indicators.hv import HV
import numpy as np
from init_metrics import InitMetrics
from ordered_set import OrderedSet
import pandas as pd

class Metrics(InitMetrics):
   
        
    def identify_algorithm(self,obj,index_obj):
        for index,value in obj.items():
             if index_obj in index:
                  return value
        return []
    
    def build_label_metrics(self,vet_metrics):
         label=OrderedSet()
         label.add("Metric")

         metric=OrderedSet()
         
         for dict_algorithm_metrics in vet_metrics:
            for key,value in dict_algorithm_metrics.items():
                 label.add(key) 
                 value_div=str(value).replace("'","").replace("{","").replace("}","")
                 value_div=value_div.split(':')
                 metric.add(value_div[0])
         

         print("label",np.array(list(label)))
         print("metrics",np.array(list(metric)))

         metric_array=np.array(list(label))

         metric_colum = metric_array.reshape(metric_array.shape[1],1)

         data_metrics=pd.DataFrame(metric_colum,columns=np.array(list(metric)))

         print("data",data_metrics)
              
              

                   
              
         
    

    def build_metrics(self,vet_metrics):
         self.build_label_metrics(vet_metrics)
         for dict_algorithm_metrics in vet_metrics:
              for index,value in dict_algorithm_metrics.items():
                value_div=str(value).replace("'","").replace("{","").replace("}","")
                value_div=value_div.split(':')
                print(index,value_div[0],"div",value_div[1])
    

    def dict_algorithm(self):
            algorithm={
              "NSGA-3" : [],
              "SPEA-2" : []           
              }
            return algorithm
            

    def get_algorithm(self):
            POF=list(self.param_point(self).values())
            POF=POF[0]
            dict_algorithm=self.dict_algorithm()
            vet_metrics=[]
            
            
            metric = [
                 self.M_GD,
                 self.M_GD_plus,
                 self.M_hypervolume
                 ]
            
            for obj in self:
                  if isinstance(obj,dict): 
                        same_keys = obj.keys() & dict_algorithm.keys()
                        if same_keys:
                             POF_algorithm=np.array(list(obj.values()))
                             POF_algorithm=POF_algorithm[0]
                             dict_algorithm_aux=self.dict_algorithm()      
                             for c,func in enumerate(metric):
                                  key_algorithm=(str(same_keys)).replace("'","").replace("{","").replace("}","")
                                  dict_algorithm_aux[key_algorithm]=func(POF_algorithm,POF)
                                  dict_algorithm_aux_valid={key: value for key,value in dict_algorithm_aux.items() if value}
                                  vet_metrics.append(dict_algorithm_aux_valid)
            self.build_metrics(vet_metrics)


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
               


    

        

    def M_GD(self,algorithm,POF):
        ind = GD(POF)
        D_ind = {

           "Generational Distance (GD)" : float(ind(algorithm))

        }
        return D_ind
    
    def M_GD_plus(self,algorithm,POF):
        ind = GDPlus(POF)
        D_ind = {

           "Generational Distance PLUS (GD+)" : float(ind(algorithm))

        }
        return D_ind
    
    def M_hypervolume(self,algorithm,POF):
        ref_point = [ 1.5  for i in range(POF.shape[1])]
        ind = HV(ref_point=ref_point)
        D_ind = {

           "Hypervolume" : float(ind(algorithm))

        }
        return D_ind
    







    
