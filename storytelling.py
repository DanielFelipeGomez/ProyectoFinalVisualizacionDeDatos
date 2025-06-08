import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns

# ========== IMPORTACIONES PARA GRÁFICOS DEMOGRÁFICOS ==========
# Importar funciones para generar los gráficos interactivos demográficos
from advanced_demographic_charts import (
    create_field_of_study_comparison_chart,
    create_financial_difficulties_comparison_chart,
    create_living_with_parents_comparison_chart,
    create_parents_financial_status_comparison_chart,
    create_comprehensive_demographic_dashboard,
    create_gender_comparison_chart,
    create_age_comparison_chart
)

# Importar funciones principales de gráficos interactivos
from interactive_storytelling_charts import (
    generate_all_interactive_charts,
    create_interactive_context_overview,
    create_interactive_spain_vs_europe_detailed
)

# ========== IMPORTACIONES PARA GRÁFICOS DE STORYTELLING GENERAL ==========
# Importar funciones del módulo de storytelling general
from storytelling_module import WorkStudyStorytellingCharts

# ========== IMPORTACIONES PARA GRÁFICOS DE RELACIÓN TRABAJO-ESTUDIO ==========
# Importar funciones para los gráficos de relación trabajo-estudio
from work_study_interactive_charts import (
    create_storytelling_work_study_charts,
    create_hero_spain_europe_comparison,
    create_european_ranking_chart,
    create_relationship_levels_chart,
    create_gap_analysis_chart,
    generate_storytelling_summary
)

# ========== IMPORTACIONES PARA GRÁFICOS DE IMPACTO DEL TRABAJO ==========
# Importar funciones para los gráficos de impacto del trabajo en los estudios
from storytelliing_charts import (
    get_work_impact_figures_for_streamlit,
    create_streamlit_abandoning_chart,
    create_spain_europe_impact_comparison,
    read_work_impact_dataset,
    generate_work_impact_summary
)

from enum import Enum

# ========== IMPORTAR CLASES DE DATASETS DE IMPACTO ==========
from storytelliing_charts import PreprocessedDatasetsNamesImpactsOnStudyForWork

# Definir datasets disponibles
class PreprocessedDatasetsNamesWorkMotiveAffordStudy(Enum):
    WORK_MOTIVE_AFFORD_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__all_students__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_SEX = 'preprocessed_excels/E8_work_motive_afford_study_5__e_sex__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_AGE = 'preprocessed_excels/E8_work_motive_afford_study_5__e_age__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FIELD_OF_STUDY = 'preprocessed_excels/E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_FINANCIAL_DIFFICULTIES = 'preprocessed_excels/E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_E_NOTLIVINGWITHPARENTS = 'preprocessed_excels/E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx'
    WORK_MOTIVE_AFFORD_STUDY_S_PARENTS_FINANCIAL_STATUS = 'preprocessed_excels/E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx'

class PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy(Enum):
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY = 'preprocessed_relationship_study_job/E8_work_related_study5__all_students__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_AGE = 'preprocessed_relationship_study_job/E8_work_related_study5__e_age__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_FIELD_OF_STUDY = 'preprocessed_relationship_study_job/E8_work_related_study5__e_field_of_study__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_INTENS = 'preprocessed_relationship_study_job/E8_work_related_study5__e_intens__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_QUALIFICATION = 'preprocessed_relationship_study_job/E8_work_related_study5__e_qualification__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_E_SEX = 'preprocessed_relationship_study_job/E8_work_related_study5__e_sex__all_contries.xlsx'
    RELATIONSHIP_BETWEEN_WORK_AND_STUDY_S_FULL_OR_PART_TIME_STUDY_PROGRAMME = 'preprocessed_relationship_study_job/E8_work_related_study5__s_full_or_part_time_study_programme__all_contries.xlsx'

# Configuración de la página
st.set_page_config(
    page_title="Trabajar y estudiar en Europa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Forzar tema claro usando múltiples métodos
st.markdown("""
<script>
// Método 1: Forzar fondo blanco
const elements = window.parent.document.querySelectorAll('.stApp');
if (elements.length > 0) {
    elements[0].style.backgroundColor = '#ffffff';
    elements[0].style.color = '#2C3E50';
}

// Método 2: Remover clases de tema oscuro
const darkThemeElements = window.parent.document.querySelectorAll('[data-theme="dark"]');
darkThemeElements.forEach(el => el.setAttribute('data-theme', 'light'));

// Método 3: Forzar el contenido principal
const mainContent = window.parent.document.querySelector('.main');
if (mainContent) {
    mainContent.style.backgroundColor = '#ffffff';
    mainContent.style.color = '#2C3E50';
}
</script>
""", unsafe_allow_html=True)

# CSS personalizado para mejorar el diseño - Sistema de colores consistente
st.markdown("""
<style>
    /* =================================
       VARIABLES DE COLOR - PALETA EUROPEA
    ================================= */
    :root {
        --primary-blue: #003DA5;        /* Azul Europa */
        --secondary-blue: #1f77b4;      /* Azul claro datos */
        --accent-blue: #3498db;         /* Azul accento */
        --spain-red: #C41E3A;           /* Rojo España */
        --success-green: #27AE60;       /* Verde éxito */
        --warning-orange: #F39C12;      /* Naranja advertencia */
        --danger-red: #E74C3C;          /* Rojo peligro */
        --neutral-gray: #7F8C8D;        /* Gris neutral */
        --light-gray: #ECF0F1;          /* Gris claro */
        --text-dark: #2C3E50;           /* Texto oscuro */
        --text-medium: #34495E;         /* Texto medio */
        --bg-light: #F8F9FA;            /* Fondo claro */
        --border-light: #DEE2E6;        /* Borde claro */
        --text-white: #FFFFFF;          /* Texto blanco */
        --text-light: #6C757D;          /* Texto claro pero visible */
    }
    
        /* =================================
       FORZAR TEMA CLARO Y CONTRASTE
    ================================= */
    /* Forzar fondo blanco en toda la aplicación */
    .stApp {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
    }
    
    /* Forzar fondo blanco en el contenido principal */
    .main .block-container {
        background-color: #ffffff !important;
        padding-top: 2rem !important;
    }
    
    /* Forzar fondo claro en sidebar */
    .css-1d391kg {
        background-color: #f8f9fa !important;
    }
    
    /* Texto base del contenido con contraste fuerte */
    p, li, span, div {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    
    /* Títulos y subtítulos siempre visibles */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    
    /* Texto en contenedores específicos de Streamlit */
    .stMarkdown {
        background-color: transparent !important;
    }
    
    .stMarkdown p, .stMarkdown li, .stMarkdown span, .stMarkdown div {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    
    /* Excepciones para elementos que necesitan colores específicos */
    .stat-spain { color: var(--spain-red) !important; }
    .stat-europe { color: var(--primary-blue) !important; }
    .stat-positive { color: var(--success-green) !important; }
    .stat-negative { color: var(--danger-red) !important; }
    .stat-warning { color: var(--warning-orange) !important; }
    .stat-neutral { color: var(--neutral-gray) !important; }
    
    /* =================================
       TIPOGRAFÍA Y HEADERS
    ================================= */
    .main-header {
        font-size: 3.2rem;
        color: var(--primary-blue);
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 700;
        line-height: 1.2;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .section-header {
        color: var(--text-dark);
        font-size: 2.2rem;
        margin-top: 4rem;
        margin-bottom: 1.5rem;
        border-bottom: 4px solid var(--accent-blue);
        padding-bottom: 0.8rem;
        font-weight: 600;
        position: relative;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 60px;
        height: 4px;
        background: var(--primary-blue);
    }
    
    .subsection-header {
        color: var(--text-medium);
        font-size: 1.6rem;
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        font-weight: 500;
        border-left: 4px solid var(--accent-blue);
        padding-left: 1rem;
    }
    
    /* =================================
       CAJAS DE CONTENIDO
    ================================= */
         .highlight-stat {
         background: linear-gradient(135deg, var(--light-gray) 0%, #ffffff 100%) !important;
         padding: 2rem;
         border-radius: 15px;
         border-left: 6px solid var(--accent-blue);
         margin: 2rem 0;
         box-shadow: 0 4px 6px rgba(0,0,0,0.07);
         transition: transform 0.2s ease;
     }
    
         .highlight-stat:hover {
         transform: translateY(-2px);
         box-shadow: 0 6px 12px rgba(0,0,0,0.1);
     }
     
     .highlight-stat p, .highlight-stat h3, .highlight-stat h4, .highlight-stat h5 {
         color: var(--text-dark) !important;
     }
    
         .insight-box {
         background: var(--bg-light) !important;
         padding: 2rem;
         border-radius: 15px;
         border: 1px solid var(--border-light);
         border-top: 4px solid var(--secondary-blue);
         margin: 2rem 0;
         box-shadow: 0 2px 4px rgba(0,0,0,0.05);
     }
    
         .insight-box h4 {
         color: var(--primary-blue) !important;
         margin-bottom: 1rem;
         font-weight: 600;
     }
     
     .insight-box p, .insight-box li {
         color: var(--text-dark) !important;
     }
     
     .conclusion-box {
         background: linear-gradient(135deg, #E8F5E8 0%, #F0FFF0 100%) !important;
         padding: 2rem;
         border-radius: 15px;
         border-left: 6px solid var(--success-green);
         margin: 2rem 0;
         box-shadow: 0 4px 8px rgba(0,0,0,0.08);
     }
     
     .conclusion-box h4 {
         color: var(--success-green) !important;
         margin-bottom: 1rem;
         font-weight: 600;
     }
     
     .conclusion-box p, .conclusion-box li {
         color: var(--text-dark) !important;
     }
    
         .warning-box {
         background: linear-gradient(135deg, #FDF2E9 0%, #FEF9E7 100%) !important;
         padding: 2rem;
         border-radius: 15px;
         border-left: 6px solid var(--warning-orange);
         margin: 2rem 0;
         box-shadow: 0 4px 8px rgba(0,0,0,0.08);
     }
    
         .warning-box h4 {
         color: var(--warning-orange) !important;
         margin-bottom: 1rem;
         font-weight: 600;
     }
     
     .warning-box p, .warning-box li {
         color: var(--text-dark) !important;
     }
     
     .danger-box {
         background: linear-gradient(135deg, #FDEDEC 0%, #FBEEE6 100%) !important;
         padding: 2rem;
         border-radius: 15px;
         border-left: 6px solid var(--danger-red);
         margin: 2rem 0;
         box-shadow: 0 4px 8px rgba(0,0,0,0.08);
     }
     
     .danger-box h4 {
         color: var(--danger-red) !important;
         margin-bottom: 1rem;
         font-weight: 600;
     }
     
     .danger-box p, .danger-box li {
         color: var(--text-dark) !important;
     }
     
     .spain-box {
         background: linear-gradient(135deg, #F8E6EA 0%, #FDEEF0 100%) !important;
         padding: 2rem;
         border-radius: 15px;
         border-left: 6px solid var(--spain-red);
         margin: 2rem 0;
         box-shadow: 0 4px 8px rgba(0,0,0,0.08);
     }
     
     .spain-box h4 {
         color: var(--spain-red) !important;
         margin-bottom: 1rem;
         font-weight: 600;
     }
     
     .spain-box p, .spain-box li {
         color: var(--text-dark) !important;
     }
    
    /* =================================
       ELEMENTOS VISUALES
    ================================= */
    .section-divider {
        height: 4px;
        background: linear-gradient(90deg, var(--accent-blue), var(--success-green), var(--primary-blue));
        margin: 5rem 0 3rem 0;
        border-radius: 2px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
        gap: 1rem;
    }
    
         .stat-item {
         text-align: center;
         padding: 1.5rem;
         background: white !important;
         border-radius: 10px;
         box-shadow: 0 2px 8px rgba(0,0,0,0.1);
         min-width: 150px;
         flex: 1;
     }
     
     .stat-number {
         font-size: 2.5rem;
         font-weight: 700;
         margin-bottom: 0.5rem;
     }
     
     .stat-label {
         font-size: 0.9rem;
         color: var(--text-medium) !important;
         font-weight: 500;
     }
    
         /* =================================
        COLORES DE ESTADÍSTICAS POR CONTEXTO - MOVIDO ARRIBA
     ================================= */
    
    /* =================================
       MEJORAS DE NAVEGACIÓN
    ================================= */
    .nav-link {
        color: var(--primary-blue);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    .nav-link:hover {
        color: var(--accent-blue);
        text-decoration: underline;
    }
    
    /* =================================
       PLACEHOLDER DE GRÁFICOS MEJORADO
    ================================= */
         .chart-placeholder {
         border: 2px dashed var(--border-light);
         padding: 3rem 2rem;
         text-align: center;
         margin: 2rem 0;
         border-radius: 15px;
         background: linear-gradient(135deg, #FAFAFA 0%, #F5F5F5 100%) !important;
         transition: all 0.3s ease;
     }
    
         .chart-placeholder:hover {
         border-color: var(--accent-blue);
         background: linear-gradient(135deg, #F0F8FF 0%, #E6F3FF 100%) !important;
     }
     
     /* =================================
        SOBREESCRIBIR TEMA OSCURO DE STREAMLIT
     ================================= */
     /* Forzar elementos específicos de Streamlit a tema claro */
     .stSelectbox > div > div {
         background-color: white !important;
         color: var(--text-dark) !important;
     }
     
     .stTabs > div > div > div > div {
         background-color: transparent !important;
         color: var(--text-dark) !important;
     }
     
     .stColumn > div {
         background-color: transparent !important;
     }
     
     /* Asegurar que el contenido markdown se vea bien */
     [data-testid="stMarkdownContainer"] {
         background-color: transparent !important;
     }
     
     [data-testid="stMarkdownContainer"] p {
         color: var(--text-dark) !important;
     }
    
         .chart-placeholder h4 {
         color: var(--primary-blue) !important;
         margin-bottom: 1rem;
     }
     
     .chart-placeholder p {
         color: var(--neutral-gray) !important;
         margin: 0.5rem 0;
     }
    
    /* =================================
       RESPONSIVE DESIGN
    ================================= */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.2rem;
        }
        
        .section-header {
            font-size: 1.8rem;
        }
        
        .subsection-header {
            font-size: 1.4rem;
        }
        
        .stats-container {
            flex-direction: column;
        }
        
        .highlight-stat, .insight-box, .conclusion-box {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Información lateral opcional
st.sidebar.title("🎓 Navegación rápida")
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Secciones del storytelling:**
- 🌍 Introducción y contexto
- 👥 ¿Quiénes trabajan?  
- 💼 Relación trabajo-estudio
- 📚 **Impacto** en estudios ✨
- 💰 Factores socioeconómicos
- ⚠️ **Consecuencias** y riesgos ✨
- 🗺️ Contraste internacional
- 🎯 Conclusiones y reflexiones

**✨ = Secciones con nuevas gráficas interactivas**
""")

# Información adicional sobre España
st.sidebar.markdown("---")
st.sidebar.markdown("""
**🇪🇸 Enfoque en España:**
- Datos de 9,072 estudiantes
- Comparación con 25 países europeos  
- Análisis de impacto específico
- Consideración de abandono estudiantil
- Políticas de apoyo recomendadas
""")

# Función para mostrar placeholder de gráfico
def show_chart_placeholder(chart_name, description=""):
    st.markdown(f"""
    <div class="chart-placeholder">
        <h4>📊 {chart_name}</h4>
        <p>{description}</p>
        <p><em>Gráfico por implementar</em></p>
    </div>
    """, unsafe_allow_html=True)

# Función para crear estadísticas consistentes
def create_stats_display(stats_data):
    """Crear display de estadísticas con estilo consistente"""
    html = '<div class="stats-container">'
    for stat in stats_data:
        color_class = stat.get('color', 'stat-neutral')
        html += f"""
        <div class="stat-item">
            <div class="stat-number {color_class}">{stat['number']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """
    html += '</div>'
    return html

# Título principal
st.markdown('<h1 class="main-header">Trabajar y estudiar en Europa:<br>¿Oportunidad, sacrificio o desigualdad?</h1>', unsafe_allow_html=True)

# ========================================
# 1. INTRODUCCIÓN/CONTEXTO
# ========================================
st.markdown('<h2 class="section-header">🌍 Introducción y Contexto</h2>', unsafe_allow_html=True)

# Estadística principal de introducción
intro_stats = [
    {'number': '50%', 'label': 'Estudiantes europeos que trabajan mientras estudian', 'color': 'stat-europe'},
    {'number': '25', 'label': 'Países europeos analizados', 'color': 'stat-neutral'},
    {'number': '9,072', 'label': 'Estudiantes españoles en el estudio', 'color': 'stat-spain'}
]

st.markdown(create_stats_display(intro_stats), unsafe_allow_html=True)

st.markdown("""
En la Europa contemporánea, la realidad universitaria ha evolucionado significativamente. Ya no es suficiente 
dedicarse únicamente a los estudios; para muchos jóvenes, trabajar mientras se estudia se ha convertido en una 
necesidad económica, una oportunidad de crecimiento profesional, o ambas cosas a la vez.

Esta investigación explora las múltiples dimensiones de esta realidad: **¿quiénes son estos estudiantes que 
trabajan?**, **¿cómo afecta esta decisión a su rendimiento académico?**, y **¿qué factores socioeconómicos 
determinan esta necesidad?**
""")

st.markdown("""
<div class="insight-box">
    <h4>🎯 Lo que descubriremos</h4>
    <ul>
        <li>Perfiles demográficos de estudiantes trabajadores</li>
        <li>Relación entre trabajo y área de estudios</li>
        <li>Impacto en el rendimiento académico y bienestar</li>
        <li>Diferencias socioeconómicas y geográficas</li>
        <li>Factores de riesgo y abandono estudiantil</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">📊 Panorama Europeo: ¿Quiénes necesitan trabajar?</h3>', unsafe_allow_html=True)

st.markdown("""
Antes de profundizar en las características específicas, veamos el panorama general europeo de la 
**necesidad de trabajar para costear estudios** por país. Este gráfico muestra la proporción de 
estudiantes que necesitan vs. no necesitan trabajar en cada país europeo.
""")

# Gráfico principal de necesidad de trabajar por país
try:
    st.markdown("#### 🌍 Necesidad de Trabajar para Costear Estudios por País")
    
    # Crear instancia del generador de gráficos
    storytelling_charts = WorkStudyStorytellingCharts()
    
    # Generar el gráfico principal
    fig_need_work = storytelling_charts.get_chart_need_vs_no_need()
    
    if fig_need_work:
        st.plotly_chart(fig_need_work, use_container_width=True, key="chart_need_vs_no_need")
        
        # Obtener insights clave para mostrar
        insights = storytelling_charts.get_key_insights()
        
        if 'error' not in insights:
            # Estadísticas destacadas basadas en los datos reales
            work_necessity_stats = [
                {
                    'number': f"{insights['spain_need_work']:.1f}%", 
                    'label': 'Estudiantes españoles necesitan trabajar', 
                    'color': 'stat-spain'
                },
                {
                    'number': f"{insights['europe_need_work']:.1f}%", 
                    'label': 'Promedio europeo necesita trabajar', 
                    'color': 'stat-europe'
                },
                {
                    'number': f"{insights['difference']:+.1f}pp", 
                    'label': 'Diferencia España vs Europa', 
                    'color': 'stat-warning' if insights['difference'] > 0 else 'stat-positive'
                }
            ]
            
            st.markdown(create_stats_display(work_necessity_stats), unsafe_allow_html=True)
            
            # Insight box con análisis automático
            st.markdown(f"""
            <div class="insight-box">
                <h4>🔍 Análisis del panorama europeo</h4>
                <ul>
                    <li><strong>🇪🇸 España:</strong> {insights['spain_need_work']:.1f}% de estudiantes necesitan trabajar para costear estudios</li>
                    <li><strong>🇪🇺 Promedio europeo:</strong> {insights['europe_need_work']:.1f}% necesitan trabajar</li>
                    <li><strong>📊 Diferencia:</strong> España está {abs(insights['difference']):.1f} puntos {'por encima' if insights['difference'] > 0 else 'por debajo'} del promedio</li>
                    <li><strong>🏆 País con menor necesidad:</strong> {insights['min_country']} ({insights['min_percentage']:.1f}%)</li>
                    <li><strong>⚠️ País con mayor necesidad:</strong> {insights['max_country']} ({insights['max_percentage']:.1f}%)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("No se pudieron obtener insights automáticos del gráfico")
    else:
        show_chart_placeholder("Necesidad de Trabajar por País", "Error generando gráfico principal")
        
except Exception as e:
    st.error(f"Error cargando gráfico principal de necesidad de trabajar: {e}")
    show_chart_placeholder("Error: Necesidad de Trabajar por País", "Error cargando datos del storytelling_module")

# España vs Europa - Comparación detallada
st.markdown('<h3 class="subsection-header">🇪🇸 España vs 🇪🇺 Europa: Análisis Detallado</h3>', unsafe_allow_html=True)

try:
    st.markdown("#### ⚖️ Comparación Directa: Motivos para Trabajar")
    
    # Generar gráfico de comparación España vs Europa
    fig_spain_europe = storytelling_charts.get_chart_spain_vs_europe()
    
    if fig_spain_europe:
        st.plotly_chart(fig_spain_europe, use_container_width=True, key="chart_spain_vs_europe_detailed")
        
        st.markdown("""
        <div class="spain-box">
            <h4>🎯 Puntos clave España vs Europa</h4>
            <p>Este gráfico detalla los <strong>diferentes niveles de necesidad</strong> (desde "aplica totalmente" 
            hasta "no aplica para nada") del motivo económico para trabajar mientras se estudia.</p>
            <ul>
                <li><strong>Diferencias en intensidad:</strong> No solo importa si necesitan trabajar, sino qué tan urgente es esa necesidad</li>
                <li><strong>Patrón español:</strong> Distribución específica de España comparada con el promedio europeo</li>
                <li><strong>Oportunidades:</strong> Identificación de dónde España puede mejorar sus políticas de apoyo estudiantil</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        show_chart_placeholder("España vs Europa - Detallado", "Error generando comparación detallada")
        
except Exception as e:
    st.error(f"Error cargando comparación España vs Europa: {e}")
    show_chart_placeholder("Error: Comparación España vs Europa", "Error cargando datos detallados")

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 2. QUIÉNES SON LOS ESTUDIANTES QUE TRABAJAN
# ========================================
st.markdown('<h2 class="section-header">👥 ¿Quiénes son los estudiantes que trabajan?</h2>', unsafe_allow_html=True)

st.markdown("""
No todos los estudiantes tienen la misma probabilidad de trabajar mientras estudian. Factores como la edad, 
la situación de convivencia, el género y el nivel educativo de los padres juegan un papel determinante.
""")

st.markdown('<h3 class="subsection-header">📊 Distribución por características demográficas</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🌍 Distribución por País")
    # Generar gráfico de contexto general europeo
    try:
        # Importar función de lectura
        from interactive_storytelling_charts import read_preprocessed_dataset
        
        # Cargar dataset general
        df_general = read_preprocessed_dataset(PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY)
        
        if df_general is not None and not df_general.empty:
            fig_overview = create_interactive_context_overview(df_general)
            st.plotly_chart(fig_overview, use_container_width=True, key="chart_country_overview")
        else:
            show_chart_placeholder("Distribución por País", "Datos no disponibles")
    except Exception as e:
        st.error(f"Error cargando gráfico de países: {e}")
        show_chart_placeholder("Error en Distribución por País", "Error cargando datos")
    
    st.markdown("#### 👤 Distribución por Género")
    # Generar gráfico comparativo por género
    try:
        fig_gender = create_gender_comparison_chart()
        st.plotly_chart(fig_gender, use_container_width=True, key="chart_gender_comparison")
    except Exception as e:
        st.error(f"Error cargando gráfico de género: {e}")
        show_chart_placeholder("Error en Distribución por Género", "Error cargando datos")

with col2:
    st.markdown("#### 📅 Distribución por Edad")
    # Generar gráfico por grupos de edad
    try:
        fig_age = create_age_comparison_chart()
        st.plotly_chart(fig_age, use_container_width=True, key="chart_age_comparison")
    except Exception as e:
        st.error(f"Error cargando gráfico de edad: {e}")
        show_chart_placeholder("Error en Distribución por Edad", "Error cargando datos")
    
    st.markdown("#### 🏠 Situación de Convivencia")
    # Generar gráfico de convivencia con padres
    try:
        fig_living = create_living_with_parents_comparison_chart()
        st.plotly_chart(fig_living, use_container_width=True, key="chart_living_situation")
    except Exception as e:
        st.error(f"Error cargando gráfico de convivencia: {e}")
        show_chart_placeholder("Error en Tipo de Convivencia", "Error cargando datos")

st.markdown('<h3 class="subsection-header">🎓 Nivel educativo familiar</h3>', unsafe_allow_html=True)

st.markdown("""
El contexto educativo familiar es un factor crucial que determina la necesidad de trabajar durante los estudios.
""")

# Generar gráfico de estado financiero de los padres
try:
    st.markdown("#### 💼 Estado Financiero de los Padres vs. Necesidad de Trabajar")
    fig_parents = create_parents_financial_status_comparison_chart()
    st.plotly_chart(fig_parents, use_container_width=True, key="chart_parents_status")
    
    # Insight automático
    st.markdown("""
    <div class="insight-box">
        <h4>🔍 Insight automático</h4>
        <p>Los datos muestran una <strong>clara correlación inversa</strong> entre el nivel socioeconómico familiar 
        y la necesidad de trabajar durante los estudios. Los estudiantes de familias con menores recursos 
        tienen una probabilidad significativamente mayor de necesitar emplearse.</p>
    </div>
    """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error cargando gráfico de educación parental: {e}")
    show_chart_placeholder("Error: Educación Parental vs. Trabajo", "Error cargando datos")

# ========================================
# ANÁLISIS DEMOGRÁFICO COMPLETO
# ========================================
st.markdown('<h3 class="subsection-header">📊 Análisis Demográfico Completo</h3>', unsafe_allow_html=True)

st.markdown("""
Para obtener una comprensión completa de qué estudiantes necesitan trabajar, presentamos un análisis 
detallado por diferentes dimensiones demográficas y socioeconómicas.
""")

# Dashboard completo de análisis demográfico
try:
    st.markdown("#### 🔍 Dashboard Demográfico Integral")
    
    # Generar todos los gráficos demográficos
    tabs = st.tabs(["🎓 Campo de Estudio", "💰 Dificultades Financieras", "🏠 Convivencia", "👨‍👩‍👧‍👦 Estado Familiar"])
    
    with tabs[0]:
        st.markdown("**Necesidad de trabajar por área de estudios**")
        fig_field = create_field_of_study_comparison_chart()
        st.plotly_chart(fig_field, use_container_width=True, key="chart_field_of_study")
        
        st.markdown("""
        <div class="insight-box">
            <h4>💡 Insights por campo de estudio</h4>
            <ul>
                <li>Los estudiantes de <strong>campos técnicos y de ingeniería</strong> a menudo tienen más oportunidades de trabajo relacionado</li>
                <li>Las <strong>humanidades y artes</strong> pueden mostrar mayor necesidad económica</li>
                <li><strong>Medicina y ciencias de la salud</strong> presentan patrones únicos debido a la intensidad de los estudios</li>
                <li><strong>Diferencias significativas</strong> entre campos sugieren necesidad de políticas específicas por área</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("**Impacto de las dificultades financieras**")
        fig_financial = create_financial_difficulties_comparison_chart()
        st.plotly_chart(fig_financial, use_container_width=True, key="chart_financial_difficulties")
        
        st.markdown("""
        <div class="insight-box">
            <h4>🚨 Patrón crítico identificado</h4>
            <p>Existe una <strong>correlación directa</strong> entre el nivel de dificultades financieras percibidas 
            y la necesidad de trabajar. Los estudiantes con mayores dificultades muestran tasas de empleo 
            significativamente más altas.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:
        st.markdown("**Independencia habitacional y necesidad de trabajar**")
        fig_living_detailed = create_living_with_parents_comparison_chart()
        st.plotly_chart(fig_living_detailed, use_container_width=True, key="chart_living_with_parents")
        
        st.markdown("""
        <div class="insight-box">
            <h4>🏠 Factor independencia</h4>
            <p>Los estudiantes que <strong>viven independientemente</strong> muestran tasas de empleo mucho más altas, 
            ya que deben cubrir gastos de vivienda, alimentación y otros costes de vida.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.markdown("**Estado socioeconómico familiar**")
        fig_parents_detailed = create_parents_financial_status_comparison_chart()
        st.plotly_chart(fig_parents_detailed, use_container_width=True, key="chart_parents_financial_status")
        
        st.markdown("""
        <div class="insight-box">
            <h4>👨‍👩‍👧‍👦 Desigualdad intergeneracional</h4>
            <p>El <strong>origen socioeconómico familiar</strong> es uno de los predictores más fuertes de la necesidad 
            de trabajar durante los estudios, perpetuando desigualdades educativas.</p>
        </div>
        """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error cargando análisis demográfico completo: {e}")
    st.markdown("**Error cargando dashboard demográfico - usando placeholders**")
    
    col1, col2 = st.columns(2)
    with col1:
        show_chart_placeholder("Campo de Estudio", "Error cargando datos")
        show_chart_placeholder("Dificultades Financieras", "Error cargando datos")
    with col2:
        show_chart_placeholder("Convivencia", "Error cargando datos")
        show_chart_placeholder("Estado Familiar", "Error cargando datos")

st.markdown("""
<div class="insight-box">
    <h4>🔍 Insights clave confirmados</h4>
    <ul>
        <li>Los estudiantes de mayor edad tienen mayor probabilidad de trabajar</li>
        <li>Quienes viven independientemente muestran tasas más altas de empleo</li>
        <li>Existe una correlación inversa entre nivel educativo parental y necesidad de trabajar</li>
        <li><strong>España ocupa el puesto #13 de 25 países europeos</strong> con un 57.0% de estudiantes que necesitan trabajar</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 3. TRABAJO: ¿RELACIONADO O NO CON LOS ESTUDIOS?
# ========================================
st.markdown('<h2 class="section-header">💼 Trabajo: ¿Relacionado o no con los estudios?</h2>', unsafe_allow_html=True)

st.markdown("""
Una distinción fundamental es si el trabajo que realizan los estudiantes está relacionado con su área de estudios 
o no. Esta diferencia puede tener implicaciones significativas tanto para el desarrollo profesional como para el 
rendimiento académico.

**España se encuentra en una posición intermedia** en cuanto a la relación entre trabajo y estudios, pero existe 
margen de mejora comparado con otros países europeos.
""")

# Gráfico hero: España vs Europa
st.markdown('<h3 class="subsection-header">🇪🇸 España vs Europa: Relación Trabajo-Estudio</h3>', unsafe_allow_html=True)

try:
    # Cargar datos y crear gráfico principal
    charts, df_work_study = create_storytelling_work_study_charts()
    
    # Mostrar gráfico hero (España vs Europa)
    st.plotly_chart(charts['hero_chart'], use_container_width=True, key="hero_work_study_chart")
    
    # Generar insights automáticos
    summary = generate_storytelling_summary(df_work_study)
    
    # Mostrar estadísticas clave de España con el nuevo sistema
    work_study_stats = [
        {
            'number': f"{summary['spain_percentage']:.1f}%", 
            'label': 'Trabajo relacionado con estudios en España', 
            'color': 'stat-spain'
        },
        {
            'number': f"{summary['europe_percentage']:.1f}%", 
            'label': 'Promedio europeo', 
            'color': 'stat-europe'
        },
        {
            'number': f"{summary['spain_rank']}/25", 
            'label': 'Posición de España en Europa', 
            'color': 'stat-warning'
        }
    ]
    
    st.markdown(create_stats_display(work_study_stats), unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="spain-box">
        <h4>🇪🇸 Insight clave sobre España</h4>
        <p>España está <strong>{summary['gap']:.1f} puntos por debajo</strong> del promedio europeo en cuanto a 
        trabajo relacionado con estudios. Esto indica que hay una <strong>desconexión significativa</strong> 
        entre la formación académica y la experiencia laboral de los estudiantes españoles.</p>
        
        <ul>
            <li>Solo el <strong>{summary['spain_very_closely']:.1f}%</strong> de estudiantes españoles tiene trabajo muy relacionado</li>
            <li>El <strong>{summary['spain_not_at_all']:.1f}%</strong> trabaja en algo completamente no relacionado</li>
            <li>España ocupa la posición <strong>{summary['spain_rank']} de 25 países</strong> europeos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error cargando datos de relación trabajo-estudio: {e}")
    show_chart_placeholder("Error: España vs Europa", "Error cargando datos principales")

# Ranking europeo y análisis detallado
st.markdown('<h3 class="subsection-header">📊 Análisis Detallado por Países</h3>', unsafe_allow_html=True)

try:
    # Crear tabs para diferentes visualizaciones
    tab1, tab2, tab3 = st.tabs(["🏆 Ranking Europeo", "📈 Distribución Detallada", "🔍 Países Comparables"])
    
    with tab1:
        st.markdown("**Posición de todos los países europeos en relación trabajo-estudio**")
        st.plotly_chart(charts['ranking_chart'], use_container_width=True, key="ranking_work_study_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>🏆 Países líderes en trabajo relacionado</h4>
            <p>Los países nórdicos y algunos países de Europa Central lideran en conectar la experiencia 
            laboral estudiantil con la formación académica. Esto puede deberse a:</p>
            <ul>
                <li><strong>Sistemas educativos duales</strong> (formación profesional + práctica)</li>
                <li><strong>Mayor coordinación</strong> entre universidades y sector empresarial</li>
                <li><strong>Políticas de fomento</strong> de prácticas profesionales relacionadas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("**Desglose completo por niveles de relación trabajo-estudio**")
        st.plotly_chart(charts['detail_chart'], use_container_width=True, key="detail_work_study_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>📈 Patrones identificados</h4>
            <ul>
                <li><strong>Polarización:</strong> Muchos países muestran patrones polarizados (muy relacionado vs. nada relacionado)</li>
                <li><strong>España presenta un patrón intermedio</strong> con distribución relativamente equilibrada</li>
                <li><strong>Oportunidad de mejora:</strong> Existe potencial para aumentar la proporción de trabajo muy relacionado</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("**España comparada con países de perfil similar**")
        st.plotly_chart(charts['insight_chart'], use_container_width=True, key="insight_work_study_chart")
        
        st.markdown("""
        <div class="insight-box">
            <h4>🇪🇸 España en contexto mediterráneo</h4>
            <p>Comparando España con países de perfil económico y cultural similar, observamos que:</p>
            <ul>
                <li><strong>Portugal y Francia</strong> muestran mejores niveles de conexión trabajo-estudio</li>
                <li><strong>Alemania y Suiza</strong> lideran claramente (tradición de formación dual)</li>
                <li><strong>España tiene potencial de mejora</strong> sin necesidad de cambios radicales del sistema</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error cargando análisis detallado: {e}")
    
    col1, col2 = st.columns(2)
    with col1:
        show_chart_placeholder("Error: Ranking Europeo", "Error cargando datos")
        show_chart_placeholder("Error: Distribución Detallada", "Error cargando datos")
    with col2:
        show_chart_placeholder("Error: Países Comparables", "Error cargando datos")

st.markdown("""
<div class="conclusion-box">
    <h4>💡 Conclusiones sobre relación trabajo-estudio</h4>
    <p><strong>España presenta una oportunidad clara de mejora:</strong></p>
    <ul>
        <li>Fortalecer los <strong>programas de prácticas profesionales</strong> relacionadas con los estudios</li>
        <li>Mejorar la <strong>coordinación universidad-empresa</strong> para ofrecer empleos más relevantes</li>
        <li>Desarrollar <strong>programas de formación dual</strong> en ciertos sectores</li>
        <li>Implementar <strong>sistemas de certificación</strong> que valoren la experiencia laboral relacionada</li>
    </ul>
    <p>Estos cambios podrían <strong>reducir la brecha con Europa</strong> y mejorar la empleabilidad de los graduados españoles.</p>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 4. IMPACTO DEL TRABAJO EN LOS ESTUDIOS
# ========================================
st.markdown('<h2 class="section-header">📚 Impacto del trabajo en los estudios</h2>', unsafe_allow_html=True)

st.markdown("""
¿Cómo afecta trabajar al rendimiento académico y la experiencia universitaria? Esta sección examina el impacto 
real del trabajo en la vida estudiantil, incluyendo la **consideración de abandono** de estudios y otros efectos 
sobre el bienestar académico.

**España presenta patrones específicos** que vale la pena analizar en detalle comparado con el resto de Europa.
""")

# Cargar figuras de impacto del trabajo
st.markdown('<h3 class="subsection-header">📊 Datos de Impacto: España en Foco</h3>', unsafe_allow_html=True)

try:
    # Cargar todas las figuras de impacto optimizadas para Streamlit
    impact_figures = get_work_impact_figures_for_streamlit()
    
    if impact_figures:
        st.success(f"✅ {len(impact_figures)} gráficas de impacto cargadas exitosamente")
        
        # Crear tabs para organizar las visualizaciones de impacto
        impact_tab1, impact_tab2, impact_tab3 = st.tabs([
            "💸 Presión Financiera", 
            "👔 Conflicto Trabajo-Estudio", 
            "🇪🇸 España vs Europa"
        ])
        
        with impact_tab1:
            st.markdown("### 💸 Abandono por Dificultades Financieras")
            st.markdown("""
            **¿Con qué frecuencia consideran los estudiantes abandonar sus estudios debido a dificultades económicas?**
            
            Este gráfico muestra la realidad de la presión financiera en la educación europea.
            """)
            
            if 'abandono_financiero' in impact_figures:
                st.plotly_chart(
                    impact_figures['abandono_financiero'], 
                    use_container_width=True, 
                    key="impact_abandono_financiero"
                )
                
                st.markdown("""
                <div class="insight-box">
                    <h4>🔍 Análisis de Presión Financiera</h4>
                    <ul>
                        <li><strong>🔴 Alta frecuencia:</strong> Estudiantes que consideran abandonar "muy frecuentemente" o "frecuentemente"</li>
                        <li><strong>🟢 Nunca considera:</strong> Estudiantes que nunca han considerado abandonar por motivos económicos</li>
                        <li><strong>🇪🇸 España destacada:</strong> Posición específica comparada con otros países europeos</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                show_chart_placeholder("Abandono por Dificultades Financieras", "Error cargando datos")
        
        with impact_tab2:
            st.markdown("### 👔 Abandono por Necesidad de Trabajar")
            st.markdown("""
            **¿Consideran los estudiantes abandonar sus estudios para poder trabajar más tiempo?**
            
            Este análisis revela el conflicto directo entre supervivencia económica y continuidad académica.
            """)
            
            if 'abandono_trabajo' in impact_figures:
                st.plotly_chart(
                    impact_figures['abandono_trabajo'], 
                    use_container_width=True, 
                    key="impact_abandono_trabajo"
                )
                
                st.markdown("""
                <div class="insight-box">
                    <h4>⚖️ Conflicto Trabajo vs. Estudios</h4>
                    <ul>
                        <li><strong>Dilema crítico:</strong> Estudiantes que necesitan trabajar más pero eso implica menos tiempo para estudiar</li>
                        <li><strong>Diferencias por país:</strong> Algunos sistemas educativos generan más presión que otros</li>
                        <li><strong>Indicador de riesgo:</strong> Alta frecuencia sugiere sistemas de apoyo insuficientes</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                show_chart_placeholder("Abandono por Necesidad de Trabajar", "Error cargando datos")
        
        with impact_tab3:
            st.markdown("### 🇪🇸 España vs 🇪🇺 Europa: Comparación Directa")
            st.markdown("""
            **¿Cómo se posiciona España específicamente en términos de impacto del trabajo en los estudios?**
            
            Comparación directa con el promedio europeo en ambos tipos de consideración de abandono.
            """)
            
            if 'espana_vs_europa_impacto' in impact_figures:
                st.plotly_chart(
                    impact_figures['espana_vs_europa_impacto'], 
                    use_container_width=True, 
                    key="impact_espana_europa"
                )
                
                # Estadísticas resumidas para España
                st.markdown("""
                <div class="highlight-stat">
                    <h4 style="text-align: center; color: #d62728;">🇪🇸 Posición de España</h4>
                    <p style="text-align: center;">
                        Los datos muestran cómo España se compara específicamente con el promedio europeo 
                        en términos de presión para abandonar estudios por motivos laborales y financieros.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="insight-box">
                    <h4>🎯 Insights sobre España</h4>
                    <ul>
                        <li><strong>🔍 Comparación contextual:</strong> España en el marco europeo de trabajo estudiantil</li>
                        <li><strong>📊 Indicadores específicos:</strong> Frecuencia de consideración de abandono comparada</li>
                        <li><strong>💡 Áreas de mejora:</strong> Identificación de dónde España puede optimizar el apoyo estudiantil</li>
                        <li><strong>🎓 Implicaciones políticas:</strong> Datos para informar decisiones sobre becas y apoyo</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                show_chart_placeholder("España vs Europa - Impacto", "Error cargando datos")
                
    else:
        st.warning("⚠️ No se pudieron cargar las gráficas de impacto")
        
        # Fallback a placeholders
        col1, col2 = st.columns(2)
        with col1:
            show_chart_placeholder("Abandono por Dificultades Financieras", "Error cargando datos")
        with col2:
            show_chart_placeholder("Abandono por Necesidad de Trabajar", "Error cargando datos")

except Exception as e:
    st.error(f"Error cargando análisis de impacto: {e}")
    
    # Fallback a placeholders originales
    col1, col2 = st.columns(2)
    with col1:
        show_chart_placeholder(
            "Horas de Trabajo vs. Horas de Estudio", 
            "Error cargando datos de impacto"
        )
        show_chart_placeholder(
            "Rendimiento Académico Percibido", 
            "Error cargando datos de impacto"
        )
    with col2:
        show_chart_placeholder(
            "Modalidad de Enseñanza e Impacto", 
            "Error cargando datos de impacto"
        )
        show_chart_placeholder(
            "Salud Percibida", 
            "Error cargando datos de impacto"
        )

st.markdown('<h3 class="subsection-header">⚖️ Balance trabajo-estudio: Factores críticos</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="insight-box">
    <h4>🎯 Factores críticos identificados</h4>
    <ul>
        <li><strong>🚨 Umbral de riesgo:</strong> Existe un punto donde la presión financiera compromete la continuidad académica</li>
        <li><strong>💼 Tipo de trabajo:</strong> El trabajo relacionado con estudios muestra menor impacto negativo</li>
        <li><strong>🇪🇸 Contexto español:</strong> España presenta patrones específicos que requieren atención particular</li>
        <li><strong>📈 Variabilidad europea:</strong> Grandes diferencias entre países sugieren que las políticas importan</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>⚠️ Implicaciones del Análisis de Impacto</h4>
    <p><strong>Los datos revelan que el trabajo durante los estudios puede tener consecuencias serias:</strong></p>
    <ol>
        <li><strong>Riesgo de abandono:</strong> La presión económica puede forzar a estudiantes a dejar los estudios</li>
        <li><strong>Desigualdad de oportunidades:</strong> No todos los estudiantes tienen las mismas opciones</li>
        <li><strong>Necesidad de apoyo:</strong> Los sistemas de becas y apoyo estudiantil son cruciales</li>
        <li><strong>España en contexto:</strong> Oportunidades específicas de mejora para el sistema español</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 5. FACTORES SOCIOECONÓMICOS Y DESIGUALDAD
# ========================================
st.markdown('<h2 class="section-header">💰 Factores socioeconómicos y desigualdad</h2>', unsafe_allow_html=True)

st.markdown("""
Las desigualdades socioeconómicas se manifiestan claramente en la experiencia universitaria. Esta sección explora 
cómo el nivel educativo parental, las dificultades económicas y las diferencias entre países afectan la necesidad 
de trabajar durante los estudios.
""")

st.markdown('<h3 class="subsection-header">🏠 Contexto familiar y económico</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    show_chart_placeholder(
        "Nivel Educativo Parental vs. Necesidad de Trabajar", 
        "Correlación entre educación familiar y trabajo estudiantil"
    )
    
    show_chart_placeholder(
        "Dificultades Económicas por País", 
        "Ranking de países según dificultades para costear estudios"
    )

with col2:
    show_chart_placeholder(
        "Mapa de Calor: Desigualdad Europea", 
        "Visualización geográfica de las diferencias socioeconómicas"
    )
    
    show_chart_placeholder(
        "Apoyo Familiar vs. Trabajo", 
        "Relación entre dependencia económica familiar y empleo"
    )

st.markdown('<h3 class="subsection-header">🌍 Comparación internacional</h3>', unsafe_allow_html=True)

show_chart_placeholder(
    "Ranking de Países: Facilidad para Estudiar sin Trabajar", 
    "Comparación de políticas de apoyo estudiantil efectivas"
)

st.markdown("""
<div class="warning-box">
    <h4>🏛️ Implicaciones políticas críticas</h4>
    <p>Los datos revelan diferencias significativas entre sistemas educativos europeos, sugiriendo que:</p>
    <ul>
        <li><strong>Sistemas de becas efectivos:</strong> Algunos países han logrado reducir significativamente la necesidad de trabajo</li>
        <li><strong>Políticas sociales determinantes:</strong> La inversión pública en educación superior marca la diferencia</li>
        <li><strong>Desigualdad sistémica:</strong> Sin políticas activas, la educación perpetúa las diferencias socioeconómicas</li>
        <li><strong>Oportunidad para España:</strong> Posición intermedia permite aprender de mejores prácticas europeas</li>
        <li><strong>Retorno de inversión:</strong> Reducir trabajo no relacionado mejora resultados educativos y económicos</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 6. CONSECUENCIAS Y RIESGOS
# ========================================
st.markdown('<h2 class="section-header">⚠️ Consecuencias y riesgos</h2>', unsafe_allow_html=True)

st.markdown("""
Trabajar mientras se estudia no solo tiene implicaciones académicas, sino que también puede afectar la salud, 
el bienestar y las redes sociales de los estudiantes. En casos extremos, puede llevar al abandono de los estudios.

**Los datos de las gráficas anteriores** ya nos han mostrado indicios preocupantes sobre la consideración de abandono. 
Aquí profundizamos en las implicaciones más amplias.
""")

st.markdown('<h3 class="subsection-header">🚪 Síntesis: Riesgo de abandono estudiantil</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>📊 Lo que nos han revelado los datos de impacto</h4>
    <p>Basándonos en las gráficas de impacto analizadas anteriormente, podemos confirmar que:</p>
    <ul>
        <li><strong>La presión financiera es real:</strong> Un porcentaje significativo de estudiantes considera abandonar por dificultades económicas</li>
        <li><strong>El conflicto trabajo-estudio existe:</strong> Algunos estudiantes ven el abandono como única forma de trabajar más</li>
        <li><strong>España no está exenta:</strong> Los patrones españoles muestran áreas específicas de preocupación</li>
        <li><strong>Hay diferencias europeas:</strong> Algunos países manejan mejor este balance que otros</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Análisis adicional basado en los datos ya cargados
try:
    st.markdown("#### 🔍 Análisis Complementario de Riesgos")
    
    # Si tenemos los datos de impacto cargados, podemos hacer análisis adicional
    if 'impact_figures' in locals() or 'impact_figures' in globals():
        st.markdown("""
        **Factores de riesgo identificados a partir de los datos de impacto:**
        
        Los gráficos anteriores nos permiten identificar patrones de riesgo específicos por país y comparar 
        España con el contexto europeo más amplio.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="insight-box">
                <h4>🇪🇸 Factores de riesgo en España</h4>
                <ul>
                    <li>Frecuencia de consideración de abandono por motivos financieros</li>
                    <li>Presión para trabajar más tiempo del disponible</li>
                    <li>Comparación con sistemas de apoyo europeos más efectivos</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="insight-box">
                <h4>🌍 Patrones europeos identificados</h4>
                <ul>
                    <li>Países con menor frecuencia de consideración de abandono</li>
                    <li>Sistemas que mejor balancean trabajo y estudios</li>
                    <li>Modelos de apoyo estudiantil más efectivos</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
    else:
        # Fallback si no tenemos los datos
        col1, col2 = st.columns(2)
        
        with col1:
            show_chart_placeholder(
                "Factores de Riesgo Específicos de España", 
                "Análisis basado en datos de impacto"
            )
        
        with col2:
            show_chart_placeholder(
                "Comparación de Riesgos Europeos", 
                "Análisis comparativo de riesgos por país"
            )

except Exception as e:
    st.warning(f"No se puede realizar análisis complementario: {e}")
    
    # Fallback a placeholders originales
    col1, col2 = st.columns(2)
    
    with col1:
        show_chart_placeholder(
            "Intención de Abandonar: Trabajadores vs. No Trabajadores", 
            "Comparación de tasas de riesgo de abandono"
        )
        
        show_chart_placeholder(
            "Factores de Riesgo Combinados", 
            "Análisis multivariable de predictores de abandono"
        )
    
    with col2:
        show_chart_placeholder(
            "Dificultades Económicas vs. Abandono", 
            "Relación entre situación económica e intención de dejar estudios"
        )
        
        show_chart_placeholder(
            "Tipo de Trabajo y Riesgo", 
            "¿El trabajo no relacionado aumenta el riesgo de abandono?"
        )

st.markdown('<h3 class="subsection-header">💊 Salud y bienestar</h3>', unsafe_allow_html=True)

st.markdown("""
Los efectos del trabajo estudiantil van más allá del rendimiento académico. La salud física y mental 
también puede verse afectada, especialmente cuando existe alta presión económica.
""")

show_chart_placeholder(
    "Salud Percibida por Tipo de Trabajo", 
    "Impacto diferencial según relación trabajo-estudios"
)

st.markdown('<h3 class="subsection-header">🤝 Redes sociales y apoyo</h3>', unsafe_allow_html=True)

show_chart_placeholder(
    "Red de Apoyo vs. Dependencia Económica", 
    "¿Los estudiantes que dependen solo de sus ingresos tienen menos apoyo social?"
)

st.markdown("""
<div class="insight-box">
    <h4>🔴 Señales de alerta confirmadas por los datos</h4>
    <ul>
        <li><strong>Círculo vicioso confirmado:</strong> Los datos de impacto muestran que la presión económica → trabajo excesivo → consideración de abandono</li>
        <li><strong>Aislamiento social:</strong> Menos tiempo para relaciones sociales y actividades extracurriculares</li>
        <li><strong>Impacto en salud:</strong> Estrés, fatiga y problemas de bienestar mental</li>
        <li><strong>Desigualdad sistémica:</strong> Los estudiantes de familias con menores recursos enfrentan riesgos desproporcionados</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>⚠️ Implicaciones para la política educativa</h4>
    <p><strong>Los datos de impacto revelan la urgencia de actuar:</strong></p>
    <ol>
        <li><strong>Sistemas de alerta temprana:</strong> Identificar estudiantes en riesgo de abandono</li>
        <li><strong>Apoyo financiero reforzado:</strong> Becas y ayudas más amplias y accesibles</li>
        <li><strong>Programas trabajo-estudio:</strong> Facilitar empleos relacionados con la formación</li>
        <li><strong>Apoyo psicosocial:</strong> Servicios de bienestar estudiantil más robustos</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 7. CONTRASTE INTERNACIONAL
# ========================================
st.markdown('<h2 class="section-header">🗺️ Contraste internacional</h2>', unsafe_allow_html=True)

st.markdown("""
Europa no es homogénea en cuanto a la experiencia de sus estudiantes universitarios. Esta sección compara 
diferentes países, destacando modelos exitosos e identificando dónde es más difícil compatibilizar trabajo y estudios.
""")

st.markdown('<h3 class="subsection-header">🏆 Ranking de países</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    show_chart_placeholder(
        "Facilidad para Estudiar sin Trabajar", 
        "Ranking de países según indicadores de apoyo estudiantil"
    )
    
    show_chart_placeholder(
        "Calidad del Trabajo Estudiantil", 
        "Proporción de trabajo relacionado con estudios por país"
    )

with col2:
    show_chart_placeholder(
        "Impacto en Rendimiento por País", 
        "Diferencias internacionales en el impacto trabajo-estudios"
    )
    
    show_chart_placeholder(
        "Desigualdad Socioeconómica", 
        "Índice de equidad educativa por país"
    )

st.markdown('<h3 class="subsection-header">🇪🇸 España en contexto</h3>', unsafe_allow_html=True)

# Generar comparación detallada España vs Europa
try:
    st.markdown("#### 🇪🇸 España vs. Promedio Europeo - Análisis Detallado")
    
    # Cargar dataset general
    from interactive_storytelling_charts import read_preprocessed_dataset
    df_general = read_preprocessed_dataset(PreprocessedDatasetsNamesWorkMotiveAffordStudy.WORK_MOTIVE_AFFORD_STUDY)
    
    if df_general is not None and not df_general.empty:
        fig_spain_europe = create_interactive_spain_vs_europe_detailed(df_general)
        st.plotly_chart(fig_spain_europe, use_container_width=True, key="chart_spain_vs_europe")
    else:
        show_chart_placeholder("España vs. Europa", "Datos no disponibles")
    
    # Estadísticas clave sobre España
    st.markdown("""
    <div class="spain-box">
        <h4 style="text-align: center;">🇪🇸 España: Puesto #13 de 25 países</h4>
    </div>
    """, unsafe_allow_html=True)
    
    spain_context_stats = [
        {'number': '57.0%', 'label': 'Estudiantes españoles que necesitan trabajar', 'color': 'stat-spain'},
        {'number': '56.7%', 'label': 'Promedio europeo', 'color': 'stat-europe'},
        {'number': '+0.3%', 'label': 'Diferencia con la media', 'color': 'stat-positive'}
    ]
    
    st.markdown(create_stats_display(spain_context_stats), unsafe_allow_html=True)
    
except Exception as e:
    st.error(f"Error cargando comparación España-Europa: {e}")
    show_chart_placeholder("Error: España vs. Media Europea", "Error cargando datos")

st.markdown("""
<div class="insight-box">
    <h4>🎯 Modelos a seguir</h4>
    <p>El análisis identificará países con:</p>
    <ul>
        <li><strong>Mejores sistemas de becas:</strong> Donde menos estudiantes necesitan trabajar</li>
        <li><strong>Mejor integración trabajo-estudio:</strong> Más empleos relacionados con la formación</li>
        <li><strong>Menor desigualdad:</strong> Donde el origen socioeconómico importa menos</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Separador visual
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ========================================
# 8. CONCLUSIONES/REFLEXIÓN
# ========================================
st.markdown('<h2 class="section-header">🎯 Conclusiones y reflexiones</h2>', unsafe_allow_html=True)

st.markdown("""
Después de analizar exhaustivamente los datos de miles de estudiantes europeos, emergen patrones reveladores 
que nos ayudan a comprender la compleja realidad de trabajar mientras se estudia en Europa contemporánea.
""")

# Estadísticas clave finales
st.markdown('<h3 class="subsection-header">📊 Síntesis de hallazgos clave</h3>', unsafe_allow_html=True)

# Crear estadísticas finales impactantes
final_key_stats = [
    {'number': '1 de 2', 'label': 'Estudiantes europeos trabaja mientras estudia', 'color': 'stat-europe'},
    {'number': '57%', 'label': 'Estudiantes españoles necesitan trabajar', 'color': 'stat-spain'},
    {'number': '#13/25', 'label': 'Posición de España en trabajo relacionado', 'color': 'stat-warning'},
    {'number': '↑ Riesgo', 'label': 'Abandono por presión económica confirmado', 'color': 'stat-negative'}
]

st.markdown(create_stats_display(final_key_stats), unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">💡 Hallazgos principales</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>🌟 El hallazgo más revelador</h4>
    <p><strong>"La necesidad económica determina más las decisiones que la vocación: muchos estudiantes trabajan en empleos no relacionados con sus estudios porque no pueden permitirse elegir"</strong></p>
    
    <ul>
        <li><strong>Desconexión educación-trabajo:</strong> España está 4.1 puntos por debajo del promedio europeo en trabajo relacionado</li>
        <li><strong>Presión de abandono real:</strong> Los datos confirman que la dificultad económica lleva a considerar dejar los estudios</li>
        <li><strong>Desigualdad sistémica:</strong> El origen socioeconómico familiar predice fuertemente la necesidad de trabajar</li>
        <li><strong>Oportunidad perdida:</strong> Trabajo relacionado con estudios muestra beneficios, pero pocos pueden acceder</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Balance de aspectos positivos y negativos
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="insight-box">
        <h4>✅ Aspectos positivos confirmados</h4>
        <ul>
            <li><strong>Experiencia valiosa:</strong> Desarrollo de competencias profesionales tempranas</li>
            <li><strong>Madurez y organización:</strong> Mejores habilidades de gestión del tiempo</li>
            <li><strong>Empleabilidad futura:</strong> Ventaja competitiva en el mercado laboral</li>
            <li><strong>Independencia:</strong> Autonomía económica y personal</li>
            <li><strong>Trabajo relacionado:</strong> Cuando es posible, refuerza el aprendizaje académico</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="danger-box">
        <h4>⚠️ Riesgos críticos identificados</h4>
        <ul>
            <li><strong>Riesgo de abandono:</strong> Presión económica lleva a considerar dejar estudios </li>
            <li><strong>Rendimiento académico:</strong> Impacto negativo en calificaciones y participación</li>
            <li><strong>Salud y bienestar:</strong> Estrés, fatiga y problemas de salud mental</li>
            <li><strong>Desigualdad educativa:</strong> Perpetuación de diferencias socioeconómicas</li>
            <li><strong>Oportunidades perdidas:</strong> Menos tiempo para networking y actividades formativas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">🇪🇸 España en perspectiva europea</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="spain-box">
    <h4>🔍 Diagnóstico específico para España</h4>
    <p><strong>España presenta un patrón intermedio pero con margen de mejora significativo:</strong></p>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
        <div>
            <h5>⚠️ Desafíos identificados:</h5>
            <ul>
                <li>Puesto #13/25 en trabajo relacionado con estudios</li>
                <li>57% de estudiantes necesita trabajar (ligeramente sobre media europea)</li>
                <li>Desconexión entre formación académica y mercado laboral</li>
                <li>Patrones de riesgo de abandono presentes</li>
            </ul>
        </div>
        
        <div>
            <h5>🎯 Oportunidades de mejora:</h5>
            <ul>
                <li>Fortalecer programas de prácticas relacionadas</li>
                <li>Mejorar coordinación universidad-empresa</li>
                <li>Ampliar sistemas de becas y apoyo económico</li>
                <li>Desarrollar formación dual en sectores clave</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">🏛️ Reflexión política y social</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    <h4>❓ Preguntas críticas para el debate europeo</h4>
    
    <p><strong>1. ¿Es aceptable que la supervivencia económica determine las trayectorias educativas?</strong></p>
    <p>Los datos revelan que muchos estudiantes no eligen trabajar por desarrollo profesional, sino por necesidad económica básica.</p>
    
    <p><strong>2. ¿Deberían los sistemas de becas europeos ser más generosos y universales?</strong></p>
    <p>Países con mejor apoyo estudiantil muestran menor necesidad de trabajo y mejores resultados educativos.</p>
    
    <p><strong>3. ¿Cómo crear más oportunidades de trabajo formativo relacionado con estudios?</strong></p>
    <p>La diferencia entre trabajo relacionado y no relacionado es crucial para el desarrollo académico y profesional.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">📋 Recomendaciones por sector</h3>', unsafe_allow_html=True)

# Recomendaciones organizadas por actor
recom_tabs = st.tabs(["🏛️ Políticas Públicas", "🎓 Instituciones Educativas", "🏢 Sector Empresarial", "👨‍🎓 Estudiantes y Familias"])

with recom_tabs[0]:
    st.markdown("""
    <div class="insight-box">
        <h4>🏛️ Recomendaciones para Políticas Públicas</h4>
        <ol>
            <li><strong>Ampliar sistemas de becas:</strong> Aumentar cobertura y cuantías para reducir dependencia del trabajo</li>
            <li><strong>Crear incentivos fiscales:</strong> Para empresas que ofrezcan trabajo relacionado con estudios</li>
            <li><strong>Desarrollar formación dual:</strong> Programas que combinen trabajo y estudio de manera estructurada</li>
            <li><strong>Monitorear indicadores:</strong> Seguimiento del riesgo de abandono por motivos económicos</li>
            <li><strong>Coordinación europea:</strong> Intercambio de mejores prácticas entre países exitosos</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

with recom_tabs[1]:
    st.markdown("""
    <div class="insight-box">
        <h4>🎓 Recomendaciones para Instituciones Educativas</h4>
        <ol>
            <li><strong>Programas trabajo-estudio:</strong> Crear más oportunidades de empleo relacionado dentro del campus</li>
            <li><strong>Flexibilidad académica:</strong> Horarios y modalidades adaptadas a estudiantes trabajadores</li>
            <li><strong>Servicios de apoyo:</strong> Orientación profesional y apoyo psicosocial especializado</li>
            <li><strong>Alianzas empresariales:</strong> Convenios para prácticas remuneradas de calidad</li>
            <li><strong>Sistemas de alerta:</strong> Identificación temprana de estudiantes en riesgo de abandono</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

with recom_tabs[2]:
    st.markdown("""
    <div class="insight-box">
        <h4>🏢 Recomendaciones para Sector Empresarial</h4>
        <ol>
            <li><strong>Empleos formativos:</strong> Crear posiciones que aporten experiencia relevante a los estudios</li>
            <li><strong>Flexibilidad horaria:</strong> Adaptarse a calendarios académicos y períodos de exámenes</li>
            <li><strong>Programas de desarrollo:</strong> Invertir en la formación de estudiantes empleados</li>
            <li><strong>Colaboración educativa:</strong> Participar en diseño de currículos y proyectos académicos</li>
            <li><strong>Responsabilidad social:</strong> Reconocer el impacto en la educación de futuras generaciones</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

with recom_tabs[3]:
    st.markdown("""
    <div class="insight-box">
        <h4>👨‍🎓 Recomendaciones para Estudiantes y Familias</h4>
        <ol>
            <li><strong>Planificación estratégica:</strong> Priorizar trabajo relacionado con estudios cuando sea posible</li>
            <li><strong>Gestión del tiempo:</strong> Desarrollar habilidades de organización y priorización</li>
            <li><strong>Búsqueda de apoyo:</strong> Utilizar servicios de orientación y becas disponibles</li>
            <li><strong>Red de contactos:</strong> Aprovechar oportunidades de networking profesional</li>
            <li><strong>Equilibrio vital:</strong> No sacrificar completamente salud y bienestar por supervivencia económica</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">🔮 Direcciones futuras de investigación</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>🔬 Próximos pasos en la investigación</h4>
    <ul>
        <li><strong>Estudios longitudinales:</strong> Seguimiento de cohortes para evaluar impacto a largo plazo</li>
        <li><strong>Análisis de políticas:</strong> Evaluación de efectividad de diferentes sistemas de apoyo</li>
        <li><strong>Impacto post-graduación:</strong> Cómo afecta la experiencia laboral estudiantil a la carrera profesional</li>
        <li><strong>Diferencias por sector:</strong> Análisis específico por campos de estudio y tipos de trabajo</li>
        <li><strong>Perspectiva de género:</strong> Profundizar en diferencias de género en patrones de trabajo-estudio</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<h3 class="subsection-header">💫 Reflexión final</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <h4>🌍 Un reto europeo, una oportunidad común</h4>
    <p><strong>El trabajo durante los estudios universitarios es una realidad compleja que requiere respuestas matizadas y coordinadas.</strong></p>
    
    <p>No se trata de eliminar completamente el trabajo estudiantil - que puede ser valioso para el desarrollo personal y profesional - 
    sino de <strong>asegurar que sea una elección y no una imposición de las circunstancias económicas</strong>.</p>
    
    <p>Los datos nos muestran que <strong>es posible hacer mejor las cosas</strong>. Países europeos con sistemas más equitativos demuestran 
    que se puede reducir la presión económica sobre los estudiantes sin comprometer la calidad educativa.</p>
    
    <p><strong>España, con su posición intermedia, tiene una oportunidad única</strong> de aprender de las mejores prácticas europeas 
    y desarrollar un sistema que combine apoyo estudiantil robusto con oportunidades de trabajo formativo de calidad.</p>
    
    <p>El futuro de la educación europea depende de nuestra capacidad para <strong>convertir esta necesidad en oportunidad</strong>, 
    asegurando que todos los estudiantes, independientemente de su origen socioeconómico, puedan acceder a una educación de 
    calidad que los prepare para el futuro.</p>
</div>
""", unsafe_allow_html=True)

# Separador final
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="
    text-align: center; 
    color: var(--neutral-gray); 
    padding: 3rem 2rem;
    background: linear-gradient(135deg, var(--bg-light) 0%, #ffffff 100%);
    border-radius: 15px;
    margin: 2rem 0;
    border-top: 4px solid var(--primary-blue);
">
    <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">📊 Storytelling con datos sobre educación y trabajo en Europa</h4>
    <p style="margin-bottom: 0.5rem;"><strong>Análisis basado en datos de estudiantes universitarios europeos</strong></p>
    <p style="font-size: 0.9rem; margin-bottom: 1rem;">Estudio comparativo de 25 países • Enfoque especial en España</p>
    
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.5rem;">
        <div style="text-align: center;">
            <div style="font-size: 1.5rem; font-weight: 600; color: var(--europe-blue);">25</div>
            <div style="font-size: 0.8rem;">Países analizados</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 1.5rem; font-weight: 600; color: var(--spain-red);">9,072</div>
            <div style="font-size: 0.8rem;">Estudiantes españoles</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 1.5rem; font-weight: 600; color: var(--success-green);">8</div>
            <div style="font-size: 0.8rem;">Dimensiones analizadas</div>
        </div>
    </div>
    
    <p style="margin-top: 1.5rem; font-size: 0.8rem; font-style: italic;">
        "Trabajar y estudiar en Europa: ¿Oportunidad, sacrificio o desigualdad?" <br>
        Una investigación sobre la realidad del trabajo estudiantil en el contexto europeo contemporáneo.
    </p>
</div>
""", unsafe_allow_html=True)
