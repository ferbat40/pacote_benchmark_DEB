from create_benchmark import CreateBenchmark
from NSGA_pymoo import NSGAPymoo
from metrics import Metrics
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo



bk = CreateBenchmark(7,1500,6,3)
print(bk.get_Nvar(), bk.get_M(), bk.get_K())


bk.call_benchmark()
points_in=bk.get_DTLZ().minimize_DTLZ()
points_out=bk.get_DTLZ().maximize_DTLZ()
bk.show_points(points_in)
#bk.show_points(points_out)
NSGA = NSGAPymoo(bk)
pt_n=NSGA.exec()
bk.show_points(pt_n)








