import streamlit as st
import plotly.graph_objects as go
from interactive_storytelling_charts import generate_all_interactive_charts
from advanced_demographic_charts import create_comprehensive_demographic_dashboard

# Configuración de la página
st.set_page_config(
    page_title="Estudiantes que Trabajan: Análisis Completo",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para scrollytelling profesional
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .section-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: #d62728;
        margin: 3rem 0 1.5rem 0;
        border-bottom: 4px solid #d62728;
        padding-bottom: 0.5rem;
    }
    
    .subsection-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1f77b4;
        margin: 2rem 0 1rem 0;
        border-left: 5px solid #1f77b4;
        padding-left: 1rem;
    }
    
    .insight-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 6px solid #d62728;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .demographic-insight {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 6px solid #1f77b4;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .metric-highlight {
        font-size: 3rem;
        font-weight: bold;
        color: #d62728;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .context-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #2c3e50;
        text-align: justify;
        margin: 1.5rem 0;
    }
    
    .story-quote {
        font-size: 1.4rem;
        font-style: italic;
        color: #5a6c7d;
        text-align: center;
        margin: 2rem 0;
        padding: 1rem;
        border-top: 2px solid #dee2e6;
        border-bottom: 2px solid #dee2e6;
    }
    
    .conclusion-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 2px solid #28a745;
        padding: 2rem;
        margin: 2rem 0;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Generar todos los gráficos (cached)
    if 'main_charts' not in st.session_state:
        with st.spinner('🎯 Generando análisis principal...'):
            st.session_state.main_charts = generate_all_interactive_charts()
    
    if 'demographic_charts' not in st.session_state:
        with st.spinner('👥 Generando análisis demográfico...'):
            st.session_state.demographic_charts = create_comprehensive_demographic_dashboard()
    
    main_charts = st.session_state.main_charts
    demographic_charts = st.session_state.demographic_charts
    insights = main_charts['insights']
    
    # ============================================================================
    # TÍTULO Y INTRODUCCIÓN
    # ============================================================================
    
    st.markdown('<h1 class="main-header">🎓 El Contexto de los Estudiantes que Trabajan en Europa</h1>', 
                unsafe_allow_html=True)
    
    st.markdown('<div class="story-quote">"Más de la mitad de los estudiantes europeos necesitan trabajar para costear sus estudios. Esta es su historia."</div>', 
                unsafe_allow_html=True)
    
    st.markdown('''
    <div class="context-text">
    En el panorama educativo europeo actual, una realidad silenciosa pero significativa define la experiencia universitaria: 
    <strong>la necesidad de trabajar para costear los estudios</strong>. Este análisis interactivo explora esta realidad desde 
    múltiples perspectivas, con especial atención a la situación de España dentro del contexto europeo.
    </div>
    ''', unsafe_allow_html=True)
    
    # ============================================================================
    # SECCIÓN 1: PANORAMA GENERAL EUROPEO
    # ============================================================================
    
    st.markdown('<h2 class="section-header">📊 Panorama General Europeo</h2>', 
                unsafe_allow_html=True)
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🇪🇺 Promedio Europeo",
            value=f"{insights['promedio_europeo']:.1f}%",
            help="Porcentaje promedio de estudiantes que necesitan trabajar"
        )
    
    with col2:
        if 'espana_necesidad' in insights:
            delta = insights['espana_necesidad'] - insights['promedio_europeo']
            st.metric(
                label="🇪🇸 España", 
                value=f"{insights['espana_necesidad']:.1f}%",
                delta=f"{delta:+.1f}% vs promedio",
                help="Posición de España respecto al promedio europeo"
            )
    
    with col3:
        st.metric(
            label="🔺 Mayor Necesidad",
            value=f"{insights['mayor_necesidad_pct']:.1f}%",
            help=f"País con mayor necesidad: {insights['pais_mayor_necesidad']}"
        )
    
    with col4:
        st.metric(
            label="📊 Países Analizados",
            value=f"{insights['total_paises']}",
            help="Total de países incluidos en el análisis"
        )
    
    # Gráfico principal del panorama europeo
    st.plotly_chart(main_charts['overview'], use_container_width=True)
    
    # Insights del panorama general
    st.markdown(f'''
    <div class="insight-box">
        <strong>💡 Insights del Panorama Europeo:</strong><br><br>
        🔍 <strong>Variabilidad Extrema:</strong> Desde {insights['pais_menor_necesidad']} con {insights['menor_necesidad_pct']:.1f}% 
        hasta {insights['pais_mayor_necesidad']} con {insights['mayor_necesidad_pct']:.1f}%<br><br>
        🇪🇸 <strong>Posición de España:</strong> Ocupa el puesto #{insights['espana_ranking'] if 'espana_ranking' in insights else 'N/A'} 
        de {insights['total_paises']} países, {"por encima" if insights.get('espana_necesidad', 0) > insights['promedio_europeo'] else "por debajo"} del promedio europeo<br><br>
        📈 <strong>Contexto Socioeconómico:</strong> Esta variabilidad refleja diferencias en sistemas de apoyo estudiantil, 
        costos de vida y políticas educativas entre países
    </div>
    ''', unsafe_allow_html=True)
    
    # ============================================================================
    # SECCIÓN 2: ESPAÑA EN DETALLE
    # ============================================================================
    
    st.markdown('<h2 class="section-header">🇪🇸 España en Detalle</h2>', 
                unsafe_allow_html=True)
    
    st.markdown('''
    <div class="context-text">
    ¿Cómo se distribuye la necesidad de trabajar entre los estudiantes españoles? 
    El análisis detallado revela una imagen compleja que va más allá de los promedios simples.
    </div>
    ''', unsafe_allow_html=True)
    
    # Gráfico detallado España vs Europa
    st.plotly_chart(main_charts['spain_vs_europe'], use_container_width=True)
    
    # Métricas específicas de España
    if 'espana_aplica_totalmente' in insights:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f'''
            <div class="insight-box">
                <strong>🔴 Necesidad Extrema:</strong><br>
                <div class="metric-highlight">{insights['espana_aplica_totalmente']:.1f}%</div>
                <p>de estudiantes españoles <strong>necesitan trabajar "totalmente"</strong> para costear sus estudios</p>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'''
            <div class="insight-box">
                <strong>🟢 Sin Necesidad:</strong><br>
                <div class="metric-highlight">{insights['espana_no_aplica']:.1f}%</div>
                <p>de estudiantes españoles <strong>no necesitan trabajar</strong> para costear sus estudios</p>
            </div>
            ''', unsafe_allow_html=True)
    
    # ============================================================================
    # SECCIÓN 3: ANÁLISIS DEMOGRÁFICO COMPLETO
    # ============================================================================
    
    st.markdown('<h2 class="section-header">👥 Contexto Demográfico: La Historia Detrás de los Números</h2>', 
                unsafe_allow_html=True)
    
    st.markdown('''
    <div class="context-text">
    Los promedios pueden ocultar realidades muy diferentes. La necesidad de trabajar para costear estudios 
    no afecta por igual a todos los grupos. Exploremos cómo varía según diferentes características demográficas 
    y socioeconómicas.
    </div>
    ''', unsafe_allow_html=True)
    
    # Subsección: Diferencias de Género
    st.markdown('<h3 class="subsection-header">👨‍👩‍👧‍👦 Diferencias de Género</h3>', 
                unsafe_allow_html=True)
    
    if 'gender' in demographic_charts:
        st.plotly_chart(demographic_charts['gender'], use_container_width=True)
        
        st.markdown('''
        <div class="demographic-insight">
            <strong>💼 Análisis de Género:</strong> Las diferencias entre hombres y mujeres en la necesidad de trabajar 
            pueden revelar patrones de desigualdad estructural, acceso diferenciado a recursos familiares, o 
            variaciones en las expectativas sociales sobre la independencia económica.
        </div>
        ''', unsafe_allow_html=True)
    
    # Subsección: Variación por Edad
    st.markdown('<h3 class="subsection-header">📅 Impacto de la Edad</h3>', 
                unsafe_allow_html=True)
    
    if 'age' in demographic_charts:
        st.plotly_chart(demographic_charts['age'], use_container_width=True)
        
        st.markdown('''
        <div class="demographic-insight">
            <strong>⏰ Factor Edad:</strong> Los estudiantes mayores tienden a tener mayor independencia económica 
            pero también más responsabilidades financieras. Este gráfico revela cómo la edad influye en la 
            necesidad de compaginar trabajo y estudios.
        </div>
        ''', unsafe_allow_html=True)
    
    # Subsección: Campo de Estudio
    st.markdown('<h3 class="subsection-header">📚 Por Campo de Estudio</h3>', 
                unsafe_allow_html=True)
    
    if 'field_of_study' in demographic_charts:
        st.plotly_chart(demographic_charts['field_of_study'], use_container_width=True)
        
        st.markdown('''
        <div class="demographic-insight">
            <strong>🎓 Realidad Académica:</strong> Diferentes disciplinas tienen distintas demandas de tiempo, 
            costos asociados y perspectivas de ingresos futuros. Algunas carreras pueden requerir más dedicación 
            exclusiva, mientras otras permiten mayor flexibilidad laboral.
        </div>
        ''', unsafe_allow_html=True)
    
    # Subsección: Contexto Socioeconómico
    st.markdown('<h3 class="subsection-header">💰 Contexto Socioeconómico</h3>', 
                unsafe_allow_html=True)
    
    # Crear tabs para los diferentes aspectos socioeconómicos
    tab1, tab2, tab3 = st.tabs([
        "💸 Dificultades Financieras", 
        "🏠 Situación de Vivienda", 
        "👨‍👩‍👧‍👦 Estado Financiero Familiar"
    ])
    
    with tab1:
        if 'financial_difficulties' in demographic_charts:
            st.plotly_chart(demographic_charts['financial_difficulties'], use_container_width=True)
            st.markdown('''
            <div class="demographic-insight">
                <strong>📉 Dificultades Financieras:</strong> La correlación entre las dificultades económicas 
                familiares y la necesidad de trabajar confirma que el contexto socioeconómico es un factor 
                determinante en la experiencia estudiantil.
            </div>
            ''', unsafe_allow_html=True)
    
    with tab2:
        if 'living_with_parents' in demographic_charts:
            st.plotly_chart(demographic_charts['living_with_parents'], use_container_width=True)
            st.markdown('''
            <div class="demographic-insight">
                <strong>🏡 Independencia Residencial:</strong> Vivir independientemente implica gastos adicionales 
                (alquiler, alimentación, servicios) que pueden incrementar significativamente la necesidad de 
                generar ingresos propios durante los estudios.
            </div>
            ''', unsafe_allow_html=True)
    
    with tab3:
        if 'parents_financial_status' in demographic_charts:
            st.plotly_chart(demographic_charts['parents_financial_status'], use_container_width=True)
            st.markdown('''
            <div class="demographic-insight">
                <strong>👪 Contexto Familiar:</strong> El nivel socioeconómico de los padres es uno de los 
                predictores más fuertes de la necesidad estudiantil de trabajar. Este análisis revela 
                la transmisión intergeneracional de las desigualdades económicas.
            </div>
            ''', unsafe_allow_html=True)
    
    # ============================================================================
    # SECCIÓN 4: SÍNTESIS Y CONCLUSIONES
    # ============================================================================
    
    st.markdown('<h2 class="section-header">🎯 Síntesis: Una Realidad Multidimensional</h2>', 
                unsafe_allow_html=True)
    
    # Conclusiones principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''
        <div class="conclusion-box">
            <h4>🔍 Hallazgos Principales</h4>
            <ul>
                <li><strong>Variabilidad Europea:</strong> Diferencias extremas entre países (0% - 83%)</li>
                <li><strong>España en Contexto:</strong> Ligeramente por encima del promedio europeo</li>
                <li><strong>Factores Múltiples:</strong> Género, edad, campo de estudio y contexto socioeconómico influyen</li>
                <li><strong>Desigualdad Estructural:</strong> El nivel familiar predice fuertemente la necesidad estudiantil</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="conclusion-box">
            <h4>💡 Implicaciones para Políticas</h4>
            <ul>
                <li><strong>Apoyo Diferenciado:</strong> Necesidad de políticas específicas por demografía</li>
                <li><strong>Equidad Educativa:</strong> Reducir barreras económicas al acceso universitario</li>
                <li><strong>Flexibilidad Académica:</strong> Programas que permitan compatibilizar trabajo y estudio</li>
                <li><strong>Monitoreo Continuo:</strong> Seguimiento de tendencias por grupos vulnerables</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)
    
    # Reflexión final
    st.markdown('''
    <div class="story-quote">
    "Detrás de cada estadística hay estudiantes reales, con sueños y desafíos únicos. 
    Comprender su contexto demográfico y socioeconómico es el primer paso para crear 
    un sistema educativo más equitativo y accesible para todos."
    </div>
    ''', unsafe_allow_html=True)
    
    # ============================================================================
    # FOOTER
    # ============================================================================
    
    st.markdown("---")
    st.markdown('''
    <div style="text-align: center; color: #7f8c8d; margin-top: 2rem;">
        <p><strong>📊 Análisis Interactivo Completo:</strong> Estudiantes que Trabajan en Europa</p>
        <p><em>Datos del Eurostudent Survey • Visualización con Plotly y Streamlit</em></p>
        <p>🎯 <strong>Enfoque Demográfico:</strong> 6 dimensiones de análisis • España vs Europa • Interactividad completa</p>
    </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 