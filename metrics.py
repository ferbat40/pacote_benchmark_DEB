from pymoo.indicators.gd import GD
from pymoo.indicators.gd_plus import GDPlus
from pymoo.indicators.hv import HV
import numpy as np

class Metrics:
    def __init__(self,POF, algorithm):
        self.POF=POF
        self.algorithm=algorithm

    def M_GD(self):
        ind = GD(self.POF)
        D_ind = {

           "Generational Distance (GD)" : ind(self.algorithm)

        }
        return D_ind
    
    def M_GD_plus(self):
        ind = GDPlus(self.POF)
        D_ind = {

           "Generational Distance PLUS (GD+)" : ind(self.algorithm)

        }
        return D_ind
    
    def M_hypervolume(self):
        ref_point = [ 1.5  for i in range(self.POF.shape[1])]
        ind = HV(ref_point=ref_point)
        D_ind = {

           "Hypervolume" : ind(self.algorithm)

        }
        return D_ind
    







    
