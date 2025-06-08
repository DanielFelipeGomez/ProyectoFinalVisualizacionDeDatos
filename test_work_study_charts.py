#!/usr/bin/env python3
"""
Script de prueba para las visualizaciones interactivas de relación trabajo-estudio
"""

from storytelliing_charts import (
    create_all_work_study_relationship_visualizations,
    read_work_study_relationship_dataset,
    PreprocessedDatasetsNamesRelationshipBetweenWorkAndStudy
)

def main():
    """
    Función principal para ejecutar las pruebas de visualización
    """
    print("🚀 DEMO: Gráficos Interactivos de Relación Trabajo-Estudio")
    print("="*60)
    
    try:
        # Ejecutar todas las visualizaciones
        results = create_all_work_study_relationship_visualizations()
        df_work_study, fig1, fig2, fig3, fig4, fig5 = results
        
        print("\n✅ ¡Todas las visualizaciones se han creado exitosamente!")
        print(f"📊 Datos procesados: {df_work_study.shape[0]} países")
        
        # Información adicional sobre las visualizaciones
        print("\n📈 Gráficos generados:")
        print("   1. Gráfico de barras apiladas - Niveles de relación trabajo-estudio")
        print("   2. Gráfico simplificado - Trabajo relacionado vs no relacionado") 
        print("   3. Ranking de países por relación trabajo-estudio")
        print("   4. Comparación España vs Promedio Europeo")
        print("   5. Análisis demográfico (resumen)")
        
        # Verificar si España está en los datos
        if 'ES' in df_work_study['Country'].values:
            spain_data = df_work_study[df_work_study['Country'] == 'ES'].iloc[0]
            spain_related = (spain_data['Very_Closely_Value'] + 
                           spain_data['Rather_Closely_Value'] + 
                           spain_data['To_Some_Extent_Value'])
            print(f"\n🇪🇸 Dato destacado de España:")
            print(f"   • {spain_related:.1f}% de estudiantes tienen trabajo relacionado con sus estudios")
        
        print("\n💡 Los gráficos interactivos se abrirán en tu navegador web")
        print("   Puedes interactuar con ellos usando hover, zoom, y filtros")
        
    except Exception as e:
        print(f"❌ Error al crear las visualizaciones: {e}")
        print("💡 Verificar que los archivos de datos están disponibles")
        
        # Intentar cargar solo los datos para diagnóstico
        try:
            print("\n🔍 Intentando cargar datos para diagnóstico...")
            df_test = read_work_study_relationship_dataset()
            print(f"✅ Datos cargados correctamente: {df_test.shape}")
            print("Países disponibles:", df_test['Country'].tolist())
        except Exception as e2:
            print(f"❌ Error al cargar datos: {e2}")

if __name__ == "__main__":
    main() 