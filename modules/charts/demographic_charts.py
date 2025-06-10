import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from enum import Enum

# Clase para los datasets preprocessados
class PreprocessedDatasetsNamesWorkMotiveAffordStudy(Enum):
    WORK_MOTIVE_AFFORD_STUDY = 'data/preprocessed_excels/E8_work_motive_afford_study_5__all_students__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_SEX = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_sex__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_AGE = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_age__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_EDUPAR = 'data/preprocessed_excels/E8_edupar_5__s_works_to_afford_to_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS = 'data/preprocessed_excels/E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx'

# Importar configuración unificada de colores
from ..core.color_config import STORYTELLING_COLORS, COLOR_PALETTES, apply_standard_layout

def translate_age_category(category):
    """
    Traduce las categorías de edad del inglés al español
    """
    # Convertir a minúsculas para hacer comparaciones case-insensitive
    category_lower = category.lower().strip()
    
    # Casos específicos exactos basados en los datos reales
    if '< 22' in category_lower:
        return 'Menos de 22 años'
    elif '22 - 24' in category_lower or '22-24' in category_lower:
        return 'Entre 22 y 24 años'
    elif '25 - 29' in category_lower or '25-29' in category_lower:
        return 'Entre 25 y 29 años'
    elif '30 years and older' in category_lower or '30 and older' in category_lower:
        return '30 años o más'
    elif any(pattern in category_lower for pattern in ['30+', '>= 30', '30 and more', '30 or more', '30 and over']):
        return '30 años o más'
    elif any(pattern in category_lower for pattern in ['22+', '22 and more', '22 or more', '22 and over']):
        return '22 años o más'
    elif 'under 22' in category_lower or 'less than 22' in category_lower:
        return 'Menos de 22 años'
    else:
        # Si no coincide con ningún patrón específico, devolver traducción básica
        # Evitar múltiples reemplazos que causan errores
        if any(word in category_lower for word in ['year', 'años', 'age', 'edad']):
            # Ya contiene palabras relacionadas con edad, solo limpiar
            clean_category = category.replace('years old', 'años').replace('year old', 'año').replace('years', 'años').replace('year', 'año')
            return clean_category.strip()
        else:
            return category  # Devolver original si no se puede traducir

def translate_field_of_study_category(category):
    """
    Traduce las categorías de campos de estudio del inglés al español
    """
    # Convertir a minúsculas para hacer comparaciones case-insensitive
    category_lower = category.lower().strip()
    
    # Mapeo de campos de estudio más comunes
    field_translations = {
        # Artes y Humanidades
        'arts and humanities': 'Artes y Humanidades',
        'arts': 'Artes',
        'humanities': 'Humanidades',
        'fine arts': 'Bellas Artes',
        'literature': 'Literatura',
        'philosophy': 'Filosofía',
        'history': 'Historia',
        'languages': 'Idiomas',
        'foreign languages': 'Idiomas Extranjeros',
        'modern languages': 'Idiomas Modernos',
        
        # Ciencias Sociales
        'social sciences': 'Ciencias Sociales',
        'sociology': 'Sociología',
        'psychology': 'Psicología',
        'political science': 'Ciencias Políticas',
        'international relations': 'Relaciones Internacionales',
        'anthropology': 'Antropología',
        'geography': 'Geografía',
        
        # Negocios y Administración
        'business and administration': 'Negocios y Administración',
        'business': 'Negocios',
        'administration': 'Administración',
        'management': 'Gestión',
        'economics': 'Economía',
        'finance': 'Finanzas',
        'accounting': 'Contabilidad',
        'marketing': 'Marketing',
        
        # Derecho
        'law': 'Derecho',
        'legal studies': 'Estudios Jurídicos',
        
        # Ciencias Naturales
        'natural sciences': 'Ciencias Naturales',
        'mathematics': 'Matemáticas',
        'physics': 'Física',
        'chemistry': 'Química',
        'biology': 'Biología',
        'environmental science': 'Ciencias Ambientales',
        
        # Ingeniería y Tecnología
        'engineering': 'Ingeniería',
        'engineering and technology': 'Ingeniería y Tecnología',
        'computer science': 'Informática',
        'information technology': 'Tecnología de la Información',
        'civil engineering': 'Ingeniería Civil',
        'mechanical engineering': 'Ingeniería Mecánica',
        'electrical engineering': 'Ingeniería Eléctrica',
        'industrial engineering': 'Ingeniería Industrial',
        
        # Medicina y Salud
        'health and medicine': 'Salud y Medicina',
        'medicine': 'Medicina',
        'nursing': 'Enfermería',
        'pharmacy': 'Farmacia',
        'dentistry': 'Odontología',
        'veterinary': 'Veterinaria',
        'public health': 'Salud Pública',
        
        # Educación
        'education': 'Educación',
        'teacher training': 'Formación del Profesorado',
        'pedagogy': 'Pedagogía',
        
        # Agricultura
        'agriculture': 'Agricultura',
        'forestry': 'Silvicultura',
        'fisheries': 'Pesca',
        
        # Servicios
        'services': 'Servicios',
        'tourism': 'Turismo',
        'hospitality': 'Hostelería',
        'transport': 'Transporte',
        
        # Comunicación
        'communication': 'Comunicación',
        'journalism': 'Periodismo',
        'media studies': 'Estudios de Medios',
    }
    
    # Buscar coincidencias exactas primero
    for english_term, spanish_term in field_translations.items():
        if english_term == category_lower:
            return spanish_term
    
    # Buscar coincidencias parciales
    for english_term, spanish_term in field_translations.items():
        if english_term in category_lower:
            return spanish_term
    
    # Si no se encuentra traducción específica, hacer traducciones básicas
    translated = category
    basic_replacements = {
        ' programmes': '',
        ' programs': '',
        'programmes': '',
        'programs': '',
        ' and ': ' y ',
        'sciences': 'Ciencias',
        'studies': 'Estudios',
        'technology': 'Tecnología',
        'engineering': 'Ingeniería',
        'health': 'Salud',
        'social': 'Social',
        'natural': 'Natural',
        'applied': 'Aplicada',
        'general': 'General'
    }
    
    for english, spanish in basic_replacements.items():
        translated = translated.replace(english, spanish)
    
    # Capitalizar primera letra de cada palabra
    translated = ' '.join(word.capitalize() for word in translated.split())
    
    return translated

# Mantener compatibilidad con código existente
COLORS = {
    'spain': STORYTELLING_COLORS['spain'],
    'europe': STORYTELLING_COLORS['europe'], 
    'female': STORYTELLING_COLORS['female'],
    'male': STORYTELLING_COLORS['male'],
    'young': STORYTELLING_COLORS['young'],
    'older': STORYTELLING_COLORS['older'],
    'high_difficulty': STORYTELLING_COLORS['high_difficulty'],
    'low_difficulty': STORYTELLING_COLORS['low_difficulty'],
    'grid': STORYTELLING_COLORS['grid']
}

def read_demographic_dataset_detailed(dataset_enum):
    """
    Lee un dataset demográfico con todas sus subcategorías
    """
    df = pd.read_excel(dataset_enum.value, header=None)
    
    # Análisis de headers para identificar subcategorías
    header_row_1 = df.iloc[0].fillna('').tolist()  # Primera fila de headers
    header_row_2 = df.iloc[1].fillna('').tolist()  # Segunda fila de headers
    
    # Los datos empiezan en la fila 3
    data_df = df.iloc[3:].copy()
    
    # Identificar las subcategorías demográficas
    subcategories = []
    current_category = None
    
    for i, (h1, h2) in enumerate(zip(header_row_1, header_row_2)):
        if h1 and h1 != 'Country':  # Nueva subcategoría encontrada
            current_category = h1
            subcategories.append((i, current_category))
    
    # Para cada subcategoría, extraer los datos de España vs promedio europeo
    results = {}
    
    for start_col, category_name in subcategories:
        # Extraer las 15 columnas que corresponden a esta subcategoría
        # (5 niveles × 3 columnas cada uno: Value, Unit, Count)
        end_col = start_col + 15
        
        if end_col <= data_df.shape[1]:
            category_data = data_df.iloc[:, [0] + list(range(start_col, end_col))].copy()
            
            # Nombrar las columnas
            column_names = ['Country']
            response_levels = ['Applies_Totally', 'Applies_Rather', 'Applies_Partially', 
                             'Applies_Rather_Not', 'Does_Not_Apply']
            
            for level in response_levels:
                column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
            
            category_data.columns = column_names
            category_data = category_data.reset_index(drop=True)
            category_data = category_data.dropna(subset=['Country'])
            
            # Convertir columnas numéricas
            for level in response_levels:
                value_col = f'{level}_Value'
                if value_col in category_data.columns:
                    category_data[value_col] = pd.to_numeric(category_data[value_col], errors='coerce')
            
            results[category_name] = category_data
    
    return results

def create_gender_comparison_chart():
    """
    Crea un gráfico comparativo específico por género
    """
    gender_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_SEX
    )
    
    if 'Female' not in gender_data or 'Male' not in gender_data:
        # Si no tenemos datos separados por género, crear un gráfico básico
        return create_basic_demographic_chart("Análisis por Género", "No se encontraron datos separados por género")
    
    # Extraer datos de España para hombres y mujeres
    female_spain = gender_data['Female'][gender_data['Female']['Country'] == 'ES']
    male_spain = gender_data['Male'][gender_data['Male']['Country'] == 'ES']
    
    if female_spain.empty or male_spain.empty:
        return create_basic_demographic_chart("Análisis por Género", "No se encontraron datos de España")
    
    # Calcular necesidad total de trabajar
    female_spain_need = (female_spain.iloc[0]['Applies_Totally_Value'] + 
                        female_spain.iloc[0]['Applies_Rather_Value'] + 
                        female_spain.iloc[0]['Applies_Partially_Value'])
    
    male_spain_need = (male_spain.iloc[0]['Applies_Totally_Value'] + 
                      male_spain.iloc[0]['Applies_Rather_Value'] + 
                      male_spain.iloc[0]['Applies_Partially_Value'])
    
    # Promedios europeos por género
    female_europe = gender_data['Female'][gender_data['Female']['Country'] != 'ES']
    male_europe = gender_data['Male'][gender_data['Male']['Country'] != 'ES']
    
    female_europe_need = (female_europe['Applies_Totally_Value'].fillna(0) + 
                         female_europe['Applies_Rather_Value'].fillna(0) + 
                         female_europe['Applies_Partially_Value'].fillna(0)).mean()
    
    male_europe_need = (male_europe['Applies_Totally_Value'].fillna(0) + 
                       male_europe['Applies_Rather_Value'].fillna(0) + 
                       male_europe['Applies_Partially_Value'].fillna(0)).mean()
    
    # Crear el gráfico
    fig = go.Figure()
    
    categories = ['Mujeres', 'Hombres']
    spain_values = [female_spain_need, male_spain_need]
    europe_values = [female_europe_need, male_europe_need]
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[x[0] - width/2, x[1] - width/2],
        y=spain_values,
        marker_color=COLORS['spain'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{x}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in spain_values],
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[x[0] + width/2, x[1] + width/2],
        y=europe_values,
        marker_color=COLORS['europe'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{x}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in europe_values],
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Género</b><br><i>España vs Promedio Europeo</i>',
        height=600,
        width=800
    )
    
    fig.update_layout(
        xaxis_title='Género',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1,
            font=dict(color='#000000')  # Leyenda en negro
        )
    )
    
    fig.update_xaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    # Configurar las etiquetas del eje X
    fig.update_xaxes(
        tickvals=x,
        ticktext=categories,  # Usar las categorías ['Mujeres', 'Hombres']
        tickfont=dict(color='black')  # Etiquetas en negro
    )
    fig.update_yaxes(
        tickfont=dict(color='black')  # Etiquetas del eje Y en negro
    )
    
    return fig

def create_age_comparison_chart():
    """
    Crea un gráfico comparativo específico por edad
    """
    age_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_AGE
    )
    
    if not age_data:
        return create_basic_demographic_chart("Análisis por Edad", "No se encontraron datos de edad")
    
    # Obtener las categorías de edad disponibles
    age_categories = list(age_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in age_categories:
        spain_row = age_data[category][age_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = age_data[category][age_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            # Traducir categorías de edad al español
            translated_category = translate_age_category(category)
            category_names.append(translated_category)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Edad", "No se encontraron datos de España por edad")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=COLORS['spain'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{x}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in spain_data],
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=COLORS['europe'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{x}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=[f'{val:.1f}%' for val in europe_data],
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Edad</b><br><i>España vs Promedio Europeo</i>',
        height=600,
        width=1000
    )
    
    fig.update_layout(
        xaxis_title='Grupo de Edad',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1,
            font=dict(color='black')  # Leyenda en negro
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=[name.replace(' años', '<br>años') for name in category_names],  # Salto de línea solo antes de "años"
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_basic_demographic_chart(title, message):
    """
    Crea un gráfico básico cuando no hay datos específicos disponibles
    """
    fig = go.Figure()
    
    fig.add_annotation(
        text=message,
        xref="paper", yref="paper",
        x=0.5, y=0.5,
        showarrow=False,
        font=dict(size=16, color=STORYTELLING_COLORS['text'])
    )
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title=f'<b>{title}</b>',
        height=400,
        width=600
    )
    
    fig.update_layout(showlegend=False)
    
    return fig

def create_field_of_study_comparison_chart():
    """
    Crea un gráfico comparativo específico por campo de estudio
    """
    field_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY
    )
    
    if not field_data:
        return create_basic_demographic_chart("Análisis por Campo de Estudio", "No se encontraron datos de campo de estudio")
    
    # Obtener las categorías de campo de estudio disponibles
    field_categories = list(field_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in field_categories:
        spain_row = field_data[category][field_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = field_data[category][field_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            # Traducir nombres al español para mejor visualización
            translated_name = translate_field_of_study_category(category)
            # Si el nombre traducido es muy largo, acortarlo
            if len(translated_name) > 25:
                translated_name = translated_name[:22] + "..."
            category_names.append(translated_name)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Campo de Estudio", "No se encontraron datos de España")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Preparar textos para hover (nombres traducidos completos)
    translated_full_names = [translate_field_of_study_category(cat) for cat in field_categories]
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=COLORS['spain'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=translated_full_names,  # Nombres traducidos completos en hover
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=COLORS['europe'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=translated_full_names,  # Nombres traducidos completos en hover
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Campo de Estudio</b><br><i>España vs Promedio Europeo</i>',
        height=700,
        width=1200
    )
    
    fig.update_layout(
        xaxis_title='Campo de Estudio',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=[name.replace(' ', '<br>') for name in category_names],
        tickangle=45,
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_financial_difficulties_comparison_chart():
    """
    Crea un gráfico comparativo específico por dificultades financieras
    """
    financial_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES
    )
    
    if not financial_data:
        return create_basic_demographic_chart("Análisis por Dificultades Financieras", "No se encontraron datos")
    
    # Obtener las categorías de dificultades financieras
    financial_categories = list(financial_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in financial_categories:
        spain_row = financial_data[category][financial_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = financial_data[category][financial_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            category_names.append(category)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Dificultades Financieras", "No se encontraron datos de España")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Colores especiales para dificultades financieras
    colors_spain = [COLORS['high_difficulty'] if 'high' in cat.lower() or 'severe' in cat.lower() 
                   else COLORS['spain'] for cat in category_names]
    colors_europe = [COLORS['high_difficulty'] if 'high' in cat.lower() or 'severe' in cat.lower() 
                    else COLORS['europe'] for cat in category_names]
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=colors_spain,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=colors_europe,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    fig.update_layout(
        title={
            'text': '<b>Necesidad de Trabajar por Dificultades Financieras</b><br><i>España vs Promedio Europeo</i>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2c3e50'}
        },
        xaxis_title='Nivel de Dificultades Financieras',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=600,
        width=1000,
        font=dict(family="Arial", size=12, color='#2c3e50'),
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=[name.replace(' ', '<br>') for name in category_names],
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        linecolor=STORYTELLING_COLORS['border'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        linecolor=STORYTELLING_COLORS['border'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_living_with_parents_comparison_chart():
    """
    Crea un gráfico comparativo específico por situación de vivienda con padres
    """
    living_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS
    )
    
    if not living_data:
        return create_basic_demographic_chart("Análisis por Situación de Vivienda", "No se encontraron datos")
    
    # Obtener las categorías disponibles
    living_categories = list(living_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in living_categories:
        spain_row = living_data[category][living_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = living_data[category][living_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            # Traducir nombres para mejor visualización
            if category == 'Not living with parents':
                simplified_name = 'Viven Independientes'
            elif category == 'Living with parents':
                simplified_name = 'Viven con Padres'
            elif 'not living' in category.lower():
                simplified_name = 'Viven Independientes'
            elif 'living with' in category.lower():
                simplified_name = 'Viven con Padres'
            else:
                # Para cualquier otra categoría, usar nombre completo traducido
                simplified_name = category.replace('parents', 'padres').replace('living', 'viviendo')
            category_names.append(simplified_name)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Situación de Vivienda", "No se encontraron datos de España")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=COLORS['spain'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=COLORS['europe'],
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Situación de Vivienda</b><br><i>España vs Promedio Europeo</i>',
        height=600,
        width=800
    )
    
    fig.update_layout(
        xaxis_title='Situación de Vivienda',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1,
            font=dict(color='black')  # Leyenda en negro
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=category_names,
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        linecolor=STORYTELLING_COLORS['border'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        linecolor=STORYTELLING_COLORS['border'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_parents_financial_status_comparison_chart():
    """
    Crea un gráfico comparativo específico por estado financiero de los padres
    """
    parents_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS
    )
    
    if not parents_data:
        return create_basic_demographic_chart("Análisis por Estado Financiero de Padres", "No se encontraron datos")
    
    # Obtener las categorías disponibles
    parents_categories = list(parents_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in parents_categories:
        spain_row = parents_data[category][parents_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = parents_data[category][parents_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            # Traducir nombres al español para mejor visualización
            if 'not at all well-off' in category:
                simplified_name = 'Situación Financiera Baja'
            elif 'not very well-off' in category:
                simplified_name = 'Situación Financiera Media-Baja'
            elif 'average' in category:
                simplified_name = 'Situación Financiera Media'
            elif 'somewhat well-off' in category:
                simplified_name = 'Situación Financiera Media-Alta'
            elif 'very well-off' in category:
                simplified_name = 'Situación Financiera Alta'
            else:
                # Para cualquier otra categoría no esperada, usar el nombre original
                simplified_name = category.replace('financial status', 'Situación Financiera').replace('parents', 'Padres').strip()
            category_names.append(simplified_name)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Estado Financiero de Padres", "No se encontraron datos de España")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Colores según el nivel financiero
    colors_spain = []
    colors_europe = []
    for cat in category_names:
        if any(word in cat.lower() for word in ['low', 'poor', 'bajo']):
            colors_spain.append(COLORS['high_difficulty'])
            colors_europe.append(COLORS['high_difficulty'])
        elif any(word in cat.lower() for word in ['high', 'wealthy', 'alto']):
            colors_spain.append(COLORS['low_difficulty'])
            colors_europe.append(COLORS['low_difficulty'])
        else:
            colors_spain.append(COLORS['spain'])
            colors_europe.append(COLORS['europe'])
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=colors_spain,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=colors_europe,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Estado Financiero de los Padres</b><br><i>España vs Promedio Europeo</i>',
        height=600,
        width=1000
    )
    
    fig.update_layout(
        xaxis_title='Estado Financiero de los Padres',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#000000')  # Leyenda en negro
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=[name.replace(' ', '<br>') for name in category_names],
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_parents_education_comparison_chart():
    """
    Crea un gráfico comparativo específico por nivel educativo de los padres
    """
    parents_education_data = read_demographic_dataset_detailed(
        PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_EDUPAR
    )
    
    if not parents_education_data:
        return create_basic_demographic_chart("Análisis por Nivel Educativo de Padres", "No se encontraron datos")
    
    # Obtener las categorías disponibles
    education_categories = list(parents_education_data.keys())
    
    spain_data = []
    europe_data = []
    category_names = []
    
    for category in education_categories:
        spain_row = parents_education_data[category][parents_education_data[category]['Country'] == 'ES']
        if not spain_row.empty:
            spain_need = (spain_row.iloc[0]['Applies_Totally_Value'] + 
                         spain_row.iloc[0]['Applies_Rather_Value'] + 
                         spain_row.iloc[0]['Applies_Partially_Value'])
            spain_data.append(spain_need)
            
            # Promedio europeo para esta categoría
            europe_rows = parents_education_data[category][parents_education_data[category]['Country'] != 'ES']
            europe_need = (europe_rows['Applies_Totally_Value'].fillna(0) + 
                          europe_rows['Applies_Rather_Value'].fillna(0) + 
                          europe_rows['Applies_Partially_Value'].fillna(0)).mean()
            europe_data.append(europe_need)
            
            # Traducir nombres al español para mejor visualización
            if 'primary' in category.lower() or 'basic' in category.lower():
                simplified_name = 'Educación Primaria'
            elif 'secondary' in category.lower() or 'high school' in category.lower():
                simplified_name = 'Educación Secundaria'
            elif 'vocational' in category.lower() or 'professional' in category.lower():
                simplified_name = 'Formación Profesional'
            elif 'bachelor' in category.lower() or 'university' in category.lower():
                simplified_name = 'Educación Universitaria'
            elif 'master' in category.lower() or 'postgraduate' in category.lower():
                simplified_name = 'Estudios de Máster'
            elif 'phd' in category.lower() or 'doctorate' in category.lower():
                simplified_name = 'Estudios de Doctorado'
            elif 'no education' in category.lower() or 'none' in category.lower():
                simplified_name = 'Sin Educación Formal'
            else:
                # Para cualquier otra categoría no esperada, usar el nombre original simplificado
                simplified_name = category.replace('education', 'Educación').replace('level', 'Nivel').strip()
            category_names.append(simplified_name)
    
    if not spain_data:
        return create_basic_demographic_chart("Análisis por Nivel Educativo de Padres", "No se encontraron datos de España")
    
    # Crear el gráfico
    fig = go.Figure()
    
    x = np.arange(len(category_names))
    width = 0.35
    
    # Colores según el nivel educativo (correlación inversa con necesidad de trabajar)
    colors_spain = []
    colors_europe = []
    for cat in category_names:
        if any(word in cat.lower() for word in ['primaria', 'sin educación', 'none', 'basic']):
            colors_spain.append(COLORS['high_difficulty'])  # Rojo para educación baja
            colors_europe.append(COLORS['high_difficulty'])
        elif any(word in cat.lower() for word in ['doctorado', 'máster', 'phd', 'postgraduate']):
            colors_spain.append(COLORS['low_difficulty'])   # Verde para educación alta
            colors_europe.append(COLORS['low_difficulty'])
        elif any(word in cat.lower() for word in ['universitaria', 'bachelor', 'university']):
            colors_spain.append(STORYTELLING_COLORS['europe']) # Azul para educación universitaria
            colors_europe.append(STORYTELLING_COLORS['europe'])
        else:
            colors_spain.append(COLORS['spain'])  # Color por defecto
            colors_europe.append(COLORS['europe'])
    
    # Barras de España
    fig.add_trace(go.Bar(
        name='España',
        x=[i - width/2 for i in x],
        y=spain_data,
        marker_color=colors_spain,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>España - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Barras de Europa
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=[i + width/2 for i in x],
        y=europe_data,
        marker_color=colors_europe,
        marker_line=dict(color='white', width=2),
        hovertemplate='<b>Promedio Europeo - %{text}</b><br>Necesidad de trabajar: %{y:.1f}%<extra></extra>',
        text=category_names,
        textposition='outside',
        width=width
    ))
    
    # Aplicar layout estándar
    fig = apply_standard_layout(
        fig, 
        title='<b>Necesidad de Trabajar por Nivel Educativo de los Padres</b><br><i>España vs Promedio Europeo</i>',
        height=600,
        width=1000
    )
    
    fig.update_layout(
        xaxis_title='Nivel Educativo de los Padres',
        yaxis_title='Porcentaje que necesita trabajar (%)',
        barmode='group',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#000000')  # Leyenda en negro
        )
    )
    
    fig.update_xaxes(
        tickvals=x,
        ticktext=[name.replace(' ', '<br>') for name in category_names],
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    fig.update_yaxes(
        showgrid=True, 
        gridwidth=1, 
        gridcolor=COLORS['grid'],
        title_font=dict(color='#000000', size=14, family='Arial, sans-serif'),
        tickfont=dict(color='#000000', size=11, family='Arial, sans-serif')
    )
    
    return fig

def create_comprehensive_demographic_dashboard():
    """
    Crea un dashboard completo con múltiples análisis demográficos
    """
    dashboard_charts = {}
    
    # Gráfico por género
    try:
        dashboard_charts['gender'] = create_gender_comparison_chart()
        print("✅ Gráfico por género creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por género: {e}")
        dashboard_charts['gender'] = create_basic_demographic_chart("Análisis por Género", "Error al cargar datos")
    
    # Gráfico por edad
    try:
        dashboard_charts['age'] = create_age_comparison_chart()
        print("✅ Gráfico por edad creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por edad: {e}")
        dashboard_charts['age'] = create_basic_demographic_chart("Análisis por Edad", "Error al cargar datos")
    
    # Gráfico por campo de estudio
    try:
        dashboard_charts['field_of_study'] = create_field_of_study_comparison_chart()
        print("✅ Gráfico por campo de estudio creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por campo de estudio: {e}")
        dashboard_charts['field_of_study'] = create_basic_demographic_chart("Análisis por Campo de Estudio", "Error al cargar datos")
    
    # Gráfico por dificultades financieras
    try:
        dashboard_charts['financial_difficulties'] = create_financial_difficulties_comparison_chart()
        print("✅ Gráfico por dificultades financieras creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por dificultades financieras: {e}")
        dashboard_charts['financial_difficulties'] = create_basic_demographic_chart("Análisis por Dificultades Financieras", "Error al cargar datos")
    
    # Gráfico por situación de vivienda con padres
    try:
        dashboard_charts['living_with_parents'] = create_living_with_parents_comparison_chart()
        print("✅ Gráfico por situación de vivienda creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por situación de vivienda: {e}")
        dashboard_charts['living_with_parents'] = create_basic_demographic_chart("Análisis por Situación de Vivienda", "Error al cargar datos")
    
    # Gráfico por estado financiero de los padres
    try:
        dashboard_charts['parents_financial_status'] = create_parents_financial_status_comparison_chart()
        print("✅ Gráfico por estado financiero de padres creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por estado financiero de padres: {e}")
        dashboard_charts['parents_financial_status'] = create_basic_demographic_chart("Análisis por Estado Financiero de Padres", "Error al cargar datos")
    
    # Gráfico por nivel educativo de los padres
    try:
        dashboard_charts['parents_education'] = create_parents_education_comparison_chart()
        print("✅ Gráfico por nivel educativo de padres creado exitosamente")
    except Exception as e:
        print(f"⚠️ Error creando gráfico por nivel educativo de padres: {e}")
        dashboard_charts['parents_education'] = create_basic_demographic_chart("Análisis por Nivel Educativo de Padres", "Error al cargar datos")
    
    return dashboard_charts

if __name__ == "__main__":
    print("🎯 Generando análisis demográfico avanzado...")
    
    # Crear dashboard demográfico
    charts = create_comprehensive_demographic_dashboard()
    
    print(f"\n📊 Dashboard generado con {len(charts)} gráficos:")
    chart_descriptions = {
        'gender': 'Género (Hombres vs Mujeres)',
        'age': 'Edad (Grupos etarios)',
        'field_of_study': 'Campo de Estudio (Carreras/Disciplinas)',
        'financial_difficulties': 'Dificultades Financieras (Nivel socioeconómico)',
        'living_with_parents': 'Situación de Vivienda (Independientes vs Con padres)',
        'parents_financial_status': 'Estado Financiero de Padres (Nivel económico familiar)',
        'parents_education': 'Nivel Educativo de Padres (Formación académica familiar)'
    }
    
    for key in charts.keys():
        description = chart_descriptions.get(key, f"Análisis por {key}")
        print(f"   • charts['{key}'] - {description}")
    
    print("\n💡 Para mostrar los gráficos:")
    print("   charts['gender'].show()                    # Análisis por género")
    print("   charts['age'].show()                       # Análisis por edad")
    print("   charts['field_of_study'].show()            # Análisis por campo de estudio")
    print("   charts['financial_difficulties'].show()    # Análisis por dificultades financieras")
    print("   charts['living_with_parents'].show()       # Análisis por situación de vivienda")
    print("   charts['parents_financial_status'].show()  # Análisis por estado financiero de padres")
    print("   charts['parents_education'].show()         # Análisis por nivel educativo de padres")
    
    # Ejemplo de insights demográficos
    print("\n🔍 INSIGHTS DEMOGRÁFICOS DISPONIBLES:")
    
    # Verificar datos de género
    try:
        gender_data = read_demographic_dataset_detailed(
            PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_SEX
        )
        if gender_data:
            print(f"   • Género: {list(gender_data.keys())}")
    except Exception as e:
        print(f"   • Género: Error - {e}")
    
    # Verificar datos de campo de estudio
    try:
        field_data = read_demographic_dataset_detailed(
            PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY
        )
        if field_data:
            field_count = len(list(field_data.keys()))
            print(f"   • Campo de Estudio: {field_count} disciplinas disponibles")
    except Exception as e:
        print(f"   • Campo de Estudio: Error - {e}")
    
    # Verificar datos de dificultades financieras
    try:
        financial_data = read_demographic_dataset_detailed(
            PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES
        )
        if financial_data:
            financial_count = len(list(financial_data.keys()))
            print(f"   • Dificultades Financieras: {financial_count} niveles disponibles")
    except Exception as e:
        print(f"   • Dificultades Financieras: Error - {e}")
    
    print("\n🎯 TODOS LOS ANÁLISIS INCLUYEN:")
    print("   ✓ Comparación España vs Promedio Europeo")
    print("   ✓ Gráficos interactivos con hover tooltips")
    print("   ✓ Colores consistentes para storytelling")
    print("   ✓ Manejo robusto de errores y datos faltantes")
    
    print("\n✅ Análisis demográfico completado!") 