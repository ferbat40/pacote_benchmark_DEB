import numpy as np


class benchmarks:
       
    def __init__(self,P,N,M,fo_in,fo_out,fo_out_g,DTLZ):
        self.__P=P
        self.__M=M
        self.__N=N
        self.__fo_in=fo_in
        self.__fo_out=fo_out
        self.__fo_out_g=fo_out_g
        self.__K = self.__N-self.__M+1
        self.__Nvar = self.__K+self.__M-1
        self.__Point_in_G = [*np.random.random((self.__P,self.__Nvar+1))]
        for i_g in self.__Point_in_G:
            i_g[self.__M:]=0.5
        self.__Point_out_G=[*np.random.random((self.__P,self.__Nvar+1))]
        self.__DTLZ=DTLZ

    def get_P (self):
        return self.__P
 
    def get_M (self):
        return self.__M
    
    def get_N (self):
        return self.__N
    
    def get_fo_in (self):
        return self.__fo_in
    
    def set_fo_in(self,fo_in):
        self.__fo_in+=fo_in
    
    def get_fo_out (self):
        return self.__fo_out
    
    def set_fo_out(self,fo_out):
        self.__fo_out+=fo_out
    
    def get_fo_out_g (self):
        return self.__fo_out_g
    
    def set_fo_out_g(self,fo_out_g):
        self.__fo_out_g+=fo_out_g
    
    def get_K (self):
        return self.__K
    
    def get_Nvar (self):
        return self.__Nvar
    
    def get_Point_in_G  (self):
        return self.__Point_in_G 
        
    def get_Point_out_G (self):
        return self.__Point_out_G
    
    def get_DTLZ(self):
        return self.__DTLZ
    
    def set_DTLZ(self,DTLZ_obj):
        self.__DTLZ=DTLZ_obj
        
        

    
        
        





