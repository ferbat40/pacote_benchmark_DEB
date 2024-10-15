from DTLZ1 import DTLZ1
from benchmarks import benchmarks
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class engine:
    def __init__(self,benchmark,P,N,M):
        self.benchmark=benchmark
        self.P=P
        self.N=N
        self.M=M
        self.fo_in=[]
        self.fo_out=[]
        self.fo_out_g=[]
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
        benchmarks(self.P,self.N,self.M,self.fo_in,self.fo_out,self.fo_out_g)
    
    
    def call_DTLZ1(self):
        DTLZ1_ = DTLZ1(self.P,self.N,self.M,self.fo_in,self.fo_out,self.fo_out_g)
        return DTLZ1_
                
    
    def call_DTLZ2(self):
        print("em construção")
        

    def call_benchmark(self):
        DTLZ=None
        if self.benchmark in self.PARAM:
            DTLZ=self.PARAM[self.benchmark]()
        return DTLZ
    

        
        
    def plot_graphic_in_G(self,fo_in,fo_out):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in fo_in ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in fo_out  ])
        print(pp.shape,cp.shape)
        if (len(cp)>0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        if (len(pp)>0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        ax.view_init(elev=360, azim=25)
        plt.show()


    def plot_graphic_out_G(self,fo_in,fo_out,fo_out_g):
        fig = plt.figure()
        fig = plt.figure(figsize=(10, 15))
        ax = fig.add_subplot(111, projection='3d')
        ff = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in fo_out_g])
        pp = np.array([fp[0:] if len(fp) > 0 else [0,0,0] for fp in fo_in ])
        cp = np.array([cv[0:] if len(cv) > 0 else [0,0,0] for cv in fo_out  ])
        print(pp.shape,cp.shape,ff.shape)
        if (len(pp) >0):
            ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')
        if (len(cp) >0):
            ax.scatter(cp[:,0],cp[:,1],cp[:,2],color='gray')
        ax.scatter(ff[:,0],ff[:,1],ff[:,2])
        ax.view_init(elev=360, azim=25)
        plt.show()

    


engine =  engine(1,1500,4,3)
DTLZ=engine.call_benchmark()
DTLZ.build_objective_space_in_G()
engine.plot_graphic_in_G(DTLZ.fo_in,DTLZ.fo_out)


DTLZ.build_objective_space_out_G()
engine.plot_graphic_out_G(DTLZ.fo_in,DTLZ.fo_out,DTLZ.fo_out_g)









