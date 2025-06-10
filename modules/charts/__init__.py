"""
Módulo charts: Gráficos organizados por categoría
- Gráficos demográficos
- Gráficos de relación trabajo-estudio  
- Gráficos de impacto
- Gráficos de percepción
- Gráficos geográficos
"""

# Gráficos demográficos
from .demographic_charts import (
    create_gender_comparison_chart,
    create_age_comparison_chart,
    create_field_of_study_comparison_chart,
    create_living_with_parents_comparison_chart
)

# Gráficos de trabajo-estudio
from .work_study_charts import (
    create_storytelling_work_study_charts,
    generate_storytelling_summary
)

# Gráficos de impacto
from .impact_charts import get_work_impact_figures_for_streamlit

# Gráficos de percepción
from .perception_charts import (
    generate_academic_perception_analysis,
    generate_happiness_work_relation_analysis
)

# Gráficos geográficos
from .geographic_charts import (
    generate_europe_cost_heatmap,
    get_cost_statistics
) 