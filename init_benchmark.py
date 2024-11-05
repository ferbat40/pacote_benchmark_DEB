import numpy as np


class InitBenchmark:
       
    def __init__(self,P,N,M,DTLZ):
        self.__P=0
        self.__M=0
        self.__N=0
        self.__K=0
        self.__Nvar=0
        self.__Point_in_G=[]
        self.__Point_out_G=[]
        self.__DTLZ=None
        self.__P=P
        self.__M=M
        self.__N=N
        self.__K = self.__N-self.__M+1
        self.__Nvar = self.__K+self.__M-1
        self.__Point_in_G=np.array([*np.random.random((self.__P,self.__Nvar))])
        self.__Point_in_G[:,self.__M-1:self.__N]=0.5
        self.__Point_out_G=np.array([*np.random.random((self.__P,self.__Nvar+1))])
        self.__DTLZ=DTLZ
          

    def get_P (self):
        return self.__P
 
    def get_M (self):
        return self.__M
    
    def get_N (self):
        return self.__N
    
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
  
    def get_Nvar(self):
        return self.__Nvar
    
   
 




    
    
    
        
        

    
        
        





