import numpy as np


class InitBenchmark:
       
    def __init__(self,P,N,M,DTLZ,constraits_SPEA_2=1.00,constraits_default=0.5,constraits_NSGA_3=0.60,POF=0.5,angle=45):
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
        self.__POF=POF
        self.__Point_in_G=np.array([*np.random.random((self.__P,self.__Nvar))])
        self.__Point_in_G[:,self.__M-1:self.__N]=self.__POF
        self.__Point_out_G=np.array([*np.random.random((self.__P,self.__Nvar))])
        self.__DTLZ=DTLZ
        self.__constraits_SPEA_2=constraits_SPEA_2
        self.__constraits_NSGA_3=constraits_NSGA_3
        self.__constraits_default=constraits_default
        self.__angle=angle
        
          

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

    def get_constraits_SPEA_2(self):
        return self.__constraits_SPEA_2
    
    def set_constraits_SPEA_2(self, constraits_SPEA_2):
         self.__constraits_SPEA_2=constraits_SPEA_2

    def get_constraits_NSGA_3(self):
        return self.__constraits_NSGA_3
    
    def set_constraits_NSGA_3(self, constraits_NSGA_3):
         self.__constraits_NSGA_3=constraits_NSGA_3
  
    def get_Nvar(self):
        return self.__Nvar
    
    def set_constraits_Default(self,constraits_default):
        self.__constraits_default=constraits_default


    def get_constraits_default(self):
        return self.__constraits_default
    

    def set_POF(self,POF):
        self.__Point_in_G[:,self.__M-1:self.__N]=POF
        self.__POF=POF
    

    def get_POF(self):
        return self.__POF
    
    def set_angle(self,angle):
        self.__angle=angle

    def get_angle(self):
        return self.__angle
    
   
 




    
    
    
        
        

    
        
        





