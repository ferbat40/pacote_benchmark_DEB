from DTLZ1 import DTLZ1
from init_benchmark import InitBenchmark
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class CreateBenchmark(InitBenchmark):
    
    def __init__(self,benchmark,P,N,M,fo_in=[],fo_out=[],fo_out_g=[],DTLZ=None):
        super().__init__(P,N,M,fo_in,fo_out,fo_out_g,DTLZ)
        self.benchmark=benchmark
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
            
    def show_fo_in(self):
        print(f'len = {len(self.get_fo_in())}')
        for i in self.get_fo_in():
            print(i)

    def show_fo_out(self):
        print(f'len = {len(self.get_fo_out())}')
        for i in self.get_fo_out():
            print(i)

    def show_fo_out_g(self):
        print(f'len = {len(self.get_fo_out_g())}')
        for i in self.get_fo_out_g():
            print(i)

    def show_var(self):
        print(f'Nvar = {self.get_Nvar()} , K = {self.get_K()} , M = {self.get_M()} , N = {self.get_N()}')
        
     
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
        print(pp.shape,cp.shape,self.get_M())
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
        print(pp.shape,cp.shape,ff.shape,self.get_M())
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        if (len(cp) >0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        ax.scatter(ff[:,0],ff[:,1],ff[:,2])
        ax.view_init(elev=360, azim=25)
        plt.show()
  
  

#benchmark = CreateBenchmark(1,1500,45,3)
#benchmark.call_benchmark()


#benchmark.get_DTLZ().build_objective_space_in_G()
#benchmark.plot_graphic_in_G()
#benchmark.show_fo_in()
#benchmark.show_fo_out()
#benchmark.show_fo_out_g()
#benchmark.show_var()




#benchmark.get_DTLZ().build_objective_space_out_G()
#benchmark.plot_graphic_out_G()









