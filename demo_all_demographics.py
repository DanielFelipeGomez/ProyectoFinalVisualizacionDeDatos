#!/usr/bin/env python3
"""
Demo completo de TODOS los análisis demográficos disponibles
Muestra cada gráfico individualmente para explorar el contexto de estudiantes que trabajan
"""

from advanced_demographic_charts import create_comprehensive_demographic_dashboard
import time

def main():
    print("🎯 DEMO COMPLETO: Análisis Demográfico de Estudiantes que Trabajan")
    print("="*70)
    print("Este demo muestra TODOS los contextos demográficos disponibles")
    print("Cada gráfico compara España vs Promedio Europeo")
    print()
    
    # Generar dashboard completo
    print("📊 Generando dashboard demográfico completo...")
    charts = create_comprehensive_demographic_dashboard()
    
    print(f"\n✅ Dashboard generado con {len(charts)} análisis diferentes!")
    
    # Mostrar cada gráfico con descripción
    analyses = [
        {
            'key': 'gender',
            'title': '👨‍👩‍👧‍👦 ANÁLISIS POR GÉNERO',
            'description': 'Compara la necesidad de trabajar entre hombres y mujeres',
            'insight': 'Revela si existen diferencias de género en la necesidad laboral estudiantil'
        },
        {
            'key': 'age', 
            'title': '📅 ANÁLISIS POR EDAD',
            'description': 'Examina cómo varía la necesidad de trabajar según grupos etarios',
            'insight': 'Muestra si estudiantes mayores tienen más necesidad de trabajar'
        },
        {
            'key': 'field_of_study',
            'title': '📚 ANÁLISIS POR CAMPO DE ESTUDIO', 
            'description': 'Analiza qué carreras/disciplinas requieren más trabajo estudiantil',
            'insight': 'Identifica campos académicos con mayor presión económica'
        },
        {
            'key': 'financial_difficulties',
            'title': '💰 ANÁLISIS POR DIFICULTADES FINANCIERAS',
            'description': 'Relaciona el nivel de dificultades económicas con la necesidad de trabajar',
            'insight': 'Confirma la correlación entre problemas financieros y trabajo estudiantil'
        },
        {
            'key': 'living_with_parents',
            'title': '🏠 ANÁLISIS POR SITUACIÓN DE VIVIENDA',
            'description': 'Compara estudiantes independientes vs que viven con padres',
            'insight': 'Explora cómo la independencia residencial afecta la necesidad laboral'
        },
        {
            'key': 'parents_financial_status',
            'title': '👨‍👩‍👧‍👦💳 ANÁLISIS POR ESTADO FINANCIERO DE PADRES',
            'description': 'Examina cómo el nivel económico familiar influye en la necesidad de trabajar',
            'insight': 'Revela el impacto del contexto socioeconómico familiar'
        }
    ]
    
    print("\n" + "="*70)
    print("🎨 MOSTRANDO GRÁFICOS INTERACTIVOS")
    print("="*70)
    print("Los gráficos se abrirán en tu navegador uno por uno...")
    print("Cierra cada ventana para continuar al siguiente")
    print()
    
    for i, analysis in enumerate(analyses, 1):
        if analysis['key'] in charts:
            print(f"\n[{i}/6] {analysis['title']}")
            print(f"📊 {analysis['description']}")
            print(f"💡 {analysis['insight']}")
            print(f"🎯 Mostrando gráfico...")
            
            # Mostrar el gráfico
            charts[analysis['key']].show()
            
            # Pausa entre gráficos
            input("Presiona Enter para continuar al siguiente gráfico...")
        else:
            print(f"\n[{i}/6] {analysis['title']}")
            print(f"⚠️ Gráfico no disponible (posible error en datos)")
    
    print("\n" + "="*70)
    print("🎯 RESUMEN DEL ANÁLISIS DEMOGRÁFICO COMPLETO")
    print("="*70)
    
    print("\n📊 GRÁFICOS GENERADOS:")
    for key, description in {
        'gender': 'Género - Diferencias hombres vs mujeres',
        'age': 'Edad - Variación por grupos etarios', 
        'field_of_study': 'Campo de Estudio - Necesidad por disciplina académica',
        'financial_difficulties': 'Dificultades Financieras - Impacto económico familiar',
        'living_with_parents': 'Situación de Vivienda - Independientes vs con padres',
        'parents_financial_status': 'Estado Financiero Padres - Nivel socioeconómico familiar'
    }.items():
        status = "✅" if key in charts else "❌"
        print(f"   {status} {description}")
    
    print("\n🔍 PARA TU SCROLLYTELLING, ESTOS GRÁFICOS PERMITEN:")
    print("   • Humanizar los datos con contexto personal")
    print("   • Mostrar que la necesidad de trabajar no afecta igual a todos")
    print("   • Identificar grupos más vulnerables económicamente")
    print("   • Comparar España con Europa en múltiples dimensiones")
    print("   • Crear narrativas específicas por demografía")
    
    print("\n💡 CÓMO USAR EN STREAMLIT:")
    print("""
    from advanced_demographic_charts import create_comprehensive_demographic_dashboard
    
    # En tu scrollytelling:
    demo_charts = create_comprehensive_demographic_dashboard()
    
    # Crear tabs por demografía
    tab1, tab2, tab3 = st.tabs(["Por Género", "Por Campo", "Por Situación Económica"])
    
    with tab1:
        st.plotly_chart(demo_charts['gender'], use_container_width=True)
    with tab2:
        st.plotly_chart(demo_charts['field_of_study'], use_container_width=True)
    with tab3:
        st.plotly_chart(demo_charts['financial_difficulties'], use_container_width=True)
    """)
    
    print("\n✅ Demo completado! Tienes un arsenal completo de gráficos demográficos.")
    print("🎯 Cada uno cuenta una parte diferente de la historia de los estudiantes que trabajan.")

if __name__ == "__main__":
    main() 