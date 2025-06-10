"""
Módulo de gráficos de impacto del trabajo en los estudios
Contiene análisis de abandono, rendimiento y efectos en la salud estudiantil
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

# Importar configuración unificada de colores
from ..core.color_config import STORYTELLING_COLORS, apply_standard_layout
from ..core.data_loaders import (
    read_work_impact_dataset,
    PreprocessedDatasetsNamesImpactsOnStudyForWork
)

def create_streamlit_abandoning_chart(df, title, subtitle):
    """
    Crea un gráfico de barras específico para análisis de abandono optimizado para Streamlit
    """
    if df is None or df.empty:
        return None
    
    # Filtrar datos de España y calcular promedio europeo
    spain_data = df[df['Country'] == 'ES']
    europe_data = df[df['Country'] != 'ES']
    
    if spain_data.empty:
        print("No se encontraron datos de España")
        return None
    
    # Categorías de frecuencia de consideración de abandono
    categories = [
        'Muy frecuentemente',
        'Frecuentemente', 
        'A veces',
        'Raramente',
        'Nunca'
    ]
    
    # Extraer valores para España
    spain_values = [
        spain_data['Very_Often_Value'].iloc[0] if not spain_data['Very_Often_Value'].isna().iloc[0] else 0,
        spain_data['Often_Value'].iloc[0] if not spain_data['Often_Value'].isna().iloc[0] else 0,
        spain_data['Sometimes_Value'].iloc[0] if not spain_data['Sometimes_Value'].isna().iloc[0] else 0,
        spain_data['Rarely_Value'].iloc[0] if not spain_data['Rarely_Value'].isna().iloc[0] else 0,
        spain_data['Never_Value'].iloc[0] if not spain_data['Never_Value'].isna().iloc[0] else 0
    ]
    
    # Calcular promedio europeo
    europe_values = [
        europe_data['Very_Often_Value'].mean() if not europe_data['Very_Often_Value'].isna().all() else 0,
        europe_data['Often_Value'].mean() if not europe_data['Often_Value'].isna().all() else 0,
        europe_data['Sometimes_Value'].mean() if not europe_data['Sometimes_Value'].isna().all() else 0,
        europe_data['Rarely_Value'].mean() if not europe_data['Rarely_Value'].isna().all() else 0,
        europe_data['Never_Value'].mean() if not europe_data['Never_Value'].isna().all() else 0
    ]
    
    # Crear gráfico
    fig = go.Figure()
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_values,
        marker_color=STORYTELLING_COLORS['spain'],
        marker_line=dict(color='white', width=2),
        text=[f'{val:.1f}%' for val in spain_values],
        textposition='outside',
        hovertemplate='<b>España - %{text}</b><br>Porcentaje: %{y:.1f}%<extra></extra>',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_values,
        marker_color=STORYTELLING_COLORS['europe'],
        marker_line=dict(color='white', width=2),
        text=[f'{val:.1f}%' for val in europe_values],
        textposition='outside',
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Porcentaje: %{y:.1f}%<extra></extra>',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig,
        title=f'<b>{title}</b><br><i>{subtitle}</i>',
        height=600,
        width=1000
    )
    
    fig.update_layout(
        xaxis_title='Frecuencia de Consideración',
        yaxis_title='Porcentaje de Estudiantes (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.95,
            xanchor="center",
            x=0.5
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=categories,
        title_font=dict(color='#000000', size=14),
        tickfont=dict(color='#000000', size=11)
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14),
        tickfont=dict(color='#000000', size=11)
    )
    
    return fig

def create_spain_europe_impact_comparison(df_financial, df_work_afford):
    """
    Crea un gráfico comparativo específico España vs Europa para diferentes tipos de impacto
    """
    # Datos para España
    spain_financial = df_financial[df_financial['Country'] == 'ES'] if df_financial is not None and not df_financial.empty else None
    spain_work = df_work_afford[df_work_afford['Country'] == 'ES'] if df_work_afford is not None and not df_work_afford.empty else None
    
    # Datos para Europa (promedio)
    europe_financial = df_financial[df_financial['Country'] != 'ES'] if df_financial is not None and not df_financial.empty else None
    europe_work = df_work_afford[df_work_afford['Country'] != 'ES'] if df_work_afford is not None and not df_work_afford.empty else None
    
    categories = ['Por Dificultades Financieras', 'Por Necesidad de Trabajar']
    spain_values = []
    europe_values = []
    
    # Calcular porcentajes de "frecuentemente + muy frecuentemente" para España
    if spain_financial is not None and not spain_financial.empty:
        spain_fin_high = (spain_financial['Very_Often_Value'].iloc[0] + spain_financial['Often_Value'].iloc[0])
        spain_values.append(spain_fin_high)
    else:
        spain_values.append(0)
    
    if spain_work is not None and not spain_work.empty:
        spain_work_high = (spain_work['Very_Often_Value'].iloc[0] + spain_work['Often_Value'].iloc[0])
        spain_values.append(spain_work_high)
    else:
        spain_values.append(0)
    
    # Calcular promedios europeos
    if europe_financial is not None and not europe_financial.empty:
        europe_fin_high = (europe_financial['Very_Often_Value'].mean() + europe_financial['Often_Value'].mean())
        europe_values.append(europe_fin_high)
    else:
        europe_values.append(0)
    
    if europe_work is not None and not europe_work.empty:
        europe_work_high = (europe_work['Very_Often_Value'].mean() + europe_work['Often_Value'].mean())
        europe_values.append(europe_work_high)
    else:
        europe_values.append(0)
    
    # Crear gráfico
    fig = go.Figure()
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barras España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_values,
        marker_color=STORYTELLING_COLORS['spain'],
        marker_line=dict(color='white', width=2),
        text=[f'{val:.1f}%' for val in spain_values],
        textposition='outside',
        hovertemplate='<b>España - %{x}</b><br>Considera abandono: %{y:.1f}%<extra></extra>',
        width=width
    ))
    
    # Barras Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_values,
        marker_color=STORYTELLING_COLORS['europe'],
        marker_line=dict(color='white', width=2),
        text=[f'{val:.1f}%' for val in europe_values],
        textposition='outside',
        hovertemplate='<b>Promedio Europeo - %{x}</b><br>Considera abandono: %{y:.1f}%<extra></extra>',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig,
        title='<b>Consideración de Abandono de Estudios</b><br><i>España vs Promedio Europeo - Porcentaje que considera frecuentemente</i>',
        height=600,
        width=800
    )
    
    fig.update_layout(
        xaxis_title='Tipo de Presión',
        yaxis_title='Porcentaje que Considera Abandonar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.90,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=categories,
        title_font=dict(color='#000000', size=14),
        tickfont=dict(color='#000000', size=11)
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14),
        tickfont=dict(color='#000000', size=11)
    )
    
    return fig

def get_work_impact_figures_for_streamlit():
    """
    Función específica para obtener las figuras de impacto del trabajo 
    optimizadas para uso en Streamlit scrollytelling
    """
    print("🔄 Cargando figuras de impacto del trabajo para Streamlit...")
    
    # Cargar datasets de impacto
    datasets = {}
    
    try:
        # Cargar solo los datasets esenciales para evitar errores
        print("📥 Cargando datasets de impacto...")
        
        # Dataset de abandono por dificultades financieras
        datasets['abandoning_financial'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__E_FINANCIAL_DIFFICULTIES
        )
        
        # Dataset de abandono por necesidad de trabajar
        datasets['abandoning_work_afford'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__S_WORK_TO_AFFORD_TO_STUDY
        )
        
        print("✅ Datasets de impacto cargados exitosamente")
        
    except Exception as e:
        print(f"⚠️ Error cargando datasets de impacto: {e}")
        return {}
    
    # Crear figuras optimizadas para Streamlit
    figures = {}
    
    try:
        # 1. Figura de abandono por dificultades financieras
        if 'abandoning_financial' in datasets and datasets['abandoning_financial'] is not None:
            figures['abandono_financiero'] = create_streamlit_abandoning_chart(
                datasets['abandoning_financial'],
                "Abandono por Dificultades Financieras",
                "Frecuencia con la que los estudiantes consideran abandonar por motivos económicos"
            )
            print("✅ Figura de abandono financiero creada")
        
        # 2. Figura de abandono por necesidad de trabajar
        if 'abandoning_work_afford' in datasets and datasets['abandoning_work_afford'] is not None:
            figures['abandono_trabajo'] = create_streamlit_abandoning_chart(
                datasets['abandoning_work_afford'],
                "Abandono por Necesidad de Trabajar",
                "Frecuencia con la que los estudiantes consideran abandonar para trabajar más tiempo"
            )
            print("✅ Figura de abandono por trabajo creada")
        
        # 3. Comparación España vs Europa
        if 'abandoning_financial' in datasets and 'abandoning_work_afford' in datasets:
            figures['espana_vs_europa_impacto'] = create_spain_europe_impact_comparison(
                datasets['abandoning_financial'],
                datasets['abandoning_work_afford']
            )
            print("✅ Figura comparativa España vs Europa creada")
        
    except Exception as e:
        print(f"⚠️ Error creando figuras de impacto: {e}")
    
    print(f"🎯 Total de figuras de impacto preparadas: {len(figures)}")
    return figures

# Función para mantener compatibilidad con código existente
def create_comprehensive_work_impact_dashboard():
    """
    Función principal que crea un dashboard completo del impacto del trabajo en los estudios
    """
    print("📊 Cargando datos de impacto del trabajo en los estudios...")
    
    # Utilizar la nueva función optimizada
    figures = get_work_impact_figures_for_streamlit()
    datasets = {}
    
    try:
        # Cargar datasets principales
        datasets['abandoning_financial'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__E_FINANCIAL_DIFFICULTIES
        )
        datasets['abandoning_work_afford'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__S_WORK_TO_AFFORD_TO_STUDY
        )
        
    except Exception as e:
        print(f"⚠️ Error cargando datasets: {e}")
    
    return datasets, figures 