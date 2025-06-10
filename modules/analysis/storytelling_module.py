"""
Módulo para generar gráficos interactivos para storytelling sobre 
la necesidad de trabajar para costear estudios universitarios
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from ..core.data_loaders import read_work_motive_afford_study_dataset

class WorkStudyStorytellingCharts:
    """
    Clase para generar gráficos de storytelling sobre trabajo y estudios
    """
    
    def __init__(self):
        """Inicializa la clase cargando los datos"""
        self.df = read_work_motive_afford_study_dataset()
        # Importar configuración unificada de colores
        from ..core.color_config import STORYTELLING_COLORS
        self.colors = STORYTELLING_COLORS
        
    def get_chart_need_vs_no_need(self, height=600, width=1200):
        """
        Retorna el gráfico interactivo de "Necesitan Trabajar" vs "No Necesitan Trabajar"
        para poder costear sus estudios
        
        Args:
            height (int): Altura del gráfico en píxeles
            width (int): Ancho del gráfico en píxeles
            
        Returns:
            plotly.graph_objects.Figure: Gráfico interactivo
        """
        # Filtrar datos excluyendo CH (Suiza)
        df_filtered = self.df[self.df['Country'] != 'CH'].copy()
        countries = df_filtered['Country'].tolist()
        
        # Calcular porcentajes agrupados
        need_to_work = (df_filtered['Applies_Totally_Value'].fillna(0) + 
                       df_filtered['Applies_Rather_Value'].fillna(0) + 
                       df_filtered['Applies_Partially_Value'].fillna(0))
        
        dont_need_to_work = (df_filtered['Applies_Rather_Not_Value'].fillna(0) + 
                            df_filtered['Does_Not_Apply_Value'].fillna(0))

        # calcular la media que necesitan trabajar
        mean_need_to_work = need_to_work.mean()
        print(f"Media de necesitan trabajar: {mean_need_to_work}")  

        # Crear el gráfico
        fig = go.Figure()
        
        # Preparar datos combinados para hover más informativo
        combined_hover_data = []
        for i in range(len(countries)):
            combined_hover_data.append([need_to_work.iloc[i], dont_need_to_work.iloc[i]])
        
        # Barra para "Necesitan Trabajar" - usando color NEGATIVE (rojo) por ser problemático
        fig.add_trace(go.Bar(
            name='Necesitan Trabajar para Pagar Estudios',
            x=countries,
            y=need_to_work,
            marker_color=self.colors['need_work'],
            customdata=combined_hover_data,  # Datos combinados para hover
            hovertemplate='<b>%{x}</b><br>' + 
                         'Necesitan Trabajar: %{customdata[0]:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in need_to_work],
            textposition='inside',
            textfont=dict(color='white', size=10, family='Arial')
        ))
        
        # Barra para "No Necesitan Trabajar" - usando color POSITIVE (verde) por ser favorable
        fig.add_trace(go.Bar(
            name='No Necesitan Trabajar para Pagar Estudios',
            x=countries,
            y=dont_need_to_work,
            base=need_to_work,
            marker_color=self.colors['dont_need_work'],
            customdata=combined_hover_data,  # Datos combinados para hover
            hovertemplate='<b>%{x}</b><br>' + 
                         'No Necesitan Trabajar: %{customdata[1]:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in dont_need_to_work],
            textposition='inside',
            textfont=dict(color='white', size=10, family='Arial')
        ))
        
        # Destacar España
        spain_idx = countries.index('ES') if 'ES' in countries else None
        if spain_idx is not None:
            fig.add_shape(
                type="rect",
                x0=spain_idx-0.4, y0=0,
                x1=spain_idx+0.4, y1=100,
                line=dict(color=self.colors['spain'], width=4),
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
                arrowcolor=self.colors['spain'],
                font=dict(size=12, color=self.colors['text'], family='Arial, sans-serif')
            )
        
        # Aplicar layout estándar
        from ..core.color_config import apply_standard_layout
        fig = apply_standard_layout(
            fig,
            title='<b>Necesidad de Trabajar para Costear Estudios por País Europeo</b><br>' +
                  '<sub>¿Qué porcentaje de estudiantes necesitan vs no necesitan trabajar para pagar sus estudios?</sub>',
            height=height,
            width=width
        )
        
        fig.update_layout(
            xaxis_title='<b>Países Europeos</b>',
            yaxis_title='<b>Porcentaje de Estudiantes (%)</b>',
            barmode='stack',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.05,
                xanchor="center",
                x=0.5,
                font=dict(size=12, color='#000000', family='Arial, sans-serif')
            ),
            margin=dict(t=170, b=60, l=60, r=60)
        )
        
        fig.update_xaxes(
            tickangle=45,
            title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
            tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
        )
        fig.update_yaxes(
            range=[0, 100],
            title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
            tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
        )
        
        return fig
    
    def get_chart_spain_vs_europe(self, height=600, width=1000):
        """
        Retorna el gráfico interactivo comparando España vs Promedio Europeo
        sobre la necesidad de trabajar para poder costear los estudios
        
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
        
        # Promedio europeo (excluyendo España y CH)
        df_no_spain = self.df[(self.df['Country'] != 'ES') & (self.df['Country'] != 'CH')]
        
        # Categorías más claras que explican la necesidad de trabajar para pagar estudios
        categories = [
            'Totalmente<br>Necesario', 
            'Bastante<br>Necesario', 
            'Parcialmente<br>Necesario', 
            'Poco<br>Necesario', 
            'Nada<br>Necesario'
        ]
        
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
        
        # Usar colores unificados
        spain_color = self.colors['spain']
        europe_color = self.colors['europe']
        
        # Crear el gráfico
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='🇪🇸 España',
            x=categories,
            y=spain_values,
            marker_color=spain_color,
            opacity=0.9,
            hovertemplate='<b>España</b><br>' + 
                         '%{x}: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in spain_values],
            textposition='outside',
            textfont=dict(size=11, color=self.colors['text'], family='Arial, sans-serif')
        ))
        
        fig.add_trace(go.Bar(
            name='🇪🇺 Promedio Europeo',
            x=categories,
            y=europe_values,
            marker_color=europe_color,
            opacity=0.9,
            hovertemplate='<b>Promedio Europeo</b><br>' + 
                         '%{x}: %{y:.1f}%<br>' +
                         '<extra></extra>',
            text=[f'{val:.1f}%' for val in europe_values],
            textposition='outside',
            textfont=dict(size=11, color=self.colors['text'], family='Arial, sans-serif')
        ))
        
        # Aplicar layout estándar
        from ..core.color_config import apply_standard_layout
        fig = apply_standard_layout(
            fig,
            title='<b>¿Qué tan necesario es trabajar para poder pagar los estudios?</b><br>' +
                  '<sub>Comparación: España vs Promedio Europeo | Porcentaje de estudiantes por nivel de necesidad</sub>',
            height=height,
            width=width
        )
        
        fig.update_layout(
            xaxis_title='<b>Nivel de Necesidad de Trabajar para Costear Estudios</b>',
            yaxis_title='<b>Porcentaje de Estudiantes (%)</b>',
            barmode='group',
            hovermode='x unified',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                font=dict(size=13, color='#000000', family='Arial, sans-serif')
            ),
            margin=dict(t=150, b=100, l=60, r=60)
        )
        
        fig.update_xaxes(
            title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
            tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
        )
        
        fig.update_yaxes(
            range=[0, max(max(spain_values), max(europe_values)) + 8],
            title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
            tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
        )
        
        # Añadir interpretación más clara en lugar del resumen numérico
        spain_high_need = spain_values[0] + spain_values[1] + spain_values[2]  # Totalmente + Bastante + Parcialmente
        europe_high_need = europe_values[0] + europe_values[1] + europe_values[2]
        
        difference = spain_high_need - europe_high_need
        
        # Determinar el mensaje según la diferencia
        if difference > 5:
            comparison_text = f"España supera a Europa en {difference:.1f} puntos porcentuales"
            comparison_color = self.colors['need_work']  # NEGATIVE color
        elif difference < -5:
            comparison_text = f"España está {abs(difference):.1f} puntos por debajo de Europa"
            comparison_color = self.colors['dont_need_work']  # POSITIVE color
        else:
            comparison_text = f"España y Europa están muy similares (diferencia: {difference:+.1f}pp)"
            comparison_color = self.colors['text_light']  # Neutral color
        
        fig.add_annotation(
            x=2, y=max(max(spain_values), max(europe_values)) + 3,
            text=f"<b>Interpretación:</b><br>" +
                 f"• España: <b>{spain_high_need:.1f}%</b> necesitan trabajar para pagar estudios<br>" +
                 f"• Europa: <b>{europe_high_need:.1f}%</b> necesitan trabajar para pagar estudios<br>" +
                 f"• <span style='color: {comparison_color}'><b>{comparison_text}</b></span>",
            showarrow=False,
            bgcolor="rgba(248,249,250,0.95)",
            bordercolor=self.colors['border'],
            borderwidth=1.5,
            font=dict(size=11, color=self.colors['text'], family='Arial, sans-serif'),
            align="left"
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
        
        # Excluir España y CH del cálculo del promedio europeo
        df_no_spain = self.df[(self.df['Country'] != 'ES') & (self.df['Country'] != 'CH')]
        europe_need_work = (df_no_spain['Applies_Totally_Value'].fillna(0) + 
                           df_no_spain['Applies_Rather_Value'].fillna(0) + 
                           df_no_spain['Applies_Partially_Value'].fillna(0)).mean()
        
        # Encontrar extremos (excluyendo CH)
        df_stats = self.df[self.df['Country'] != 'CH'].copy()
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