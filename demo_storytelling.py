#!/usr/bin/env python3
"""
Demo del Storytelling Completo con Gráficos Integrados
=====================================================

Este script demuestra el storytelling final con todos los gráficos demográficos integrados.

Uso:
    streamlit run demo_storytelling.py

Autor: Asistente IA
Fecha: 2024
"""

import streamlit as st
import sys
import os

def main():
    """Función principal que ejecuta la demostración del storytelling completo."""
    
    st.set_page_config(
        page_title="🎓 Demo - Trabajar y estudiar en Europa",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Título de la demo
    st.markdown("""
    <div style="background-color: #e8f4fd; padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="text-align: center; color: #1f77b4;">🎓 Demostración del Storytelling Completo</h1>
        <h3 style="text-align: center; color: #34495e;">Trabajar y estudiar en Europa con Gráficos Interactivos</h3>
        <p style="text-align: center; font-size: 1.1rem;">
            Esta demostración muestra el storytelling final con todos los gráficos demográficos integrados
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Información sobre las funcionalidades integradas
    st.markdown("""
    ## 🎯 Funcionalidades Integradas
    
    ### ✅ Gráficos Demográficos Incluidos:
    - **🌍 Distribución por País** - Contexto europeo completo
    - **👤 Análisis por Género** - Comparaciones entre géneros
    - **📅 Grupos de Edad** - Tendencias por edad
    - **🏠 Situación de Convivencia** - Independencia vs. vivir con padres
    - **🎓 Campo de Estudio** - Análisis por disciplinas académicas
    - **💰 Dificultades Financieras** - Impacto de la situación económica
    - **👨‍👩‍👧‍👦 Estado Financiero Familiar** - Origen socioeconómico
    - **🇪🇸 España vs. Europa** - Comparación detallada
    
    ### 🔧 Características Técnicas:
    - **Gráficos Interactivos con Plotly** - Hover tooltips y zoom
    - **Manejo de Errores Robusto** - Fallback a placeholders si hay problemas
    - **CSS Personalizado** - Diseño profesional para scrollytelling
    - **Análisis Automático** - Insights generados automáticamente
    - **Responsive Design** - Adaptado para diferentes tamaños de pantalla
    """)
    
    # Ejecutar el storytelling principal
    st.markdown("---")
    st.markdown("## 📖 Storytelling Principal")
    
    # Botón para ejecutar
    if st.button("🚀 Ejecutar Storytelling Completo", type="primary"):
        try:
            st.markdown("### ✅ Ejecutando storytelling con gráficos integrados...")
            
            # Información sobre qué se está ejecutando
            with st.spinner("Cargando análisis demográfico completo..."):
                # Importar el storytelling principal
                exec(open('storytelling.py').read())
                
        except FileNotFoundError:
            st.error("""
            ❌ **Error:** No se encontró el archivo `storytelling.py`
            
            Asegúrate de que el archivo `storytelling.py` esté en el directorio actual.
            """)
            
        except Exception as e:
            st.error(f"""
            ❌ **Error ejecutando storytelling:** {e}
            
            Verifica que todos los archivos de dependencias estén disponibles:
            - `advanced_demographic_charts.py`
            - `interactive_storytelling_charts.py`
            - Datasets en `preprocessed_excels/`
            """)
    
    # Instrucciones alternativas
    st.markdown("""
    ## 🔧 Ejecución Alternativa
    
    Si prefieres ejecutar directamente el storytelling, usa:
    
    ```bash
    streamlit run storytelling.py
    ```
    
    ## 📁 Estructura de Archivos Necesaria
    
    ```
    proyecto/
    ├── storytelling.py                    # Storytelling principal ✅
    ├── advanced_demographic_charts.py     # Análisis demográfico ✅
    ├── interactive_storytelling_charts.py # Gráficos interactivos ✅
    ├── demo_storytelling.py              # Este archivo ✅
    └── preprocessed_excels/               # Datasets ✅
        ├── E8_work_motive_afford_study_5__all_students__all_contries.xlsx
        ├── E8_work_motive_afford_study_5__e_sex__all_contries.xlsx
        ├── E8_work_motive_afford_study_5__e_age__all_contries.xlsx
        ├── E8_work_motive_afford_study_5__e_field_of_study__all_contries.xlsx
        ├── E8_work_motive_afford_study_5__e_financial_difficulties__all_contries.xlsx
        ├── E8_work_motive_afford_study_5__e_notlivingwithparents__all_contries.xlsx
        └── E8_work_motive_afford_study_5__s_parents_financial_status__all_contries.xlsx
    ```
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 2rem;">
        <p><strong>🎓 Storytelling Interactivo sobre Educación y Trabajo en Europa</strong></p>
        <p>Análisis completo con España como foco principal de comparación</p>
        <p><em>Todos los gráficos demográficos integrados exitosamente</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 