import numpy as np

class DTLZ8:


    def __init__(self,new_benchmark_obj):
        self.new_benchmark_obj=None
        self.new_benchmark_obj=new_benchmark_obj
       



    def minimize_DTLZ(self):
        print("dtlz",self.new_benchmark_obj.get_DTLZ())
        print(self.new_benchmark_obj.get_Nvar(), "N ",self.new_benchmark_obj.get_NTimes() )
        