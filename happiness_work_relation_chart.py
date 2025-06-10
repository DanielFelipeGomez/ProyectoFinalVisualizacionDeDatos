import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def load_happiness_work_relation_data(file_path="preprocessed_relationship_study_job/E8_happiness_5__s_relationship_job_study__all_contries_not_spain.xlsx"):
    """Cargar y procesar los datos de felicidad según relación trabajo-estudio"""
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(file_path)
        
        # La estructura es:
        # Fila 0: Niveles de felicidad (Extremely happy, Very happy, etc.)
        # Fila 1: Metadatos (Value, Unit, Count)
        # Fila 2+: Datos por país
        
        # Definir niveles de relación trabajo-estudio
        work_relation_levels = ['very closely', 'closely', 'in between', 'not closely', 'not closely at all']
        
        # Niveles de felicidad esperados
        happiness_levels = ['Extremely happy', 'Very happy', 'Fairly happy', 'Not very happy', 'Extremely unhappy']
        
        processed_data = []
        
        # Procesar para cada nivel de relación trabajo-estudio
        for work_level in work_relation_levels:
            if work_level in df.columns:
                # Encontrar el índice de la columna principal
                work_col_idx = df.columns.get_loc(work_level)
                
                # Procesar cada nivel de felicidad (cada 3 columnas: Value, Unit, Count)
                for i, happiness_level in enumerate(happiness_levels):
                    value_col_idx = work_col_idx + (i * 3)
                    
                    if value_col_idx < len(df.columns):
                        # Procesar cada país (desde fila 2)
                        for row_idx in range(2, len(df)):
                            country = df.iloc[row_idx, 0]  # Primera columna es Country
                            
                            if pd.notna(country) and country != 'Country':
                                value = df.iloc[row_idx, value_col_idx]
                                
                                # Convertir valor a float si es posible
                                if pd.notna(value) and value != 'n. a.' and isinstance(value, (int, float, str)):
                                    try:
                                        percentage = float(value)
                                        processed_data.append({
                                            'country': country,
                                            'work_relation_level': work_level,
                                            'happiness_level': happiness_level,
                                            'percentage': percentage
                                        })
                                    except (ValueError, TypeError):
                                        continue
        
        processed_df = pd.DataFrame(processed_data)
        
        if processed_df.empty:
            print("No se pudieron procesar datos válidos, usando datos de ejemplo")
            return create_example_happiness_data()
        
        print(f"Datos procesados: {len(processed_df)} registros")
        print("Muestra de datos:")
        print(processed_df.head(10))
        
        return processed_df
        
    except Exception as e:
        print(f"Error procesando datos: {e}")
        return create_example_happiness_data()

def load_happiness_students_work_data(file_path="preprocessed_relationship_study_job/E8_happiness_5__studients_work_or_not__all_contries.xlsx"):
    """Cargar y procesar los datos de felicidad según si los estudiantes trabajan o no"""
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(file_path)
        
        # Niveles de felicidad
        happiness_levels = ['Extremely happy', 'Very happy', 'Fairly happy', 'Not very happy', 'Extremely unhappy']
        
        processed_data = []
        
        # Estructura del archivo:
        # - Columnas 1-15: students without paid employment during the semester  
        # - Columnas 16-30: students working in paid job less than 20 hours per week
        # - Columnas 31-45: students working in paid job more than 20 hours per week
        # Cada grupo tiene 5 niveles de felicidad con 3 columnas cada uno (Value, Unit, Count)
        
        work_categories = [
            ('Sin trabajo', 1),  # Inicia en columna 1
            ('Trabajo < 20h', 16),  # Inicia en columna 16  
            ('Trabajo > 20h', 31)   # Inicia en columna 31
        ]
        
        # Procesar cada categoría de trabajo
        for work_category, start_col in work_categories:
            # Procesar cada nivel de felicidad (cada 3 columnas: Value, Unit, Count)
            for i, happiness_level in enumerate(happiness_levels):
                value_col_idx = start_col + (i * 3)  # Columnas: 1,4,7,10,13 / 16,19,22,25,28 / 31,34,37,40,43
                
                if value_col_idx < len(df.columns):
                    # Procesar cada país (desde fila 2)
                    for row_idx in range(2, len(df)):
                        country = df.iloc[row_idx, 0]  # Primera columna es Country
                        
                        if pd.notna(country) and country != 'Country':
                            value = df.iloc[row_idx, value_col_idx]
                            
                            # Convertir valor a float si es posible
                            if pd.notna(value) and value != 'n. a.' and isinstance(value, (int, float, str)):
                                try:
                                    percentage = float(value)
                                    processed_data.append({
                                        'country': country,
                                        'work_category': work_category,
                                        'happiness_level': happiness_level,
                                        'percentage': percentage
                                    })
                                except (ValueError, TypeError):
                                    continue
        
        processed_df = pd.DataFrame(processed_data)
        
        if processed_df.empty:
            print("No se pudieron procesar datos de estudiantes que trabajan/no trabajan")
            return None
        
        print(f"Datos de trabajo/no trabajo procesados: {len(processed_df)} registros")
        return processed_df
        
    except Exception as e:
        print(f"Error procesando datos de trabajo: {e}")
        return None

def create_example_happiness_data():
    """Crear datos de ejemplo para testing"""
    
    work_levels = ['very closely', 'closely', 'in between', 'not closely', 'not closely at all']
    happiness_levels = ['Extremely happy', 'Very happy', 'Fairly happy', 'Not very happy', 'Extremely unhappy']
    countries = ['Austria', 'Germany', 'France', 'Spain', 'Italy', 'Netherlands', 'Poland', 'Sweden']
    
    data = []
    for country in countries:
        for work_level in work_levels:
            # Simular distribución de felicidad
            # Más trabajo relacionado → distribución sesgada hacia felicidad alta
            if work_level == 'very closely':
                percentages = [35, 30, 25, 8, 2]
            elif work_level == 'closely':
                percentages = [25, 35, 30, 8, 2]
            elif work_level == 'in between':
                percentages = [15, 25, 35, 20, 5]
            elif work_level == 'not closely':
                percentages = [10, 20, 30, 30, 10]
            else:  # not closely at all
                percentages = [5, 15, 25, 35, 20]
            
            for happiness_level, percentage in zip(happiness_levels, percentages):
                # Agregar algo de variación aleatoria
                final_percentage = max(0, percentage + np.random.normal(0, 2))
                data.append({
                    'country': country,
                    'work_relation_level': work_level,
                    'happiness_level': happiness_level,
                    'percentage': final_percentage
                })
    
    return pd.DataFrame(data)

def calculate_happiness_score(df):
    """Calcular score promedio de felicidad por trabajo-estudio"""
    
    # Asignar pesos a niveles de felicidad
    happiness_weights = {
        'Extremely happy': 5,
        'Very happy': 4,
        'Fairly happy': 3,
        'Not very happy': 2,
        'Extremely unhappy': 1
    }
    
    # Calcular score ponderado para cada combinación país-trabajo
    scores = []
    
    for country in df['country'].unique():
        for work_level in df['work_relation_level'].unique():
            subset = df[(df['country'] == country) & (df['work_relation_level'] == work_level)]
            
            if not subset.empty:
                weighted_score = 0
                total_percentage = 0
                
                for _, row in subset.iterrows():
                    happiness_level = row['happiness_level']
                    percentage = row['percentage']
                    weight = happiness_weights.get(happiness_level, 3)
                    
                    weighted_score += (weight * percentage)
                    total_percentage += percentage
                
                if total_percentage > 0:
                    avg_score = weighted_score / total_percentage
                    scores.append({
                        'country': country,
                        'work_relation_level': work_level,
                        'happiness_score': avg_score
                    })
    
    return pd.DataFrame(scores)

def calculate_happiness_score_work_categories(df):
    """Calcular score promedio de felicidad por categoría de trabajo (sin trabajo, <20h, >20h)"""
    
    # Asignar pesos a niveles de felicidad
    happiness_weights = {
        'Extremely happy': 5,
        'Very happy': 4,
        'Fairly happy': 3,
        'Not very happy': 2,
        'Extremely unhappy': 1
    }
    
    # Calcular score ponderado para cada combinación país-categoría
    scores = []
    
    for country in df['country'].unique():
        for work_category in df['work_category'].unique():
            subset = df[(df['country'] == country) & (df['work_category'] == work_category)]
            
            if not subset.empty:
                weighted_score = 0
                total_percentage = 0
                
                for _, row in subset.iterrows():
                    happiness_level = row['happiness_level']
                    percentage = row['percentage']
                    weight = happiness_weights.get(happiness_level, 3)
                    
                    weighted_score += (weight * percentage)
                    total_percentage += percentage
                
                if total_percentage > 0:
                    avg_score = weighted_score / total_percentage
                    scores.append({
                        'country': country,
                        'work_category': work_category,
                        'happiness_score': avg_score
                    })
    
    return pd.DataFrame(scores)

def calculate_eu_average(df):
    """Calcular promedio de la Unión Europea"""
    
    # Calcular score de felicidad por país y trabajo
    scores_df = calculate_happiness_score(df)
    
    # Calcular promedio UE por nivel de relación trabajo-estudio
    eu_average = scores_df.groupby('work_relation_level')['happiness_score'].mean().reset_index()
    eu_average['country'] = 'EU Average'
    
    return eu_average

def calculate_eu_average_work_categories(df):
    """Calcular promedio de la UE para categorías de trabajo"""
    
    # Calcular score de felicidad por país y categoría de trabajo
    scores_df = calculate_happiness_score_work_categories(df)
    
    # Calcular promedio UE por categoría de trabajo
    eu_average = scores_df.groupby('work_category')['happiness_score'].mean().reset_index()
    eu_average['country'] = 'EU Average'
    
    return eu_average

def create_happiness_work_relation_chart():
    """Crear gráfico de felicidad según relación trabajo-estudio (promedio UE)"""
    
    # Cargar datos procesados
    df = load_happiness_work_relation_data()
    
    # Calcular promedio de la UE
    eu_avg = calculate_eu_average(df)
    
    # Ordenar niveles de relación trabajo-estudio (de más a menos relacionado)
    work_levels_ordered = [
        'very closely',
        'closely', 
        'in between',
        'not closely',
        'not closely at all'
    ]
    
    # Filtrar solo niveles que existen en los datos
    available_levels = [level for level in work_levels_ordered if level in eu_avg['work_relation_level'].values]
    eu_avg_filtered = eu_avg[eu_avg['work_relation_level'].isin(available_levels)]
    eu_avg_filtered = eu_avg_filtered.set_index('work_relation_level').reindex(available_levels).reset_index()
    
    # Etiquetas más legibles para el gráfico
    work_labels = {
        'very closely': 'Muy relacionado',
        'closely': 'Relacionado',
        'in between': 'Intermedio', 
        'not closely': 'Poco relacionado',
        'not closely at all': 'Nada relacionado'
    }
    
    # Crear etiquetas para el eje X
    x_labels = [work_labels.get(level, level) for level in eu_avg_filtered['work_relation_level']]
    
    # Definir colores consistentes con el storytelling - paleta Europa
    primary_blue = '#003DA5'  # Azul Europa principal
    
    # Crear gráfico de barras
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=x_labels,
        y=eu_avg_filtered['happiness_score'],
        name='Promedio Unión Europea',
        marker_color=primary_blue,
        opacity=0.8,
        text=[f"{val:.2f}" for val in eu_avg_filtered['happiness_score']],
        textposition='outside',
        textfont=dict(size=12, color='#000000', family='Arial Black'),
        marker=dict(
            line=dict(color='#002080', width=1.5)  # Borde más oscuro
        )
    ))
    
    # Configurar layout del gráfico
    fig.update_layout(
        title={
            'text': '<b>Nivel de Felicidad/Satisfacción según Relación Trabajo-Estudio</b><br><sub>Promedio Unión Europea - "¿Qué tan feliz/satisfecho te sientes con tu situación trabajo-estudio?"</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#000000', 'family': 'Arial'}
        },
        xaxis_title="Nivel de Relación entre Trabajo y Estudios",
        yaxis_title="Nivel de Felicidad/Satisfacción (1-5)",
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'color': '#000000', 'family': 'Arial'},
        showlegend=False,  # No necesitamos leyenda para una sola serie
        margin=dict(t=120, l=60, r=50, b=80),
        height=500
    )
    
    # Estilo de ejes consistente con el storytelling
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        linecolor='#000000',
        tickangle=45,
        title_font={'color': '#000000', 'size': 14},
        tickfont={'color': '#000000', 'size': 12}
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)', 
        linecolor='#000000',
        range=[0, 5.5],  # Escala 1-5 con margen
        title_font={'color': '#000000', 'size': 14},
        tickfont={'color': '#000000', 'size': 12}
    )
    
    return fig, eu_avg_filtered

def create_happiness_work_comparison_chart():
    """Crear gráfico comparativo de felicidad: relación trabajo-estudio vs sin trabajo"""
    
    # Cargar datos de relación trabajo-estudio
    df_work_relation = load_happiness_work_relation_data()
    eu_avg_work_relation = calculate_eu_average(df_work_relation)
    
    # Cargar datos de estudiantes que trabajan/no trabajan
    df_work_categories = load_happiness_students_work_data()
    
    if df_work_categories is None:
        print("No se pudieron cargar datos de trabajo/no trabajo, usando solo datos de relación trabajo-estudio")
        return create_happiness_work_relation_chart()
    
    eu_avg_work_categories = calculate_eu_average_work_categories(df_work_categories)
    
    # Preparar datos para el gráfico
    # Solo nos interesa el score de "Sin trabajo"
    no_work_score = eu_avg_work_categories[eu_avg_work_categories['work_category'] == 'Sin trabajo']['happiness_score'].iloc[0]
    
    # Ordenar niveles de relación trabajo-estudio
    work_levels_ordered = ['very closely', 'closely', 'in between', 'not closely', 'not closely at all']
    available_levels = [level for level in work_levels_ordered if level in eu_avg_work_relation['work_relation_level'].values]
    eu_avg_filtered = eu_avg_work_relation[eu_avg_work_relation['work_relation_level'].isin(available_levels)]
    eu_avg_filtered = eu_avg_filtered.set_index('work_relation_level').reindex(available_levels).reset_index()
    
    # Crear etiquetas
    work_labels = {
        'very closely': 'Muy relacionado',
        'closely': 'Relacionado', 
        'in between': 'Intermedio',
        'not closely': 'Poco relacionado',
        'not closely at all': 'Nada relacionado'
    }
    
    # Preparar datos para el gráfico
    x_labels = [work_labels.get(level, level) for level in eu_avg_filtered['work_relation_level']] + ['Sin trabajo']
    y_values = list(eu_avg_filtered['happiness_score']) + [no_work_score]
    
    # Colores: azules para niveles de trabajo, rojo para sin trabajo
    colors = ['#003DA5', '#1E4FBF', '#3A66D9', '#567DF3', '#7294FF', '#FF6B6B']
    
    # Crear gráfico
    fig = go.Figure()
    
    # Barras de estudiantes que trabajan (diferentes niveles de relación)
    fig.add_trace(go.Bar(
        x=x_labels[:-1],  # Todos excepto el último (Sin trabajo)
        y=y_values[:-1],
        name='Estudiantes que trabajan',
        marker_color=colors[:-1],
        opacity=0.8,
        text=[f"{val:.2f}" for val in y_values[:-1]],
        textposition='outside',
        textfont=dict(size=11, color='#000000', family='Arial Black'),
        marker=dict(line=dict(color='#002080', width=1.2)),
        showlegend=True
    ))
    
    # Barra de estudiantes sin trabajo
    fig.add_trace(go.Bar(
        x=[x_labels[-1]],  # Solo "Sin trabajo"
        y=[y_values[-1]],
        name='Estudiantes sin trabajo',
        marker_color=colors[-1],
        opacity=0.8,
        text=[f"{y_values[-1]:.2f}"],
        textposition='outside',
        textfont=dict(size=11, color='#000000', family='Arial Black'),
        marker=dict(line=dict(color='#CC5555', width=1.2)),
        showlegend=True
    ))
    
    # Configurar layout
    fig.update_layout(
        title={
            'text': '<b>Comparación: Felicidad según Relación Trabajo-Estudio vs Sin Trabajo</b><br><sub>Promedio Unión Europea - "¿Qué tan feliz/satisfecho te sientes?"</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#000000', 'family': 'Arial'}
        },
        xaxis_title="Situación Laboral/Académica",
        yaxis_title="Nivel de Felicidad/Satisfacción (1-5)",
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'color': '#000000', 'family': 'Arial'},
        showlegend=True,
        legend=dict(
            x=1,
            xanchor="right",
            y=1,
            yanchor="bottom",
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='rgba(0,0,0,0.3)',
            borderwidth=1,
            font=dict(color='#000000', size=12)
        ),
        margin=dict(t=120, l=60, r=50, b=100),
        height=550
    )
    
    # Estilo de ejes
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        linecolor='#000000',
        tickangle=45,
        title_font={'color': '#000000', 'size': 14},
        tickfont={'color': '#000000', 'size': 11}
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        linecolor='#000000',
        range=[0, 5.5],
        title_font={'color': '#000000', 'size': 14},
        tickfont={'color': '#000000', 'size': 12}
    )
    
    return fig, {'work_relation': eu_avg_filtered, 'work_categories': eu_avg_work_categories}

def create_streamlit_happiness_chart():
    """Versión optimizada para Streamlit con comparación trabajo vs sin trabajo"""
    fig, data = create_happiness_work_comparison_chart()
    
    # Ajustes específicos para Streamlit
    fig.update_layout(
        height=600,
        margin=dict(t=100, l=50, r=50, b=100)
    )
    
    return fig, data

def get_happiness_insights(data):
    """Generar insights clave del análisis de felicidad comparativo"""
    
    insights = {}
    
    # Si es el formato anterior (solo df), usar la lógica anterior
    if isinstance(data, pd.DataFrame):
        df = data
        # Lógica anterior para retrocompatibilidad
        max_happiness_idx = df['happiness_score'].idxmax()
        highest_happiness_level = df.loc[max_happiness_idx, 'work_relation_level']
        highest_happiness_score = df.loc[max_happiness_idx, 'happiness_score']
        
        min_happiness_idx = df['happiness_score'].idxmin()
        lowest_happiness_level = df.loc[min_happiness_idx, 'work_relation_level']
        lowest_happiness_score = df.loc[min_happiness_idx, 'happiness_score']
        
        insights = {
            'highest_happiness_level': highest_happiness_level,
            'highest_happiness_score': highest_happiness_score,
            'lowest_happiness_level': lowest_happiness_level,
            'lowest_happiness_score': lowest_happiness_score,
            'total_levels': len(df)
        }
        return insights
    
    # Nueva lógica para datos comparativos
    work_relation_df = data['work_relation']
    work_categories_df = data['work_categories']
    
    # Insights de relación trabajo-estudio
    max_work_idx = work_relation_df['happiness_score'].idxmax()
    highest_work_level = work_relation_df.loc[max_work_idx, 'work_relation_level']
    highest_work_score = work_relation_df.loc[max_work_idx, 'happiness_score']
    
    min_work_idx = work_relation_df['happiness_score'].idxmin()
    lowest_work_level = work_relation_df.loc[min_work_idx, 'work_relation_level']
    lowest_work_score = work_relation_df.loc[min_work_idx, 'happiness_score']
    
    # Score de estudiantes sin trabajo
    no_work_data = work_categories_df[work_categories_df['work_category'] == 'Sin trabajo']
    no_work_score = no_work_data['happiness_score'].iloc[0] if not no_work_data.empty else None
    
    # Comparaciones clave
    very_closely_data = work_relation_df[work_relation_df['work_relation_level'] == 'very closely']
    very_closely_score = very_closely_data['happiness_score'].iloc[0] if not very_closely_data.empty else None
    
    # Diferencia entre trabajo muy relacionado vs sin trabajo
    work_vs_no_work_diff = None
    if very_closely_score is not None and no_work_score is not None:
        work_vs_no_work_diff = very_closely_score - no_work_score
    
    # Promedio general de estudiantes que trabajan
    avg_working_score = work_relation_df['happiness_score'].mean()
    
    insights = {
        'highest_work_level': highest_work_level,
        'highest_work_score': highest_work_score,
        'lowest_work_level': lowest_work_level,
        'lowest_work_score': lowest_work_score,
        'no_work_score': no_work_score,
        'very_closely_score': very_closely_score,
        'work_vs_no_work_diff': work_vs_no_work_diff,
        'avg_working_score': avg_working_score,
        'total_work_levels': len(work_relation_df),
        'comparison_available': True
    }
    
    return insights

# Función principal para usar en el storytelling
def generate_happiness_work_relation_analysis():
    """Función principal para integrar en el storytelling con comparación trabajo vs sin trabajo"""
    try:
        fig, data = create_streamlit_happiness_chart()
        insights = get_happiness_insights(data)
        return fig, insights
    except Exception as e:
        print(f"Error generando análisis de felicidad trabajo-estudio: {e}")
        return None, None

# Test del script
if __name__ == "__main__":
    fig, insights = generate_happiness_work_relation_analysis()
    if fig:
        fig.show()
        print("Gráfico creado exitosamente")
        print("Insights clave:", insights)
    else:
        print("Error creando el gráfico") 