"""
Módulo para generar gráficos interactivos para storytelling sobre 
la necesidad de trabajar para costear estudios universitarios
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from storytelliing_charts import read_work_motive_afford_study_dataset

class WorkStudyStorytellingCharts:
    """
    Clase para generar gráficos de storytelling sobre trabajo y estudios
    """
    
    def __init__(self):
        """Inicializa la clase cargando los datos"""
        self.df = read_work_motive_afford_study_dataset()
        self.colors = {
            'need_work': '#d62728',
            'dont_need_work': '#2ca02c', 
            'spain': '#d62728',
            'europe': '#1f77b4'
        }
        
    def get_chart_need_vs_no_need(self, height=600, width=1200):
        """
        Retorna el gráfico interactivo de "Necesitan Trabajar" vs "No Necesitan Trabajar"
        
        Args:
            height (int): Altura del gráfico en píxeles
            width (int): Ancho del gráfico en píxeles
            
        Returns:
            plotly.graph_objects.Figure: Gráfico interactivo
        """
        countries = self.df['Country'].tolist()
        
        # Calcular porcentajes agrupados
        need_to_work = (self.df['Applies_Totally_Value'].fillna(0) + 
                       self.df['Applies_Rather_Value'].fillna(0) + 
                       self.df['Applies_Partially_Value'].fillna(0))
        
        dont_need_to_work = (self.df['Applies_Rather_Not_Value'].fillna(0) + 
                            self.df['Does_Not_Apply_Value'].fillna(0))
        
        # Crear el gráfico
        fig = go.Figure()
        
        # Barra para "Necesitan Trabajar"
        fig.add_trace(go.Bar(
            name='Necesitan Trabajar',
            x=countries,
            y=need_to_work,
            marker_color=self.colors['need_work'],
            hovertemplate='<b>%{x}</b><br>' + 
                         'Necesitan Trabajar: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in need_to_work],
            textposition='inside',
            textfont=dict(color='white', size=10)
        ))
        
        # Barra para "No Necesitan Trabajar"
        fig.add_trace(go.Bar(
            name='No Necesitan Trabajar',
            x=countries,
            y=dont_need_to_work,
            base=need_to_work,
            marker_color=self.colors['dont_need_work'],
            hovertemplate='<b>%{x}</b><br>' + 
                         'No Necesitan Trabajar: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in dont_need_to_work],
            textposition='inside',
            textfont=dict(color='white', size=10)
        ))
        
        # Destacar España
        spain_idx = countries.index('ES') if 'ES' in countries else None
        if spain_idx is not None:
            fig.add_shape(
                type="rect",
                x0=spain_idx-0.4, y0=0,
                x1=spain_idx+0.4, y1=100,
                line=dict(color="black", width=3),
                fillcolor="rgba(0,0,0,0)"
            )
            
            spain_need = need_to_work.iloc[spain_idx]
            fig.add_annotation(
                x=spain_idx,
                y=spain_need + 5,
                text="🇪🇸 España",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="black",
                font=dict(size=12, color="black")
            )
        
        # Personalizar layout
        fig.update_layout(
            title={
                'text': '<b>Necesidad de Trabajar para Costear Estudios por País</b><br>' +
                       '<sub>Porcentaje de estudiantes que necesitan vs no necesitan trabajar</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18}
            },
            xaxis_title='<b>Países</b>',
            yaxis_title='<b>Porcentaje (%)</b>',
            barmode='stack',
            height=height,
            width=width,
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                font=dict(size=12)
            ),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray',
            tickangle=45
        )
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray',
            range=[0, 100]
        )
        
        return fig
    
    def get_chart_spain_vs_europe(self, height=600, width=1000):
        """
        Retorna el gráfico interactivo comparando España vs Promedio Europeo
        
        Args:
            height (int): Altura del gráfico en píxeles
            width (int): Ancho del gráfico en píxeles
            
        Returns:
            plotly.graph_objects.Figure: Gráfico interactivo
        """
        spain_data = self.df[self.df['Country'] == 'ES'].iloc[0] if 'ES' in self.df['Country'].values else None
        
        if spain_data is None:
            print("España no encontrada en los datos")
            return None
        
        # Promedio europeo (excluyendo España)
        df_no_spain = self.df[self.df['Country'] != 'ES']
        
        categories = ['Aplica<br>Totalmente', 'Aplica<br>Bastante', 'Aplica<br>Parcialmente', 
                     'No Aplica<br>Mucho', 'No Aplica<br>Para Nada']
        
        spain_values = [
            spain_data['Applies_Totally_Value'], 
            spain_data['Applies_Rather_Value'],
            spain_data['Applies_Partially_Value'], 
            spain_data['Applies_Rather_Not_Value'],
            spain_data['Does_Not_Apply_Value']
        ]
        
        europe_values = [
            df_no_spain['Applies_Totally_Value'].mean(),
            df_no_spain['Applies_Rather_Value'].mean(),
            df_no_spain['Applies_Partially_Value'].mean(),
            df_no_spain['Applies_Rather_Not_Value'].mean(),
            df_no_spain['Does_Not_Apply_Value'].mean()
        ]
        
        # Crear el gráfico
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='🇪🇸 España',
            x=categories,
            y=spain_values,
            marker_color=self.colors['spain'],
            opacity=0.8,
            hovertemplate='<b>España</b><br>' + 
                         '%{x}: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in spain_values],
            textposition='outside',
            textfont=dict(size=11)
        ))
        
        fig.add_trace(go.Bar(
            name='🇪🇺 Promedio Europeo',
            x=categories,
            y=europe_values,
            marker_color=self.colors['europe'],
            opacity=0.8,
            hovertemplate='<b>Promedio Europeo</b><br>' + 
                         '%{x}: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in europe_values],
            textposition='outside',
            textfont=dict(size=11)
        ))
        
        # Personalizar layout
        fig.update_layout(
            title={
                'text': '<b>España vs Promedio Europeo</b><br>' +
                       '<sub>Motivos para trabajar y costear estudios</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18}
            },
            xaxis_title='<b>Nivel de Aplicación del Motivo</b>',
            yaxis_title='<b>Porcentaje (%)</b>',
            barmode='group',
            height=height,
            width=width,
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                font=dict(size=12)
            ),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray'
        )
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray',
            range=[0, max(max(spain_values), max(europe_values)) + 10]
        )
        
        # Añadir resumen
        spain_need_work = spain_values[0] + spain_values[1] + spain_values[2]
        europe_need_work = europe_values[0] + europe_values[1] + europe_values[2]
        
        fig.add_annotation(
            x=2, y=max(max(spain_values), max(europe_values)) + 5,
            text=f"<b>Resumen:</b><br>España: {spain_need_work:.1f}% necesitan trabajar<br>Europa: {europe_need_work:.1f}% necesitan trabajar",
            showarrow=False,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="gray",
            borderwidth=1,
            font=dict(size=10)
        )
        
        return fig
    
    def get_key_insights(self):
        """
        Retorna los insights clave para storytelling
        
        Returns:
            dict: Diccionario con insights y estadísticas clave
        """
        spain_data = self.df[self.df['Country'] == 'ES'].iloc[0] if 'ES' in self.df['Country'].values else None
        
        if spain_data is None:
            return {"error": "España no encontrada en los datos"}
        
        spain_need_work = (spain_data['Applies_Totally_Value'] + 
                          spain_data['Applies_Rather_Value'] + 
                          spain_data['Applies_Partially_Value'])
        
        df_no_spain = self.df[self.df['Country'] != 'ES']
        europe_need_work = (df_no_spain['Applies_Totally_Value'].fillna(0) + 
                           df_no_spain['Applies_Rather_Value'].fillna(0) + 
                           df_no_spain['Applies_Partially_Value'].fillna(0)).mean()
        
        # Encontrar extremos
        df_stats = self.df.copy()
        df_stats['Need_Work_Total'] = (df_stats['Applies_Totally_Value'].fillna(0) + 
                                      df_stats['Applies_Rather_Value'].fillna(0) + 
                                      df_stats['Applies_Partially_Value'].fillna(0))
        
        max_country = df_stats.loc[df_stats['Need_Work_Total'].idxmax(), 'Country']
        max_percentage = df_stats['Need_Work_Total'].max()
        
        min_country = df_stats.loc[df_stats['Need_Work_Total'].idxmin(), 'Country']
        min_percentage = df_stats['Need_Work_Total'].min()
        
        return {
            'spain_need_work': spain_need_work,
            'europe_need_work': europe_need_work,
            'difference': spain_need_work - europe_need_work,
            'spain_totally_applies': spain_data['Applies_Totally_Value'],
            'spain_not_apply': spain_data['Does_Not_Apply_Value'],
            'europe_totally_applies': df_no_spain['Applies_Totally_Value'].mean(),
            'max_country': max_country,
            'max_percentage': max_percentage,
            'min_country': min_country,
            'min_percentage': min_percentage,
            'total_students_spain': (spain_data['Applies_Totally_Count'] + 
                                   spain_data['Applies_Rather_Count'] + 
                                   spain_data['Applies_Partially_Count'] + 
                                   spain_data['Applies_Rather_Not_Count'] + 
                                   spain_data['Does_Not_Apply_Count'])
        }
    
    def save_charts(self, save_path="./"):
        """
        Guarda los gráficos como archivos HTML
        
        Args:
            save_path (str): Ruta donde guardar los archivos
        """
        chart1 = self.get_chart_need_vs_no_need()
        chart2 = self.get_chart_spain_vs_europe()
        
        chart1.write_html(f"{save_path}grafico_necesidad_trabajar.html")
        chart2.write_html(f"{save_path}grafico_espana_vs_europa.html")
        
        print("✅ Gráficos guardados:")
        print(f"   • {save_path}grafico_necesidad_trabajar.html")
        print(f"   • {save_path}grafico_espana_vs_europa.html")


# Función de conveniencia para uso rápido
def create_work_study_charts():
    """
    Función de conveniencia para crear rápidamente los gráficos
    
    Returns:
        tuple: (chart1, chart2, insights)
    """
    storytelling = WorkStudyStorytellingCharts()
    
    chart1 = storytelling.get_chart_need_vs_no_need()
    chart2 = storytelling.get_chart_spain_vs_europe()
    insights = storytelling.get_key_insights()
    
    return chart1, chart2, insights

# Demo cuando se ejecuta directamente
if __name__ == "__main__":
    storytelling = WorkStudyStorytellingCharts()
    
    print("🎯 INSIGHTS CLAVE:")
    insights = storytelling.get_key_insights()
    print(f"• España: {insights['spain_need_work']:.1f}% necesitan trabajar")
    print(f"• Europa: {insights['europe_need_work']:.1f}% necesitan trabajar")
    print(f"• Diferencia: {insights['difference']:+.1f} puntos porcentuales")
    
    print("\n📊 Generando gráficos...")
    chart1 = storytelling.get_chart_need_vs_no_need()
    chart2 = storytelling.get_chart_spain_vs_europe()
    
    storytelling.save_charts()
    
    print("\n✨ Listo para usar en tu storytelling!")
    print("Puedes usar:")
    print("   from storytelling_module import WorkStudyStorytellingCharts")
    print("   storytelling = WorkStudyStorytellingCharts()")
    print("   chart1 = storytelling.get_chart_need_vs_no_need()")
    print("   chart2 = storytelling.get_chart_spain_vs_europe()") 