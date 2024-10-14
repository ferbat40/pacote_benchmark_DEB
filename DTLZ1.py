import numpy as np

class DTLZ1:
        

    def exibir(self):
        K = self.N-self.M+1
        Nvar = K+self.M-1
        S = self.P=1500
        Point = [*np.random.random((S,Nvar+1))]
        print(f"valor de k = {K} , valor de Nvar = {Nvar}")
        for i_g in Point:
            i_g[self.M:]=0.5

        for i in Point:
            print(i) 
