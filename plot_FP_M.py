import ipywidgets as widgets
import plotly.express as px
from IPython.display import display
import plotly.io as pio


class PlotFP_M():
     def __init__(self,pd_fo):
         self.pd_fo=pd_fo  

         self.x_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo x")
         self.y_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo y")
         self.z_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo z")

         display(self.x_axis_widgets,self.y_axis_widgets,self.z_axis_widgets)

         self.button = widgets.Button(description="Atualizar")
         self.button.on_click(self.plot_FP_M)
         display(self.button)
        

     def plot_FP_M(self,b):
        x_axis=self.x_axis_widgets.value
        y_axis=self.y_axis_widgets.value
        z_axis=self.z_axis_widgets.value
        try:
            fig = px.scatter_3d(
                 self.pd_fo,
                 x=x_axis,
                 y=y_axis,
                 z=z_axis,
                 title="Multiobjetivo",
                 color_discrete_sequence=['blue']
                 )
            fig.show()
        except Exception as e:
            print("Erro ao plotar o gráfico:", e)