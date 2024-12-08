from pymoo.indicators.gd import GD
from pymoo.indicators.gd_plus import GDPlus
from pymoo.indicators.igd import IGD
from pymoo.indicators.igd_plus import IGDPlus
from pymoo.indicators.hv import HV
import numpy as np
from init_metrics import InitMetrics
from ordered_set import OrderedSet
import pandas as pd
import inspect


class Metrics(InitMetrics):
    
    def identify_algorithm_obj(self,algorithm):
         algorithm_v = str(algorithm).split("-")[0]
         parameters=""
         try:
              for obj in self:
               algorithm_obj = str(type(obj).__name__)
               if algorithm_v in algorithm_obj:
                    param=inspect.signature(obj.__init__).parameters
                    var_const = [ i  for i in param if i != 'self']
                    val = {var: getattr(obj,var) for var in var_const}
                    for index, (key,value) in enumerate(val.items(),start =1):
                         if index == 2 or index == 3 or index == 5:
                              parameters =  parameters + f'{str(key[0:3]).upper()}={value},'
         except Exception:
               pass
         len_param=len(parameters)
         return "     "+algorithm+" ("+parameters[0:len_param-1]+")" if len_param > 0 else algorithm
              
   
        
    def identify_algorithm(self,obj,index_obj):
        for index,value in obj.items():
             if index_obj in index:
                  return value
        return []
    


    def build_metrics(self,vet_metrics,object_DTLZ):
         label=OrderedSet()
         label.add(f'{object_DTLZ}')

         metric=OrderedSet()
         
         for dict_algorithm_metrics in vet_metrics:
            for key,value in dict_algorithm_metrics.items():
                 label.add(key) 
                 value_div=str(value).replace("'","").replace("{","").replace("}","")
                 value_div=value_div.split(':')
                 metric.add(value_div[0])
         
         label_data=np.array(list(label))
         metrics=np.array(list(metric))
         
         data_metrics=pd.DataFrame(
              
              {
                   label_data[0] : metrics
              }
         )


         for index_col in range(1,len(label_data)):
              data_metrics[label_data[index_col]]=pd.NA
              
         index_aux=0
         for (label_data) in zip(vet_metrics):
              for obj in label_data:
                   value=np.array(list(obj.values()))
                   value_div=str(value).replace("'","").replace("{","").replace("}","").replace("]","")
                   value_div=value_div.split(':')   
                   key=str(np.array(list(obj.keys())))
                   key_div=key.replace("'","").replace("[","").replace("]","")
                   data_metrics.at[index_aux,key_div]=value_div[1]
                   index_aux=index_aux+1
                   if index_aux > data_metrics.shape[0]-1:
                        index_aux=0
         data_metrics_reset=data_metrics.reset_index(drop=True)
         data_metrics_reset.index= pd.Index(range(1, len(data_metrics_reset)+1))
          
         return data_metrics_reset


    def dict_algorithm(self):
            algorithm={
              "NSGA-3"   : [],
              "SPEA-2"   : [],
              "RVEA"     : [],
              "MOEAD"    : [],
              "U_NSGA-3"  : []        
              }
            return algorithm
            

    def get_metric(self):
            POF=list(self.param_point(self).values())
            assert len(POF[0]) > 0, "The matrix for POF is empty, it needs to be greater than 0"
            POF=POF[0]
            dict_algorithm=self.dict_algorithm()
            vet_metrics=[]
            object_DTLZ=""
            
            metric = [
                 self.M_GD,
                 self.M_GD_plus,
                 self.M_IGD,
                 self.M_IGD_plus,
                 self.M_hypervolume
                 ]
            
            for obj in self:
                  object_DTLZ = f'Metrics for {str(type(obj).__name__)[0:5]} (M={obj.new_benchmark_obj.get_M()},K={obj.new_benchmark_obj.get_K()},N={obj.new_benchmark_obj.get_Nvar()})' if str(type(obj).__name__)[0:4] == "DTLZ" and int(str(type(obj).__name__)[4:5]) <= 7 and len(object_DTLZ)==0 else object_DTLZ
                  object_DTLZ = f'{str(type(obj).__name__)[0:5]} with ( M = {obj.new_benchmark_obj.get_M()}, N = {obj.new_benchmark_obj.get_Nvar()} )' if str(type(obj).__name__)[0:4] == "DTLZ" and int(str(type(obj).__name__)[4:5]) > 7 and len(object_DTLZ)==0 else object_DTLZ
                  
                  if isinstance(obj,dict): 
                        same_keys = obj.keys() & dict_algorithm.keys()
                        if same_keys:
                             POF_algorithm=np.array(list(obj.values()))
                             POF_algorithm=POF_algorithm[0]
                             dict_algorithm_aux=self.dict_algorithm()      
                             for c,func in enumerate(metric):
                                  key_algorithm=(str(same_keys)).replace("'","").replace("{","").replace("}","")
                                  dict_algorithm_aux[key_algorithm]=func(POF_algorithm,POF)
                                  dict_algorithm_aux_valid={self.identify_algorithm_obj(key) : value for key,value in dict_algorithm_aux.items() if value}
                                  vet_metrics.append(dict_algorithm_aux_valid)
            assert len(np.array(vet_metrics)) > 0, "No matrix for algorithms was sent"
            return self.build_metrics(vet_metrics,object_DTLZ)


    def param_point(self,obj):
        param={
            "Minimization" : [],     
            "Maximization" : []
        }

       
        for index,value in param.items():
                 for i in obj:
                      if isinstance(i,dict): 
                        point_algorithm=[]
                        point_algorithm=self.identify_algorithm(i,index)
                        if len(point_algorithm) != 0 and len(value) == 0:
                             param[index]=np.array(point_algorithm)

        param_valid={key: value for key,value in param.items() if len(np.array(list(value)))>0}
        return param_valid
               
        

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
    

    def M_IGD(self,algorithm,POF):
        ind = IGD(POF)
        D_ind = {

           "Inverted Generational Distance (IGD)" : float(ind(algorithm))

        }
        return D_ind
    

    def M_IGD_plus(self,algorithm,POF):
        ind = IGDPlus(POF)
        D_ind = {

           "Inverted Generational Distance Plus (IGD+)" : float(ind(algorithm))

        }
        return D_ind
    
    def M_hypervolume(self,algorithm,POF):
        ref_point = [ 1.5  for i in range(POF.shape[1])]
        ind = HV(ref_point=ref_point)
        D_ind = {

           "Hypervolume" : float(ind(algorithm))

        }
        return D_ind
    







    
