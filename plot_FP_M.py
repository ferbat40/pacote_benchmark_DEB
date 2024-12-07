import ipywidgets as widgets
from IPython.display import display,HTML
import matplotlib.pyplot as plt
import numpy as np



class PlotFP_M():
     def __init__(self,benchmark,Objectives,labels,vet_pt=[],angle_azim=None,angle_elevate=None):
         self.labels=labels
         self.angle_azim=angle_azim
         self.angle_elevate=angle_elevate 
         self.benchmark=benchmark
                     
    
         try:
             self.pt1=[np.array(vet_pt[0])]
         except Exception:
             self.pt1=[]
         
         try:
             self.pt2=[np.array(vet_pt[1])]
         except Exception:
             self.pt2=[]
         
         try:
             self.pt3=[np.array(vet_pt[2])]
         except Exception:
             self.pt3=[]
         
         
         self.list_axis=[f'Objective {i+1}' for i in range(Objectives)]

      
         self.x_axis = widgets.Dropdown(options=self.list_axis, description="Axis X")
         self.y_axis = widgets.Dropdown(options=self.list_axis, description="Axis Y")
         self.z_axis = widgets.Dropdown(options=self.list_axis, description="Axis Z")
         self.button = widgets.Button(description="PLOT")
         self.button.on_click(self.PlotPF) 
         display(self.x_axis,self.y_axis,self.z_axis,self.button)
                
                  

     def PlotPF(self,b):
         self.x_axis_index = int(self.x_axis.value.split()[-1])-1
         self.y_axis_index = int(self.y_axis.value.split()[-1])-1
         self.z_axis_index = int(self.z_axis.value.split()[-1])-1
         
         colors  = ['red','gray','blue']
         vectors = self.labels         
         fig = plt.figure(figsize=(12.5, 12.5))
         ax = fig.add_subplot(111, projection='3d')


         for (data,color,vector) in zip([self.pt1,self.pt2,self.pt3],colors,vectors):
             for point in data:
                 if len(point) > 0:
                     ax.scatter(point[:,self.x_axis_index], point[:,self.y_axis_index], point[:,self.z_axis_index], color=color, label = vector)
         ax.set_xlabel(self.x_axis.value)
         ax.set_ylabel(self.y_axis.value)
         ax.set_zlabel(self.z_axis.value)
         ax.view_init(elev=self.angle_elevate, azim=self.angle_azim)
         ax.legend()
         title=f'"""<div style="text-align: center; font-size: 16 px;">Plotting Graph<br>with ( M = {self.benchmark.get_M()}, K = {self.benchmark.get_K()}, N= {self.benchmark.get_Nvar()} )</div>"""'
         ax.set_title(display(HTML(title)))
         plt.draw()
    
              


         



