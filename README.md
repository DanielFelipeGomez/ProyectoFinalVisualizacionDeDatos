# 🎓 Trabajar y estudiar en Europa: Análisis Interactivo

Una aplicación interactiva de Streamlit que analiza la realidad de los estudiantes europeos que necesitan trabajar para costear sus estudios, con especial foco en España.

## 📊 Características

- **Análisis comparativo** entre España y otros 24 países europeos
- **Visualizaciones interactivas** con Plotly
- **Múltiples perspectivas**: demográficas, socioeconómicas y de bienestar
- **Storytelling visual** con datos del estudio EUROSTUDENT

## 🔧 Características Técnicas

### Arquitectura Modular Mejorada
- **📦 Módulo Core**: Funcionalidades centrales (carga de datos, configuración)
- **📊 Módulo Charts**: Gráficos organizados por categoría temática
- **🔍 Módulo Analysis**: Análisis especializados y narrativa
- **🎨 Configuración unificada**: Colores y estilos consistentes
- **⚡ Carga optimizada**: Data loaders centralizados y eficientes

### Tecnologías Utilizadas
- **Streamlit**: Framework principal para la aplicación web
- **Plotly**: Visualizaciones interactivas y mapas
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **OpenPyXL**: Lectura de archivos Excel

### Organización del Código
- **Separación de responsabilidades**: Cada módulo tiene una función específica
- **Reutilización**: Componentes compartidos en el módulo core
- **Mantenibilidad**: Estructura clara y documentada
- **Escalabilidad**: Fácil adición de nuevos análisis y gráficos

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone [tu-repo]
   cd ProyectoFinal
   ```

2. **Crear entorno virtual (recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   streamlit run storytelling.py
   ```

5. **Abrir en el navegador**:
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre automáticamente, copia la URL que aparece en la terminal

## 📁 Estructura del Proyecto

```
ProyectoFinal/
├── storytelling.py              # Aplicación principal de Streamlit
├── requirements.txt             # Dependencias del proyecto
├── README.md                   # Documentación del proyecto
├── .gitignore                  # Archivos a ignorar en Git
│
├── modules/                    # Módulos organizados por funcionalidad
│   ├── __init__.py
│   │
│   ├── core/                   # Funcionalidades centrales
│   │   ├── __init__.py
│   │   ├── color_config.py     # Configuración de colores y estilos
│   │   └── data_loaders.py     # Funciones de carga de datos
│   │
│   ├── charts/                 # Gráficos organizados por categoría
│   │   ├── __init__.py
│   │   ├── demographic_charts.py      # Gráficos demográficos
│   │   ├── work_study_charts.py       # Gráficos trabajo-estudio
│   │   ├── impact_charts.py           # Gráficos de impacto
│   │   ├── perception_charts.py       # Gráficos de percepción
│   │   └── geographic_charts.py       # Mapas y gráficos geográficos
│   │
│   └── analysis/               # Análisis específicos y especializados
│       ├── __init__.py
│       ├── storytelling_module.py     # Narrativa principal
│       ├── sankey_analysis.py         # Análisis de flujo Sankey
│       └── isotype_analysis.py        # Análisis isotype por edad
│
├── data/                       # Datos organizados por tipo
│   ├── preprocessed_excels/           # Datos preprocessados principales
│   ├── preprocessed_impact_by_job/    # Datos de impacto del trabajo
│   ├── preprocessed_relationship_study_job/  # Datos relación trabajo-estudio
│   ├── raw_excels_data/              # Datos originales sin procesar
│   └── sankey_excels/                # Datos específicos para Sankey
│
└── assets/                     # Recursos multimedia
    ├── images/                        # Imágenes del proyecto
    └── logos/                         # Logos institucionales
```

## 🎯 Funcionalidades Principales

### 1. **Panorama Europeo**
- Comparación de necesidad de trabajar por país
- España vs promedio europeo
- Identificación de patrones regionales

### 2. **Análisis Demográfico**
- Por género, edad, campo de estudio
- Situación de convivencia y nivel socioeconómico
- Mapas de calor interactivos

### 3. **Tipos de Trabajo**
- Trabajo relacionado vs no relacionado con estudios
- Análisis de la desconexión laboral-académica

### 4. **Impacto en Bienestar**
- Efectos en felicidad y rendimiento académico
- Consideración de abandono de estudios
- Correlaciones trabajo-bienestar

### 5. **Visualizaciones Especiales**
- Diagrama Sankey de trayectorias estudiantiles
- Gráficos isotype por edad
- Mapas de costos europeos

## 📈 Datos

Los datos provienen del estudio **EUROSTUDENT Ronda 8**, que analiza las condiciones de vida y estudio de estudiantes de educación superior en Europa.

- **25 países europeos** analizados
- **9,072 estudiantes españoles** en la muestra
- **8 dimensiones** de análisis principal

## 📝 Autor

**Daniel Felipe Gómez Aristizábal**  
Máster Universitario en Ciencia de Datos - UOC  
Asignatura: Visualización de Datos

## 📄 Licencia

Este proyecto tiene fines académicos y utiliza datos públicos del estudio EUROSTUDENT.

---

## 🚀 Cómo Contribuir

Si encuentras errores o tienes sugerencias:

1. Abre un *issue* describiendo el problema
2. Propón mejoras en las visualizaciones
3. Comparte insights adicionales sobre los datos

**¡La educación europea nos concierne a todos!** 🇪🇺 