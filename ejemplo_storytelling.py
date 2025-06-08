"""
Ejemplo de uso de los gráficos interactivos en storytelling
"""

from storytelling_module import WorkStudyStorytellingCharts

def main_storytelling():
    """
    Ejemplo de storytelling con gráficos interactivos
    """
    # Crear la instancia de gráficos
    charts = WorkStudyStorytellingCharts()
    
    # Obtener insights clave
    insights = charts.get_key_insights()
    
    print("🎬 STORYTELLING: LA REALIDAD LABORAL DE LOS ESTUDIANTES EUROPEOS")
    print("="*70)
    
    # Introducción del tema
    print(f"""
📖 CONTEXTO:
En una Europa donde la educación superior es cada vez más costosa, 
muchos estudiantes se ven obligados a trabajar para financiar sus estudios.

🔍 ¿QUÉ REVELAN LOS DATOS?
Según el estudio European Survey on Students, el {insights['spain_need_work']:.1f}% 
de los estudiantes españoles necesitan trabajar para costear sus estudios, 
comparado con el {insights['europe_need_work']:.1f}% del promedio europeo.
""")
    
    # Primer gráfico - Panorama general
    print("📊 GRÁFICO 1: Panorama Europeo")
    print("-" * 40)
    chart1 = charts.get_chart_need_vs_no_need(height=500, width=1000)
    
    # El gráfico se abre automáticamente en el navegador
    chart1.show()
    
    print(f"""
💡 INSIGHTS DEL GRÁFICO 1:
• España está prácticamente en la media europea ({insights['difference']:+.1f} puntos de diferencia)
• {insights['max_country']} lidera con el mayor porcentaje de estudiantes que necesitan trabajar ({insights['max_percentage']:.1f}%)
• La situación más favorable se encuentra en {insights['min_country']} ({insights['min_percentage']:.1f}%)
""")
    
    # Segundo gráfico - Enfoque en España
    print("📊 GRÁFICO 2: España en Detalle")
    print("-" * 40)
    chart2 = charts.get_chart_spain_vs_europe(height=500, width=900)
    chart2.show()
    
    print(f"""
💡 INSIGHTS DEL GRÁFICO 2:
• El {insights['spain_totally_applies']:.1f}% de estudiantes españoles considera que trabajar 
  para costear estudios "aplica totalmente" a su situación
• Esto es {insights['spain_totally_applies'] - insights['europe_totally_applies']:+.1f} puntos 
  superior al promedio europeo ({insights['europe_totally_applies']:.1f}%)
• Solo el {insights['spain_not_apply']:.1f}% de estudiantes españoles dice que trabajar 
  para estudiar "no aplica para nada" a su situación
""")
    
    # Conclusiones narrativas
    print(f"""
🎯 CONCLUSIONES PARA EL STORYTELLING:

1. 📈 TENDENCIA GENERAL:
   Más de la mitad de los estudiantes europeos ({insights['europe_need_work']:.1f}%) 
   necesitan trabajar para financiar sus estudios.

2. 🇪🇸 SITUACIÓN ESPAÑOLA:
   España se encuentra ligeramente por encima de la media europea, 
   lo que indica una presión económica significativa en los estudiantes.

3. 🔴 PUNTO CRÍTICO:
   Que el {insights['spain_totally_applies']:.1f}% de estudiantes españoles diga que trabajar 
   para costear estudios "aplica totalmente" sugiere una dependencia laboral real.

4. 📊 COMPARACIÓN EUROPEA:
   La diferencia entre {insights['max_country']} ({insights['max_percentage']:.1f}%) y 
   {insights['min_country']} ({insights['min_percentage']:.1f}%) muestra la disparidad 
   socioeconómica en Europa.

💬 MENSAJE CLAVE PARA TU STORYTELLING:
"En España, más de 4 de cada 10 estudiantes universitarios trabajan por necesidad, 
no por elección. Esta realidad refleja no solo la situación económica individual, 
sino también las políticas educativas y de apoyo estudiantil del país."
""")
    
    # Guardar los gráficos
    charts.save_charts()
    
    return insights

def get_narrative_elements():
    """
    Función para obtener elementos narrativos listos para usar
    """
    charts = WorkStudyStorytellingCharts()
    insights = charts.get_key_insights()
    
    narrative = {
        'hook': f"Imagina que de cada 10 estudiantes universitarios en España, {int(insights['spain_need_work']/10)} necesitan trabajar para poder estudiar.",
        
        'problema': f"El {insights['spain_need_work']:.1f}% de estudiantes españoles enfrentan la presión de equilibrar trabajo y estudios.",
        
        'contexto': f"España está {abs(insights['difference']):.1f} puntos {'por encima' if insights['difference'] > 0 else 'por debajo'} del promedio europeo.",
        
        'dramatico': f"Para {insights['total_students_spain']:,} estudiantes españoles encuestados, trabajar no es una opción, es una necesidad.",
        
        'esperanza': f"Sin embargo, el {100 - insights['spain_need_work']:.1f}% restante puede dedicarse completamente a sus estudios.",
        
        'call_to_action': "¿Qué políticas educativas podrían cambiar esta realidad?"
    }
    
    return narrative, insights

# Ejemplo de uso
if __name__ == "__main__":
    # Storytelling completo
    insights = main_storytelling()
    
    print("\n" + "="*70)
    print("🎭 ELEMENTOS NARRATIVOS ADICIONALES")
    print("="*70)
    
    # Elementos narrativos
    narrative, _ = get_narrative_elements()
    
    print("📝 FRASES PARA TU STORYTELLING:")
    for key, value in narrative.items():
        print(f"\n{key.upper()}: {value}")
    
    print(f"""
    
🎬 ESTRUCTURA SUGERIDA PARA TU STORYTELLING:

1. HOOK: {narrative['hook']}
2. PROBLEMA: {narrative['problema']}
3. [MOSTRAR GRÁFICO 1]
4. CONTEXTO: {narrative['contexto']}
5. [MOSTRAR GRÁFICO 2]
6. IMPACTO: {narrative['dramatico']}
7. BALANCE: {narrative['esperanza']}
8. CIERRE: {narrative['call_to_action']}
""") 