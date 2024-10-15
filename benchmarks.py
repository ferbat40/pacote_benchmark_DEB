import numpy as np


class benchmarks:
       
    def __init__(self,P,N,M,fo_in,fo_out,fo_out_g):
        self.P=P
        self.M=M
        self.N=N
        self.fo_in=fo_in
        self.fo_out=fo_out
        self.fo_out_g=fo_out_g
        self.K = self.N-self.M+1
        self.Nvar = self.K+self.M-1
        self.Point_in_G = [*np.random.random((self.P,self.Nvar+1))]
        for i_g in self.Point_in_G:
            i_g[self.M:]=0.5
        self.Point_out_G=[*np.random.random((self.P,self.Nvar+1))]
        
        





