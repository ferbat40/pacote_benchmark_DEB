from create_benchmark import CreateBenchmark
from NSGA_pymoo import NSGAPymoo
from metrics import Metrics
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo



bk = CreateBenchmark(8,1500,10,3)



bk.call_benchmark()
#print(bk.get_Nvar(), bk.get_M(), bk.get_K())
points_in=bk.get_DTLZ().minimize_DTLZ()
#points_out=bk.get_DTLZ().maximize_DTLZ()
bk.show_points(points_in)
#bk.show_points(points_out)
#NSGA = NSGAPymoo(bk,40,500)
#pt_NSGA =NSGA.exec()
#bk.show_points(pt_NSGA )


#SPEA_2 = SPEAPymoo(bk,30,500)
#pt_SPEA_2=SPEA_2.exec()
#bk.show_points(pt_SPEA_2)


#RVEA = RVEAymoo(bk,20)
#pt_RVEA=RVEA.exec()
#bk.show_points(pt_RVEA)


#MOEDA = MOEADpymoo(bk,20)
#pt_MOEDA=MOEDA.exec()
#bk.show_points(pt_MOEDA)








