import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from storytelliing_charts import read_work_motive_afford_study_dataset

# Configuración de colores consistentes
COLORS = {
    'need_work': '#d62728',
    'dont_need_work': '#2ca02c', 
    'spain': '#d62728',
    'europe': '#1f77b4',
    'applies_totally': '#8B0000',
    'applies_rather': '#FF4500',
    'applies_partially': '#FFA500',
    'applies_rather_not': '#DDA0DD',
    'does_not_apply': '#228B22'
}

def create_interactive_need_vs_no_need_chart(df):
    """
    Crea un gráfico interactivo que compara "Necesitan Trabajar" vs "No Necesitan Trabajar"
    """
    # Preparar los datos
    countries = df['Country'].tolist()
    
    # Calcular porcentajes agrupados
    need_to_work = (df['Applies_Totally_Value'].fillna(0) + 
                   df['Applies_Rather_Value'].fillna(0) + 
                   df['Applies_Partially_Value'].fillna(0))
    
    dont_need_to_work = (df['Applies_Rather_Not_Value'].fillna(0) + 
                        df['Does_Not_Apply_Value'].fillna(0))
    
    # Crear el gráfico de barras apiladas
    fig = go.Figure()
    
    # Barra para "Necesitan Trabajar"
    fig.add_trace(go.Bar(
        name='Necesitan Trabajar',
        x=countries,
        y=need_to_work,
        marker_color=COLORS['need_work'],
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
        marker_color=COLORS['dont_need_work'],
        hovertemplate='<b>%{x}</b><br>' + 
                     'No Necesitan Trabajar: %{y:.1f}%<br>' +
                     '<extra></extra>',
        text=[f'{val:.1f}%' for val in dont_need_to_work],
        textposition='inside',
        textfont=dict(color='white', size=10)
    ))
    
    # Destacar España con un borde
    spain_idx = countries.index('ES') if 'ES' in countries else None
    if spain_idx is not None:
        # Añadir marcador especial para España
        fig.add_shape(
            type="rect",
            x0=spain_idx-0.4, y0=0,
            x1=spain_idx+0.4, y1=100,
            line=dict(color="black", width=3),
            fillcolor="rgba(0,0,0,0)"
        )
        
        # Añadir anotación para España
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
    
    # Personalizar el layout
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
        height=600,
        width=1200,
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
    
    # Personalizar ejes
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

def create_interactive_spain_vs_europe_chart(df):
    """
    Crea un gráfico interactivo comparando España vs Promedio Europeo
    """
    # Datos de España
    spain_data = df[df['Country'] == 'ES'].iloc[0] if 'ES' in df['Country'].values else None
    
    if spain_data is None:
        print("España no encontrada en los datos")
        return None
    
    # Promedio europeo (excluyendo España)
    df_no_spain = df[df['Country'] != 'ES']
    
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
    
    # Crear el gráfico de barras agrupadas
    fig = go.Figure()
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='🇪🇸 España',
        x=categories,
        y=spain_values,
        marker_color=COLORS['spain'],
        opacity=0.8,
        hovertemplate='<b>España</b><br>' + 
                     '%{x}: %{y:.1f}%<br>' +
                     '<extra></extra>',
        text=[f'{val:.1f}%' for val in spain_values],
        textposition='outside',
        textfont=dict(size=11)
    ))
    
    # Barras del promedio europeo
    fig.add_trace(go.Bar(
        name='🇪🇺 Promedio Europeo',
        x=categories,
        y=europe_values,
        marker_color=COLORS['europe'],
        opacity=0.8,
        hovertemplate='<b>Promedio Europeo</b><br>' + 
                     '%{x}: %{y:.1f}%<br>' +
                     '<extra></extra>',
        text=[f'{val:.1f}%' for val in europe_values],
        textposition='outside',
        textfont=dict(size=11)
    ))
    
    # Personalizar el layout
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
        height=600,
        width=1000,
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
    
    # Personalizar ejes
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
    
    # Añadir anotaciones explicativas
    spain_need_work = spain_values[0] + spain_values[1] + spain_values[2]  # Suma de los 3 primeros
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

def save_charts_for_storytelling(df, save_html=True):
    """
    Genera y guarda los gráficos para usar en storytelling
    """
    print("🎨 Generando gráficos interactivos para storytelling...")
    
    # Crear los gráficos
    chart1 = create_interactive_need_vs_no_need_chart(df)
    chart2 = create_interactive_spain_vs_europe_chart(df)
    
    if save_html:
        # Guardar como HTML
        chart1.write_html("grafico_necesidad_trabajar.html")
        chart2.write_html("grafico_espana_vs_europa.html")
        print("✅ Gráficos guardados como:")
        print("   • grafico_necesidad_trabajar.html")
        print("   • grafico_espana_vs_europa.html")
    
    # Mostrar los gráficos
    print("\n📊 Mostrando gráficos...")
    chart1.show()
    chart2.show()
    
    return chart1, chart2

def get_storytelling_insights(df):
    """
    Genera insights clave para el storytelling
    """
    # Calcular datos clave
    spain_data = df[df['Country'] == 'ES'].iloc[0] if 'ES' in df['Country'].values else None
    
    if spain_data is None:
        return "España no encontrada en los datos"
    
    spain_need_work = (spain_data['Applies_Totally_Value'] + 
                      spain_data['Applies_Rather_Value'] + 
                      spain_data['Applies_Partially_Value'])
    
    df_no_spain = df[df['Country'] != 'ES']
    europe_need_work = (df_no_spain['Applies_Totally_Value'].fillna(0) + 
                       df_no_spain['Applies_Rather_Value'].fillna(0) + 
                       df_no_spain['Applies_Partially_Value'].fillna(0)).mean()
    
    # Encontrar países extremos
    df_stats = df.copy()
    df_stats['Need_Work_Total'] = (df_stats['Applies_Totally_Value'].fillna(0) + 
                                  df_stats['Applies_Rather_Value'].fillna(0) + 
                                  df_stats['Applies_Partially_Value'].fillna(0))
    
    max_country = df_stats.loc[df_stats['Need_Work_Total'].idxmax(), 'Country']
    max_percentage = df_stats['Need_Work_Total'].max()
    
    min_country = df_stats.loc[df_stats['Need_Work_Total'].idxmin(), 'Country']
    min_percentage = df_stats['Need_Work_Total'].min()
    
    insights = f"""
🎯 INSIGHTS PARA STORYTELLING:

📈 DATOS CLAVE:
• España: {spain_need_work:.1f}% de estudiantes necesitan trabajar para costear estudios
• Promedio Europeo: {europe_need_work:.1f}% 
• Diferencia: {spain_need_work - europe_need_work:+.1f} puntos porcentuales

🏆 EXTREMOS:
• Mayor necesidad: {max_country} ({max_percentage:.1f}%)
• Menor necesidad: {min_country} ({min_percentage:.1f}%)

🔍 MENSAJE PRINCIPAL:
{'España está por encima del promedio europeo' if spain_need_work > europe_need_work else 'España está por debajo del promedio europeo'} 
en cuanto a estudiantes que necesitan trabajar para costear sus estudios.

💡 STORYTELLING ANGLE:
El {spain_data['Applies_Totally_Value']:.1f}% de estudiantes españoles considera que trabajar 
para costear estudios "aplica totalmente" a su situación, comparado con el 
{df_no_spain['Applies_Totally_Value'].mean():.1f}% del promedio europeo.
"""
    
    return insights

# Función principal para ejecutar todo
def main():
    """Función principal para generar los gráficos interactivos"""
    # Cargar datos
    df = read_work_motive_afford_study_dataset()
    
    # Generar insights
    insights = get_storytelling_insights(df)
    print(insights)
    
    # Crear y guardar gráficos
    chart1, chart2 = save_charts_for_storytelling(df)
    
    return chart1, chart2, insights

if __name__ == "__main__":
    main() 