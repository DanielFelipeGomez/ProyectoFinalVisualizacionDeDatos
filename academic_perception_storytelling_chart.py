import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def load_academic_perception_data(file_path="preprocessed_impact_by_job/E8_selfevaluation__s_performance_self_assessment__ES.xlsx"):
    """Cargar y procesar los datos de percepción académica"""
    
    # Leer el archivo Excel
    df = pd.read_excel(file_path)
    
    # Los datos están estructurados de forma especial, necesitamos procesarlos
    # Fila 0: Categorías de percepción académica (Better, Just as good, Worse)
    # Fila 1: Metadatos (Value, Unit, Count)
    # Fila 2: Datos de España
    
    # Crear estructura de datos procesada
    work_relation_levels = [
        'very closely',     # Muy relacionado
        'closely',          # Relacionado
        'in between',       # Intermedio
        'not closely',      # Poco relacionado
        'not closely at all' # Nada relacionado
    ]
    
    academic_perception_categories = ['Better', 'Just as good', 'Worse']
    
    # Extraer datos para cada nivel de relación trabajo-estudio
    processed_data = []
    
    for work_level in work_relation_levels:
        # Encontrar las columnas correspondientes a este nivel
        work_col_idx = df.columns.tolist().index(work_level)
        
        # Extraer datos para las tres categorías de percepción
        for i, perception in enumerate(academic_perception_categories):
            # Los datos están en grupos de 3 columnas: Value, Unit, Count
            value_col_idx = work_col_idx + (i * 3)
            count_col_idx = work_col_idx + (i * 3) + 2
            
            if value_col_idx < len(df.columns) and count_col_idx < len(df.columns):
                # Obtener el valor (porcentaje) y el conteo de la fila de datos (fila 2)
                percentage = df.iloc[2, value_col_idx]
                count = df.iloc[2, count_col_idx]
                
                # Agregar al dataset procesado
                processed_data.append({
                    'work_relation_level': work_level,
                    'academic_perception': perception,
                    'percentage': float(percentage) if pd.notna(percentage) else 0,
                    'count': int(count) if pd.notna(count) else 0
                })
    
    return pd.DataFrame(processed_data)

def create_academic_perception_chart():
    """Crear gráfico de percepción académica personal según relación trabajo-estudio"""
    
    # Cargar datos procesados
    df = load_academic_perception_data()
    
    # Definir colores consistentes con el storytelling
    colors = {
        'Better': '#27AE60',      # Verde para "mejor"
        'Just as good': '#F39C12', # Naranja para "igual de bien"  
        'Worse': '#E74C3C'        # Rojo para "peor"
    }
    
    # Crear gráfico de barras agrupadas
    fig = go.Figure()
    
    # Ordenar niveles de relación trabajo-estudio (de más a menos relacionado)
    work_levels_ordered = [
        'very closely',
        'closely', 
        'in between',
        'not closely',
        'not closely at all'
    ]
    
    # Etiquetas más legibles para el gráfico
    work_labels = {
        'very closely': 'Muy relacionado',
        'closely': 'Relacionado',
        'in between': 'Intermedio', 
        'not closely': 'Poco relacionado',
        'not closely at all': 'Nada relacionado'
    }
    
    # Crear una serie para cada categoría de percepción académica
    for perception in ['Better', 'Just as good', 'Worse']:
        # Filtrar datos para esta percepción
        data_subset = df[df['academic_perception'] == perception]
        
        # Ordenar datos según el orden de niveles de relación
        data_subset = data_subset.set_index('work_relation_level').reindex(work_levels_ordered).reset_index()
        
        # Crear etiquetas para el eje X
        x_labels = [work_labels[level] for level in data_subset['work_relation_level']]
        
        # Mapear nombre de percepción a español
        perception_spanish = {
            'Better': 'Mejor rendimiento',
            'Just as good': 'Mismo rendimiento', 
            'Worse': 'Peor rendimiento'
        }
        
        fig.add_trace(go.Bar(
            x=x_labels,
            y=data_subset['percentage'],
            name=perception_spanish[perception],
            marker_color=colors[perception],
            opacity=0.8,
            text=[f"{val:.1f}%" for val in data_subset['percentage']],
            textposition='outside',
            textfont=dict(size=10, color='#000000')
        ))
    
    # Configurar layout del gráfico
    fig.update_layout(
        title={
            'text': '<b>Percepción Académica Personal según Relación Trabajo-Estudio</b><br><sub>España - "¿Cómo consideras que tu trabajo afecta tu rendimiento académico?"</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#000000'}
        },
        xaxis_title="Nivel de Relación entre Trabajo y Estudios",
        yaxis_title="Porcentaje de Estudiantes (%)",
        barmode='group',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'color': '#000000'},
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom", 
            y=1,
            xanchor="right",
            x=1,
            font={'color': '#000000'}
        ),
        margin=dict(t=120, l=60, r=50, b=80),
        height=500
    )
    
    # Estilo de ejes consistente con el storytelling
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        linecolor='#000000',
        tickangle=45,
        title_font={'color': '#000000'},
        tickfont={'color': '#000000'}
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)', 
        linecolor='#000000',
        range=[0, max(df['percentage']) * 1.1],  # Ajustar rango Y
        title_font={'color': '#000000'},
        tickfont={'color': '#000000'}
    )
    
    return fig, df

def create_streamlit_academic_perception_chart():
    """Versión optimizada para Streamlit"""
    fig, df = create_academic_perception_chart()
    
    # Ajustes específicos para Streamlit
    fig.update_layout(
        height=550,
        margin=dict(t=100, l=50, r=50, b=100),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.8,
            xanchor="right", 
            x=1,
            font={'color': '#000000'}
        )
    )
    
    return fig, df

def get_academic_perception_insights(df):
    """Generar insights clave del análisis"""
    
    insights = {}
    
    # Encontrar el nivel con mejor percepción académica
    better_data = df[df['academic_perception'] == 'Better']
    best_relation_level = better_data.loc[better_data['percentage'].idxmax(), 'work_relation_level']
    best_percentage = better_data['percentage'].max()
    
    # Encontrar el nivel con peor percepción académica
    worse_data = df[df['academic_perception'] == 'Worse']
    worst_relation_level = worse_data.loc[worse_data['percentage'].idxmax(), 'work_relation_level']
    worst_percentage = worse_data['percentage'].max()
    
    # Calcular diferencia entre muy relacionado y nada relacionado para "Better"
    very_closely_better = df[(df['work_relation_level'] == 'very closely') & 
                           (df['academic_perception'] == 'Better')]['percentage'].iloc[0]
    not_at_all_better = df[(df['work_relation_level'] == 'not closely at all') & 
                         (df['academic_perception'] == 'Better')]['percentage'].iloc[0]
    
    insights = {
        'best_relation_level': best_relation_level,
        'best_percentage': best_percentage,
        'worst_relation_level': worst_relation_level, 
        'worst_percentage': worst_percentage,
        'very_closely_better': very_closely_better,
        'not_at_all_better': not_at_all_better,
        'difference_very_vs_none': very_closely_better - not_at_all_better,
        'total_students': df['count'].sum()
    }
    
    return insights

# Función principal para usar en el storytelling
def generate_academic_perception_analysis():
    """Función principal para integrar en el storytelling"""
    try:
        fig, df = create_streamlit_academic_perception_chart()
        insights = get_academic_perception_insights(df)
        return fig, insights
    except Exception as e:
        print(f"Error generando análisis de percepción académica: {e}")
        return None, None

# Test del script
if __name__ == "__main__":
    fig, insights = generate_academic_perception_analysis()
    if fig:
        fig.show()
        print("Gráfico creado exitosamente")
        print("Insights clave:", insights)
    else:
        print("Error creando el gráfico") 