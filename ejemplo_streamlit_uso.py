"""
EJEMPLO DE USO: Integración de gráficas de impacto del trabajo en Streamlit Scrollytelling

Este archivo muestra cómo usar las funciones de storytelliing_charts.py 
en tu aplicación de Streamlit para el scrollytelling.
"""

import streamlit as st
import plotly.graph_objects as go
from storytelliing_charts import (
    get_all_figures_for_streamlit,
    get_work_impact_figures_for_streamlit,
    create_streamlit_work_motivation_chart,
    read_work_motive_afford_study_dataset
)

def main_scrollytelling_app():
    """
    Aplicación principal de scrollytelling con todas las gráficas de trabajo estudiantil
    """
    
    st.set_page_config(
        page_title="Trabajo Estudiantil en Europa: Enfoque en España",
        page_icon="🎓",
        layout="wide"
    )
    
    # Título principal
    st.title("🎓 El Trabajo Estudiantil en Europa")
    st.subheader("🇪🇸 Un Análisis Centrado en España")
    
    # Sidebar con navegación
    st.sidebar.title("📋 Navegación")
    section = st.sidebar.selectbox(
        "Selecciona una sección:",
        [
            "🏠 Introducción",
            "💰 Motivación para Trabajar", 
            "🔗 Relación Trabajo-Estudio",
            "📊 Impacto en los Estudios",
            "🎯 Conclusiones"
        ]
    )
    
    # Cargar todas las figuras una sola vez
    if 'figures_loaded' not in st.session_state:
        with st.spinner("🔄 Cargando datos y creando visualizaciones..."):
            st.session_state.figures = get_all_figures_for_streamlit()
            st.session_state.figures_loaded = True
        st.success(f"✅ {len(st.session_state.figures)} gráficas cargadas exitosamente")
    
    # Mostrar sección seleccionada
    if section == "🏠 Introducción":
        show_introduction()
    elif section == "💰 Motivación para Trabajar":
        show_work_motivation_section()
    elif section == "🔗 Relación Trabajo-Estudio":
        show_work_study_relationship_section()
    elif section == "📊 Impacto en los Estudios":
        show_work_impact_section()
    elif section == "🎯 Conclusiones":
        show_conclusions()


def show_introduction():
    """
    Sección de introducción
    """
    st.header("🌍 Contexto de la Investigación")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### ¿Por qué España?
        
        España representa un caso de estudio fascinante en el contexto europeo del trabajo estudiantil. 
        Con un **9,072 estudiantes** participando en la encuesta EUROSTUDENT VIII, España ofrece 
        una muestra robusta para analizar:
        
        - 🎯 **Motivaciones** para trabajar mientras estudian
        - 🔄 **Relación** entre el trabajo y los estudios
        - 📈 **Impacto** del trabajo en el rendimiento académico
        - 🌍 **Comparaciones** con el resto de Europa
        """)
        
        st.info("""
        💡 **Metodología**: Utilizamos datos de EUROSTUDENT VIII, la encuesta más completa 
        sobre condiciones sociales y económicas de estudiantes en Europa.
        """)
    
    with col2:
        st.metric(
            label="🇪🇸 Estudiantes Españoles",
            value="9,072",
            delta="Muestra robusta"
        )
        
        st.metric(
            label="🇪🇺 Países Europeos",
            value="25+",
            delta="Comparación amplia"
        )


def show_work_motivation_section():
    """
    Sección de motivación para trabajar
    """
    st.header("💰 ¿Por qué Trabajan los Estudiantes?")
    
    st.markdown("""
    La **necesidad económica** es uno de los principales factores que empujan a los estudiantes 
    a buscar trabajo remunerado durante sus estudios. Analicemos cómo se posiciona España 
    en comparación con el resto de Europa.
    """)
    
    # Mostrar gráfica de motivación
    if 'motivacion_trabajar' in st.session_state.figures:
        st.plotly_chart(
            st.session_state.figures['motivacion_trabajar'],
            use_container_width=True
        )
        
        # Análisis de la gráfica
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📊 Análisis de Datos
            
            El gráfico muestra el porcentaje de estudiantes que **necesitan trabajar** 
            para costear sus estudios (combinando respuestas "aplica totalmente", 
            "aplica bastante" y "aplica parcialmente").
            """)
        
        with col2:
            st.markdown("""
            ### 🇪🇸 Posición de España
            
            España se encuentra **destacada en rojo** para facilitar la comparación 
            con el resto de países europeos en términos de necesidad económica 
            de trabajo estudiantil.
            """)
    
    else:
        st.error("❌ No se pudo cargar la gráfica de motivación")
    
    # Insights adicionales
    st.markdown("""
    ---
    ### 💡 Insights Clave
    
    - Los estudiantes que necesitan trabajar enfrentan **mayores desafíos** para concentrarse en sus estudios
    - Las **diferencias entre países** reflejan distintos sistemas de apoyo financiero estudiantil
    - España muestra patrones específicos que vale la pena analizar en detalle
    """)


def show_work_study_relationship_section():
    """
    Sección de relación trabajo-estudio
    """
    st.header("🔗 Relación entre Trabajo y Estudios")
    
    st.markdown("""
    No todos los trabajos estudiantiles son iguales. La **relación** entre el trabajo 
    y el campo de estudio puede influir significativamente en la experiencia académica.
    """)
    
    # Mostrar gráfica de relación
    if 'relacion_trabajo_estudio' in st.session_state.figures:
        st.plotly_chart(
            st.session_state.figures['relacion_trabajo_estudio'],
            use_container_width=True
        )
        
        # Análisis
        st.markdown("""
        ### 🎯 ¿Qué Significa "Trabajo Relacionado"?
        
        Un trabajo **relacionado con los estudios** puede:
        - 📚 **Complementar** el aprendizaje académico
        - 🛠️ Proporcionar **experiencia práctica** en el campo de estudio
        - 🌟 **Mejorar** las perspectivas de carrera futuras
        - ⚡ Reducir el **impacto negativo** en el rendimiento académico
        """)
    
    else:
        st.error("❌ No se pudo cargar la gráfica de relación trabajo-estudio")


def show_work_impact_section():
    """
    Sección principal de impacto del trabajo en los estudios
    """
    st.header("📊 Impacto del Trabajo en los Estudios")
    
    st.markdown("""
    El trabajo durante los estudios puede tener **efectos diversos** en la experiencia académica. 
    Analicemos específicamente cómo afecta la **consideración de abandono** de estudios.
    """)
    
    # Mostrar gráficas de impacto
    impact_tab1, impact_tab2, impact_tab3 = st.tabs([
        "💸 Dificultades Financieras", 
        "👔 Necesidad de Trabajar", 
        "🇪🇸 España vs Europa"
    ])
    
    with impact_tab1:
        st.subheader("💸 Abandono por Dificultades Financieras")
        
        if 'abandono_financiero' in st.session_state.figures:
            st.plotly_chart(
                st.session_state.figures['abandono_financiero'],
                use_container_width=True
            )
            
            st.markdown("""
            ### 📈 Interpretación
            
            Este gráfico muestra la **frecuencia** con la que los estudiantes consideran 
            abandonar sus estudios debido a **dificultades financieras**:
            
            - 🔴 **Alta frecuencia**: Considera abandono "muy frecuentemente" o "frecuentemente"
            - 🟢 **Nunca considera**: Nunca ha considerado abandonar por motivos financieros
            """)
        else:
            st.error("❌ No se pudo cargar la gráfica de abandono financiero")
    
    with impact_tab2:
        st.subheader("👔 Abandono por Necesidad de Trabajar")
        
        if 'abandono_trabajo' in st.session_state.figures:
            st.plotly_chart(
                st.session_state.figures['abandono_trabajo'],
                use_container_width=True
            )
            
            st.markdown("""
            ### 🎯 Enfoque
            
            Estudiantes que consideran **abandonar** los estudios para poder 
            **dedicar más tiempo al trabajo remunerado**:
            
            - Refleja la **presión económica** que enfrentan
            - Muestra el **conflicto** entre supervivencia financiera y educación
            - Varía significativamente **entre países**
            """)
        else:
            st.error("❌ No se pudo cargar la gráfica de abandono por trabajo")
    
    with impact_tab3:
        st.subheader("🇪🇸 España vs 🇪🇺 Europa")
        
        if 'espana_vs_europa_impacto' in st.session_state.figures:
            st.plotly_chart(
                st.session_state.figures['espana_vs_europa_impacto'],
                use_container_width=True
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                ### 🇪🇸 España
                - Datos específicos de estudiantes españoles
                - Refleja el contexto socioeconómico nacional
                - Base: 9,072 estudiantes encuestados
                """)
            
            with col2:
                st.markdown("""
                ### 🇪🇺 Promedio Europeo
                - Promedio de todos los países (excluyendo España)
                - Contexto comparativo continental
                - Múltiples sistemas educativos y económicos
                """)
        else:
            st.error("❌ No se pudo cargar la comparación España vs Europa")
    
    # Resumen de impacto
    st.markdown("""
    ---
    ### ⚠️ Implicaciones del Impacto
    
    El análisis del **impacto del trabajo** en los estudios revela:
    
    1. **🎯 Variabilidad entre países**: Diferentes contextos socioeconómicos generan diferentes presiones
    2. **💰 Presión financiera**: La necesidad económica puede comprometer la continuidad académica  
    3. **🇪🇸 Contexto español**: España muestra patrones específicos que requieren atención
    4. **📊 Necesidad de políticas**: Los datos sugieren áreas donde se requiere apoyo institucional
    """)


def show_conclusions():
    """
    Sección de conclusiones
    """
    st.header("🎯 Conclusiones y Reflexiones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔍 Hallazgos Principales
        
        1. **💰 Necesidad Económica**
           - Significativo porcentaje de estudiantes necesita trabajar
           - Variaciones importantes entre países europeos
           
        2. **🔗 Relación Trabajo-Estudio**
           - No todos los trabajos tienen la misma relación con los estudios
           - Trabajos relacionados pueden ser más beneficiosos
           
        3. **📊 Impacto en Persistencia**
           - El trabajo puede influir en consideración de abandono
           - Dificultades financieras son un factor crítico
        """)
    
    with col2:
        st.markdown("""
        ### 🇪🇸 España en Contexto
        
        1. **📈 Posición Europea**
           - España muestra patrones específicos
           - Comparaciones revelan áreas de fortaleza y mejora
           
        2. **🎓 Implicaciones Políticas**
           - Necesidad de sistemas de apoyo financiero
           - Programas de trabajo-estudio integrados
           
        3. **🔮 Futuras Investigaciones**
           - Análisis longitudinal de impacto
           - Políticas de apoyo efectivas
        """)
    
    st.info("""
    💡 **Recomendación**: Los datos sugieren la necesidad de políticas educativas que 
    reconozcan la realidad del trabajo estudiantil y proporcionen apoyo adecuado para 
    minimizar el impacto negativo en la experiencia académica.
    """)


# Función auxiliar para cargar figuras específicas si es necesario
def load_specific_impact_figures():
    """
    Función para cargar solo las figuras de impacto si se necesita por separado
    """
    return get_work_impact_figures_for_streamlit()


if __name__ == "__main__":
    main_scrollytelling_app() 