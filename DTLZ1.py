import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DTLZ1:

    def __init__(self,P,N,M):
        self.P=P
        self.M=M
        self.N=N
        self.K = self.N-self.M+1
        self.Nvar = self.K+self.M-1
        self.Point = [*np.random.random((self.P,self.Nvar+1))]
        for i_g in self.Point:
            i_g[self.M:]=0.5

    def FPF_cg(self,F):
        sum_xm=np.sum(i  for i in F[0:len(F)] )
        sum_xm_aval = [(sum_xm) for i in range(0,1) ]
        #BETWEEN hyperplane
        bt_hyper = [0, *[ c == 0.50 for c in sum_xm_aval ]]
        return bt_hyper

    def PROD_xi(i,f,x):
        if i and f != 0:
            return np.product(list(map(lambda xi: xi, x[i:f])))
        else:
            return 0


    def FO_PARM(self,index_v_f,param_1,param_2,param_3,param_4,param_5,param_6,param_7,size_f):
        PARAM = {
          (0,0) : param_1*param_3,
          (1,1) : param_2*param_4*param_3,
          (2,size_f-2) : param_7*param_5*param_3,
          (size_f-1,size_f-1) : param_6*param_3
        }
        for P_FO,V_FO in PARAM.items():
            if P_FO[0] <= index_v_f <= P_FO[1]:
                return 1/2*V_FO
        return index_v_f
    
    
    def FO(self,G,X):
        F_index=[]
        for v in range(0,self.M):
            F_index.append(v)
        param_1 = np.prod(X[1:(self.M-1+1)])
        param_2 = np.prod(X[1:(self.M-1)])
        param_3 = (1+G)
        param_4 = (1-X[self.M-1])
        param_5 = (1-X[2])
        param_6 = (1-X[1])
        param_7 = (X[1])
        F_O=[self.FO_PARM(i,param_1,param_2,param_3,param_4,param_5,param_6,param_7,len(F_index)) for i in F_index]
        return F_O

        
    def build_objective_space(self):
        fo_in,fo_out=[],[]
        for i in self.Point:
            G = self.F_G(i[self.M:])
            F= self.FO(G,i)
            FPF_c_g=self.FPF_cg(F)
            FPF_c_g_aval=list(filter(lambda v: v == False, FPF_c_g[1:] ))
            ind = [0,1,2]
            F = [F[i] for i in ind]
            if len(FPF_c_g_aval) == 0:
                fo_in += [F]
            else:
                fo_out += [F]
        print(f"valor de k = {self.K} , valor de Nvar = {self.Nvar} {fo_in} {fo_out}")
        self.plot_graphic(fo_in,fo_out)
            
  
            

    def F_G(self,Xm):
        G_Xm=[self.K+np.sum([((xi-0.5)**2)-np.cos(20*np.pi*(xi-0.5)) for xi in Xm])]
        return 100*G_Xm[0]
    
    def plot_graphic(self,fo_in,fo_out):
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

    
            



        

