"""
Módulo analysis: Análisis específicos y especializados
- Storytelling y narrativa
- Análisis Sankey
- Análisis isotype
"""

# Storytelling
from .storytelling_module import WorkStudyStorytellingCharts

# Análisis Sankey
from .sankey_analysis import get_sankey_for_streamlit

# Análisis isotype
from .isotype_analysis import create_age_isotype_for_streamlit 