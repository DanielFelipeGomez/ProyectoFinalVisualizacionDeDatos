import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from enum import Enum


class Colors(Enum):
    EUROPE = "#1E88E5"
    NEGATIVE = "#E53935"
    SPAIN = "#FDD835"
    POSITIVE = "#43A047"
    WARNING = "#EF6C00"
    DANGER = "#B71C1C"


from advanced_demographic_charts import (
    create_field_of_study_comparison_chart,
    create_living_with_parents_comparison_chart,
    create_gender_comparison_chart,
    create_age_comparison_chart,
)

from storytelling_module import WorkStudyStorytellingCharts

from work_study_interactive_charts import (
    create_storytelling_work_study_charts,
    generate_storytelling_summary,
)

from storytelliing_charts import get_work_impact_figures_for_streamlit

from academic_perception_storytelling_chart import generate_academic_perception_analysis

from happiness_work_relation_chart import generate_happiness_work_relation_analysis

from cost_map_chart import generate_europe_cost_heatmap, get_cost_statistics

from sankey_student_journey_chart import get_sankey_for_streamlit

from age_isotype_chart import create_age_isotype_for_streamlit





st.set_page_config(
    page_title="Trabajar y estudiar en Europa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)



st.markdown(
    """
<style>
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
        --text-white: #FFFFFF;
        --text-light: #6C757D;
    }
    .stApp {
        background-color: #ffffff !important;
        color: var(--text-dark) !important;
    }
    
    /* Forzar fondo blanco en el contenido principal */
    .main .block-container {
        background-color: #ffffff !important;
        padding-top: 2rem !important;
    }
    
    .css-1d391kg {
        background-color: #f8f9fa !important;
    }
    .stApp > div > div > div > div > button,
    .stApp button[data-testid="collapsedControl"],
    .stApp button[title="Show sidebar"],
    .stApp button[title="Hide sidebar"],
    .css-1outpf7, 
    .css-1outpf7:hover, 
    .css-1outpf7:active, 
    .css-1outpf7:focus,
    [data-testid="collapsedControl"], 
    [data-testid="collapsedControl"]:hover,
    [data-testid="collapsedControl"]:active,
    [data-testid="collapsedControl"]:focus,
    button[title="Show sidebar"],
    button[title="Show sidebar"]:hover,
    button[title="Hide sidebar"],
    button[title="Hide sidebar"]:hover {
        background-color: #ffffff !important;
        background: #ffffff !important;
        color: #2C3E50 !important;
        border: 2px solid #DEE2E6 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
        border-radius: 8px !important;
    }
    
    .stApp button[data-testid="collapsedControl"] svg,
    .stApp button[title="Show sidebar"] svg,
    .stApp button[title="Hide sidebar"] svg,
    .css-1outpf7 svg, 
    .css-1outpf7 svg path,
    [data-testid="collapsedControl"] svg,
    [data-testid="collapsedControl"] svg path,
    button[title="Show sidebar"] svg,
    button[title="Show sidebar"] svg path,
    button[title="Hide sidebar"] svg,
    button[title="Hide sidebar"] svg path {
        color: #2C3E50 !important;
        fill: #2C3E50 !important;
        stroke: #2C3E50 !important;
    }
    .stSidebar button,
    .stSidebar button:hover,
    .css-1kyxreq button,
    .css-1kyxreq button:hover {
        background-color: #ffffff !important;
        color: #2C3E50 !important;
        border: 2px solid #DEE2E6 !important;
    }
    
    p, li, span, div {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    
    .stMarkdown {
        background-color: transparent !important;
    }
    
    .stMarkdown p, .stMarkdown li, .stMarkdown span, .stMarkdown div {
        color: var(--text-dark) !important;
        background-color: transparent !important;
    }
    .stat-spain { color: var(--spain-red) !important; }
    .stat-europe { color: var(--primary-blue) !important; }
    .stat-positive { color: var(--success-green) !important; }
    .stat-negative { color: var(--danger-red) !important; }
    .stat-warning { color: var(--warning-orange) !important; }
    .stat-neutral { color: var(--neutral-gray) !important; }
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
         background: linear-gradient(135deg, #E3F2FD 0%, #F0F8FF 100%) !important;
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
        width: 100% !important;
        align-items: stretch;
    }
    
         .stat-item {
         text-align: center;
         padding: 1.5rem;
         background: white !important;
         border-radius: 10px;
         box-shadow: 0 2px 8px rgba(0,0,0,0.1);
         min-width: 150px;
         flex: 1;
         display: flex !important;
         flex-direction: column;
         justify-content: center;
         margin: 0.5rem;
     }
     
     .stat-number {
         font-size: 2.5rem;
         font-weight: 700;
         margin-bottom: 0.5rem;
     }

     .stat-title {
         font-size: 1.2rem;
         font-weight: 700;
         margin-bottom: 0.5rem;
     }
     
     .stat-label {
         font-size: 0.9rem;
         color: var(--text-medium) !important;
         font-weight: 500;
     }
    

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
    

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background: transparent !important;
        padding: 0.5rem 0 !important;
        border-bottom: 3px solid var(--border-light) !important;
        margin-bottom: 1.5rem !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #F8F9FA 0%, #FFFFFF 100%) !important;
        border: 2px solid var(--border-light) !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.5rem !important;
        color: var(--text-dark) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08) !important;
        margin: 0 0.3rem !important;
        text-align: center !important;
        min-width: auto !important;
        white-space: nowrap !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--secondary-blue) 100%) !important;
        color: white !important;
        border-color: var(--accent-blue) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3) !important;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%) !important;
        color: white !important;
        border-color: var(--primary-blue) !important;
        box-shadow: 0 4px 16px rgba(0, 61, 165, 0.4) !important;
        transform: translateY(-1px) !important;
    }
    
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] div {
        color: inherit !important;
        font-weight: inherit !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        padding: 1.5rem 0 !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"]::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        border-bottom: 8px solid var(--primary-blue);
    }
    

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
        
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: wrap !important;
            justify-content: center !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.85rem !important;
            padding: 0.6rem 1rem !important;
            margin: 0.2rem !important;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """
    <style>
    .sidebar-nav {
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .sidebar-nav h3 {
        color: white !important;
        margin-bottom: 1rem;
        text-align: center;
        font-size: 1.1rem;
    }
    .sidebar-nav-item {
        color: white !important;
        text-decoration: none;
        display: block;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        transition: all 0.2s ease;
    }
    .sidebar-nav-item:hover {
        color: #FDD835 !important;
        background: rgba(255,255,255,0.1);
        padding-left: 0.5rem;
        border-radius: 5px;
        text-decoration: none;
    }
    .sidebar-nav-item:last-child {
        border-bottom: none;
    }
    .sidebar-note {
        color: rgba(255,255,255,0.8) !important;
        font-size: 0.8rem;
        font-style: italic;
        margin-top: 1rem;
        text-align: center;
    }
    .sidebar-info {
        background: linear-gradient(135deg, #C41E3A 0%, #E74C3C 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    .sidebar-info h4 {
        color: white !important;
        margin-bottom: 0.8rem;
        text-align: center;
        font-size: 1rem;
    }
    .sidebar-info ul {
        color: white !important;
        padding-left: 1rem;
    }
    .sidebar-info li {
        color: white !important;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """
    <div class="sidebar-nav">
        <h3>Navegación rápida</h3>
        <a href="#introduccion-y-contexto-europeo" class="sidebar-nav-item">Contexto europeo</a>
        <a href="#perfil-completo-de-los-estudiantes-que-trabajan" class="sidebar-nav-item">Perfil de estudiantes</a>
        <a href="#tipos-de-trabajo-relacionado-o-supervivencia" class="sidebar-nav-item">Tipos de trabajo</a>
        <a href="#impacto-real-consecuencias-del-trabajo" class="sidebar-nav-item">Impacto y consecuencias</a>
        <a href="#conclusiones-y-reflexiones" class="sidebar-nav-item">Conclusiones</a>
    </div>
    """,
    unsafe_allow_html=True,
)


def show_chart_placeholder(chart_name, description=""):
    st.markdown(
        f"""
    <div class="chart-placeholder">
        <h4>{chart_name}</h4>
        <p>{description}</p>
        <p><em>Gráfico por implementar</em></p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def create_stats_display(stats_data):
    """Crear display de estadísticas usando columnas de Streamlit"""
    cols = st.columns(len(stats_data))

    for i, stat in enumerate(stats_data):
        color_class = stat.get("color", "stat-neutral")
        with cols[i]:
            st.markdown(
                f"""
            <div class="stat-item">
                <div class="stat-number {color_class}">{stat['number']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )


def create_text_stats_display(stats_data):
    cols = st.columns(len(stats_data))

    for i, stat in enumerate(stats_data):
        color_class = stat.get("color", "stat-neutral")
        with cols[i]:
            st.markdown(
                f"""
            <div class="stat-item">
                <div class="stat-title {color_class}">{stat['title']}</div>
                <div class="stat-text">{stat['text']}</div>
                <div class="stat-subtext">{stat['subtext']}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )


st.markdown(
    '<h1 class="main-header">Trabajar y estudiar en Europa:<br>¿Oportunidad, sacrificio o desigualdad?</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<h2 class="section-header" id="introduccion-y-contexto-europeo">Introducción y Contexto Europeo</h2>',
    unsafe_allow_html=True,
)
intro_stats = [
    {
        "number": "50%",
        "label": "Estudiantes europeos que trabajan mientras estudian",
        "color": "stat-europe",
    },
    {"number": "25", "label": "Países europeos analizados", "color": "stat-europe"},
    {
        "number": "9,072",
        "label": "Estudiantes españoles en el estudio",
        "color": "stat-spain",
    },
]

create_stats_display(intro_stats)

st.markdown(
    """
La Unión Europea es considerada un referente internacional en educación superior, con más de 17,5 millones de estudiantes universitarios y numerosos programas de movilidad e innovación educativa. Sin embargo, detrás de estas cifras positivas, existen retos importantes que afectan la experiencia y el futuro académico de miles de jóvenes. Factores como la necesidad de trabajar para costearse los estudios, las diferencias socioeconómicas y la modalidad de enseñanza pueden marcar una diferencia crucial en el rendimiento, la salud y las oportunidades de los estudiantes.

En este análisis, exploramos el equilibrio entre trabajo y estudios en Europa, teniendo como foco principal España: ¿es una oportunidad para crecer profesionalmente, o una barrera que limita el acceso y el éxito académico? A través de datos comparativos de diferentes países, identificamos tendencias, desigualdades y áreas de mejora clave para lograr una educación realmente inclusiva y competitiva."""
)

st.markdown(
    """
<div class="insight-box">
    <h4>Lo que descubrirás en este análisis</h4>
    <ul>
        <li><strong>¿Quiénes trabajan y por qué?</strong> Perfil demográfico y motivos de los estudiantes que compaginan empleo y estudios en 25 países europeos.</li>
        <li><strong>¿Es igual para todos?</strong> Diferencias por género, edad, situación económica y campo de estudio, con foco en las desigualdades.</li>
        <li><strong>¿Qué supone trabajar?</strong> Impacto en el rendimiento académico, el bienestar y la felicidad.</li>
        <li><strong>¿Trabajo útil o solo por necesidad?</strong> Relación entre el empleo de los estudiantes y sus estudios, con el caso especial de España.</li>
        <li><strong>¿Qué riesgos y oportunidades existen?</strong> Factores de abandono, beneficios y desventajas según los datos.</li>
        <li><strong>¿Cómo mejorar?</strong> Recomendaciones y reflexiones finales para estudiantes, instituciones y responsables políticos.</li>
    </ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<h3 class="subsection-header">Panorama Europeo: ¿Quiénes necesitan trabajar?</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    """
Antes de profundizar en las características específicas, veamos el panorama general europeo de la 
**necesidad de trabajar para costear estudios** por país. Este gráfico muestra la proporción de 
estudiantes que necesitan vs. no necesitan trabajar en cada país europeo.
"""
)

try:
    st.markdown("#### Necesidad de Trabajar para Costear Estudios por País")

    storytelling_charts = WorkStudyStorytellingCharts()
    fig_need_work = storytelling_charts.get_chart_need_vs_no_need()

    if fig_need_work:
        st.plotly_chart(
            fig_need_work, use_container_width=True, key="chart_need_vs_no_need"
        )

        insights = storytelling_charts.get_key_insights()

        if "error" not in insights:
            work_necessity_stats = [
                {
                    "number": f"{insights['spain_need_work']:.1f}%",
                    "label": "Estudiantes españoles necesitan trabajar",
                    "color": "stat-spain",
                },
                {
                    "number": f"{insights['europe_need_work']:.1f}%",
                    "label": "Promedio europeo necesita trabajar",
                    "color": "stat-europe",
                },
                {
                    "number": f"{insights['difference']:+.1f}pp",
                    "label": "Diferencia España vs Europa",
                    "color": (
                        "stat-warning"
                        if insights["difference"] > 0
                        else "stat-positive"
                    ),
                },
            ]

            create_stats_display(work_necessity_stats)
            st.markdown(
                f"""
            <div class="insight-box">
                <h4>🔍 Análisis del panorama europeo</h4>
                <ul>
                    <li><strong>País con menor necesidad:</strong> {insights['min_country']} ({insights['min_percentage']:.1f}%)</li>
                    <li><strong>País con mayor necesidad:</strong> {insights['max_country']} ({insights['max_percentage']:.1f}%)</li>
                </ul>
                <p>El 57% de los estudiantes españoles necesita trabajar para costear sus estudios, una cifra ligeramente inferior al promedio europeo (59.1%). Aunque esta diferencia parece pequeña, implica que <strong>más de la mitad de los universitarios en España compaginan trabajo y estudios</strong>, lo que puede tener un impacto en su rendimiento académico y bienestar personal.

La realidad europea es muy heterogénea: en países como Azerbaiyán, solo un 30.7% de estudiantes necesita trabajar, probablemente por un mayor apoyo estatal o un menor coste de vida. En el otro extremo, en Islandia el 83% debe hacerlo, reflejando posiblemente una menor cobertura de becas o costes de vida elevados.

¿Qué implicaciones tiene para la equidad y la calidad educativa esta gran disparidad? ¿Podría España aspirar a reducir todavía más la necesidad de trabajar entre sus estudiantes, acercándose a los países más "protegidos"? ¿Cómo afecta esto a la experiencia universitaria y al futuro profesional de los jóvenes? Estas preguntas nos invitan a reflexionar sobre el papel de las políticas públicas y el apoyo institucional en la vida del estudiantado.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("No se pudieron obtener insights automáticos del gráfico")
    else:
        show_chart_placeholder(
            "Necesidad de Trabajar por País", "Error generando gráfico principal"
        )

except Exception as e:
    st.error(f"Error cargando gráfico principal de necesidad de trabajar: {e}")
    show_chart_placeholder(
        "Error: Necesidad de Trabajar por País",
        "Error cargando datos del storytelling_module",
    )

st.markdown(
    '<h3 class="subsection-header">España vs Europa: Comparación Directa de Motivos para Trabajar</h3>',
    unsafe_allow_html=True,
)

try:
    fig_spain_europe = storytelling_charts.get_chart_spain_vs_europe()

    if fig_spain_europe:
        st.plotly_chart(
            fig_spain_europe,
            use_container_width=True,
            key="chart_spain_vs_europe_detailed",
        )

        st.markdown(
            """
        <div class="insight-box">
            <h3>Puntos clave España vs Europa</h3>
            <ul>
                <li><strong>42,4%</strong> de los alumnos españoles se plantean seriamente tener que trabajar para poder pagar sus estudios, una cifra superior al <strong>38%</strong> del promedio europeo.</li>
                <li>Por otro lado, <strong>34,8%</strong> consideran que no necesitarán trabajar para costearse sus estudios, lo cual también supera al promedio europeo del <strong>30%</strong>.</li>
                <li><strong>Dato relevante:</strong> cerca del <strong>57%</strong> de los estudiantes españoles trabajan, y uno de los motivos principales es poder costear sus estudios. Esto refleja que, aunque existen ayudas gubernamentales, una parte considerable de los estudiantes no recibe el apoyo suficiente.</li>
            </ul>
            <p>
                <em>Estudiar, para muchos, deja de ser una elección libre y pasa a depender del trabajo como única vía para hacerlo posible.</em>
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        show_chart_placeholder(
            "España vs Europa - Detallado", "Error generando comparación detallada"
        )

except Exception as e:
    st.error(f"Error cargando comparación España vs Europa: {e}")
    show_chart_placeholder(
        "Error: Comparación España vs Europa", "Error cargando datos detallados"
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-header" id="perfil-completo-de-los-estudiantes-que-trabajan">Perfil Completo de los Estudiantes que Trabajan</h2>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Quiénes son realmente los estudiantes que necesitan trabajar mientras estudian?** 

No todos los estudiantes tienen la misma probabilidad de trabajar. La realidad europea revela diferencias significativas 
por país, edad, género, situación familiar y campo de estudio. Esta sección explora el perfil completo de estos estudiantes, 
desde la perspectiva europea general hasta las características específicas de España.
"""
)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Distribución por País")
    st.markdown(
        """
        <div class="insight-box">
    <h4>Análisis por País</h4>
    <p>
        Los costes mensuales de los estudiantes universitarios en Europa varían mucho según el país, influyendo en la necesidad de trabajar para financiar los estudios. Por ejemplo, países como Hungría o Polonia tienen gastos bajos, mientras que Islandia e Irlanda presentan costes elevados. 
    </p>
    <p>
        <strong>España</strong> se sitúa ligeramente por encima de la media europea en gasto mensual (<strong>1.228 €</strong>), pero las becas públicas solo cubren una parte reducida de estos costes, lo que obliga a muchos estudiantes a trabajar.
    </p>
    <p>
        <strong>Conclusión:</strong> La necesidad de trabajar no depende solo del coste de vida, sino también del nivel de apoyo público y las becas disponibles. Países con mejores ayudas permiten que más estudiantes se dediquen plenamente a sus estudios.
    </p>
</div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    try:
        fig_cost_map = generate_europe_cost_heatmap()

        if fig_cost_map:
            st.plotly_chart(
                fig_cost_map, use_container_width=True, key="chart_europe_cost_heatmap"
            )

            cost_stats = get_cost_statistics()

            if "error" not in cost_stats:
                cost_display_stats = [
                    {
                        "number": f"€{cost_stats['promedio_europa']:,.0f}",
                        "label": "Promedio Europeo",
                        "color": "stat-europe",
                    },
                    {
                        "number": f"€{cost_stats.get('coste_espana', 0):,.0f}",
                        "label": "España",
                        "color": "stat-spain",
                    },
                    {
                        "number": f"#{cost_stats.get('ranking_espana', 'N/A')}/{cost_stats['total_paises']}",
                        "label": "Ranking España",
                        "color": "stat-warning",
                    },
                ]

                create_stats_display(cost_display_stats)

        else:
            show_chart_placeholder("Mapa de Costes Europeos", "Error generando mapa")

    except Exception as e:
        st.error(f"Error cargando mapa de costes: {e}")
        show_chart_placeholder(
            "Error en Mapa de Costes", "Error cargando datos de costes"
        )

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Distribución por Género")
    try:
        fig_gender = create_gender_comparison_chart()
        st.plotly_chart(
            fig_gender, use_container_width=True, key="chart_gender_comparison"
        )
    except Exception as e:
        st.error(f"Error cargando gráfico de género: {e}")
        show_chart_placeholder(
            "Error en Distribución por Género", "Error cargando datos"
        )

with col2:
    st.markdown(
        """
    <div class="insight-box">
        <h4>Diferencias de género en la necesidad de trabajar</h4>
        <ul>
            <li>En terminos generales no se evidencia una diferencia significativa entre hombres y mujeres en la necesidad de trabajar mientras estudian.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Distribución por Edad")

    st.markdown(
        """
    <div class="insight-box">
        <h4>Necesidad de Trabajar por Edad (España vs Europa)</h4>
  <p>
    El gráfico por edades muestra una tendencia clara: a mayor edad, mayor presión económica sobre los estudiantes, especialmente en España:
  </p>
  <ul>
    <li><strong>Menores de 22 años:</strong> España 21,2 % vs Europa 40,1 %.</li>
    <li><strong>De 22 a 24 años:</strong> España 38,6 % vs Europa 49,1 %.</li>
    <li><strong>De 25 a 29 años:</strong> España 75,4 % vs Europa 68,3 %.</li>
    <li><strong>30 años o más:</strong> España 91,2 % vs Europa 82,0 %.</li>
  </ul>
  <p>
    Esta evolución indica que los <strong>estudiantes adultos en España</strong> enfrentan mayores obstáculos económicos, probablemente debido a la pérdida de acceso a ayudas o el aumento de responsabilidades económicas personales.
  </p>

</div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    try:
        fig_age = create_age_comparison_chart()
        st.plotly_chart(fig_age, use_container_width=True, key="chart_age_comparison")
    except Exception as e:
        st.error(f"Error cargando gráfico de edad: {e}")
        show_chart_placeholder("Error en Distribución por Edad", "Error cargando datos")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Situación de Convivencia")
    try:
        fig_living = create_living_with_parents_comparison_chart()
        st.plotly_chart(
            fig_living, use_container_width=True, key="chart_living_situation"
        )
    except Exception as e:
        st.error(f"Error cargando gráfico de convivencia: {e}")
        show_chart_placeholder("Error en Tipo de Convivencia", "Error cargando datos")

with col2:
    st.markdown(
        """
    <div class="insight-box">
        <h4>Necesidad de Trabajar según la Situación de Vivienda</h4>
        <p>
            Esta gráfica muestra claramente cómo la necesidad de trabajar se ve influida por el hecho de vivir o no con los padres, comparando a <strong>España</strong> con el <strong>promedio europeo</strong>:
        </p>
        <ul>
            <li>
            Entre quienes <strong>viven con sus padres</strong>, la necesidad de trabajar es menor en España (≈36 %) que en Europa (≈43 %), lo que sugiere un mayor grado de apoyo familiar directo en el contexto español.
            </li>
            <li>
            Sin embargo, para los estudiantes que <strong>no viven con sus padres</strong>, la diferencia se invierte y se amplía: en España, el porcentaje que necesita trabajar supera el <strong>75 %</strong>, frente a alrededor del <strong>65 %</strong> en la media europea.
            </li>
        </ul>
        
    </div>
    """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
<div
  class="context-box"
  style="
    background: #f8f9fa;
    border-left: 4px solid #007bff;
    padding: 15px;
    margin: 20px 0;
    border-radius: 8px;
  "
>
  <p>
    Esta diferencia puede explicarse por el
    <strong>alto coste de la emancipación estudiantil</strong> en España y la
    limitada cobertura de becas. Además, en muchas regiones, los estudiantes se
    ven obligados a abandonar su hogar para acceder a estudios superiores.
  </p>
  <strong>Ejemplo contextual – Canarias:</strong><br />
  En comunidades como <strong>Canarias</strong>, numerosos estudiantes se ven
  forzados a dejar sus islas natales para estudiar en universidades que se
  ubican únicamente en <strong>Tenerife</strong> o
  <strong>Gran Canaria</strong>, o incluso en la península. Esta situación
  implica gastos de alojamiento y manutención que no tendrían si pudieran
  estudiar desde casa, lo cual incrementa drásticamente su necesidad de ingresos
  y los obliga a trabajar mientras cursan sus estudios.
</div>

""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Necesidad de Trabajar por Área de Estudios")

    st.markdown(
        """
    <div class="insight-box">
    <h4>Campo de estudio</h4>
    <p>
        En los campos de estudio, vemos que en España se presenta una clara disparidad en el área de ciencias naturales, matemáticas y estadísticas, donde el 75,3 % de las personas necesitan trabajar, frente al 43,3 % del promedio europeo en la misma área.
    También se observa una disminución en la necesidad de trabajar entre los estudiantes del ámbito de la salud.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    try:
        fig_field = create_field_of_study_comparison_chart()
        st.plotly_chart(fig_field, use_container_width=True, key="chart_field_of_study")
    except Exception as e:
        st.error(f"Error cargando gráfico de campo de estudio: {e}")
        show_chart_placeholder("Error en Campo de Estudio", "Error cargando datos")



st.markdown(
    '<h3 class="subsection-header">Trayectoria Académica y Perfil Socioeconómico en España</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Cómo se conectan las características demográficas de los estudiantes españoles con su situación académica y económica?**
"""
)

try:
    sankey_result = get_sankey_for_streamlit()

    if sankey_result["success"] and sankey_result["figure"]:
        st.plotly_chart(
            sankey_result["figure"],
            use_container_width=True,
            key="sankey_student_journey",
        )

        insights = sankey_result["insights"]

        if insights and "error" not in insights:
            sankey_stats = [
                {
                    "title": "Perfil Edad",
                    "text": "Mayoría ≤ 22 años",
                    "subtext": "Concentrados en Ingeniería y Ciencias Sociales",
                    "color": "stat-europe",
                },
                {
                    "title": "Perfil Género",
                    "text": "Ingeniería: Más masculina",
                    "subtext": "Salud y Sociales: Más femenina",
                    "color": "stat-spain",
                },
                {
                    "title": "Perfil Ingresos",
                    "text": "Negocios/Ingeniería → Altos",
                    "subtext": "Salud/Sociales → Medios/Bajos",
                    "color": "stat-positive",
                },
            ]

            create_text_stats_display(sankey_stats)
            st.markdown(
                """
            <div class="conclusion-box">
                <h4>Reflexiones clave sobre el perfil del estudiante español</h4>
                <ul>
                    <li><strong>Diversidad de edad:</strong> Los estudiantes más jóvenes (≤22) dominan, pero también hay participación significativa de mayores de 23.</li>
                    <li><strong>Segregación por género:</strong> Persisten patrones tradicionales en la elección de carrera.</li>
                    <li><strong>Campo de estudio y oportunidades económicas:</strong> Ingeniería y Negocios se asocian con niveles de ingresos más altos.</li>
                    <li><strong>Implicaciones para políticas públicas:</strong> Los datos revelan brechas estructurales que requieren atención.</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        else:
            st.warning("No se pudieron generar insights automáticos del Sankey")

    else:
        error_msg = sankey_result.get("error", "Error desconocido")
        st.error(f"❌ Error cargando diagrama de Sankey: {error_msg}")
        show_chart_placeholder(
            "Diagrama de Sankey - Trayectoria del Estudiante Español",
            "Error cargando datos para el diagrama interactivo",
        )

except Exception as e:
    st.error(f"Error crítico en sección Sankey: {e}")
    show_chart_placeholder(
        "Error: Diagrama de Sankey", "Error crítico cargando el módulo de Sankey"
    )



st.markdown(
    """
<div class="insight-box">
    <h4>Síntesis del Perfil Completo de Estudiantes</h4>
    <ul>
        <li><strong>Gran variabilidad del coste de estudios en Europa:</strong> <br>
            <span>España destaca por la <strong>presión económica</strong> sobre sus estudiantes, según el nivel de gasto y ayudas públicas.</span>
        </li>
        <li><strong>No hay diferencias significativas por género:</strong> <br>
            <span><strong>Hombres y mujeres</strong> comparten una necesidad similar de trabajar mientras estudian.</span>
        </li>
        <li><strong>La edad influye mucho en la necesidad de trabajar en España:</strong> <br>
            <span>Aumenta con la edad y <strong>supera la media europea</strong> en los tramos más altos.</span>
        </li>
        <li><strong>Vivir fuera del hogar familiar aumenta la necesidad de trabajar:</strong> <br>
            <span>En España es especialmente grave por el <strong>alto coste de emancipación</strong> y las <strong>becas limitadas</strong>.</span>
        </li>
        <li><strong>Diferencias marcadas por campo de estudio:</strong> <br>
            <span>Alta necesidad de trabajar en <strong>ciencias naturales, matemáticas y estadísticas</strong>; menor en el <strong>área de salud</strong>.</span>
        </li>
        <li><strong>Trayectoria socioeconómica:</strong> <br>
            <span>El perfil demográfico determina fuertemente las <strong>oportunidades económicas futuras</strong> de los estudiantes.</span>
        </li>
    </ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-header" id="tipos-de-trabajo-relacionado-o-supervivencia">Tipos de Trabajo: ¿Relacionado o Supervivencia?</h2>',
    unsafe_allow_html=True,
)

st.markdown(
    """
Una distinción fundamental es si el trabajo que realizan los estudiantes está relacionado con su área de estudios 
o no. Esta diferencia puede tener implicaciones significativas tanto para el desarrollo profesional como para el 
rendimiento académico.

**España se encuentra en una posición intermedia** en cuanto a la relación entre trabajo y estudios, pero existe 
margen de mejora comparado con otros países europeos.
"""
)


st.markdown(
    '<h3 class="subsection-header">España vs Europa: Relación Trabajo-Estudio</h3>',
    unsafe_allow_html=True,
)

try:
    charts, df_work_study = create_storytelling_work_study_charts()

    st.plotly_chart(
        charts["hero_chart"], use_container_width=True, key="hero_work_study_chart"
    )

    summary = generate_storytelling_summary(df_work_study)
    work_study_stats = [
        {
            "number": f"{summary['spain_percentage']:.1f}%",
            "label": "Trabajo relacionado con estudios en España",
            "color": "stat-spain",
        },
        {
            "number": f"{summary['europe_percentage']:.1f}%",
            "label": "Promedio europeo",
            "color": "stat-europe",
        },
        {
            "number": f"{summary['spain_rank']}/25",
            "label": "Posición de España en Europa",
            "color": "stat-warning",
        },
    ]

    create_stats_display(work_study_stats)

    st.markdown(
        f"""
    <div class="spain-box">
    <h4>Problemática del empleo no relacionado en estudiantes en España</h4>
    <p>
        En España, un preocupante <strong>45,4% de los estudiantes que trabajan lo hacen en empleos poco o nada relacionados</strong> con sus estudios. 
        Esta cifra supera notablemente el <strong>promedio europeo del 37,7%</strong>, lo que evidencia una <strong>desconexión estructural</strong> entre el mundo académico y el laboral.
    </p>
    <ul>
        <li>Este alto porcentaje indica una <strong>falta de oportunidades laborales alineadas con la formación</strong> de los jóvenes.</li>
        <li>Puede provocar <strong>desmotivación y pérdida de valor práctico</strong> de los estudios universitarios.</li>
        <li>Limita el desarrollo de experiencia profesional relevante antes de graduarse.</li>
        <li>España necesita <strong>mejorar los vínculos entre universidades y el mercado laboral</strong> para reducir esta brecha.</li>
    </ul>
</div>

    """,
        unsafe_allow_html=True,
    )

except Exception as e:
    st.error(f"Error cargando datos de relación trabajo-estudio: {e}")
    show_chart_placeholder(
        "Error: España vs Europa", "Error cargando datos principales"
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-header" id="impacto-real-consecuencias-del-trabajo">Impacto Real: Consecuencias del Trabajo</h2>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Cómo afecta trabajar al rendimiento académico y la experiencia universitaria?**

Esta sección examina el impacto real del trabajo en la vida estudiantil, incluyendo la **consideración de abandono** de estudios y otros efectos sobre el bienestar académico.
"""
)

try:
    impact_figures = get_work_impact_figures_for_streamlit()

    if impact_figures:
        impact_tab1, impact_tab2, impact_tab3 = st.tabs(
            [
                "💸 Presión Financiera",
                "👔 Conflicto Trabajo-Estudio",
                "🇪🇸 España vs Europa",
            ]
        )

        with impact_tab1:
            st.markdown("### Abandono por Dificultades Financieras")
            st.markdown(
                """
            **¿Con qué frecuencia consideran los estudiantes abandonar sus estudios debido a dificultades económicas?**
            
            Este gráfico muestra la realidad de la presión financiera en la educación europea.
            """
            )

            if "abandono_financiero" in impact_figures:
                st.plotly_chart(
                    impact_figures["abandono_financiero"],
                    use_container_width=True,
                    key="impact_abandono_financiero",
                )

            else:
                show_chart_placeholder(
                    "Abandono por Dificultades Financieras", "Error cargando datos"
                )

        with impact_tab2:
            st.markdown("### Abandono por Necesidad de Trabajar")
            st.markdown(
                """
            **¿Consideran los estudiantes abandonar sus estudios para poder trabajar más tiempo?**
            
            Este análisis revela el conflicto directo entre supervivencia económica y continuidad académica.
            """
            )

            if "abandono_trabajo" in impact_figures:
                st.plotly_chart(
                    impact_figures["abandono_trabajo"],
                    use_container_width=True,
                    key="impact_abandono_trabajo",
                )

            else:
                show_chart_placeholder(
                    "Abandono por Necesidad de Trabajar", "Error cargando datos"
                )

        with impact_tab3:
            st.markdown("### España vs Europa: Comparación Directa")
            st.markdown(
                """
            **¿Cómo se posiciona España específicamente en términos de impacto del trabajo en los estudios?**
            
            Comparación directa con el promedio europeo en ambos tipos de consideración de abandono.
            """
            )

            if "espana_vs_europa_impacto" in impact_figures:
                st.plotly_chart(
                    impact_figures["espana_vs_europa_impacto"],
                    use_container_width=True,
                    key="impact_espana_europa",
                )
            else:
                show_chart_placeholder(
                    "España vs Europa - Impacto", "Error cargando datos"
                )

    else:
        st.warning("No se pudieron cargar las gráficas de impacto")
        col1, col2 = st.columns(2)
        with col1:
            show_chart_placeholder(
                "Abandono por Dificultades Financieras", "Error cargando datos"
            )
        with col2:
            show_chart_placeholder(
                "Abandono por Necesidad de Trabajar", "Error cargando datos"
            )

except Exception as e:
    st.error(f"Error cargando análisis de impacto: {e}")
    col1, col2 = st.columns(2)
    with col1:
        show_chart_placeholder(
            "Horas de Trabajo vs. Horas de Estudio", "Error cargando datos de impacto"
        )
        show_chart_placeholder(
            "Rendimiento Académico Percibido", "Error cargando datos de impacto"
        )
    with col2:
        show_chart_placeholder(
            "Modalidad de Enseñanza e Impacto", "Error cargando datos de impacto"
        )
        show_chart_placeholder("Salud Percibida", "Error cargando datos de impacto")


st.markdown(
    '<h3 class="subsection-header">Percepción Académica Personal</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Cómo perciben los propios estudiantes que su trabajo afecta su rendimiento académico?**

Se les preguntó a los estudiantes españoles si sentían que tenían un **rendimiento mejor, igual o peor** en comparación con sus **compañeros de clase**.  
Observamos que, según la **relación con el esfuerzo que dedican al estudio**, las respuestas **difieren drásticamente**.
"""
)

try:
    fig_academic_perception, insights_academic = generate_academic_perception_analysis()

    if fig_academic_perception and insights_academic:
        st.plotly_chart(
            fig_academic_perception,
            use_container_width=True,
            key="chart_academic_perception",
        )

        academic_perception_stats = [
            {
                "number": f"{insights_academic['very_closely_better']:.1f}%",
                "label": "Mejor rendimiento - Trabajo muy relacionado",
                "color": "stat-positive",
            },
            {
                "number": f"{insights_academic['not_at_all_better']:.1f}%",
                "label": "Mejor rendimiento - Trabajo nada relacionado",
                "color": "stat-warning",
            },
            {
                "number": f"+{insights_academic['difference_very_vs_none']:.1f}pp",
                "label": "Diferencia favorable al trabajo relacionado",
                "color": "stat-positive",
            },
        ]

        create_stats_display(academic_perception_stats)

        st.markdown(
            f"""
        <div class="insight-box">
    <h4>Factores que explican la percepción académica positiva</h4>
    <p><strong>¿Por qué los estudiantes que trabajan en su sector perciben mejor rendimiento académico?</strong></p>
    <ul>
        <li><strong>Aplicación práctica:</strong> Usan lo aprendido en contextos reales, lo que refuerza el conocimiento teórico.</li>
        <li><strong>Mayor motivación:</strong> Al ver la utilidad directa de los contenidos, aumentan su interés y esfuerzo.</li>
        <li><strong>Feedback constante:</strong> El trabajo les da retroalimentación continua sobre sus competencias.</li>
        <li><strong>Habilidades transversales:</strong> Desarrollan comunicación, organización y trabajo en equipo.</li>
        <li><strong>Red profesional:</strong> El entorno laboral les aporta referentes y apoyo que refuerzan su confianza.</li>
    </ul>
    <p><em>Estos factores contribuyen a que quienes trabajan en el sector de lo que estudian se sientan más competentes y seguros en su desempeño académico.</em></p>
</div>
        """,
            unsafe_allow_html=True,
        )

    else:
        show_chart_placeholder(
            "Percepción Académica Personal",
            "Error cargando datos de percepción académica",
        )

except Exception as e:
    st.error(f"Error cargando análisis de percepción académica: {e}")
    show_chart_placeholder(
        "Error: Percepción Académica Personal", "Error cargando datos específicos"
    )


st.markdown(
    '<h3 class="subsection-header">Felicidad y Bienestar: El Factor Emocional</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Afecta la relación entre trabajo y estudios al bienestar emocional de los estudiantes?**

Se les preguntó a los estudiantes por su **grado de felicidad** en una escala del **1 al 5**.  
A continuación, observamos los resultados en relación con **cuán relacionado está su trabajo actual con lo que estudiaron**.
"""
)

try:
    fig_happiness, insights_happiness = generate_happiness_work_relation_analysis()

    if fig_happiness and insights_happiness:
        st.plotly_chart(
            fig_happiness, use_container_width=True, key="chart_happiness_work_relation"
        )


        happiness_stats = [
            {
                "number": f"{insights_happiness['very_closely_score']:.2f}",
                "label": "Felicidad promedio - Trabajo muy relacionado",
                "color": "stat-positive",
            },
            {
                "number": f"{insights_happiness['no_work_score']:.2f}",
                "label": "Felicidad promedio - Sin trabajo",
                "color": "stat-warning",
            },
            {
                "number": f"+{insights_happiness['work_vs_no_work_diff']:.2f}",
                "label": "Diferencia trabajo relacionado vs sin trabajo (1-5)",
                "color": "stat-positive",
            },
        ]

        create_stats_display(happiness_stats)

        st.markdown(
            f"""
        <div class="insight-box">
  <h4>Análisis Impactante</h4>
  <ul>
    <li><strong>Los estudiantes con trabajos muy relacionados con sus estudios alcanzan el mayor nivel de felicidad promedio (3.79)</strong>, superando incluso a quienes no trabajan (3.53).</li>
    <li><strong>A medida que el trabajo se aleja del área de estudio, el nivel de satisfacción disminuye progresivamente</strong>, alcanzando su punto más bajo (3.47) cuando el empleo no está nada relacionado.</li>
    <li><strong>La diferencia de felicidad entre trabajar en algo muy relacionado y no trabajar es de +0.26 puntos</strong>, lo que indica un impacto positivo notable.</li>
    <li><strong>No cualquier trabajo aporta bienestar al estudiante; el tipo de empleo importa tanto como su existencia.</strong></li>
    <li><strong>Conclusión clave:</strong> Integrar el trabajo con la carrera académica no solo enriquece la experiencia formativa, sino que <strong>aumenta el bienestar emocional de los estudiantes</strong>.</li>
  </ul>
</div>
        """,
            unsafe_allow_html=True,
        )

    else:
        show_chart_placeholder(
            "Felicidad según Relación Trabajo-Estudio",
            "Error cargando datos de felicidad",
        )

except Exception as e:
    st.error(f"Error cargando análisis de felicidad trabajo-estudio: {e}")
    show_chart_placeholder(
        "Error: Felicidad según Relación Trabajo-Estudio",
        "Error cargando datos específicos",
    )



st.markdown(
    '<h3 class="subsection-header">Análisis Visual por Edad: Estudiantes con Trabajos No Relacionados</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    """
**¿Cómo se distribuye por edad el problema de los trabajos no relacionados con los estudios?**
"""
)

try:
    isotype_result = create_age_isotype_for_streamlit()

    if isotype_result["success"] and isotype_result["figure"]:
        st.plotly_chart(
            isotype_result["figure"], use_container_width=True, key="age_isotype_chart"
        )

        insights = isotype_result["insights"]

        if insights and "error" not in insights:
            isotype_stats = [
                {
                    "number": f"{insights['age_data']['< 22 años']:.1f}%",
                    "label": "Estudiantes < 22 años con trabajo no relacionado",
                    "color": "stat-danger",
                },
                {
                    "number": f"{insights['age_data']['25-29 años']:.1f}%",
                    "label": "Estudiantes 25-29 años (menor impacto)",
                    "color": "stat-positive",
                },
                {
                    "number": f"{insights['age_data']['30+ años']:.1f}%",
                    "label": "Estudiantes 30+ años",
                    "color": "stat-warning",
                },
            ]

            create_stats_display(isotype_stats)
            st.markdown(
                f"""
            <div class="danger-box">
                <h4>Patrón Preocupante: Los Más Jóvenes, Más Desconectados y en Mayor Riesgo</h4>
                <p><strong>¿Por qué los estudiantes más jóvenes trabajan en empleos no relacionados?</strong></p>
                <ul>
                    <li>Menor experiencia laboral para encontrar trabajos relacionados</li>
                    <li>Presión económica inmediata los lleva a aceptar cualquier empleo</li>
                    <li>Falta de redes profesionales en su campo de estudio</li>
                    <li>Menor valoración por parte de empleadores de su formación incompleta</li>
                </ul>
                <p><strong>Consecuencias en cadena altamente preocupantes:</strong></p>
                <p>Recordemos que en nuestros análisis anteriores identificamos que <strong>las personas con trabajos menos relacionados con sus estudios se perciben menos felices</strong> (3.47 vs 3.79) y además <strong>se perciben peor académicamente</strong> comparado con sus compañeros de clase.</p>
                <p><strong>Esto significa que los estudiantes más jóvenes tienen mayor riesgo de:</strong></p>
                <ul>
                    <li>Ser infelices durante sus estudios</li>
                    <li>Percibir peor rendimiento académico</li>
                    <li>Abandonar prematuramente la educación superior</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        else:
            st.warning("No se pudieron generar insights automáticos del isotype")

    else:
        error_msg = isotype_result.get("error", "Error desconocido")
        st.error(f"❌ Error cargando isotype de edad: {error_msg}")
        show_chart_placeholder(
            "Isotype: Impacto por Edad", "Error cargando datos para el gráfico isotype"
        )

except Exception as e:
    st.error(f"Error crítico en sección isotype: {e}")
    show_chart_placeholder(
        "Error: Isotype de Edad", "Error crítico cargando el módulo de isotype"
    )


st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-header" id="conclusiones-y-reflexiones">Conclusiones y Reflexiones</h2>',
    unsafe_allow_html=True,
)

st.markdown(
    '<h3 class="subsection-header">💡 Hallazgos principales</h3>',
    unsafe_allow_html=True,
)


st.markdown("#### 1. Presión económica generalizada en Europa")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/1_of_2_students_work.png",
                width=500,
                caption="1 de cada 2 estudiantes trabaja",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/1_of_2_students_work.png")


    st.markdown(
        """
            <div class="stat-label" style="text-align: center; font-size: 1.2rem; margin-top: 1rem;">
            <span class="stat-number stat-europe" style="font-size: 4rem; text-align: center;">57%</span>
                 de estudiantes españoles necesitan trabajar para costear estudios
            </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="warning-box">
            <h4>Problemática identificada</h4>
            <p>Más de la <strong>mitad de los estudiantes europeos</strong> necesita trabajar para costear estudios. En España, aunque ligeramente menor que la media europea, esto implica que <strong>millones de jóvenes no pueden dedicarse exclusivamente a su formación</strong>.</p>
            <ul>
                <li>La falta de becas suficientes obliga a trabajar</li>
                <li>Alto coste de emancipación estudiantil</li>
                <li>Desigualdad en el acceso a la educación</li>
            </ul>
        </div>
        
        <div class="conclusion-box">
            <h4>Soluciones propuestas</h4>
            <ul>
                <li><strong>Ampliar sistemas de becas:</strong> Cobertura más universal y montos más altos</li>
                <li><strong>Apoyo para emancipación:</strong> Residencias estudiantiles subvencionadas</li>
                <li><strong>Políticas coordinadas EU:</strong> Estándares mínimos de apoyo estudiantil</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown(
    "#### 2. Desigualdades por perfil demográfico y beneficios del trabajo especializado"
)

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/oldest_students_help.png",
                width=600,
                caption="Estudiantes mayores necesitan más apoyo",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/oldest_students_help.png")


with col2:
    st.markdown(
        """
        <div class="warning-box">
            <h4>Problemática identificada</h4>
            <p><strong>Grandes desigualdades según perfil del estudiante:</strong></p>
            <ul>
                <li><strong>Por campo:</strong> Ciencias Naturales 75.3% vs Salud con menor necesidad</li>
                <li><strong>Por edad:</strong> Mayores de 25 años con 91.2% de necesidad en España</li>
                <li><strong>Acceso desigual:</strong> Pocos estudiantes acceden a trabajo relacionado con estudios</li>
            </ul>
            <p>Esto perpetúa desigualdades estructurales en el sistema educativo.</p>
        </div>
        
        <div class="conclusion-box">
            <h4>Soluciones propuestas</h4>
            <ul>
                <li><strong>Becas específicas por área:</strong> Apoyo especial para campos más vulnerables</li>
                <li><strong>Programas trabajo-estudio:</strong> Fomentar empleos relacionados con la formación</li>
                <li><strong>Apoyo estudiantes adultos:</strong> Flexibilidad y ayudas para mayores de 25</li>
                <li><strong>Colaboración universidad-empresa:</strong> Crear más oportunidades formativas</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown("#### 3. Igualdad de género en la necesidad de trabajar")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/equality_gender_students.png",
                width=500,
                caption="Igualdad de género en necesidad de trabajar",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/equality_gender_students.png")
    

with col2:
    st.markdown(
        """
        <div class="insight-box">
            <h4>Hallazgo positivo</h4>
            <p><strong>La necesidad económica trasciende las diferencias de género.</strong> Tanto hombres como mujeres enfrentan presiones similares para trabajar mientras estudian.</p>
            <ul>
                <li>No hay brecha de género en necesidad económica</li>
                <li>Ambos géneros igualmente vulnerables</li>
            </ul>
        </div>

        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown("#### 4. Crisis de la emancipación estudiantil")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/rent_problem_student.png",
                width=500,
                caption="Crisis de emancipación estudiantil",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/rent_problem_student.png")
    
 

with col2:
    st.markdown(
        """
        <div class="danger-box">
            <h4>Crisis crítica identificada</h4>
            <p><strong>La emancipación se ha vuelto un lujo inaccesible</strong> para muchos estudiantes españoles:</p>
            <ul>
                <li><strong>Costes prohibitivos:</strong> Alquiler + manutención + tasas universitarias</li>
                <li><strong>Becas insuficientes:</strong> No cubren gastos reales de vida independiente</li>
                <li><strong>Geografía penaliza:</strong> Estudiantes de provincias forzados a emigrar</li>
                <li><strong>Desigualdad territorial:</strong> Especialmente grave en comunidades insulares</li>
            </ul>
        </div>
        
        <div class="conclusion-box">
            <h4>Soluciones urgentes</h4>
            <ul>
                <li><strong>Residencias estudiantiles públicas:</strong> Inversión masiva en alojamiento universitario</li>
                <li><strong>Becas de emancipación:</strong> Ayudas específicas para gastos de vivienda</li>
                <li><strong>Descentralización universitaria:</strong> Más centros en provincias</li>
                <li><strong>Regulación alquileres:</strong> Control de precios en zonas universitarias</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown("#### 5. Desconexión entre trabajo y formación")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/not_related_jobs_student.png",
                width=500,
                caption="Trabajos no relacionados con estudios",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/not_related_jobs_student.png")
    
    st.markdown(
        """
            <div class="stat-label" style="text-align: center; font-size: 1.1rem; margin-top: 1rem;">
                <span class="stat-number stat-warning" style="font-size: 3.5rem;">45.4%</span> de estudiantes españoles que trabajan lo hacen en empleos NO relacionados
                vs. 37.7% promedio europeo
            </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="warning-box">
            <h4>Oportunidad perdida masiva</h4>
            <p><strong>Casi la mitad del trabajo estudiantil en España es "supervivencia" en lugar de "formación":</strong></p>
            <ul>
                <li><strong>Pérdida de valor formativo:</strong> Trabajo no aporta a desarrollo profesional</li>
                <li><strong>Competitividad futura:</strong> Graduados con menos experiencia relevante</li>
                <li><strong>Desmotivación académica:</strong> Desconexión entre realidad laboral y estudios</li>
                <li><strong>Círculo vicioso:</strong> Necesidad económica impide elegir trabajos formativos</li>
            </ul>
        </div>
        
        <div class="conclusion-box">
            <h4>Transformación necesaria</h4>
            <ul>
                <li><strong>Programas de prácticas remuneradas:</strong> Expandir oportunidades formativas pagadas</li>
                <li><strong>Colaboración universidad-empresa:</strong> Crear más empleos alineados con estudios</li>
                <li><strong>Flexibilidad académica:</strong> Horarios compatibles con trabajo formativo</li>
                <li><strong>Incentivos empresariales:</strong> Beneficios fiscales por contratar estudiantes</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown("#### 6. El coste del trabajo no relacionado en bienestar y rendimiento")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/health_problems_student.png",
                width=500,
                caption="Problemas de salud y bienestar estudiantil",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/health_problems_student.png")
    
 
with col2:
    st.markdown(
        """
        <div class="danger-box">
            <h4>Impacto grave en bienestar</h4>
            <p><strong>El trabajo no relacionado con estudios tiene consecuencias serias:</strong></p>
            <ul>
                <li><strong>Menor felicidad:</strong> 3.47 vs 3.79 en trabajos relacionados</li>
                <li><strong>Riesgo de abandono:</strong> Consideran dejar estudios por presión económica</li>
                <li><strong>Peor rendimiento percibido:</strong> Se sienten menos competentes académicamente</li>
                <li><strong>Estrés y fatiga:</strong> Doble carga sin beneficio formativo</li>
            </ul>
        </div>
        
        <div class="conclusion-box">
            <h4>Mejora integral necesaria</h4>
            <ul>
                <li><strong>Conexión universidad-empresa:</strong> Puentes efectivos para empleos formativos</li>
                <li><strong>Apoyo psicológico:</strong> Servicios de bienestar estudiantil</li>
                <li><strong>Flexibilidad académica:</strong> Adaptación a estudiantes trabajadores</li>
                <li><strong>Indicadores de calidad:</strong> Medir impacto del trabajo en experiencia educativa</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)

st.markdown("#### 7. Desigualdad estructural en el acceso a la educación")

col1, col2 = st.columns([1, 1])

with col1:
    try:
        img_col1, img_col2, img_col3 = st.columns([1, 0.5, 1])
        with img_col1:
            st.image(
                "images/general_problems_students.png",
                width=500,
                caption="Problemas estructurales del sistema educativo",
            )
    except Exception as e:
        st.warning("No se pudo cargar la imagen: images/general_problems_students.png")
    
    

with col2:
    st.markdown(
        """
        <div class="danger-box">
            <h4>Inequidad sistémica</h4>
            <p><strong>El sistema perpetúa desigualdades profundas:</strong></p>
            <ul>
                <li><strong>Por edad:</strong> Estudiantes adultos casi abandonados por el sistema</li>
                <li><strong>Por campo:</strong> Áreas científicas penalizadas vs áreas de salud</li>
                <li><strong>Por origen:</strong> Clase socioeconómica determina oportunidades</li>
                <li><strong>Por geografía:</strong> Estudiantes rurales/insulares más vulnerables</li>
            </ul>
            <p><em>La meritocracia se ve comprometida por factores estructurales.</em></p>
        </div>
        
        <div class="conclusion-box">
            <h4>Reforma estructural</h4>
            <ul>
                <li><strong>Universalidad del derecho:</strong> Educación superior como derecho garantizado</li>
                <li><strong>Discriminación positiva:</strong> Apoyos específicos para grupos vulnerables</li>
                <li><strong>Inversión pública masiva:</strong> Financiación adecuada del sistema</li>
                <li><strong>Coordinación europea:</strong> Estándares mínimos de equidad educativa</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )




st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown(
    """
<div style="
    text-align: center; 
    color: var(--neutral-gray); 
    padding: 1rem 2rem;
">
    <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">
        "Trabajar y estudiar en Europa: ¿Oportunidad, sacrificio o desigualdad?"
    </h4>
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin: 1rem 0;">
        <div style="text-align: center;">
            <div style="font-size: 1.5rem; font-weight: 600; color: var(--europe-blue);">25</div>
            <div style="font-size: 0.8rem;">Países europeos</div>
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
    <p style="margin-top: 1.5rem; font-size: 0.8rem;">
        Trabajo realizado por <strong>Daniel Felipe Gómez Aristizábal</strong> con fines académicos, 
        como parte de la asignatura <em>Visualización de Datos</em> del Máster Universitario en Ciencia de Datos de la <strong>UOC</strong>.
    </p>
    <p style="font-size: 0.8rem;">
        Fuente de datos: <a href="https://www.eurostudent.eu/" target="_blank">EUROSTUDENT</a>, iniciativa que recopila y analiza información comparable 
        sobre las condiciones de vida y estudio de los estudiantes de educación superior en Europa. 
        Se ha utilizado su base de datos pública de la <a href="https://database.eurostudent.eu/drm/" target="_blank">Ronda 8</a>, 
        centrando el análisis en España, con una muestra de <strong>9,072 estudiantes</strong>.
    </p>
</div>
""",
    unsafe_allow_html=True,
)


logo_col1, logo_col2, logo_col3 = st.columns([1, 2, 1])

with logo_col2:
    sub_col1, sub_col2 = st.columns(2)

    with sub_col1:
        try:
            st.image(
                "logos/eurostudent_logo.png",
                caption="EUROSTUDENT - Fuente de datos",
                use_container_width=True,
            )
        except Exception as e:
            st.warning("No se pudo cargar el logo de EUROSTUDENT")

    with sub_col2:
        try:
            st.image(
                "logos/uoc_masterbrand_2linies_posititiu.png",
                caption="UOC - Institución académica",
                use_container_width=True,
            )
        except Exception as e:
            st.warning("No se pudo cargar el logo de UOC")
