from DTLZ1 import DTLZ1
from benchmarks import benchmarks

class engine:
    def __init__(self,benchmark,P,N,M):
        self.benchmark=benchmark
        self.P=P
        self.N=N
        self.M=M
        self.PARAM = {
                1:  self.call_DTLZ1,
                2:  self.call_DTLZ2,
                }
    
    
    def call_DTLZ1(self):
        benchmarks(self.P,self.N,self.M)
        DTLZ1_ = DTLZ1(self.P,self.N,self.M)
        DTLZ1_.build_objective_space()
        #print(self.G,"objeto dtlz1")
                
    
    def call_DTLZ2(self):
        print("em construção")
        

    def call_benchmark(self):
        if self.benchmark in self.PARAM:
            DTLZ=self.PARAM[self.benchmark]()

    


engine =  engine(1,1500,4,3)
engine.call_benchmark()




