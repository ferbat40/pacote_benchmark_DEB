import numpy as np


class InitBenchmark:
       
    def __init__(self,P,M,DTLZ,constraits_SPEA_2=1.00,constraits_default=0.5,constraits_NSGA_3=0.60,POF=0.5,angle=45,n_ieq_constr=1):
        self.__P=0
        self.__M=0
        self.__K=0
        self.__Nvar=0
        self.__Point_in_G=[]
        self.__Point_out_G=[]
        self.__DTLZ=None
        self.__P=P
        self.__M=M
        self.__POF=POF
        self.__DTLZ=DTLZ
        self.__constraits_SPEA_2=constraits_SPEA_2
        self.__constraits_NSGA_3=constraits_NSGA_3
        self.__constraits_default=constraits_default
        self.__angle=angle
        self.__n_ieq_constr=n_ieq_constr
        self.__c_fj_fi=[]
            

    def get_P (self):
        return self.__P
 
    def get_M (self):
        return self.__M
    

    def set_K (self,K):
        self.__K=K
    
    
    def get_K (self):
        return self.__K
    
    
   
    def set_NVar (self):
        number_DTLZ =  int(str(type(self.get_DTLZ()).__name__)[4:5])
        if number_DTLZ <=7:
            self.__Nvar = self.get_K()+self.get_M()-1
        elif number_DTLZ > 7:
            self.__Nvar = self.get_M()*self.get_K()
        
    
    def get_Nvar (self):
        return self.__Nvar
    
    
    def set_Point(self):
            self.__Point_in_G=np.array([*np.random.random((self.get_P(),self.get_Nvar()))*1.0])
            self.__Point_out_G=np.array([*np.random.random((self.get_P(),self.get_Nvar()))*1.0])
  
      
  
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
        number_DTLZ =  int(str(type(self.get_DTLZ()).__name__)[4:5])
        if number_DTLZ <=7:
            self.__Point_in_G[:,self.get_M()-1:self.get_Nvar()]=POF
            self.__POF=POF
    

    def get_POF(self):
        return self.__POF
    
    
    def set_angle(self,angle):
        self.__angle=angle


    def get_angle(self):
        return self.__angle
    
    
    def set_n_ieq_constr(self,n_ieq_constr):
        self.__n_ieq_constr=n_ieq_constr


    def get_n_ieq_constr(self):
        return self.__n_ieq_constr
    

    def set_c_fj_fi(self,c_fj_fi):
       self.__c_fj_fi=c_fj_fi


    def get_c_fj_fi(self):
        return self.__c_fj_fi
    
   
 




    
    
    
        
        

    
        
        





