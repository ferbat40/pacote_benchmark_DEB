from create_benchmark import CreateBenchmark
from NSGA_pymoo import NSGAPymoo
from metrics import Metrics
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo



bk = CreateBenchmark(4, 1500,4,3)
bk.call_benchmark()

points_in=bk.get_DTLZ().minimize_DTLZ()
#points_out=bk.get_DTLZ().maximize_DTLZ()
bk.show_points(points_in)







print(bk.get_Nvar(), bk.get_M(), bk.get_K())
