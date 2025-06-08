import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from enum import Enum
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Configuración de estilo para gráficos más atractivos
plt.style.use('default')
sns.set_palette("husl")

type DatasetName = CompleteDatasetsName | PreprocessedDatasetsNamesWorkMotiveAffordStudy | PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy

class PreprocessedDatasetsNamesImpactsOnStudyForWork(Enum):
    # This dataset only includes students that have a job that is not related to their study and Students were asked to indicate if they would like to spend (1) "less", (2) "same" or (3) "more" time on paid jobs. Paid job during lecture period: Paid work alongside studies during the lecture period; including (occasional) jobs from time to time during the lecture period and (regular) jobs during the entire semester.
    IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_NOTRELATED = 'preprocessed_impact_by_job/E8_time_budget_satisf_job_notrelated__all_students__all_contries.xlsx'
    # seems like the people with more job time are more tend to want to spend more time on their study and less time on paid jobs
    IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_RELATED = 'preprocessed_impact_by_job/E8_time_budget_all__e_satisf__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__E_FINANCIAL_DIFFICULTIES = 'preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__e_financial_difficulties__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__E_SATISFACTION = 'preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__e_satisf__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_WORK_TO_AFFORD_TO_STUDY = 'preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__s_work_to_afford_to_study__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_RELATIONSHIP_JOB_STUDY = 'preprocessed_impact_by_job/E8_health__s_relationship_job_study__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_PERFORMANCE_SELF_ASSESSMENT = 'preprocessed_impact_by_job/E8_selfevaluation__s_performance_self_assessment__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_NOT_LIVING_WITH_PARENTS = 'preprocessed_impact_by_job/E8_time_budget_all__e_notlivingwithparents__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_TEACHING_TYPE = 'preprocessed_impact_by_job/E8_work_related_study5__e_teachingtype__ES.xlsx'



class PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy(Enum):
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY = 'preprocessed_relationship_study_job/E8_work_related_study5__all_students__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_AGE = 'preprocessed_relationship_study_job/E8_work_related_study5__e_age__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_FIELD_OF_STUDY = 'preprocessed_relationship_study_job/E8_work_related_study5__e_field_of_study__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_INTENS = 'preprocessed_relationship_study_job/E8_work_related_study5__e_intens__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_QUALIFICATION = 'preprocessed_relationship_study_job/E8_work_related_study5__e_qualification__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_SEX = 'preprocessed_relationship_study_job/E8_work_related_study5__e_sex__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_S_FULL_OR_PART_TIME_STUDY_PROGRAMME = 'preprocessed_relationship_study_job/E8_work_related_study5__s_full_or_part_time_study_programme__all_contries.xlsx'

class PreprocessedDatasetsNamesWorkMotiveAffordStudy(Enum):
    WORK_MOTIVE_AFFORD_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__all_students__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_SEX = 'preprocessed_excels/E8_work_motive_afford_study_5__e_sex__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_AGE = 'preprocessed_excels/E8_work_motive_afford_study_5__e_age__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES = 'preprocessed_excels/E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS = 'preprocessed_excels/E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS = 'preprocessed_excels/E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx'


class CompleteDatasetsName(Enum):
    STUDENTS_CHARACTERISTICS = 'E8_topic_A__Students_characteristics.xlsx'
    SOCIOECONOMIC_BACKGROUND = 'E8_topic_B__Socioeconomic_background.xlsx'
    TRANSITION_AND_ACCESS = 'E8_topic_C__Transition_and_access.xlsx'
    TYPES_AND_MODES_OF_STUDY = 'E8_topic_D__Types_and_modes_of_study.xlsx'
    HOUSING_SITUATION = 'E8_topic_E__Housing_situation.xlsx'
    STUDENTS_EXPENSES = 'E8_topic_F__Students_expenses.xlsx'
    STUDENTS_RESOURCES = 'E8_topic_G__Students_resources.xlsx'
    EMPLOYMENT = 'E8_topic_H__Employment.xlsx'
    TIME_BUDGET = 'E8_topic_I__Time_budget.xlsx'
    INTERNATIONAL_STUDENT_MOBILITY = 'E8_topic_J__International_student_mobility.xlsx'
    ASSESSMENT_OF_STUDIES_AND_PERFORMANCE = 'E8_topic_K__Assessment_of_studies_and_performance.xlsx'
    COUNSELLING_SERVICES = 'E8_topic_L__Counselling_Services.xlsx'
    HEALTH_WELLBEING = 'E8_topic_M__Health__wellbeing.xlsx'
    EFFECTS_OF_THE_COVID_19_PANDEMIC = 'E8_topic_N__Effects_of_the_Covid-19_Pandemic.xlsx'
    EQUIPMENT_AT_HOME = 'E8_topic_O__Equipment_at_home.xlsx'
    DIGITALISATION = 'E8_topic_P__Digitalisation.xlsx'
    DISCRIMINATION_SAFETY_FEELING = 'E8_topic_Q__Discrimination__safety_feeling.xlsx'

NUM_SPANISH_PARTICIPANTS = 9072


def read_dataset(dataset_name: DatasetName):
    df = pd.read_excel(dataset_name.value)
    return df


def read_work_motive_afford_study_dataset():
    """
    Función especializada para leer el dataset de motivos de trabajo para costear estudios.
    Este Excel tiene una estructura compleja con múltiples niveles de headers.
    """
    # Leemos el archivo sin headers para poder procesarlo manualmente
    df = pd.read_excel(PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY.value, header=None)
    
    # Los datos reales empiezan en la fila 3 (índice 3)
    data_df = df.iloc[3:].copy()
    
    # Creamos nombres de columnas más descriptivos basados en la estructura
    # Las columnas van de 3 en 3: Value, Unit, Count para cada nivel de respuesta
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
    
    # Asignamos los nombres de columnas
    data_df.columns = column_names
    
    # Reseteamos el índice
    data_df = data_df.reset_index(drop=True)
    
    # Limpiamos los datos - eliminamos filas que no sean países (con NaN en Country)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertimos las columnas numéricas
    for level in response_levels:
        # Convertimos Value columns a float, manejando 'n. a.' como NaN
        value_col = f'{level}_Value'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        
        # Convertimos Count columns a int, manejando errores
        count_col = f'{level}_Count'
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def read_work_impact_dataset(dataset_enum):
    """
    Función especializada para leer los datasets de impacto del trabajo en los estudios.
    Estos Excel tienen estructuras complejas con múltiples niveles de headers.
    """
    # Leemos el archivo sin headers para poder procesarlo manualmente
    df = pd.read_excel(dataset_enum.value, header=None)
    
    # Los datos reales suelen empezar en la fila 3 (índice 3)
    data_df = df.iloc[3:].copy()
    
    # Detectar el tipo de dataset basado en el nombre del archivo
    filename = dataset_enum.value.lower()
    
    if 'time_budget_satisf' in filename:
        return _process_time_budget_satisfaction_dataset(data_df)
    elif 'abandoning' in filename or 'assess' in filename:
        return _process_study_abandoning_dataset(data_df)
    elif 'selfevaluation' in filename:
        return _process_self_evaluation_dataset(data_df)
    elif 'health' in filename:
        return _process_health_relationship_dataset(data_df)
    else:
        # Estructura genérica para otros datasets
        return _process_generic_impact_dataset(data_df)


def _process_time_budget_satisfaction_dataset(data_df):
    """
    Procesa datasets de satisfacción con presupuesto de tiempo
    """
    column_names = ['Country']
    satisfaction_levels = [
        'Less_Time',        # Menos tiempo en trabajo remunerado
        'Same_Time',        # Mismo tiempo en trabajo remunerado  
        'More_Time'         # Más tiempo en trabajo remunerado
    ]
    
    for level in satisfaction_levels:
        column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
    
    data_df.columns = column_names
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertir columnas numéricas
    for level in satisfaction_levels:
        value_col = f'{level}_Value'
        count_col = f'{level}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def _process_study_abandoning_dataset(data_df):
    """
    Procesa datasets relacionados con abandono/consideración de abandono de estudios
    """
    # Detectar automáticamente la estructura basada en el número de columnas
    num_cols = len(data_df.columns)
    
    if num_cols == 46:
        # Estructura compleja con 3 grupos de dificultades financieras
        column_names = ['Country']
        
        # Grupo 1: with financial difficulties (columnas 1-15)
        abandoning_levels_1 = ['With_Fin_Diff_Very_Often', 'With_Fin_Diff_Often', 'With_Fin_Diff_Sometimes', 'With_Fin_Diff_Rarely', 'With_Fin_Diff_Never']
        for level in abandoning_levels_1:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Grupo 2: with somewhat financial difficulties (columnas 16-30)
        abandoning_levels_2 = ['Somewhat_Fin_Diff_Very_Often', 'Somewhat_Fin_Diff_Often', 'Somewhat_Fin_Diff_Sometimes', 'Somewhat_Fin_Diff_Rarely', 'Somewhat_Fin_Diff_Never']
        for level in abandoning_levels_2:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Grupo 3: without financial difficulties (columnas 31-45)
        abandoning_levels_3 = ['Without_Fin_Diff_Very_Often', 'Without_Fin_Diff_Often', 'Without_Fin_Diff_Sometimes', 'Without_Fin_Diff_Rarely', 'Without_Fin_Diff_Never']
        for level in abandoning_levels_3:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Para compatibilidad con código existente, usamos el primer grupo como principal
        all_levels = abandoning_levels_1 + abandoning_levels_2 + abandoning_levels_3
        
        # También creamos aliases para compatibilidad con funciones existentes
        data_df.columns = column_names
        data_df = data_df.reset_index(drop=True)
        data_df = data_df.dropna(subset=['Country'])
        
        # Crear columnas agregadas para compatibilidad
        data_df['Very_Often_Value'] = data_df['With_Fin_Diff_Very_Often_Value'].fillna(0)
        data_df['Often_Value'] = data_df['With_Fin_Diff_Often_Value'].fillna(0)
        data_df['Sometimes_Value'] = data_df['With_Fin_Diff_Sometimes_Value'].fillna(0)
        data_df['Rarely_Value'] = data_df['With_Fin_Diff_Rarely_Value'].fillna(0)
        data_df['Never_Value'] = data_df['With_Fin_Diff_Never_Value'].fillna(0)
        
        data_df['Very_Often_Count'] = data_df['With_Fin_Diff_Very_Often_Count'].fillna(0)
        data_df['Often_Count'] = data_df['With_Fin_Diff_Often_Count'].fillna(0)
        data_df['Sometimes_Count'] = data_df['With_Fin_Diff_Sometimes_Count'].fillna(0)
        data_df['Rarely_Count'] = data_df['With_Fin_Diff_Rarely_Count'].fillna(0)
        data_df['Never_Count'] = data_df['With_Fin_Diff_Never_Count'].fillna(0)
        
    elif num_cols == 31:
        # Estructura con 2 grupos de respuestas (31 = 1 + 2*15)
        column_names = ['Country']
        
        # Grupo 1: (columnas 1-15) - 5 niveles x 3 columnas
        abandoning_levels_1 = ['Group1_Very_Often', 'Group1_Often', 'Group1_Sometimes', 'Group1_Rarely', 'Group1_Never']
        for level in abandoning_levels_1:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Grupo 2: (columnas 16-30) - 5 niveles x 3 columnas  
        abandoning_levels_2 = ['Group2_Very_Often', 'Group2_Often', 'Group2_Sometimes', 'Group2_Rarely', 'Group2_Never']
        for level in abandoning_levels_2:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Asignar columnas (solo hasta 30, dejando la última columna)
        data_df.columns = column_names[:len(data_df.columns)]
        data_df = data_df.reset_index(drop=True)
        data_df = data_df.dropna(subset=['Country'])
        
        # Crear aliases para compatibilidad usando el primer grupo
        data_df['Very_Often_Value'] = data_df.get('Group1_Very_Often_Value', 0)
        data_df['Often_Value'] = data_df.get('Group1_Often_Value', 0)
        data_df['Sometimes_Value'] = data_df.get('Group1_Sometimes_Value', 0)
        data_df['Rarely_Value'] = data_df.get('Group1_Rarely_Value', 0)
        data_df['Never_Value'] = data_df.get('Group1_Never_Value', 0)
        
        data_df['Very_Often_Count'] = data_df.get('Group1_Very_Often_Count', 0)
        data_df['Often_Count'] = data_df.get('Group1_Often_Count', 0)
        data_df['Sometimes_Count'] = data_df.get('Group1_Sometimes_Count', 0)
        data_df['Rarely_Count'] = data_df.get('Group1_Rarely_Count', 0)
        data_df['Never_Count'] = data_df.get('Group1_Never_Count', 0)
        
    else:
        # Estructura simple original
        column_names = ['Country']
        abandoning_levels = [
            'Very_Often',       # Muy frecuentemente
            'Often',           # Frecuentemente
            'Sometimes',       # A veces
            'Rarely',          # Raramente
            'Never'            # Nunca
        ]
        
        for level in abandoning_levels:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Ajustar nombres de columnas al número real de columnas
        data_df.columns = column_names[:len(data_df.columns)]
        data_df = data_df.reset_index(drop=True)
        data_df = data_df.dropna(subset=['Country'])
        
        all_levels = abandoning_levels
    
    # Convertir columnas numéricas para las columnas principales de compatibilidad
    main_levels = ['Very_Often', 'Often', 'Sometimes', 'Rarely', 'Never']
    for level in main_levels:
        value_col = f'{level}_Value'
        count_col = f'{level}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def _process_self_evaluation_dataset(data_df):
    """
    Procesa datasets de auto-evaluación de rendimiento
    """
    column_names = ['Country']
    performance_levels = [
        'Very_Good',        # Muy bueno
        'Good',            # Bueno
        'Satisfactory',    # Satisfactorio
        'Poor',            # Malo
        'Very_Poor'        # Muy malo
    ]
    
    for level in performance_levels:
        column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
    
    data_df.columns = column_names
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertir columnas numéricas
    for level in performance_levels:
        value_col = f'{level}_Value'
        count_col = f'{level}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def _process_health_relationship_dataset(data_df):
    """
    Procesa datasets de salud y relación trabajo-estudio
    """
    column_names = ['Country']
    health_levels = [
        'Excellent',        # Excelente
        'Very_Good',       # Muy buena
        'Good',            # Buena
        'Fair',            # Regular
        'Poor'             # Mala
    ]
    
    for level in health_levels:
        column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
    
    data_df.columns = column_names
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertir columnas numéricas
    for level in health_levels:
        value_col = f'{level}_Value'
        count_col = f'{level}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def _process_generic_impact_dataset(data_df):
    """
    Procesamiento genérico para otros datasets de impacto
    """
    # Intentamos detectar automáticamente la estructura
    # Asumimos estructura estándar: Country + grupos de 3 columnas (Value, Unit, Count)
    num_cols = len(data_df.columns)
    
    # Ajustar para estructuras conocidas
    if num_cols == 31:
        # Estructura con 2 grupos de respuestas (31 = 1 + 2*15)
        # Calcular exactamente: (31-1)/3 = 10
        num_response_levels = (num_cols - 1) // 3
    else:
        num_response_levels = (num_cols - 1) // 3
    
    column_names = ['Country']
    for i in range(num_response_levels):
        level_name = f'Level_{i+1}'
        column_names.extend([f'{level_name}_Value', f'{level_name}_Unit', f'{level_name}_Count'])
    
    # Asegurar que no excedemos el número de columnas disponibles
    max_columns_needed = 1 + (num_response_levels * 3)
    if max_columns_needed > num_cols:
        num_response_levels = (num_cols - 1) // 3
        column_names = ['Country']
        for i in range(num_response_levels):
            level_name = f'Level_{i+1}'
            column_names.extend([f'{level_name}_Value', f'{level_name}_Unit', f'{level_name}_Count'])
    
    # Ajustar al número exacto de columnas
    data_df.columns = column_names[:len(data_df.columns)]
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    # Para compatibilidad, crear aliases de las columnas principales si existen
    if num_response_levels >= 5:
        data_df['Very_Often_Value'] = data_df.get('Level_1_Value', 0)
        data_df['Often_Value'] = data_df.get('Level_2_Value', 0)
        data_df['Sometimes_Value'] = data_df.get('Level_3_Value', 0)
        data_df['Rarely_Value'] = data_df.get('Level_4_Value', 0)
        data_df['Never_Value'] = data_df.get('Level_5_Value', 0)
    
    # Convertir columnas numéricas
    for i in range(num_response_levels):
        level_name = f'Level_{i+1}'
        value_col = f'{level_name}_Value'
        count_col = f'{level_name}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def create_work_necessity_charts(df):
    """
    Crea múltiples visualizaciones para mostrar la necesidad de trabajar para costear estudios
    """
    
    # 1. Gráfico de barras apiladas por país
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('Necesidad de Trabajar para Costear Estudios - Análisis por País', fontsize=16, fontweight='bold')
    
    # 1.1 Gráfico apilado con todos los niveles
    ax1 = axes[0, 0]
    
    # Preparamos los datos para el gráfico apilado
    countries = df['Country'].tolist()
    
    # Obtenemos los valores de cada nivel (manejando NaN)
    applies_totally = df['Applies_Totally_Value'].fillna(0).tolist()
    applies_rather = df['Applies_Rather_Value'].fillna(0).tolist()
    applies_partially = df['Applies_Partially_Value'].fillna(0).tolist()
    applies_rather_not = df['Applies_Rather_Not_Value'].fillna(0).tolist()
    does_not_apply = df['Does_Not_Apply_Value'].fillna(0).tolist()
    
    # Creamos el gráfico de barras apiladas
    x = np.arange(len(countries))
    width = 0.8
    
    bars1 = ax1.bar(x, applies_totally, width, label='Aplica Totalmente', color='#d62728')
    bars2 = ax1.bar(x, applies_rather, width, bottom=applies_totally, label='Aplica Bastante', color='#ff7f0e')
    bars3 = ax1.bar(x, applies_partially, width, 
                   bottom=np.array(applies_totally) + np.array(applies_rather), 
                   label='Aplica Parcialmente', color='#ffbb78')
    bars4 = ax1.bar(x, applies_rather_not, width,
                   bottom=np.array(applies_totally) + np.array(applies_rather) + np.array(applies_partially),
                   label='No Aplica Mucho', color='#c5b0d5')
    bars5 = ax1.bar(x, does_not_apply, width,
                   bottom=np.array(applies_totally) + np.array(applies_rather) + 
                          np.array(applies_partially) + np.array(applies_rather_not),
                   label='No Aplica Para Nada', color='#2ca02c')
    
    ax1.set_xlabel('Países')
    ax1.set_ylabel('Porcentaje (%)')
    ax1.set_title('Distribución de Respuestas por País')
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries, rotation=45, ha='right')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.grid(True, alpha=0.3)
    
    # 1.2 Gráfico simplificado: Necesitan trabajar vs No necesitan
    ax2 = axes[0, 1]
    
    # Agrupamos las respuestas
    need_to_work = np.array(applies_totally) + np.array(applies_rather) + np.array(applies_partially)
    dont_need_to_work = np.array(applies_rather_not) + np.array(does_not_apply)
    
    bars_need = ax2.bar(x, need_to_work, width, label='Necesitan Trabajar', color='#d62728', alpha=0.8)
    bars_dont_need = ax2.bar(x, dont_need_to_work, width, bottom=need_to_work, 
                            label='No Necesitan Trabajar', color='#2ca02c', alpha=0.8)
    
    ax2.set_xlabel('Países')
    ax2.set_ylabel('Porcentaje (%)')
    ax2.set_title('Necesidad de Trabajar para Estudiar (Agrupado)')
    ax2.set_xticks(x)
    ax2.set_xticklabels(countries, rotation=45, ha='right')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Destacamos España
    spain_idx = countries.index('ES') if 'ES' in countries else None
    if spain_idx is not None:
        for bar in [bars_need[spain_idx], bars_dont_need[spain_idx]]:
            bar.set_edgecolor('black')
            bar.set_linewidth(2)
    
    # 1.3 Top 10 países que más necesitan trabajar
    ax3 = axes[1, 0]
    
    # Ordenamos por necesidad de trabajar
    df_sorted = df.copy()
    df_sorted['Need_Work_Percentage'] = (df_sorted['Applies_Totally_Value'].fillna(0) + 
                                        df_sorted['Applies_Rather_Value'].fillna(0) + 
                                        df_sorted['Applies_Partially_Value'].fillna(0))
    df_sorted = df_sorted.sort_values('Need_Work_Percentage', ascending=False).head(10)
    
    colors = ['#d62728' if country == 'ES' else '#1f77b4' for country in df_sorted['Country']]
    bars = ax3.bar(df_sorted['Country'], df_sorted['Need_Work_Percentage'], color=colors)
    
    ax3.set_xlabel('Países')
    ax3.set_ylabel('Porcentaje (%)')
    ax3.set_title('Top 10: Mayor Necesidad de Trabajar para Estudiar')
    ax3.tick_params(axis='x', rotation=45)
    ax3.grid(True, alpha=0.3)
    
    # Añadimos valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', va='bottom')
    
    # 1.4 Comparación con España destacada
    ax4 = axes[1, 1]
    
    # Datos de España
    spain_data = df[df['Country'] == 'ES'].iloc[0] if 'ES' in df['Country'].values else None
    
    if spain_data is not None:
        # Promedio europeo (excluyendo España)
        df_no_spain = df[df['Country'] != 'ES']
        avg_applies_totally = df_no_spain['Applies_Totally_Value'].mean()
        avg_applies_rather = df_no_spain['Applies_Rather_Value'].mean()
        avg_applies_partially = df_no_spain['Applies_Partially_Value'].mean()
        avg_applies_rather_not = df_no_spain['Applies_Rather_Not_Value'].mean()
        avg_does_not_apply = df_no_spain['Does_Not_Apply_Value'].mean()
        
        categories = ['Aplica\nTotalmente', 'Aplica\nBastante', 'Aplica\nParcialmente', 
                     'No Aplica\nMucho', 'No Aplica\nPara Nada']
        spain_values = [spain_data['Applies_Totally_Value'], spain_data['Applies_Rather_Value'],
                       spain_data['Applies_Partially_Value'], spain_data['Applies_Rather_Not_Value'],
                       spain_data['Does_Not_Apply_Value']]
        europe_values = [avg_applies_totally, avg_applies_rather, avg_applies_partially,
                        avg_applies_rather_not, avg_does_not_apply]
        
        x_pos = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax4.bar(x_pos - width/2, spain_values, width, label='España', color='#d62728', alpha=0.8)
        bars2 = ax4.bar(x_pos + width/2, europe_values, width, label='Promedio Europeo', color='#1f77b4', alpha=0.8)
        
        ax4.set_xlabel('Niveles de Respuesta')
        ax4.set_ylabel('Porcentaje (%)')
        ax4.set_title('España vs Promedio Europeo')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(categories)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # Añadimos valores en las barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                if not np.isnan(height):
                    ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                            f'{height:.1f}%', ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    # 2. Crear un resumen estadístico
    print("\n" + "="*80)
    print("RESUMEN: NECESIDAD DE TRABAJAR PARA COSTEAR ESTUDIOS")
    print("="*80)
    
    # Calcular estadísticas
    df_stats = df.copy()
    df_stats['Need_Work_Total'] = (df_stats['Applies_Totally_Value'].fillna(0) + 
                                  df_stats['Applies_Rather_Value'].fillna(0) + 
                                  df_stats['Applies_Partially_Value'].fillna(0))
    
    print(f"\n📊 ESTADÍSTICAS GENERALES:")
    print(f"   • Promedio europeo de estudiantes que necesitan trabajar: {df_stats['Need_Work_Total'].mean():.1f}%")
    print(f"   • País con mayor necesidad: {df_stats.loc[df_stats['Need_Work_Total'].idxmax(), 'Country']} ({df_stats['Need_Work_Total'].max():.1f}%)")
    print(f"   • País con menor necesidad: {df_stats.loc[df_stats['Need_Work_Total'].idxmin(), 'Country']} ({df_stats['Need_Work_Total'].min():.1f}%)")
    
    if 'ES' in df['Country'].values:
        spain_stats = df[df['Country'] == 'ES'].iloc[0]
        spain_need_work = (spain_stats['Applies_Totally_Value'] + 
                          spain_stats['Applies_Rather_Value'] + 
                          spain_stats['Applies_Partially_Value'])
        print(f"\n🇪🇸 DATOS DE ESPAÑA:")
        print(f"   • Estudiantes que necesitan trabajar: {spain_need_work:.1f}%")
        print(f"   • Aplica totalmente: {spain_stats['Applies_Totally_Value']:.1f}%")
        print(f"   • No aplica para nada: {spain_stats['Does_Not_Apply_Value']:.1f}%")
        print(f"   • Número total de estudiantes encuestados: {spain_stats['Applies_Totally_Count'] + spain_stats['Applies_Rather_Count'] + spain_stats['Applies_Partially_Count'] + spain_stats['Applies_Rather_Not_Count'] + spain_stats['Does_Not_Apply_Count']}")


def read_work_study_relationship_dataset(dataset_enum=None):
    """
    Función especializada para leer el dataset de relación entre trabajo y estudios.
    Este Excel tiene una estructura compleja con múltiples niveles de headers.
    """
    if dataset_enum is None:
        dataset_enum = PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy.RELATIONSHIP_BETWEEN_WORK_AND_STUDY
    
    # Leemos el archivo sin headers para poder procesarlo manualmente
    df = pd.read_excel(dataset_enum.value, header=None)
    
    # Los datos reales empiezan en la fila 3 (índice 3)
    data_df = df.iloc[3:].copy()
    
    # Creamos nombres de columnas más descriptivos basados en la estructura
    # Las columnas van de 3 en 3: Value, Unit, Count para cada nivel de relación
    column_names = ['Country']
    relationship_levels = [
        'Very_Closely',         # Nivel 1 - Muy relacionado
        'Rather_Closely',       # Nivel 2 - Bastante relacionado  
        'To_Some_Extent',       # Nivel 3 - En cierta medida relacionado
        'Rather_Not',           # Nivel 4 - No muy relacionado
        'Not_At_All'           # Nivel 5 - Para nada relacionado
    ]
    
    for level in relationship_levels:
        column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
    
    # Asignamos los nombres de columnas
    data_df.columns = column_names
    
    # Reseteamos el índice
    data_df = data_df.reset_index(drop=True)
    
    # Limpiamos los datos - eliminamos filas que no sean países (con NaN en Country)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertimos las columnas numéricas
    for level in relationship_levels:
        # Convertimos Value columns a float, manejando 'n. a.' como NaN
        value_col = f'{level}_Value'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        
        # Convertimos Count columns a int, manejando errores
        count_col = f'{level}_Count'
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df


def create_interactive_work_study_relationship_charts(df):
    """
    Crea visualizaciones interactivas para mostrar la relación entre el trabajo y los estudios
    con España como foco principal
    """
    
    # Configuración de colores consistente con España destacada
    spain_color = '#d62728'  # Rojo para España
    other_countries_color = '#1f77b4'  # Azul para otros países
    
    # 1. Gráfico de barras apiladas interactivo
    fig1 = create_stacked_relationship_chart(df, spain_color, other_countries_color)
    
    # 2. Gráfico de relación simplificada (Relacionado vs No relacionado)
    fig2 = create_simplified_relationship_chart(df, spain_color, other_countries_color)
    
    # 3. Ranking de países por relación trabajo-estudio
    fig3 = create_relationship_ranking_chart(df, spain_color, other_countries_color)
    
    # 4. Comparación España vs Promedio Europeo
    fig4 = create_spain_vs_europe_comparison(df, spain_color, other_countries_color)
    
    # 5. Análisis por segmentos demográficos
    fig5 = create_demographic_analysis_charts(df)
    
    return fig1, fig2, fig3, fig4, fig5


def create_stacked_relationship_chart(df, spain_color, other_countries_color):
    """
    Crea un gráfico de barras apiladas interactivo mostrando los niveles de relación trabajo-estudio
    """
    # Preparar datos
    countries = df['Country'].tolist()
    
    # Obtener valores para cada nivel de relación
    very_closely = df['Very_Closely_Value'].fillna(0).tolist()
    rather_closely = df['Rather_Closely_Value'].fillna(0).tolist()
    to_some_extent = df['To_Some_Extent_Value'].fillna(0).tolist()
    rather_not = df['Rather_Not_Value'].fillna(0).tolist()
    not_at_all = df['Not_At_All_Value'].fillna(0).tolist()
    
    # Crear colores destacando España
    colors = [spain_color if country == 'ES' else other_countries_color for country in countries]
    
    fig = go.Figure()
    
    # Añadir cada nivel como una barra en el stack
    fig.add_trace(go.Bar(
        name='Muy Relacionado',
        x=countries,
        y=very_closely,
        marker_color='#2ca02c',  # Verde oscuro
        hovertemplate='<b>%{x}</b><br>Muy Relacionado: %{y}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Bastante Relacionado',
        x=countries,
        y=rather_closely,
        marker_color='#7fbf7f',  # Verde claro
        hovertemplate='<b>%{x}</b><br>Bastante Relacionado: %{y}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Algo Relacionado',
        x=countries,
        y=to_some_extent,
        marker_color='#ffbb78',  # Naranja claro
        hovertemplate='<b>%{x}</b><br>Algo Relacionado: %{y}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Poco Relacionado',
        x=countries,
        y=rather_not,
        marker_color='#ff7f0e',  # Naranja
        hovertemplate='<b>%{x}</b><br>Poco Relacionado: %{y}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Nada Relacionado',
        x=countries,
        y=not_at_all,
        marker_color='#d62728',  # Rojo
        hovertemplate='<b>%{x}</b><br>Nada Relacionado: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Relación entre Trabajo y Estudios por País<br><sub>¿Qué tan relacionado está el trabajo con los estudios?</sub>',
            'x': 0.5,
            'font': {'size': 20}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        barmode='stack',
        hovermode='closest',
        template='plotly_white',
        font={'size': 12},
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': -0.3,
            'xanchor': 'center',
            'x': 0.5
        },
        height=600
    )
    
    # Destacar España con borde
    spain_idx = countries.index('ES') if 'ES' in countries else None
    if spain_idx is not None:
        # Añadir anotación para España
        fig.add_annotation(
            x=spain_idx,
            y=100,
            text="🇪🇸 ESPAÑA",
            showarrow=True,
            arrowhead=2,
            arrowcolor=spain_color,
            bgcolor=spain_color,
            bordercolor="white",
            font={'color': 'white', 'size': 12}
        )
    
    return fig


def create_simplified_relationship_chart(df, spain_color, other_countries_color):
    """
    Crea un gráfico simplificado: Trabajo relacionado vs No relacionado con estudios
    """
    # Calcular datos agrupados
    df_simplified = df.copy()
    df_simplified['Related_Work'] = (
        df_simplified['Very_Closely_Value'].fillna(0) + 
        df_simplified['Rather_Closely_Value'].fillna(0) + 
        df_simplified['To_Some_Extent_Value'].fillna(0)
    )
    df_simplified['Unrelated_Work'] = (
        df_simplified['Rather_Not_Value'].fillna(0) + 
        df_simplified['Not_At_All_Value'].fillna(0)
    )
    
    # Ordenar por trabajo relacionado
    df_simplified = df_simplified.sort_values('Related_Work', ascending=True)
    
    countries = df_simplified['Country'].tolist()
    related_work = df_simplified['Related_Work'].tolist()
    unrelated_work = df_simplified['Unrelated_Work'].tolist()
    
    # Crear colores destacando España
    colors_related = [spain_color if country == 'ES' else '#2ca02c' for country in countries]
    colors_unrelated = [spain_color if country == 'ES' else '#d62728' for country in countries]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Trabajo Relacionado con Estudios',
        x=countries,
        y=related_work,
        marker_color=colors_related,
        hovertemplate='<b>%{x}</b><br>Trabajo Relacionado: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Trabajo No Relacionado con Estudios',
        x=countries,
        y=unrelated_work,
        marker_color=colors_unrelated,
        hovertemplate='<b>%{x}</b><br>Trabajo No Relacionado: %{y:.1f}%<extra></extra>',
        base=related_work
    ))
    
    fig.update_layout(
        title={
            'text': 'Trabajo Relacionado vs No Relacionado con Estudios<br><sub>Comparación simplificada por países</sub>',
            'x': 0.5,
            'font': {'size': 20}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        barmode='stack',
        template='plotly_white',
        hovermode='closest',
        font={'size': 12},
        height=500,
        xaxis={'tickangle': 45}
    )
    
    # Destacar España
    spain_idx = countries.index('ES') if 'ES' in countries else None
    if spain_idx is not None:
        spain_related = related_work[spain_idx]
        fig.add_annotation(
            x=spain_idx,
            y=spain_related + 5,
            text=f"🇪🇸 España<br>{spain_related:.1f}% relacionado",
            showarrow=True,
            arrowhead=2,
            arrowcolor=spain_color,
            bgcolor=spain_color,
            bordercolor="white",
            font={'color': 'white', 'size': 10}
        )
    
    return fig


def create_relationship_ranking_chart(df, spain_color, other_countries_color):
    """
    Crea un ranking de países por nivel de relación trabajo-estudio
    """
    # Calcular score de relación (weighted average)
    df_ranking = df.copy()
    df_ranking['Relationship_Score'] = (
        df_ranking['Very_Closely_Value'].fillna(0) * 5 +
        df_ranking['Rather_Closely_Value'].fillna(0) * 4 +
        df_ranking['To_Some_Extent_Value'].fillna(0) * 3 +
        df_ranking['Rather_Not_Value'].fillna(0) * 2 +
        df_ranking['Not_At_All_Value'].fillna(0) * 1
    ) / 5
    
    # Ordenar por score
    df_ranking = df_ranking.sort_values('Relationship_Score', ascending=True)
    
    countries = df_ranking['Country'].tolist()
    scores = df_ranking['Relationship_Score'].tolist()
    
    # Crear colores destacando España
    colors = [spain_color if country == 'ES' else other_countries_color for country in countries]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=scores,
        y=countries,
        orientation='h',
        marker_color=colors,
        hovertemplate='<b>%{y}</b><br>Score de Relación: %{x:.1f}<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Ranking: Relación Trabajo-Estudio por País<br><sub>Score ponderado (1=Sin relación, 5=Muy relacionado)</sub>',
            'x': 0.5,
            'font': {'size': 18}
        },
        xaxis_title='Score de Relación (1-5)',
        yaxis_title='Países',
        template='plotly_white',
        height=600,
        font={'size': 11}
    )
    
    # Añadir línea de promedio
    avg_score = np.mean(scores)
    fig.add_vline(
        x=avg_score,
        line_dash="dash",
        line_color="gray",
        annotation_text=f"Promedio: {avg_score:.1f}",
        annotation_position="top"
    )
    
    return fig


def create_spain_vs_europe_comparison(df, spain_color, other_countries_color):
    """
    Comparación detallada de España vs promedio europeo
    """
    # Datos de España
    spain_data = df[df['Country'] == 'ES'].iloc[0] if 'ES' in df['Country'].values else None
    
    if spain_data is None:
        return go.Figure().add_annotation(text="Datos de España no disponibles")
    
    # Promedio europeo (excluyendo España)
    df_europe = df[df['Country'] != 'ES']
    europe_avg = {
        'Very_Closely': df_europe['Very_Closely_Value'].mean(),
        'Rather_Closely': df_europe['Rather_Closely_Value'].mean(),
        'To_Some_Extent': df_europe['To_Some_Extent_Value'].mean(),
        'Rather_Not': df_europe['Rather_Not_Value'].mean(),
        'Not_At_All': df_europe['Not_At_All_Value'].mean()
    }
    
    categories = ['Muy<br>Relacionado', 'Bastante<br>Relacionado', 'Algo<br>Relacionado', 
                 'Poco<br>Relacionado', 'Nada<br>Relacionado']
    
    spain_values = [
        spain_data['Very_Closely_Value'],
        spain_data['Rather_Closely_Value'],
        spain_data['To_Some_Extent_Value'],
        spain_data['Rather_Not_Value'],
        spain_data['Not_At_All_Value']
    ]
    
    europe_values = list(europe_avg.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='España',
        x=categories,
        y=spain_values,
        marker_color=spain_color,
        hovertemplate='<b>España</b><br>%{x}: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Promedio Europeo',
        x=categories,
        y=europe_values,
        marker_color=other_countries_color,
        hovertemplate='<b>Promedio Europeo</b><br>%{x}: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': '🇪🇸 España vs 🇪🇺 Europa: Relación Trabajo-Estudio<br><sub>Comparación detallada por niveles de relación</sub>',
            'x': 0.5,
            'font': {'size': 18}
        },
        xaxis_title='Nivel de Relación',
        yaxis_title='Porcentaje (%)',
        barmode='group',
        template='plotly_white',
        hovermode='closest',
        font={'size': 12},
        height=500
    )
    
    return fig


def create_demographic_analysis_charts(df_main):
    """
    Análisis por segmentos demográficos (género, edad, campo de estudio)
    """
    # Leer datasets segmentados
    datasets = {
        'Por Género': PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy.RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_SEX,
        'Por Edad': PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy.RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_AGE,
        'Por Campo de Estudio': PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy.RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_FIELD_OF_STUDY
    }
    
    # Crear subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=['General', 'Por Género', 'Por Edad', 'Por Campo de Estudio'],
        specs=[[{"type": "bar"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "bar"}]]
    )
    
    # Datos generales (España vs Promedio)
    spain_data = df_main[df_main['Country'] == 'ES'].iloc[0] if 'ES' in df_main['Country'].values else None
    if spain_data is not None:
        spain_related = spain_data['Very_Closely_Value'] + spain_data['Rather_Closely_Value'] + spain_data['To_Some_Extent_Value']
        europe_related = df_main[df_main['Country'] != 'ES'][['Very_Closely_Value', 'Rather_Closely_Value', 'To_Some_Extent_Value']].sum(axis=1).mean()
        
        fig.add_trace(
            go.Bar(x=['España', 'Europa'], y=[spain_related, europe_related], 
                   marker_color=['#d62728', '#1f77b4'], name='Trabajo Relacionado'),
            row=1, col=1
        )
    
    # Los otros subgráficos requerirían leer y procesar cada dataset específico
    # Por simplicidad, mostraremos solo el resumen general aquí
    
    fig.update_layout(
        title='Análisis Demográfico: Relación Trabajo-Estudio',
        height=800,
        showlegend=False
    )
    
    return fig


# Función principal para ejecutar todas las visualizaciones
def create_all_work_study_relationship_visualizations():
    """
    Función principal que crea todas las visualizaciones de relación trabajo-estudio
    """
    print("📊 Cargando datos de relación trabajo-estudio...")
    
    # Cargar dataset principal
    df_work_study = read_work_study_relationship_dataset()
    
    print(f"✅ Dataset cargado: {df_work_study.shape[0]} países")
    print("🎨 Creando visualizaciones interactivas...")
    
    # Crear todas las visualizaciones
    fig1, fig2, fig3, fig4, fig5 = create_interactive_work_study_relationship_charts(df_work_study)
    
    # Mostrar las visualizaciones
    print("📈 Mostrando gráficos interactivos...")
    
    fig1.show()
    fig2.show() 
    fig3.show()
    fig4.show()
    fig5.show()
    
    # Generar resumen estadístico
    generate_work_study_summary(df_work_study)
    
    return df_work_study, fig1, fig2, fig3, fig4, fig5


def generate_work_study_summary(df):
    """
    Genera un resumen estadístico de la relación trabajo-estudio
    """
    print("\n" + "="*80)
    print("📋 RESUMEN: RELACIÓN ENTRE TRABAJO Y ESTUDIOS")
    print("="*80)
    
    # Calcular estadísticas
    df_stats = df.copy()
    df_stats['Related_Work_Total'] = (
        df_stats['Very_Closely_Value'].fillna(0) + 
        df_stats['Rather_Closely_Value'].fillna(0) + 
        df_stats['To_Some_Extent_Value'].fillna(0)
    )
    
    df_stats['Relationship_Score'] = (
        df_stats['Very_Closely_Value'].fillna(0) * 5 +
        df_stats['Rather_Closely_Value'].fillna(0) * 4 +
        df_stats['To_Some_Extent_Value'].fillna(0) * 3 +
        df_stats['Rather_Not_Value'].fillna(0) * 2 +
        df_stats['Not_At_All_Value'].fillna(0) * 1
    ) / 5
    
    print(f"\n📊 ESTADÍSTICAS GENERALES:")
    print(f"   • Promedio europeo de trabajo relacionado con estudios: {df_stats['Related_Work_Total'].mean():.1f}%")
    print(f"   • País con mayor relación trabajo-estudio: {df_stats.loc[df_stats['Related_Work_Total'].idxmax(), 'Country']} ({df_stats['Related_Work_Total'].max():.1f}%)")
    print(f"   • País con menor relación trabajo-estudio: {df_stats.loc[df_stats['Related_Work_Total'].idxmin(), 'Country']} ({df_stats['Related_Work_Total'].min():.1f}%)")
    print(f"   • Score promedio de relación (1-5): {df_stats['Relationship_Score'].mean():.2f}")
    
    if 'ES' in df['Country'].values:
        spain_stats = df[df['Country'] == 'ES'].iloc[0]
        spain_related = (spain_stats['Very_Closely_Value'] + 
                        spain_stats['Rather_Closely_Value'] + 
                        spain_stats['To_Some_Extent_Value'])
        spain_score = (spain_stats['Very_Closely_Value'] * 5 +
                      spain_stats['Rather_Closely_Value'] * 4 +
                      spain_stats['To_Some_Extent_Value'] * 3 +
                      spain_stats['Rather_Not_Value'] * 2 +
                      spain_stats['Not_At_All_Value'] * 1) / 5
        
        print(f"\n🇪🇸 DATOS DE ESPAÑA:")
        print(f"   • Trabajo relacionado con estudios: {spain_related:.1f}%")
        print(f"   • Muy relacionado: {spain_stats['Very_Closely_Value']:.1f}%")
        print(f"   • Nada relacionado: {spain_stats['Not_At_All_Value']:.1f}%")
        print(f"   • Score de relación: {spain_score:.2f}/5.0")
        
        # Comparación con promedio europeo
        europe_avg_related = df_stats[df_stats['Country'] != 'ES']['Related_Work_Total'].mean()
        europe_avg_score = df_stats[df_stats['Country'] != 'ES']['Relationship_Score'].mean()
        
        print(f"\n🇪🇺 COMPARACIÓN CON EUROPA:")
        print(f"   • España vs Europa (trabajo relacionado): {spain_related:.1f}% vs {europe_avg_related:.1f}%")
        print(f"   • España vs Europa (score relación): {spain_score:.2f} vs {europe_avg_score:.2f}")
        
        if spain_related > europe_avg_related:
            print(f"   ✅ España está {spain_related - europe_avg_related:.1f} puntos POR ENCIMA del promedio europeo")
        else:
            print(f"   ⚠️ España está {europe_avg_related - spain_related:.1f} puntos POR DEBAJO del promedio europeo")


def create_time_budget_satisfaction_charts(df_job_related, df_job_not_related):
    """
    Crea visualizaciones sobre satisfacción con presupuesto de tiempo para trabajo relacionado y no relacionado
    """
    spain_color = '#d62728'
    other_color = '#1f77b4'
    
    # Crear subplot con 2 gráficos lado a lado
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=['Trabajo Relacionado con Estudios', 'Trabajo NO Relacionado con Estudios'],
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )
    
    # Función helper para añadir barras
    def add_bars_to_subplot(df, row, col, title_suffix=""):
        if df is None or df.empty:
            return
            
        countries = df['Country'].tolist()
        less_time = df['Less_Time_Value'].fillna(0).tolist()
        same_time = df['Same_Time_Value'].fillna(0).tolist()
        more_time = df['More_Time_Value'].fillna(0).tolist()
        
        # Destacar España
        colors_less = [spain_color if country == 'ES' else '#ff7f7f' for country in countries]
        colors_same = [spain_color if country == 'ES' else '#ffbb78' for country in countries]  
        colors_more = [spain_color if country == 'ES' else '#2ca02c' for country in countries]
        
        fig.add_trace(go.Bar(
            name=f'Menos Tiempo{title_suffix}',
            x=countries,
            y=less_time,
            marker_color=colors_less,
            hovertemplate='<b>%{x}</b><br>Menos Tiempo: %{y:.1f}%<extra></extra>',
            showlegend=(col == 1)  # Solo mostrar leyenda en el primer subplot
        ), row=row, col=col)
        
        fig.add_trace(go.Bar(
            name=f'Mismo Tiempo{title_suffix}',
            x=countries,
            y=same_time,
            marker_color=colors_same,
            hovertemplate='<b>%{x}</b><br>Mismo Tiempo: %{y:.1f}%<extra></extra>',
            showlegend=(col == 1)
        ), row=row, col=col)
        
        fig.add_trace(go.Bar(
            name=f'Más Tiempo{title_suffix}',
            x=countries,
            y=more_time,
            marker_color=colors_more,
            hovertemplate='<b>%{x}</b><br>Más Tiempo: %{y:.1f}%<extra></extra>',
            showlegend=(col == 1)
        ), row=row, col=col)
    
    # Añadir datos a ambos subplots
    add_bars_to_subplot(df_job_related, 1, 1)
    add_bars_to_subplot(df_job_not_related, 1, 2)
    
    fig.update_layout(
        title={
            'text': 'Preferencias de Tiempo en Trabajo Remunerado<br><sub>¿Cuánto tiempo les gustaría dedicar al trabajo remunerado?</sub>',
            'x': 0.5,
            'font': {'size': 18}
        },
        barmode='group',
        template='plotly_white',
        height=600,
        font={'size': 11}
    )
    
    # Actualizar ejes X
    fig.update_xaxes(tickangle=45, row=1, col=1)
    fig.update_xaxes(tickangle=45, row=1, col=2)
    
    # Actualizar ejes Y
    fig.update_yaxes(title_text="Porcentaje (%)", row=1, col=1)
    fig.update_yaxes(title_text="Porcentaje (%)", row=1, col=2)
    
    return fig


def create_study_abandoning_analysis_charts(df_financial, df_work_afford, df_satisfaction):
    """
    Crea análisis sobre consideración de abandono de estudios por diferentes motivos
    """
    spain_color = '#d62728'
    
    # Crear subplot con 3 gráficos
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            'Por Dificultades Financieras',
            'Por Necesidad de Trabajar', 
            'Por Insatisfacción',
            'Comparación España vs Europa'
        ],
        specs=[[{"type": "bar"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "bar"}]]
    )
    
    def create_abandoning_bars(df, row, col, show_legend=False):
        if df is None or df.empty:
            return
            
        countries = df['Country'].tolist()
        
        # Agrupar frecuencias altas vs bajas
        high_frequency = (df['Very_Often_Value'].fillna(0) + df['Often_Value'].fillna(0)).tolist()
        low_frequency = (df['Rarely_Value'].fillna(0) + df['Never_Value'].fillna(0)).tolist()
        
        colors_high = [spain_color if country == 'ES' else '#ff4444' for country in countries]
        colors_low = [spain_color if country == 'ES' else '#44ff44' for country in countries]
        
        fig.add_trace(go.Bar(
            name='Alta Frecuencia',
            x=countries,
            y=high_frequency,
            marker_color=colors_high,
            hovertemplate='<b>%{x}</b><br>Alta Frecuencia: %{y:.1f}%<extra></extra>',
            showlegend=show_legend
        ), row=row, col=col)
        
        fig.add_trace(go.Bar(
            name='Baja Frecuencia',
            x=countries,
            y=low_frequency,
            marker_color=colors_low,
            hovertemplate='<b>%{x}</b><br>Baja Frecuencia: %{y:.1f}%<extra></extra>',
            showlegend=show_legend
        ), row=row, col=col)
    
    # Añadir datos a los subplots
    create_abandoning_bars(df_financial, 1, 1, True)
    create_abandoning_bars(df_work_afford, 1, 2)
    create_abandoning_bars(df_satisfaction, 2, 1)
    
    # Subplot 4: Comparación España vs Europa
    if df_financial is not None and 'ES' in df_financial['Country'].values:
        spain_financial = df_financial[df_financial['Country'] == 'ES'].iloc[0]
        europe_financial = df_financial[df_financial['Country'] != 'ES']
        
        if not europe_financial.empty:
            spain_high_freq = spain_financial['Very_Often_Value'] + spain_financial['Often_Value']
            europe_avg_high_freq = (europe_financial['Very_Often_Value'].fillna(0) + 
                                   europe_financial['Often_Value'].fillna(0)).mean()
            
            fig.add_trace(go.Bar(
                name='España',
                x=['España'],
                y=[spain_high_freq],
                marker_color=spain_color,
                hovertemplate='<b>España</b><br>%{y:.1f}%<extra></extra>',
                showlegend=False
            ), row=2, col=2)
            
            fig.add_trace(go.Bar(
                name='Promedio Europeo',
                x=['Promedio Europeo'],
                y=[europe_avg_high_freq],
                marker_color='#1f77b4',
                hovertemplate='<b>Europa</b><br>%{y:.1f}%<extra></extra>',
                showlegend=False
            ), row=2, col=2)
    
    fig.update_layout(
        title={
            'text': 'Consideración de Abandono de Estudios por Diferentes Motivos<br><sub>Frecuencia con la que los estudiantes consideran abandonar</sub>',
            'x': 0.5,
            'font': {'size': 16}
        },
        barmode='group',
        template='plotly_white',
        height=800,
        font={'size': 10}
    )
    
    # Actualizar ejes
    for i in range(1, 3):
        for j in range(1, 3):
            fig.update_xaxes(tickangle=45, row=i, col=j)
            fig.update_yaxes(title_text="Porcentaje (%)", row=i, col=j)
    
    return fig


def create_performance_self_assessment_chart(df_performance):
    """
    Crea visualización de auto-evaluación de rendimiento académico
    """
    if df_performance is None or df_performance.empty:
        return go.Figure().add_annotation(text="Datos no disponibles")
    
    spain_color = '#d62728'
    other_color = '#1f77b4'
    
    countries = df_performance['Country'].tolist()
    
    # Agrupar rendimientos
    good_performance = (df_performance['Very_Good_Value'].fillna(0) + 
                       df_performance['Good_Value'].fillna(0)).tolist()
    poor_performance = (df_performance['Poor_Value'].fillna(0) + 
                       df_performance['Very_Poor_Value'].fillna(0)).tolist()
    satisfactory = df_performance['Satisfactory_Value'].fillna(0).tolist()
    
    fig = go.Figure()
    
    # Colores destacando España
    colors_good = [spain_color if country == 'ES' else '#2ca02c' for country in countries]
    colors_satisfactory = [spain_color if country == 'ES' else '#ffbb78' for country in countries]
    colors_poor = [spain_color if country == 'ES' else '#ff4444' for country in countries]
    
    fig.add_trace(go.Bar(
        name='Buen Rendimiento',
        x=countries,
        y=good_performance,
        marker_color=colors_good,
        hovertemplate='<b>%{x}</b><br>Buen Rendimiento: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Rendimiento Satisfactorio',
        x=countries,
        y=satisfactory,
        marker_color=colors_satisfactory,
        hovertemplate='<b>%{x}</b><br>Satisfactorio: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Rendimiento Deficiente',
        x=countries,
        y=poor_performance,
        marker_color=colors_poor,
        hovertemplate='<b>%{x}</b><br>Deficiente: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Auto-evaluación del Rendimiento Académico<br><sub>¿Cómo evalúan los estudiantes su propio rendimiento?</sub>',
            'x': 0.5,
            'font': {'size': 18}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        barmode='stack',
        template='plotly_white',
        height=600,
        font={'size': 12},
        xaxis={'tickangle': 45}
    )
    
    # Destacar España con anotación
    if 'ES' in countries:
        spain_idx = countries.index('ES')
        spain_good = good_performance[spain_idx]
        fig.add_annotation(
            x=spain_idx,
            y=spain_good + 10,
            text=f"🇪🇸 España<br>{spain_good:.1f}% buen rendimiento",
            showarrow=True,
            arrowhead=2,
            arrowcolor=spain_color,
            bgcolor=spain_color,
            bordercolor="white",
            font={'color': 'white', 'size': 10}
        )
    
    return fig


def create_comprehensive_work_impact_dashboard():
    """
    Función principal que crea un dashboard completo del impacto del trabajo en los estudios
    """
    print("📊 Cargando datos de impacto del trabajo en los estudios...")
    
    # Cargar todos los datasets de impacto
    datasets = {}
    
    try:
        # Dataset de satisfacción con tiempo de trabajo (trabajo no relacionado)
        datasets['time_budget_not_related'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_NOTRELATED
        )
        print("✅ Dataset de satisfacción temporal (trabajo no relacionado) cargado")
        
        # Dataset de satisfacción con tiempo de trabajo (trabajo relacionado)  
        datasets['time_budget_related'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_RELATED
        )
        print("✅ Dataset de satisfacción temporal (trabajo relacionado) cargado")
        
        # Dataset de abandono por dificultades financieras
        datasets['abandoning_financial'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__E_FINANCIAL_DIFFICULTIES
        )
        print("✅ Dataset de abandono por dificultades financieras cargado")
        
        # Dataset de abandono por satisfacción
        datasets['abandoning_satisfaction'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__E_SATISFACTION
        )
        print("✅ Dataset de abandono por satisfacción cargado")
        
        # Dataset de abandono por necesidad de trabajar
        datasets['abandoning_work_afford'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__S_WORK_TO_AFFORD_TO_STUDY
        )
        print("✅ Dataset de abandono por necesidad de trabajar cargado")
        
        # Dataset de auto-evaluación de rendimiento
        datasets['performance_self_assessment'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_ABANDONING_ALL_T__S_PERFORMANCE_SELF_ASSESSMENT
        )
        print("✅ Dataset de auto-evaluación de rendimiento cargado")
        
    except Exception as e:
        print(f"⚠️ Error cargando algunos datasets: {e}")
    
    print(f"📈 Datasets cargados exitosamente: {len(datasets)}")
    print("🎨 Creando visualizaciones interactivas...")
    
    # Crear visualizaciones
    figures = {}
    
    # 1. Gráfico de satisfacción con presupuesto de tiempo
    if 'time_budget_related' in datasets and 'time_budget_not_related' in datasets:
        figures['time_budget'] = create_time_budget_satisfaction_charts(
            datasets['time_budget_related'], 
            datasets['time_budget_not_related']
        )
        print("✅ Gráfico de satisfacción temporal creado")
    
    # 2. Análisis de abandono de estudios
    if all(key in datasets for key in ['abandoning_financial', 'abandoning_work_afford', 'abandoning_satisfaction']):
        figures['study_abandoning'] = create_study_abandoning_analysis_charts(
            datasets['abandoning_financial'],
            datasets['abandoning_work_afford'], 
            datasets['abandoning_satisfaction']
        )
        print("✅ Análisis de abandono de estudios creado")
    
    # 3. Auto-evaluación de rendimiento
    if 'performance_self_assessment' in datasets:
        figures['performance'] = create_performance_self_assessment_chart(
            datasets['performance_self_assessment']
        )
        print("✅ Gráfico de auto-evaluación de rendimiento creado")
    
    # Mostrar todas las visualizaciones
    print("📊 Mostrando dashboard de impacto del trabajo en estudios...")
    
    for name, fig in figures.items():
        print(f"Mostrando: {name}")
        fig.show()
    
    # Generar resumen estadístico
    generate_work_impact_summary(datasets)
    
    return datasets, figures


def generate_work_impact_summary(datasets):
    """
    Genera un resumen estadístico del impacto del trabajo en los estudios
    """
    print("\n" + "="*80)
    print("📋 RESUMEN: IMPACTO DEL TRABAJO EN LOS ESTUDIOS")
    print("="*80)
    
    # Análisis de satisfacción con tiempo de trabajo
    if 'time_budget_not_related' in datasets:
        df_time = datasets['time_budget_not_related']
        if 'ES' in df_time['Country'].values:
            spain_time = df_time[df_time['Country'] == 'ES'].iloc[0]
            print(f"\n⏰ SATISFACCIÓN CON TIEMPO DE TRABAJO (España):")
            print(f"   • Prefiere menos tiempo trabajando: {spain_time['Less_Time_Value']:.1f}%")
            print(f"   • Prefiere mismo tiempo trabajando: {spain_time['Same_Time_Value']:.1f}%")
            print(f"   • Prefiere más tiempo trabajando: {spain_time['More_Time_Value']:.1f}%")
    
    # Análisis de consideración de abandono
    if 'abandoning_financial' in datasets:
        df_abandon = datasets['abandoning_financial']
        if 'ES' in df_abandon['Country'].values:
            spain_abandon = df_abandon[df_abandon['Country'] == 'ES'].iloc[0]
            high_freq_abandon = spain_abandon['Very_Often_Value'] + spain_abandon['Often_Value']
            never_abandon = spain_abandon['Never_Value']
            
            print(f"\n🚨 CONSIDERACIÓN DE ABANDONO POR MOTIVOS FINANCIEROS (España):")
            print(f"   • Considera abandono frecuentemente: {high_freq_abandon:.1f}%")
            print(f"   • Nunca considera abandono: {never_abandon:.1f}%")
            
            # Comparación con Europa
            europe_abandon = df_abandon[df_abandon['Country'] != 'ES']
            if not europe_abandon.empty:
                europe_high_freq = (europe_abandon['Very_Often_Value'].fillna(0) + 
                                  europe_abandon['Often_Value'].fillna(0)).mean()
                print(f"   • Europa (promedio considera abandono): {europe_high_freq:.1f}%")
                
                if high_freq_abandon > europe_high_freq:
                    print(f"   ⚠️ España está {high_freq_abandon - europe_high_freq:.1f} puntos POR ENCIMA del promedio europeo")
                else:
                    print(f"   ✅ España está {europe_high_freq - high_freq_abandon:.1f} puntos POR DEBAJO del promedio europeo")
    
    # Análisis de rendimiento académico
    if 'performance_self_assessment' in datasets:
        df_perf = datasets['performance_self_assessment']
        if 'ES' in df_perf['Country'].values:
            spain_perf = df_perf[df_perf['Country'] == 'ES'].iloc[0]
            good_performance = spain_perf['Very_Good_Value'] + spain_perf['Good_Value']
            poor_performance = spain_perf['Poor_Value'] + spain_perf['Very_Poor_Value']
            
            print(f"\n📚 AUTO-EVALUACIÓN DE RENDIMIENTO ACADÉMICO (España):")
            print(f"   • Buen rendimiento académico: {good_performance:.1f}%")
            print(f"   • Rendimiento deficiente: {poor_performance:.1f}%")
            print(f"   • Rendimiento satisfactorio: {spain_perf['Satisfactory_Value']:.1f}%")
    
    print(f"\n💡 CONCLUSIONES CLAVE:")
    print(f"   • Los datos muestran el impacto diferencial del trabajo en los estudios")
    print(f"   • España presenta patrones específicos comparado con otros países europeos")
    print(f"   • Es importante considerar tanto aspectos positivos como negativos del trabajo estudiantil")


# Función principal actualizada para incluir análisis de impacto
def create_complete_student_work_analysis():
    """
    Función principal que crea el análisis completo del trabajo estudiantil:
    1. Motivación para trabajar
    2. Relación trabajo-estudio  
    3. Impacto del trabajo en los estudios
    """
    print("🚀 INICIANDO ANÁLISIS COMPLETO DEL TRABAJO ESTUDIANTIL")
    print("="*60)
    
    # 1. Análisis de motivación para trabajar
    print("\n📊 FASE 1: Motivación para trabajar y costear estudios")
    df_work_motive = read_work_motive_afford_study_dataset()
    create_work_necessity_charts(df_work_motive)
    
    # 2. Análisis de relación trabajo-estudio
    print("\n📊 FASE 2: Relación entre trabajo y estudios")
    df_work_study, fig1, fig2, fig3, fig4, fig5 = create_all_work_study_relationship_visualizations()
    
    # 3. Análisis de impacto del trabajo en estudios
    print("\n📊 FASE 3: Impacto del trabajo en los estudios")
    datasets_impact, figures_impact = create_comprehensive_work_impact_dashboard()
    
    print("\n✅ ANÁLISIS COMPLETO FINALIZADO")
    print("="*60)
    
    return {
        'work_motive': df_work_motive,
        'work_study_relationship': df_work_study,
        'work_impact': datasets_impact,
        'figures_relationship': [fig1, fig2, fig3, fig4, fig5],
        'figures_impact': figures_impact
    }


# ========================================================================
# FUNCIONES ESPECÍFICAS PARA STREAMLIT SCROLLYTELLING
# ========================================================================

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
        
        # Dataset de satisfacción temporal (trabajo no relacionado)
        datasets['time_budget_not_related'] = read_work_impact_dataset(
            PreprocessedDatasetsNamesImpactsOnStudyForWork.IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_NOTRELATED
        )
        
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
        # 1. Gráfico de abandono por dificultades financieras (España destacada)
        if 'abandoning_financial' in datasets:
            figures['abandono_financiero'] = create_streamlit_abandoning_chart(
                datasets['abandoning_financial'],
                title="Consideración de Abandono por Dificultades Financieras",
                subtitle="Frecuencia con la que los estudiantes consideran abandonar por motivos económicos"
            )
            
        # 2. Gráfico de abandono por necesidad de trabajar (España destacada)
        if 'abandoning_work_afford' in datasets:
            figures['abandono_trabajo'] = create_streamlit_abandoning_chart(
                datasets['abandoning_work_afford'],
                title="Consideración de Abandono por Necesidad de Trabajar",
                subtitle="Estudiantes que consideran abandonar para poder trabajar más"
            )
            
        # 3. Comparación España vs Europa - Impacto del trabajo
        if 'abandoning_financial' in datasets and 'abandoning_work_afford' in datasets:
            figures['espana_vs_europa_impacto'] = create_spain_europe_impact_comparison(
                datasets['abandoning_financial'],
                datasets['abandoning_work_afford']
            )
            
        print(f"✅ {len(figures)} figuras creadas para Streamlit")
        
    except Exception as e:
        print(f"⚠️ Error creando figuras: {e}")
    
    return figures


def create_streamlit_abandoning_chart(df, title, subtitle):
    """
    Crea un gráfico de abandono optimizado para Streamlit con España destacada
    """
    if df is None or df.empty:
        return go.Figure().add_annotation(text="Datos no disponibles")
    
    spain_color = '#d62728'
    europe_color = '#1f77b4'
    
    countries = df['Country'].tolist()
    
    # Calcular frecuencias de consideración de abandono
    high_frequency = (df['Very_Often_Value'].fillna(0) + df['Often_Value'].fillna(0)).tolist()
    never_considers = df['Never_Value'].fillna(0).tolist()
    
    # Ordenar países por frecuencia alta (descendente)
    country_freq_pairs = list(zip(countries, high_frequency, never_considers))
    country_freq_pairs.sort(key=lambda x: x[1], reverse=True)
    
    sorted_countries = [pair[0] for pair in country_freq_pairs]
    sorted_high_freq = [pair[1] for pair in country_freq_pairs]
    sorted_never = [pair[2] for pair in country_freq_pairs]
    
    # Colores destacando España
    colors_high = [spain_color if country == 'ES' else '#ff6666' for country in sorted_countries]
    colors_never = [spain_color if country == 'ES' else '#66cc66' for country in sorted_countries]
    
    fig = go.Figure()
    
    # Barras para alta frecuencia
    fig.add_trace(go.Bar(
        name='Considera Abandono Frecuentemente',
        x=sorted_countries,
        y=sorted_high_freq,
        marker_color=colors_high,
        hovertemplate='<b>%{x}</b><br>Considera abandono: %{y:.1f}%<extra></extra>',
        opacity=0.8
    ))
    
    # Barras para nunca considera
    fig.add_trace(go.Bar(
        name='Nunca Considera Abandono',
        x=sorted_countries,
        y=sorted_never,
        marker_color=colors_never,
        hovertemplate='<b>%{x}</b><br>Nunca considera: %{y:.1f}%<extra></extra>',
        opacity=0.8
    ))
    
    fig.update_layout(
        title={
            'text': f'{title}<br><sub>{subtitle}</sub>',
            'x': 0.5,
            'font': {'size': 16}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        barmode='group',
        template='plotly_white',
        height=500,
        font={'size': 11},
        xaxis={'tickangle': 45},
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': -0.3,
            'xanchor': 'center',
            'x': 0.5
        }
    )
    
    # Destacar España con anotación
    if 'ES' in sorted_countries:
        spain_idx = sorted_countries.index('ES')
        spain_freq = sorted_high_freq[spain_idx]
        
        fig.add_annotation(
            x=spain_idx,
            y=spain_freq + 2,
            text=f"🇪🇸 {spain_freq:.1f}%",
            showarrow=True,
            arrowhead=2,
            arrowcolor=spain_color,
            bgcolor=spain_color,
            bordercolor="white",
            font={'color': 'white', 'size': 10}
        )
    
    return fig


def create_spain_europe_impact_comparison(df_financial, df_work_afford):
    """
    Crea una comparación específica España vs Europa para el impacto del trabajo
    """
    fig = go.Figure()
    
    # Datos de España
    spain_financial = df_financial[df_financial['Country'] == 'ES'].iloc[0] if 'ES' in df_financial['Country'].values else None
    spain_work = df_work_afford[df_work_afford['Country'] == 'ES'].iloc[0] if 'ES' in df_work_afford['Country'].values else None
    
    # Promedios europeos (sin España)
    europe_financial = df_financial[df_financial['Country'] != 'ES']
    europe_work = df_work_afford[df_work_afford['Country'] != 'ES']
    
    if spain_financial is not None and spain_work is not None and not europe_financial.empty and not europe_work.empty:
        
        # Calcular métricas
        spain_financial_abandon = spain_financial['Very_Often_Value'] + spain_financial['Often_Value']
        spain_work_abandon = spain_work['Very_Often_Value'] + spain_work['Often_Value']
        
        europe_financial_abandon = (europe_financial['Very_Often_Value'].fillna(0) + 
                                   europe_financial['Often_Value'].fillna(0)).mean()
        europe_work_abandon = (europe_work['Very_Often_Value'].fillna(0) + 
                              europe_work['Often_Value'].fillna(0)).mean()
        
        categories = ['Abandono por<br>Dificultades Financieras', 'Abandono por<br>Necesidad de Trabajar']
        spain_values = [spain_financial_abandon, spain_work_abandon]
        europe_values = [europe_financial_abandon, europe_work_abandon]
        
        # Crear barras agrupadas
        fig.add_trace(go.Bar(
            name='🇪🇸 España',
            x=categories,
            y=spain_values,
            marker_color='#d62728',
            hovertemplate='<b>España</b><br>%{x}: %{y:.1f}%<extra></extra>',
            width=0.4
        ))
        
        fig.add_trace(go.Bar(
            name='🇪🇺 Promedio Europeo',
            x=categories,
            y=europe_values,
            marker_color='#1f77b4',
            hovertemplate='<b>Europa</b><br>%{x}: %{y:.1f}%<extra></extra>',
            width=0.4
        ))
        
        # Añadir valores en las barras
        for i, (spain_val, europe_val) in enumerate(zip(spain_values, europe_values)):
            fig.add_annotation(
                x=i,
                y=spain_val + 1,
                text=f"{spain_val:.1f}%",
                showarrow=False,
                font={'color': '#d62728', 'size': 12, 'family': 'Arial Black'}
            )
            fig.add_annotation(
                x=i,
                y=europe_val + 1,
                text=f"{europe_val:.1f}%",
                showarrow=False,
                font={'color': '#1f77b4', 'size': 12, 'family': 'Arial Black'}
            )
    
    fig.update_layout(
        title={
            'text': '🇪🇸 España vs 🇪🇺 Europa: Impacto del Trabajo en los Estudios<br><sub>Comparación de frecuencia de consideración de abandono</sub>',
            'x': 0.5,
            'font': {'size': 16}
        },
        xaxis_title='Motivos de Consideración de Abandono',
        yaxis_title='Porcentaje (%)',
        barmode='group',
        template='plotly_white',
        height=500,
        font={'size': 12},
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': -0.2,
            'xanchor': 'center',
            'x': 0.5
        }
    )
    
    return fig


def get_all_figures_for_streamlit():
    """
    Función principal que obtiene TODAS las figuras optimizadas para Streamlit
    Incluye: motivación, relación trabajo-estudio, e impacto
    """
    print("🚀 Preparando todas las figuras para Streamlit scrollytelling...")
    
    all_figures = {}
    
    # 1. Figuras de motivación para trabajar
    try:
        print("📊 Cargando figuras de motivación...")
        df_work_motive = read_work_motive_afford_study_dataset()
        
        # Crear figura específica para Streamlit
        all_figures['motivacion_trabajar'] = create_streamlit_work_motivation_chart(df_work_motive)
        print("✅ Figura de motivación creada")
        
    except Exception as e:
        print(f"⚠️ Error con figuras de motivación: {e}")
    
    # 2. Figuras de relación trabajo-estudio
    try:
        print("📊 Cargando figuras de relación trabajo-estudio...")
        df_work_study = read_work_study_relationship_dataset()
        
        # Crear figura simplificada para Streamlit
        all_figures['relacion_trabajo_estudio'] = create_streamlit_work_study_relationship_chart(df_work_study)
        print("✅ Figura de relación trabajo-estudio creada")
        
    except Exception as e:
        print(f"⚠️ Error con figuras de relación: {e}")
    
    # 3. Figuras de impacto del trabajo
    try:
        print("📊 Cargando figuras de impacto...")
        impact_figures = get_work_impact_figures_for_streamlit()
        all_figures.update(impact_figures)
        print(f"✅ {len(impact_figures)} figuras de impacto añadidas")
        
    except Exception as e:
        print(f"⚠️ Error con figuras de impacto: {e}")
    
    print(f"🎯 Total de figuras preparadas para Streamlit: {len(all_figures)}")
    
    return all_figures


def create_streamlit_work_motivation_chart(df):
    """
    Crea gráfico de motivación para trabajar optimizado para Streamlit
    """
    if df is None or df.empty:
        return go.Figure().add_annotation(text="Datos no disponibles")
    
    # Calcular necesidad de trabajar (agrupando niveles altos)
    df_chart = df.copy()
    df_chart['Need_Work_Total'] = (
        df_chart['Applies_Totally_Value'].fillna(0) + 
        df_chart['Applies_Rather_Value'].fillna(0) + 
        df_chart['Applies_Partially_Value'].fillna(0)
    )
    
    # Ordenar por necesidad de trabajar
    df_chart = df_chart.sort_values('Need_Work_Total', ascending=True)
    
    countries = df_chart['Country'].tolist()
    need_work = df_chart['Need_Work_Total'].tolist()
    
    # Colores destacando España
    colors = ['#d62728' if country == 'ES' else '#1f77b4' for country in countries]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=countries,
        y=need_work,
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Necesita trabajar: %{y:.1f}%<extra></extra>',
        opacity=0.8
    ))
    
    fig.update_layout(
        title={
            'text': 'Necesidad de Trabajar para Costear Estudios<br><sub>Porcentaje de estudiantes que necesitan trabajar</sub>',
            'x': 0.5,
            'font': {'size': 16}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        template='plotly_white',
        height=500,
        font={'size': 11},
        xaxis={'tickangle': 45}
    )
    
    # Destacar España
    if 'ES' in countries:
        spain_idx = countries.index('ES')
        spain_value = need_work[spain_idx]
        
        fig.add_annotation(
            x=spain_idx,
            y=spain_value + 2,
            text=f"🇪🇸 {spain_value:.1f}%",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#d62728',
            bgcolor='#d62728',
            bordercolor="white",
            font={'color': 'white', 'size': 10}
        )
    
    return fig


def create_streamlit_work_study_relationship_chart(df):
    """
    Crea gráfico de relación trabajo-estudio optimizado para Streamlit
    """
    if df is None or df.empty:
        return go.Figure().add_annotation(text="Datos no disponibles")
    
    # Calcular trabajo relacionado con estudios
    df_chart = df.copy()
    df_chart['Related_Work'] = (
        df_chart['Very_Closely_Value'].fillna(0) + 
        df_chart['Rather_Closely_Value'].fillna(0) + 
        df_chart['To_Some_Extent_Value'].fillna(0)
    )
    
    # Ordenar por relación trabajo-estudio
    df_chart = df_chart.sort_values('Related_Work', ascending=True)
    
    countries = df_chart['Country'].tolist()
    related_work = df_chart['Related_Work'].tolist()
    
    # Colores destacando España
    colors = ['#d62728' if country == 'ES' else '#2ca02c' for country in countries]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=countries,
        y=related_work,
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Trabajo relacionado: %{y:.1f}%<extra></extra>',
        opacity=0.8
    ))
    
    fig.update_layout(
        title={
            'text': 'Relación entre Trabajo y Estudios<br><sub>Porcentaje de estudiantes con trabajo relacionado con sus estudios</sub>',
            'x': 0.5,
            'font': {'size': 16}
        },
        xaxis_title='Países',
        yaxis_title='Porcentaje (%)',
        template='plotly_white',
        height=500,
        font={'size': 11},
        xaxis={'tickangle': 45}
    )
    
    # Destacar España
    if 'ES' in countries:
        spain_idx = countries.index('ES')
        spain_value = related_work[spain_idx]
        
        fig.add_annotation(
            x=spain_idx,
            y=spain_value + 2,
            text=f"🇪🇸 {spain_value:.1f}%",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#d62728',
            bgcolor='#d62728',
            bordercolor="white",
            font={'color': 'white', 'size': 10}
        )
    
    return fig


if __name__ == "__main__":
    # Ejecutar análisis completo del trabajo estudiantil
    print("🎯 INICIANDO ANÁLISIS COMPLETO DEL TRABAJO ESTUDIANTIL")
    print("="*60)
    print("Este análisis incluye:")
    print("   1. 💰 Motivación para trabajar y costear estudios")
    print("   2. 🔗 Relación entre trabajo y estudios")
    print("   3. 📊 Impacto del trabajo en los estudios")
    print("   🇪🇸 Con España como foco principal de comparación")
    print("="*60)

    # Ejecutar análisis completo
    results = create_complete_student_work_analysis()
    
    print("\n🎉 ANÁLISIS COMPLETADO EXITOSAMENTE!")
    print(f"📈 Datasets procesados: {len(results)}")
    print("📊 Las visualizaciones interactivas han sido generadas y mostradas")
    print("\n💡 Los resultados incluyen:")
    print("   • Datos de motivación para trabajar")
    print("   • Análisis de relación trabajo-estudio")  
    print("   • Impacto del trabajo en rendimiento académico")
    print("   • Comparaciones detalladas España vs Europa")
    print("   • Resúmenes estadísticos completos")