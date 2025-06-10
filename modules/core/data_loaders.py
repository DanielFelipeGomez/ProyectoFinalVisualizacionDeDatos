"""
Módulo centralizado para carga de datos
Contiene todas las funciones de lectura y procesamiento de datasets
"""

import pandas as pd
from enum import Enum

# === DEFINICIÓN DE ENUMS ===

class PreprocessedDatasetsNamesImpactsOnStudyForWork(Enum):
    IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_NOTRELATED = 'data/preprocessed_impact_by_job/E8_time_budget_satisf_job_notrelated__all_students__all_contries.xlsx'
    IMPACT_ON_STUDY_FOR_WORK_TIME_BUDGET_SATISFACTION_JOB_RELATED = 'data/preprocessed_impact_by_job/E8_time_budget_all__e_satisf__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__E_FINANCIAL_DIFFICULTIES = 'data/preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__e_financial_difficulties__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__E_SATISFACTION = 'data/preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__e_satisf__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_WORK_TO_AFFORD_TO_STUDY = 'data/preprocessed_impact_by_job/E8_assess_study_abandoning_all_t__s_work_to_afford_to_study__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_RELATIONSHIP_JOB_STUDY = 'data/preprocessed_impact_by_job/E8_health__s_relationship_job_study__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_PERFORMANCE_SELF_ASSESSMENT = 'data/preprocessed_impact_by_job/E8_selfevaluation__s_performance_self_assessment__ES.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_NOT_LIVING_WITH_PARENTS = 'data/preprocessed_impact_by_job/E8_time_budget_all__e_notlivingwithparents__all_contries.xlsx'
    IMPACT_ON_STUDY_ABANDONING_ALL_T__S_TEACHING_TYPE = 'data/preprocessed_impact_by_job/E8_work_related_study5__e_teachingtype__ES.xlsx'

class PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy(Enum):
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY = 'data/preprocessed_relationship_study_job/E8_work_related_study5__all_students__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_AGE = 'data/preprocessed_relationship_study_job/E8_work_related_study5__e_age__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_FIELD_OF_STUDY = 'data/preprocessed_relationship_study_job/E8_work_related_study5__e_field_of_study__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_INTENS = 'data/preprocessed_relationship_study_job/E8_work_related_study5__e_intens__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_QUALIFICATION = 'data/preprocessed_relationship_study_job/E8_work_related_study5__e_qualification__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_SEX = 'data/preprocessed_relationship_study_job/E8_work_related_study5__e_sex__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_S_FULL_OR_PART_TIME_STUDY_PROGRAMME = 'data/preprocessed_relationship_study_job/E8_work_related_study5__s_full_or_part_time_study_programme__all_contries.xlsx'

class PreprocessedDatasetsNamesWorkMotiveAffordStudy(Enum):
    WORK_MOTIVE_AFFORD_STUDY = 'data/preprocessed_excels/E8_work_motive_afford_study_5__all_students__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_SEX = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_sex__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_AGE = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_age__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS = 'data/preprocessed_excels/E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS = 'data/preprocessed_excels/E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx'

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

# === CONSTANTES ===

NUM_SPANISH_PARTICIPANTS = 9072

# === FUNCIONES DE CARGA DE DATOS ===

def read_dataset(dataset_name):
    """Función genérica para leer datasets"""
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

def read_work_study_relationship_dataset(dataset_enum=None):
    """
    Función especializada para leer el dataset de relación trabajo-estudio.
    Estos Excel tienen estructuras complejas con múltiples niveles de headers.
    """
    if dataset_enum is None:
        dataset_enum = PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy.RELATIONSHIP_BETWEEN_WORK_AND_STUDY
    
    try:
        # Leer sin headers para procesar manualmente
        df = pd.read_excel(dataset_enum.value, header=None)
        
        # Los datos reales empiezan en la fila 3 (índice 3)
        data_df = df.iloc[3:].copy()
        
        # Crear nombres de columnas descriptivos para relación trabajo-estudio
        column_names = ['Country']
        relationship_levels = [
            'Very_Closely',      # Muy relacionado
            'Closely',           # Relacionado
            'Somewhat',          # Algo relacionado
            'Not_Closely',       # Poco relacionado
            'Not_At_All'         # Nada relacionado
        ]
        
        # Agregar columnas Value, Unit, Count para cada nivel
        for level in relationship_levels:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Ajustar a la cantidad real de columnas disponibles
        data_df.columns = column_names[:len(data_df.columns)]
        data_df = data_df.reset_index(drop=True)
        data_df = data_df.dropna(subset=['Country'])
        
        # Convertir columnas numéricas
        for level in relationship_levels:
            value_col = f'{level}_Value'
            count_col = f'{level}_Count'
            if value_col in data_df.columns:
                data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
            if count_col in data_df.columns:
                data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
        
        # Crear aliases para compatibilidad con código existente
        if 'Very_Closely_Value' in data_df.columns:
            data_df['Very_Closely_Value'] = data_df['Very_Closely_Value']
        if 'Not_At_All_Value' in data_df.columns:
            data_df['Not_At_All_Value'] = data_df['Not_At_All_Value']
        
        # Verificar que España esté en los datos
        if 'ES' not in data_df['Country'].values:
            print(f"⚠️ España no encontrada en {dataset_enum.value}")
        
        return data_df
        
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {dataset_enum.value}")
        return None
    except Exception as e:
        print(f"❌ Error cargando {dataset_enum.value}: {e}")
        return None

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

# === FUNCIONES DE PROCESAMIENTO ESPECÍFICO ===

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
        
        # Convertir todas las columnas numéricas
        for level in all_levels:
            value_col = f'{level}_Value'
            count_col = f'{level}_Count'
            if value_col in data_df.columns:
                data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
            if count_col in data_df.columns:
                data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
        
        # Crear aliases para compatibilidad
        data_df['Very_Often_Value'] = data_df['With_Fin_Diff_Very_Often_Value']
        data_df['Often_Value'] = data_df['With_Fin_Diff_Often_Value']
        data_df['Sometimes_Value'] = data_df['With_Fin_Diff_Sometimes_Value']
        data_df['Rarely_Value'] = data_df['With_Fin_Diff_Rarely_Value']
        data_df['Never_Value'] = data_df['With_Fin_Diff_Never_Value']
        
    elif num_cols == 31:
        # Estructura con 2 grupos de escalas Likert (como "work to afford study")
        column_names = ['Country']
        
        # Grupo 1: "partly or does not apply (at all)" (columnas 1-15)
        abandoning_levels_1 = ['Partly_Strongly_Agree', 'Partly_Agree_2', 'Partly_Agree_3', 'Partly_Agree_4', 'Partly_Disagree_All']
        for level in abandoning_levels_1:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        # Grupo 2: "applies (totally)" (columnas 16-30)
        abandoning_levels_2 = ['Totally_Strongly_Agree', 'Totally_Agree_2', 'Totally_Agree_3', 'Totally_Agree_4', 'Totally_Disagree_All']
        for level in abandoning_levels_2:
            column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
        
        all_levels = abandoning_levels_1 + abandoning_levels_2
        
        # Asignar nombres de columnas
        data_df.columns = column_names
        data_df = data_df.reset_index(drop=True)
        data_df = data_df.dropna(subset=['Country'])
        
        # Convertir todas las columnas numéricas
        for level in all_levels:
            value_col = f'{level}_Value'
            count_col = f'{level}_Count'
            if value_col in data_df.columns:
                data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
            if count_col in data_df.columns:
                data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
        
        # Crear aliases para compatibilidad usando el primer grupo como principal
        # Mapeamos las escalas Likert a frecuencias equivalentes
        data_df['Very_Often_Value'] = data_df['Partly_Strongly_Agree_Value']  # Strongly agree = Very often
        data_df['Often_Value'] = data_df['Partly_Agree_2_Value']               # Level 2 = Often
        data_df['Sometimes_Value'] = data_df['Partly_Agree_3_Value']           # Level 3 = Sometimes
        data_df['Rarely_Value'] = data_df['Partly_Agree_4_Value']              # Level 4 = Rarely
        data_df['Never_Value'] = data_df['Partly_Disagree_All_Value']          # Disagree all = Never
        
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
    Procesa datasets de autoevaluación de rendimiento
    """
    column_names = ['Country']
    evaluation_levels = [
        'Much_Better',      # Mucho mejor
        'Better',           # Mejor
        'About_Same',       # Más o menos igual
        'Worse',            # Peor
        'Much_Worse'        # Mucho peor
    ]
    
    for level in evaluation_levels:
        column_names.extend([f'{level}_Value', f'{level}_Unit', f'{level}_Count'])
    
    data_df.columns = column_names
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    # Convertir columnas numéricas
    for level in evaluation_levels:
        value_col = f'{level}_Value'
        count_col = f'{level}_Count'
        if value_col in data_df.columns:
            data_df[value_col] = pd.to_numeric(data_df[value_col], errors='coerce')
        if count_col in data_df.columns:
            data_df[count_col] = pd.to_numeric(data_df[count_col], errors='coerce').astype('Int64')
    
    return data_df

def _process_health_relationship_dataset(data_df):
    """
    Procesa datasets de relación trabajo-salud
    """
    column_names = ['Country']
    health_levels = [
        'Very_Positive',    # Muy positivo
        'Positive',         # Positivo
        'Neutral',          # Neutral
        'Negative',         # Negativo
        'Very_Negative'     # Muy negativo
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
    Procesa datasets genéricos de impacto (estructura básica)
    """
    # Estructura genérica simple
    data_df.columns = [f'Col_{i}' for i in range(len(data_df.columns))]
    data_df.columns[0] = 'Country'
    data_df = data_df.reset_index(drop=True)
    data_df = data_df.dropna(subset=['Country'])
    
    return data_df 