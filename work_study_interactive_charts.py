#!/usr/bin/env python3
"""
Módulo especializado para crear gráficos interactivos de relación trabajo-estudio
Optimizado para uso en storytelling con España como foco principal
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
from storytelliing_charts import (
    read_work_study_relationship_dataset,
    PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy
)

# Importar configuración unificada de colores
from color_config import STORYTELLING_COLORS, COLOR_PALETTES, apply_standard_layout

# Configuración de colores para storytelling
SPAIN_COLOR = STORYTELLING_COLORS['spain']
EUROPE_COLOR = STORYTELLING_COLORS['europe']
NEUTRAL_COLOR = STORYTELLING_COLORS['text_light']
SUCCESS_COLOR = STORYTELLING_COLORS['dont_need_work']
WARNING_COLOR = STORYTELLING_COLORS['warning']

def create_storytelling_work_study_charts():
    """
    Crea un conjunto de gráficos interactivos optimizados para storytelling
    con España como protagonista
    """
    # Cargar datos
    df = read_work_study_relationship_dataset()
    
    charts = {}
    
    # 1. Hero Chart: España vs Europa - Comparación Principal
    charts['hero_chart'] = create_hero_spain_europe_comparison(df)
    
    # 2. Context Chart: Ranking Europeo con España destacada
    charts['ranking_chart'] = create_european_ranking_chart(df)
    
    # 3. Detail Chart: Desglose por niveles de relación
    charts['detail_chart'] = create_relationship_levels_chart(df)
    
    # 4. Insight Chart: Análisis de brechas
    charts['insight_chart'] = create_gap_analysis_chart(df)
    
    return charts, df


def create_hero_spain_europe_comparison(df):
    """
    Gráfico principal: España vs Europa - Hero chart para storytelling
    """
    # Calcular datos de España vs Europa
    spain_data = df[df['Country'] == 'ES'].iloc[0]
    europe_data = df[df['Country'] != 'ES']
    
    # Datos de España
    spain_values = {
        'Muy Relacionado': spain_data['Very_Closely_Value'],
        'Bastante Relacionado': spain_data['Rather_Closely_Value'],
        'Algo Relacionado': spain_data['To_Some_Extent_Value'],
        'Poco Relacionado': spain_data['Rather_Not_Value'],
        'Nada Relacionado': spain_data['Not_At_All_Value']
    }
    
    # Promedio europeo
    europe_values = {
        'Muy Relacionado': europe_data['Very_Closely_Value'].mean(),
        'Bastante Relacionado': europe_data['Rather_Closely_Value'].mean(),
        'Algo Relacionado': europe_data['To_Some_Extent_Value'].mean(),
        'Poco Relacionado': europe_data['Rather_Not_Value'].mean(),
        'Nada Relacionado': europe_data['Not_At_All_Value'].mean()
    }
    
    categories = list(spain_values.keys())
    spain_vals = list(spain_values.values())
    europe_vals = list(europe_values.values())
    
    fig = go.Figure()
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='🇪🇸 España',
        x=categories,
        y=spain_vals,
        marker_color=SPAIN_COLOR,
        hovertemplate='<b>España</b><br>%{x}: %{y:.1f}%<extra></extra>',
        text=[f'{v:.1f}%' for v in spain_vals],
        textposition='outside'
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='🇪🇺 Promedio Europeo',
        x=categories,
        y=europe_vals,
        marker_color=EUROPE_COLOR,
        hovertemplate='<b>Promedio Europeo</b><br>%{x}: %{y:.1f}%<extra></extra>',
        text=[f'{v:.1f}%' for v in europe_vals],
        textposition='outside'
    ))
    
    # Calcular el total relacionado para el insight
    spain_related = sum(spain_vals[:3])  # Muy + Bastante + Algo relacionado
    europe_related = sum(europe_vals[:3])
    gap = europe_related - spain_related
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig,
        title=f'🇪🇸 España vs 🇪🇺 Europa: Relación Trabajo-Estudio<br>' +
              f'<sub>España: {spain_related:.1f}% | Europa: {europe_related:.1f}% | Brecha: {gap:.1f} puntos</sub>',
        height=500,
        width=800
    )
    
    fig.update_layout(
        xaxis_title='Nivel de Relación',
        yaxis_title='Porcentaje de Estudiantes (%)',
        barmode='group',
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1,
            'xanchor': 'right',
            'x': 1
        }
    )
    
    fig.update_xaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    # Añadir anotación con insight clave
    fig.add_annotation(
        x=2,  # Posición central
        y=max(max(spain_vals), max(europe_vals)) + 5,
        text=f"<b>Gap de {gap:.1f} puntos</b><br>España por debajo del promedio europeo",
        showarrow=False,
        bgcolor=WARNING_COLOR,
        bordercolor='white',
        font={'color': 'white', 'size': 12},
        borderwidth=2
    )
    
    return fig


def create_european_ranking_chart(df):
    """
    Ranking europeo con España destacada - Para mostrar posición relativa
    """
    # Calcular score de relación para cada país
    df_rank = df.copy()
    df_rank['Related_Total'] = (
        df_rank['Very_Closely_Value'].fillna(0) + 
        df_rank['Rather_Closely_Value'].fillna(0) + 
        df_rank['To_Some_Extent_Value'].fillna(0)
    )
    
    # Ordenar por score
    df_rank = df_rank.sort_values('Related_Total', ascending=True)
    
    countries = df_rank['Country'].tolist()
    scores = df_rank['Related_Total'].tolist()
    
    # Crear colores destacando España
    colors = [SPAIN_COLOR if country == 'ES' else NEUTRAL_COLOR for country in countries]
    
    # Encontrar posición de España
    spain_position = countries.index('ES') + 1 if 'ES' in countries else None
    total_countries = len(countries)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=countries,
        x=scores,
        orientation='h',
        marker_color=colors,
        hovertemplate='<b>%{y}</b><br>Trabajo Relacionado: %{x:.1f}%<extra></extra>',
        text=[f'{s:.1f}%' for s in scores],
        textposition='outside'
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig,
        title=f'Ranking Europeo: Relación Trabajo-Estudio<br>' +
              f'<sub>España en posición {spain_position}/{total_countries}</sub>',
        height=700,
        width=800
    )
    
    fig.update_layout(
        xaxis_title='Porcentaje de Trabajo Relacionado con Estudios (%)',
        yaxis_title='Países',
    )
    
    fig.update_xaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    # Línea de promedio
    avg_score = np.mean(scores)
    fig.add_vline(
        x=avg_score,
        line_dash="dash",
        line_color=EUROPE_COLOR,
        annotation_text=f"Promedio Europeo: {avg_score:.1f}%",
        annotation_position="top"
    )
    
    return fig


def create_relationship_levels_chart(df):
    """
    Gráfico de barras apiladas mostrando distribución de niveles
    """
    countries = df['Country'].tolist()
    
    # Preparar datos para stack
    very_closely = df['Very_Closely_Value'].fillna(0).tolist()
    rather_closely = df['Rather_Closely_Value'].fillna(0).tolist()
    to_some_extent = df['To_Some_Extent_Value'].fillna(0).tolist()
    rather_not = df['Rather_Not_Value'].fillna(0).tolist()
    not_at_all = df['Not_At_All_Value'].fillna(0).tolist()
    
    fig = go.Figure()
    
    # Añadir trazas con gradiente de colores
    fig.add_trace(go.Bar(
        name='Muy Relacionado',
        x=countries,
        y=very_closely,
        marker_color='#1f77b4',
        hovertemplate='<b>%{x}</b><br>Muy Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Bastante Relacionado',
        x=countries,
        y=rather_closely,
        marker_color='#7fbf7f',
        hovertemplate='<b>%{x}</b><br>Bastante Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Algo Relacionado',
        x=countries,
        y=to_some_extent,
        marker_color='#ffbb78',
        hovertemplate='<b>%{x}</b><br>Algo Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Poco Relacionado',
        x=countries,
        y=rather_not,
        marker_color='#ff7f0e',
        hovertemplate='<b>%{x}</b><br>Poco Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Nada Relacionado',
        x=countries,
        y=not_at_all,
        marker_color='#d62728',
        hovertemplate='<b>%{x}</b><br>Nada Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Distribución de Niveles de Relación Trabajo-Estudio por País',
            'x': 0.5,
            'font': {'size': 18}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        barmode='stack',
        plot_bgcolor=STORYTELLING_COLORS['background'],
        paper_bgcolor=STORYTELLING_COLORS['background'],
        font={'size': 11, 'color': STORYTELLING_COLORS['text'], 'family': 'Arial, sans-serif'},
        height=600,
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': -0.3,
            'xanchor': 'center',
            'x': 0.5
        },
        xaxis={'tickangle': 45}
    )
    
    fig.update_xaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    # Destacar España
    spain_idx = countries.index('ES') if 'ES' in countries else None
    if spain_idx is not None:
        fig.add_annotation(
            x=spain_idx,
            y=105,
            text="🇪🇸",
            showarrow=True,
            arrowhead=2,
            arrowcolor=SPAIN_COLOR,
            font={'size': 20}
        )
    
    return fig


def create_gap_analysis_chart(df):
    """
    Análisis de brechas: España vs otros países similares
    """
    # Seleccionar países comparables (sur de Europa + algunos centrales)
    comparable_countries = ['ES', 'PT', 'IT', 'FR', 'DE', 'AT', 'CH']
    df_comp = df[df['Country'].isin(comparable_countries)].copy()
    
    # Calcular trabajo relacionado total
    df_comp['Related_Total'] = (
        df_comp['Very_Closely_Value'].fillna(0) + 
        df_comp['Rather_Closely_Value'].fillna(0) + 
        df_comp['To_Some_Extent_Value'].fillna(0)
    )
    
    # Ordenar por score
    df_comp = df_comp.sort_values('Related_Total', ascending=False)
    
    countries = df_comp['Country'].tolist()
    scores = df_comp['Related_Total'].tolist()
    
    # Colores especiales
    colors = [SPAIN_COLOR if country == 'ES' else NEUTRAL_COLOR for country in countries]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=countries,
        y=scores,
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Trabajo Relacionado: %{y:.1f}%<extra></extra>',
        text=[f'{s:.1f}%' for s in scores],
        textposition='outside'
    ))
    
    # Línea de España para comparación
    spain_score = df_comp[df_comp['Country'] == 'ES']['Related_Total'].iloc[0]
    fig.add_hline(
        y=spain_score,
        line_dash="dash",
        line_color=SPAIN_COLOR,
        annotation_text=f"España: {spain_score:.1f}%",
        annotation_position="right"
    )
    
    fig.update_layout(
        title={
            'text': 'España vs Países Comparables: Trabajo Relacionado con Estudios',
            'x': 0.5,
            'font': {'size': 18}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje de Trabajo Relacionado (%)',
        plot_bgcolor=STORYTELLING_COLORS['background'],
        paper_bgcolor=STORYTELLING_COLORS['background'],
        font={'size': 14, 'color': STORYTELLING_COLORS['text'], 'family': 'Arial, sans-serif'},
        height=500
    )
    
    fig.update_xaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig


def export_charts_for_storytelling(charts, output_dir='storytelling_charts'):
    """
    Exporta los gráficos en diferentes formatos para uso en storytelling
    """
    import os
    
    # Crear directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    formats = {
        'html': lambda fig, name: fig.write_html(f"{output_dir}/{name}.html"),
        'png': lambda fig, name: fig.write_image(f"{output_dir}/{name}.png", width=1200, height=800),
        'svg': lambda fig, name: fig.write_image(f"{output_dir}/{name}.svg", width=1200, height=800),
        'json': lambda fig, name: fig.write_json(f"{output_dir}/{name}.json")
    }
    
    for chart_name, fig in charts.items():
        for format_name, export_func in formats.items():
            try:
                export_func(fig, chart_name)
                print(f"✅ Exported {chart_name}.{format_name}")
            except Exception as e:
                print(f"❌ Error exporting {chart_name}.{format_name}: {e}")


def generate_storytelling_summary(df):
    """
    Genera un resumen narrativo para storytelling
    """
    # Datos de España
    spain_data = df[df['Country'] == 'ES'].iloc[0]
    spain_related = (spain_data['Very_Closely_Value'] + 
                    spain_data['Rather_Closely_Value'] + 
                    spain_data['To_Some_Extent_Value'])
    
    # Promedio europeo
    europe_data = df[df['Country'] != 'ES']
    europe_related = (europe_data['Very_Closely_Value'].mean() + 
                     europe_data['Rather_Closely_Value'].mean() + 
                     europe_data['To_Some_Extent_Value'].mean())
    
    # Ranking
    df_rank = df.copy()
    df_rank['Related_Total'] = (
        df_rank['Very_Closely_Value'].fillna(0) + 
        df_rank['Rather_Closely_Value'].fillna(0) + 
        df_rank['To_Some_Extent_Value'].fillna(0)
    )
    df_rank = df_rank.sort_values('Related_Total', ascending=False)
    spain_position = df_rank[df_rank['Country'] == 'ES'].index[0] + 1
    
    summary = {
        'spain_percentage': spain_related,
        'europe_percentage': europe_related,
        'gap': europe_related - spain_related,
        'spain_rank': spain_position,
        'total_countries': len(df),
        'spain_very_closely': spain_data['Very_Closely_Value'],
        'spain_not_at_all': spain_data['Not_At_All_Value'],
        'narrative': f"""
        📊 HISTORIA DE LOS DATOS: RELACIÓN TRABAJO-ESTUDIO EN ESPAÑA

        🇪🇸 En España, el {spain_related:.1f}% de los estudiantes tienen un trabajo 
        relacionado con sus estudios, comparado con el {europe_related:.1f}% del promedio europeo.

        📉 BRECHA IDENTIFICADA: España está {europe_related - spain_related:.1f} puntos 
        por debajo del promedio europeo, ocupando la posición {spain_position} de {len(df)} países.

        🔍 ANÁLISIS DETALLADO:
        • Solo el {spain_data['Very_Closely_Value']:.1f}% tiene trabajo muy relacionado
        • El {spain_data['Not_At_All_Value']:.1f}% tiene trabajo nada relacionado con sus estudios

        💡 OPORTUNIDAD: Existe margen para mejorar la conexión entre 
        formación académica y experiencia laboral de los estudiantes españoles.
        """
    }
    
    return summary


def main():
    """
    Función principal para demostrar el uso de los gráficos
    """
    print("🎨 Creando gráficos interactivos para storytelling...")
    
    # Crear todos los gráficos
    charts, df = create_storytelling_work_study_charts()
    
    # Mostrar gráficos
    for name, fig in charts.items():
        print(f"📊 Mostrando: {name}")
        fig.show()
    
    # Generar resumen narrativo
    summary = generate_storytelling_summary(df)
    print(summary['narrative'])
    
    # Exportar gráficos (opcional)
    # export_charts_for_storytelling(charts)
    
    return charts, df, summary


if __name__ == "__main__":
    main() 