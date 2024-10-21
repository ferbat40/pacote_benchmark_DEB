import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt



class PlotFP_M():
     def __init__(self,Objectives,pt1=[],pt2=[],pt3=[]):
         self.pt1=pt1
         self.pt2=pt2
         self.pt3=pt3
         self.list_axis=[f'Objective {i+1}' for i in range(Objectives)]

      
         self.x_axis = widgets.Dropdown(options=self.list_axis, description="Axis X")
         self.y_axis = widgets.Dropdown(options=self.list_axis, description="Axis Y")
         self.z_axis = widgets.Dropdown(options=self.list_axis, description="Axis Z")
         self.button = widgets.Button(description="Plot")
         self.button.on_click(self.PlotPF) 
         display(self.x_axis,self.y_axis,self.z_axis,self.button)
                
                  

     def PlotPF(self,b):
         print("plotar grafico")
         self.x_axis_index = int(self.x_axis.value.split()[1])-1
         self.y_axis_index = int(self.y_axis.value.split()[1])-1
         self.z_axis_index = int(self.z_axis.value.split()[1])-1
         colors  = ['azul','verde','amarelo']
         vectors = ['vetor1','vetor2','vetor3']         
         fig = plt.figure(figsize=(10, 15))
         ax = fig.add_subplot(111, projection='3d')


         for (data,color,vector) in zip([self.pt1,self.pt2,self.pt3],colors,vectors):
             for point in data:
                 ax.scatter(point[:,self.x_axis_index], point[:,self.y_axis_index], point[:,self.z_axis_index], color=color, label = vector)
                 #print(f'data {point} colors {color} vetor {vector}')

         ax.set_xlabel(self.x_axis.value)
         ax.set_ylabel(self.y_axis.value)
         ax.set_zlabel(self.z_axis.value)
         ax.view_init(elev=360, azim=25)
         ax.legend()
         plt.show()
    
              


         



