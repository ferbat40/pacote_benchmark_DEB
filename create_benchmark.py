from DTLZ1 import DTLZ1
from init_benchmark import InitBenchmark
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from algorithms import NSGA_benchmark




class CreateBenchmark(InitBenchmark):
    
    def __init__(self,benchmark,P,N,M,DTLZ=None):
        super().__init__(P,N,M,DTLZ)
        self.benchmark=benchmark
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
          
            
        
    def call_DTLZ1(self):
        self.set_DTLZ(DTLZ1(self))

    
    def call_DTLZ2(self):
        print("em construção")


    def call_benchmark(self):
        if self.benchmark in self.PARAM:
           self.PARAM[self.benchmark]()

    def const_in_g(self,vet_out_connstrain):
        return vet_out_connstrain[0]

    def const_close_g(self,vet_out_connstrain):
        return vet_out_connstrain[1]
    
    def const_out_g(self,vet_out_connstrain):
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

        
  

#bk = CreateBenchmark(1,1500,7,3)
#bk.call_benchmark()
#var1=bk.get_DTLZ().build_in_G()
#var2=bk.get_DTLZ().build_out_G()
#pt1=bk.const_in_g(var1)
#print(len(pt1))
#pt2=bk.const_close_g(var1)
#print(len(pt2))
#pt3=bk.const_out_g(var2)
#print(len(pt3))
#bk.plot_FP(pt1,pt3)


