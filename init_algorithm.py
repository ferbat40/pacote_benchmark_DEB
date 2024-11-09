import numpy as np
from pymoo.core.problem import Problem


class InitAlgorithm(Problem):
    def __init__(self,benchmark,partitions=15, generations=300,seed=15,pop_size=100):
        self.benchmark=benchmark
        self.partitions=partitions
        self.generations=generations
        self.seed=seed
        xl = np.full(self.benchmark.get_Nvar(),0)
        xu = np.full(self.benchmark.get_Nvar(),1)
        self.DTLZ=self.benchmark.get_DTLZ()
        super(). __init__(n_var=self.benchmark.get_Nvar(), n_obj=self.benchmark.get_M(), n_ieq_constr=1, xl=xl, xu=xu)



