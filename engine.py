from DTLZ1 import DTLZ1
from benchmarks import benchmarks
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class new_benchmark(benchmarks):
    
    def __init__(self,benchmark,P,N,M,fo_in=[],fo_out=[],fo_out_g=[],DTLZ=None):
        super().__init__(P,N,M,fo_in,fo_out,fo_out_g,DTLZ)
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

  
    
    def plot_graphic_in_G(self):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_in() ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in self.get_fo_out() ])
        print(pp.shape,cp.shape)
        if (len(cp)>0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        if (len(pp)>0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        ax.view_init(elev=360, azim=25)
        plt.show()


    def plot_graphic_out_G(self):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_out_g()])
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in self.get_fo_in() ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in self.get_fo_out()  ])
        print(pp.shape,cp.shape,ff.shape)
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        if (len(cp) >0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        ax.scatter(ff[:,0],ff[:,1],ff[:,2])
        ax.view_init(elev=360, azim=25)
        plt.show()
  
  

#new_benchmark_obj = new_benchmark(1,1500,18,3)
#new_benchmark_obj.call_benchmark()


#new_benchmark_obj.get_DTLZ().build_objective_space_in_G()
#new_benchmark_obj.plot_graphic_in_G()


#new_benchmark_obj.get_DTLZ().build_objective_space_out_G()
#new_benchmark_obj.plot_graphic_out_G()









