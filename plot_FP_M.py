import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt



class PlotFP_M():
     def __init__(self,pd_fo):
         self.pd_fo=pd_fo  


         self.objectives = list(self.pd_fo.columns)
         self.y_axis_widgets = widgets.SelectMultiple(options=self.objectives, description = "MultiObjetivo")
         self.button=widgets.Button(description="Plotar")
         self.button.on_click(self.plot_FP_M)

         display(self.y_axis_widgets, self.button)
       

     def plot_FP_M(self,b):
        selected_objectives = list(self.y_axis_widgets.value)
        plt.figure(figsize=(10,6))


        for i in selected_objectives:
            plt.plot(self.pd_fo.index, self.pd_fo[i], marker='o', label =i)
        plt.title("Objetives")
        plt.xlabel("Indice")
        plt.ylabel("valor")
        plt.grid()
        plt.show()



        