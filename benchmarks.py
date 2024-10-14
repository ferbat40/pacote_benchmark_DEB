import numpy as np


class benchmarks:
    def __init__(self,P,N,M):
        self.P=P
        self.M=M
        self.N=N
        self.K = self.N-self.M+1
        self.Nvar = self.K+self.M-1
        self.Point = [*np.random.random((self.P,self.Nvar+1))]
        for i_g in self.Point:
            i_g[self.M:]=0.5



