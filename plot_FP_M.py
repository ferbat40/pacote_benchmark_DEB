import ipywidgets as widgets
import plotly.express as px
from IPython.display import display
import plotly.io as pio
pio.renderers.default = 'colab'


class PlotFP_M():
     def __init__(self,pd_fo):
         self.pd_fo=pd_fo
         
    

         x_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo x")
         y_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo y")
         z_axis_widgets=widgets.Dropdown(options=self.pd_fo.columns, description="Eixo z")

         interactive_fo=widgets.interactive(self.plot_FP_M,
                            x_axis=x_axis_widgets,
                            y_axis=y_axis_widgets,
                            z_axis=z_axis_widgets,                 
                            )
         display(interactive_fo)


     def plot_FP_M(self,x_axis,y_axis,z_axis):
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