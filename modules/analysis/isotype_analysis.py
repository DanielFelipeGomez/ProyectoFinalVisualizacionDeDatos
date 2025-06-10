import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
# Importar configuración unificada de colores
from ..core.color_config import STORYTELLING_COLORS, apply_standard_layout

def load_age_relationship_data():
    """
    Cargar y procesar datos de relación trabajo-estudio por edad en España
    """
    try:
        # Cargar el archivo Excel
        df = pd.read_excel("data/preprocessed_relationship_study_job/E8_age__relationship_job_study__ES.xlsx")
        
        print("Columnas disponibles:")
        print(df.columns.tolist())
        print("\nPrimeras filas:")
        print(df.head())
        print("\nForma del dataset:")
        print(df.shape)
        
        return df
        
    except Exception as e:
        print(f"Error cargando datos: {e}")
        return None

def create_age_isotype_chart():
    """
    Crear un isotype (gráfico con iconos) mostrando por edad 
    los estudiantes con trabajos NO relacionados con sus estudios
    """
    try:
        # Cargar datos
        df = load_age_relationship_data()
        if df is None:
            return None, {"error": "No se pudieron cargar los datos"}
        
        # Extraer datos de "not closely at all" (nada relacionado) por edad
        # Fila 2 contiene los datos de España (ES)
        data_row = df.iloc[2]
        
        # Extraer percentages para cada grupo de edad para "not closely at all"
        age_data = {
            "< 22 años": float(data_row['not closely at all']),  # 35.2%
            "22-24 años": float(data_row['Unnamed: 52']),        # 22.2%
            "25-29 años": float(data_row['Unnamed: 55']),        # 15.5%
            "30+ años": float(data_row['Unnamed: 58'])           # 27%
        }
        
        print("Datos extraídos (trabajo nada relacionado por edad):")
        for age, pct in age_data.items():
            print(f"{age}: {pct}%")
        
        # Crear isotype con figuras humanas
        fig = create_human_isotype(age_data)
        
        # Retornar información útil
        insights = {
            "age_data": age_data,
            "total_students_unrelated": sum(age_data.values()),
            "highest_group": max(age_data, key=age_data.get),
            "lowest_group": min(age_data, key=age_data.get)
        }
        
        return fig, insights
        
    except Exception as e:
        print(f"Error creando isotype: {e}")
        return None, {"error": str(e)}

def create_human_isotype(age_data):
    """
    Crear un gráfico isotype con figuras humanas representando los porcentajes
    """
    
    # Colores para cada grupo de edad
    colors = {
        "< 22 años": "#E74C3C",     # Rojo fuerte - mayor impacto
        "22-24 años": "#F39C12",    # Naranja
        "25-29 años": "#3498DB",    # Azul
        "30+ años": "#9B59B6"       # Morado
    }
    
    # Iconos Unicode para representar personas - usando diferentes iconos para cada edad
    person_icons = {
        "< 22 años": "👦🏽",     # Estudiante joven
        "22-24 años": "👱🏻‍♂️",       # Persona adulta joven  
        "25-29 años": "🧔🏻‍♂️",     # Profesional
        "30+ años": "👴🏼"        # Adulto maduro
    }
    
    # Crear figura única
    fig = go.Figure()
    
    # Configuración para organizar todos los iconos juntos
    icons_per_row = 6  # Menos iconos por fila para hacer más cuadrado
    current_x = 0
    current_y = 0
    icons_in_current_row = 0  # Contador simple para la fila actual
    
    # Procesar cada grupo de edad
    for age_group, percentage in age_data.items():
        # Calcular número de iconos a mostrar (cada icono representa ~2.5%)
        num_icons = max(1, int(percentage / 2.5))
        num_icons = min(num_icons, 20)  # Máximo 20 iconos para evitar overflow
        
        x_positions = []
        y_positions = []
        
        # Posicionar iconos en secuencia con menos espaciado
        for icon_idx in range(num_icons):
            x_positions.append(current_x)
            y_positions.append(current_y)
            
            current_x += 0.3  # Espaciado horizontal muy pequeño entre columnas
            icons_in_current_row += 1
            
            # Saltar a nueva fila cuando llegamos al límite
            if icons_in_current_row >= icons_per_row:
                current_x = 0
                current_y -= 0.7  # Reducir espaciado vertical
                icons_in_current_row = 0
        
        # Añadir scatter plot para este grupo
        fig.add_trace(
            go.Scatter(
                x=x_positions,
                y=y_positions,
                mode='text',  # Solo texto, sin markers
                text=[person_icons[age_group]] * num_icons,
                textfont=dict(size=40, color=colors[age_group]),  # Iconos grandes y con color
                showlegend=False,
                name=f"{age_group}: {percentage}%",
                hovertemplate=f"<b>{age_group}</b><br>" +
                             f"Trabajo nada relacionado: <b>{percentage}%</b><br>" +
                             f"Cada {person_icons[age_group]} ≈ 2.5% de estudiantes<br>" +
                             "<extra></extra>"
            )
        )
    
    # Configurar ejes únicos con rangos centrados
    # Calcular el ancho real que ocupan los iconos
    real_width = (icons_per_row - 1) * 0.3  # Ancho real basado en espaciado actual
    total_range = (icons_per_row - 1) * 0.6 + 0.6  # Rango total que queremos mostrar
    center_offset = (total_range - real_width) / 2  # Calcular offset para centrar
    
    fig.update_xaxes(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[-center_offset, real_width + center_offset]  # Centrar el contenido
    )
    fig.update_yaxes(
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        range=[current_y - 0.5, 0.5]  # Ajustar al nuevo espaciado vertical
    )
    
    # Layout general
    fig.update_layout(
        title={
            'text': "Trabajos No Relacionados con los Estudios por Edad en España<br>" +
                   "<sub style='color: #7F8C8D; font-size: 14px;'>Cada figura representa ≈2.5% de estudiantes | Datos: trabajos 'nada relacionados' con estudios</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}  # Título más grande
        },
        height=600,  # Reducir altura ya que los iconos están más juntos
        width=180,   # Reducir ancho también
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2C3E50'),
        showlegend=False,
        annotations=[
            dict(
                text="<b>🔍 Leyenda de Iconos:</b><br>" +
                     "<span style='color: #E74C3C;'>👦🏽 < 22 años (35.2%)</span> | " +
                     "<span style='color: #F39C12;'>👱🏻‍♂️ 22-24 años (22.2%)</span> | " +
                     "<span style='color: #3498DB;'>🧔🏻‍♂️ 25-29 años (15.5%)</span> | " +
                     "<span style='color: #9B59B6;'>👴🏼 30+ años (27.0%)</span>",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.5, y=-0.15,
                xanchor='center',
                font=dict(size=13, color='#2C3E50'),
                bgcolor="rgba(248, 249, 250, 0.9)",
                bordercolor="#DEE2E6",
                borderwidth=1,
                borderpad=12
            )
        ]
    )
    
    return fig

def create_age_isotype_for_streamlit():
    """
    Función optimizada para Streamlit que genera el isotype de edad
    """
    fig, insights = create_age_isotype_chart()
    
    return {
        'figure': fig,
        'insights': insights,
        'success': fig is not None
    }

if __name__ == "__main__":
    # Test de la función
    result = create_age_isotype_for_streamlit()
    print("Resultado:", result['success'])
    if result['insights']:
        print("Insights:", result['insights']) 