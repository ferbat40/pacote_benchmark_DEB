from create_benchmark import CreateBenchmark
from NSGA_pymoo import NSGAPymoo
from metrics import Metrics
from SPEA_pymoo import SPEAPymoo
from RVEA_pymoo import RVEAymoo
from MOEAD_pymoo import MOEADpymoo


bk = CreateBenchmark(1, 200,6,3)
bk.call_benchmark()

points_in=bk.get_DTLZ().minimize_DTLZ()
points_out=bk.get_DTLZ().maximize_DTLZ()





NSGAP = NSGAPymoo(bk)
pt_nsga= NSGAP.exec()


#metric = Metrics()
#metric.add_t(NSGAP)
#metric.add_t(pt_nsga)
#metric.add_t(points_in)






SPEA = SPEAPymoo(bk)
pt_spea= SPEA.exec()
#metric.add_t(SPEA)
#metric.add_t(pt_spea)

#bk.show_points(points_in)
#bk.show_points(pt_nsga)
#bk.show_points(pt_spea)

RVEA_= RVEAymoo(bk)
pt_rvea = RVEA_.exec()
#metric.add_t(RVEA_)
#metric.add_t(pt_rvea)

MOEAD_= MOEADpymoo(bk)
pt_moead = MOEAD_.exec()
#metric.add_t(MOEAD_)
#metric.add_t(pt_moead)

#bk.call_plot_PF_M(points_in,points_in)
bk.call_plot_PF_M(pt_rvea,pt_moead,pt_nsga)




#pd_metric=metric.get_metric()
#print("pd_metric")
#print(pd_metric)


#print(bk.get_Nvar(), bk.get_M(), bk.get_K(), bk.get_constraits_default(), bk.get_constraits_NSGA_3(), bk.get_constraits_SPEA_2())
