import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from enum import Enum

# Clase para los datasets preprocessados (mismo que en storytelling_charts.py)
class PreprocessedDatasetsNamesWorkMotiveAffordStudy(Enum):
    WORK_MOTIVE_AFFORD_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__all_students__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_SEX = 'preprocessed_excels/E8_work_motive_afford_study_5__e_sex__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_AGE = 'preprocessed_excels/E8_work_motive_afford_study_5__e_age__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES = 'preprocessed_excels/E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS = 'preprocessed_excels/E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS = 'preprocessed_excels/E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx'

# Configuración de colores para storytelling
STORYTELLING_COLORS = {
    'spain': '#d62728',           # Rojo para España (destacado)
    'europe': '#1f77b4',          # Azul para promedio europeo
    'need_work': '#d62728',       # Rojo para necesidad de trabajar
    'dont_need_work': '#2ca02c',  # Verde para no necesidad
    'applies_totally': '#8B0000',  # Rojo oscuro
    'applies_rather': '#FF4500',   # Naranja rojizo
    'applies_partially': '#FFA500', # Naranja
    'applies_rather_not': '#DDA0DD', # Lila
    'does_not_apply': '#228B22',   # Verde oscuro
    'background': '#f8f9fa',       # Gris claro para fondos
    'text': '#2c3e50'             # Azul oscuro para texto
}

def read_preprocessed_dataset(dataset_enum):
    """
    Lee un dataset preprocessado con la estructura estándar
    """
    df = pd.read_excel(dataset_enum.value, header=None)
    
    # Los datos reales empiezan en la fila 3 (índice 3)
    data_df = df.iloc[3:].copy()
    
    # Verificar si es un dataset simple (16 columnas) o complejo (más columnas)
    if data_df.shape[1] == 16:
        # Estructura estándar simple
        column_names = ['Country']
        response_levels = [
            'Applies_Totally',      # Nivel 1 - Aplica totalmente
            'Applies_Rather',       # Nivel 2 - Aplica bastante
            'Applies_Partially',    # Nivel 3 - Aplica parcialmente  
            'Applies_Rather_Not',   # Nivel 4 - No aplica mucho
            'Does_Not_Apply'        # Nivel 5 - No aplica para nada
        ]
        
        for level in response_levels:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        data_df.columns = column_names
        
        # Convertir columnas numéricas
        for level in response_levels:
            value_col = f'{level}_Value'
            if value_col in data_df.columns:
                data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
            
            count_col = f'{level}_Count'
            if count_col in data_df.columns:
                data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    else:
        # Estructura compleja con múltiples subcategorías demográficas
        # Para estos casos, vamos a crear una estructura simplificada
        # tomando solo las primeras 16 columnas que corresponden al patrón estándar
        data_df_simple = data_df.iloc[:, :16].copy()
        
        column_names = ['Country']
        response_levels = [
            'Applies_Totally',      
            'Applies_Rather',       
            'Applies_Partially',    
            'Applies_Rather_Not',   
            'Does_Not_Apply'        
        ]
        
        for level in response_levels:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        data_df_simple.columns = column_names
        
        # Convertir columnas numéricas
        for level in response_levels:
            value_col = f'{level}_Value'
            if value_col in data_df_simple.columns:
                data_df_simple[value_col] = pd.to_numeric(data_df_simple[value_col], errors='coerce')
            
            count_col = f'{level}_Count'
            if count_col in data_df_simple.columns:
                data_df_simple[count_col] = pd.to_numeric(data_df_simple[count_col], errors='coerce').astype('Int64')
        
        data_df = data_df_simple
    
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    return data_df

def get_spain_comparison_data(df):
    """
    Extrae y prepara los datos de España vs promedio europeo
    """
    spain_data = df[df['Country'] == 'ES'].iloc[0] if 'ES' in df['Country'].values else None
    
    if spain_data is None:
        return None, None
    
    # Promedio europeo (excluyendo España)
    df_no_spain = df[df['Country'] != 'ES']
    
    spain_values = {
        'totally': spain_data['Applies_Totally_Value'],
        'rather': spain_data['Applies_Rather_Value'],
        'partially': spain_data['Applies_Partially_Value'],
        'rather_not': spain_data['Applies_Rather_Not_Value'],
        'not_apply': spain_data['Does_Not_Apply_Value']
    }
    
    europe_values = {
        'totally': df_no_spain['Applies_Totally_Value'].mean(),
        'rather': df_no_spain['Applies_Rather_Value'].mean(),  
        'partially': df_no_spain['Applies_Partially_Value'].mean(),
        'rather_not': df_no_spain['Applies_Rather_Not_Value'].mean(),
        'not_apply': df_no_spain['Does_Not_Apply_Value'].mean()
    }
    
    return spain_values, europe_values

def create_interactive_context_overview(df_general):
    """
    Crea una visualización general interactiva del contexto de trabajo para estudios
    """
    # Calcular necesidad total de trabajar por país
    df_work = df_general.copy()
    df_work['Need_Work_Total'] = (df_work['Applies_Totally_Value'].fillna(0) + 
                                 df_work['Applies_Rather_Value'].fillna(0) + 
                                 df_work['Applies_Partially_Value'].fillna(0))
    
    # Ordenar por necesidad de trabajar
    df_work = df_work.sort_values('Need_Work_Total', ascending=True)
    
    # Colores: España en rojo, otros en azul
    colors = [STORYTELLING_COLORS['spain'] if country == 'ES' 
              else STORYTELLING_COLORS['europe'] for country in df_work['Country']]
    
    fig = go.Figure()
    
    # Barra horizontal para mejor visualización con muchos países
    fig.add_trace(go.Bar(
        x=df_work['Need_Work_Total'],
        y=df_work['Country'],
        orientation='h',
        marker_color=colors,
        marker_line=dict(color='white', width=1),
        hovertemplate='<b>%{y}</b><br>' + 
                     'Necesidad de trabajar: %{x:.1f}%<br>' +
                     '<extra></extra>',
        text=[f'{val:.1f}%' for val in df_work['Need_Work_Total']],
        textposition='inside',
        textfont=dict(color='white', size=11, family='Arial Black')
    ))
    
    # Línea de promedio europeo
    avg_europe = df_work[df_work['Country'] != 'ES']['Need_Work_Total'].mean()
    fig.add_vline(x=avg_europe, line_dash="dash", line_color="gray", 
                  annotation_text=f"Promedio Europeo: {avg_europe:.1f}%")
    
    fig.update_layout(
        title={
            'text': '<b>¿Cuánto necesitan trabajar los estudiantes para costear sus estudios?</b><br>' +
                   '<i>Porcentaje de estudiantes por país que necesitan trabajar</i>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': STORYTELLING_COLORS['text']}
        },
        xaxis_title='Porcentaje de estudiantes (%)',
        yaxis_title='País',
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=800,
        width=1000,
        font=dict(family="Arial", size=12, color=STORYTELLING_COLORS['text']),
        showlegend=False,
        margin=dict(l=80, r=50, t=100, b=50)
    )
    
    # Grid sutil
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig

def create_interactive_spain_vs_europe_detailed(df_general):
    """
    Crea una comparación detallada España vs Europa con los 5 niveles
    """
    spain_values, europe_values = get_spain_comparison_data(df_general)
    
    if spain_values is None:
        return None
    
    categories = ['Aplica<br>Totalmente', 'Aplica<br>Bastante', 'Aplica<br>Parcialmente',
                 'No Aplica<br>Mucho', 'No Aplica<br>Para Nada']
    
    spain_data = [spain_values['totally'], spain_values['rather'], spain_values['partially'],
                  spain_values['rather_not'], spain_values['not_apply']]
    europe_data = [europe_values['totally'], europe_values['rather'], europe_values['partially'],
                   europe_values['rather_not'], europe_values['not_apply']]
    
    fig = go.Figure()
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=categories,
        y=spain_data,
        marker_color=STORYTELLING_COLORS['spain'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España</b><br>%{x}: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in spain_data],
        textposition='outside',
        width=0.35
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=categories,
        y=europe_data,
        marker_color=STORYTELLING_COLORS['europe'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo</b><br>%{x}: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in europe_data],
        textposition='outside',
        width=0.35
    ))
    
    fig.update_layout(
        title={
            'text': '<b>España vs Europa: Niveles de necesidad de trabajar</b><br>' +
                   '<i>Comparación detallada por niveles de respuesta</i>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': STORYTELLING_COLORS['text']}
        },
        xaxis_title='Nivel de necesidad',
        yaxis_title='Porcentaje de estudiantes (%)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=600,
        width=1000,
        font=dict(family="Arial", size=12, color=STORYTELLING_COLORS['text']),
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig

def create_interactive_context_by_demographics(dataset_enum, title_context, demographic_label):
    """
    Crea visualización interactiva por demografía específica (sexo, edad, etc.)
    """
    df = read_preprocessed_dataset(dataset_enum)
    
    # Esta función maneja datasets con múltiples categorías demográficas
    # Necesitamos adaptar la lectura según la estructura específica
    
    # Por ahora, crear un gráfico básico de España vs Europa
    spain_values, europe_values = get_spain_comparison_data(df)
    
    if spain_values is None:
        return None
    
    # Calcular necesidad total
    spain_need = spain_values['totally'] + spain_values['rather'] + spain_values['partially']
    europe_need = europe_values['totally'] + europe_values['rather'] + europe_values['partially']
    
    fig = go.Figure()
    
    categories = ['España', 'Promedio Europeo']
    values = [spain_need, europe_need]
    colors = [STORYTELLING_COLORS['spain'], STORYTELLING_COLORS['europe']]
    
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker_color=colors,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>%{x}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in values],
        textposition='outside',
        width=0.6
    ))
    
    fig.update_layout(
        title={
            'text': f'<b>{title_context}</b><br><i>España vs Europa - {demographic_label}</i>',
            'x': 0.5,
            'xanchor': 'center', 
            'font': {'size': 18, 'color': STORYTELLING_COLORS['text']}
        },
        xaxis_title='',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=500,
        width=600,
        font=dict(family="Arial", size=12, color=STORYTELLING_COLORS['text']),
        showlegend=False
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig

def create_storytelling_insights():
    """
    Genera insights clave para el storytelling
    """
    df_general = read_preprocessed_dataset(PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY)
    
    # Calcular estadísticas
    df_stats = df_general.copy()
    df_stats['Need_Work_Total'] = (df_stats['Applies_Totally_Value'].fillna(0) + 
                                  df_stats['Applies_Rather_Value'].fillna(0) + 
                                  df_stats['Applies_Partially_Value'].fillna(0))
    
    spain_data = df_stats[df_stats['Country'] == 'ES'].iloc[0] if 'ES' in df_stats['Country'].values else None
    
    insights = {
        'promedio_europeo': df_stats['Need_Work_Total'].mean(),
        'pais_mayor_necesidad': df_stats.loc[df_stats['Need_Work_Total'].idxmax(), 'Country'],
        'mayor_necesidad_pct': df_stats['Need_Work_Total'].max(),
        'pais_menor_necesidad': df_stats.loc[df_stats['Need_Work_Total'].idxmin(), 'Country'],
        'menor_necesidad_pct': df_stats['Need_Work_Total'].min(),
        'total_paises': len(df_stats),
    }
    
    if spain_data is not None:
        insights.update({
            'espana_necesidad': spain_data['Need_Work_Total'],
            'espana_aplica_totalmente': spain_data['Applies_Totally_Value'],
            'espana_no_aplica': spain_data['Does_Not_Apply_Value'],
            'espana_ranking': (df_stats['Need_Work_Total'] > spain_data['Need_Work_Total']).sum() + 1
        })
    
    return insights

# Función principal para generar todos los gráficos
def generate_all_interactive_charts():
    """
    Genera todos los gráficos interactivos para el scrollytelling
    """
    charts = {}
    
    # 1. Gráfico general de contexto
    df_general = read_preprocessed_dataset(PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY)
    charts['overview'] = create_interactive_context_overview(df_general)
    
    # 2. Comparación detallada España vs Europa
    charts['spain_vs_europe'] = create_interactive_spain_vs_europe_detailed(df_general)
    
    # 3. Contexto por demografías
    charts['by_sex'] = create_interactive_context_by_demographics(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_SEX,
        'Contexto por Género',
        'Diferencias entre hombres y mujeres'
    )
    
    charts['by_age'] = create_interactive_context_by_demographics(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_AGE,
        'Contexto por Edad',
        'Diferencias por grupos de edad'
    )
    
    charts['by_financial_difficulties'] = create_interactive_context_by_demographics(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES,
        'Contexto por Dificultades Financieras',
        'Impacto de las dificultades económicas'
    )
    
    # 4. Insights para storytelling
    charts['insights'] = create_storytelling_insights()
    
    return charts

if __name__ == "__main__":
    # Ejemplo de uso
    print("Generando gráficos interactivos para storytelling...")
    
    # Generar todos los gráficos
    all_charts = generate_all_interactive_charts()
    
    # Mostrar insights
    insights = all_charts['insights']
    print(f"\n🎯 INSIGHTS CLAVE PARA STORYTELLING:")
    print(f"   • Promedio europeo: {insights['promedio_europeo']:.1f}%")
    if 'espana_necesidad' in insights:
        print(f"   • España: {insights['espana_necesidad']:.1f}% (puesto #{insights['espana_ranking']} de {insights['total_paises']})")
    print(f"   • País con mayor necesidad: {insights['pais_mayor_necesidad']} ({insights['mayor_necesidad_pct']:.1f}%)")
    print(f"   • País con menor necesidad: {insights['pais_menor_necesidad']} ({insights['menor_necesidad_pct']:.1f}%)")
    
    # Los gráficos se pueden mostrar individualmente:
    # all_charts['overview'].show()
    # all_charts['spain_vs_europe'].show()
    
    print("\n✅ Gráficos generados exitosamente!")
    print("   • Usa all_charts['overview'] para el gráfico general")
    print("   • Usa all_charts['spain_vs_europe'] para la comparación detallada")
    print("   • Usa all_charts['by_sex'], all_charts['by_age'], etc. para contextos específicos") 