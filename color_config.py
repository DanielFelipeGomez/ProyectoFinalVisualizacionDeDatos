"""
Configuración unificada de colores para todas las gráficas del storytelling
Basado en la paleta definida en storytelling.py
"""

from enum import Enum

class Colors(Enum):
    EUROPE = "#1E88E5"
    NEGATIVE = "#E53935"
    SPAIN = "#FDD835"
    POSITIVE = "#43A047"
    WARNING = "#EF6C00"
    DANGER = "#B71C1C"

# Configuración de colores para gráficas
STORYTELLING_COLORS = {
    # Colores principales del storytelling
    'spain': Colors.SPAIN.value,           # Amarillo para España (destacado)
    'europe': Colors.EUROPE.value,         # Azul para promedio europeo
    'need_work': Colors.NEGATIVE.value,    # Rojo para necesidad de trabajar (negativo)
    'dont_need_work': Colors.POSITIVE.value, # Verde para no necesidad (positivo)
    'warning': Colors.WARNING.value,       # Naranja para advertencias
    'danger': Colors.DANGER.value,         # Rojo oscuro para peligro
    
    # Gradientes para escalas de respuesta (5 niveles)
    'applies_totally': Colors.DANGER.value,     # Rojo oscuro - problemático
    'applies_rather': Colors.NEGATIVE.value,    # Rojo - negativo
    'applies_partially': Colors.WARNING.value,  # Naranja - precaución
    'applies_rather_not': Colors.POSITIVE.value, # Verde - positivo
    'does_not_apply': Colors.EUROPE.value,      # Azul - muy positivo
    
    # Colores por demografía
    'female': '#E377C2',     # Rosa para mujeres
    'male': '#17BECF',       # Cian para hombres
    'young': Colors.POSITIVE.value,    # Verde para jóvenes
    'older': Colors.WARNING.value,     # Naranja para mayores
    'high_difficulty': Colors.NEGATIVE.value,   # Rojo para alta dificultad
    'low_difficulty': Colors.POSITIVE.value,    # Verde para baja dificultad
    
    # Colores de texto y fondo (optimizado para fondo claro)
    'text': '#2C3E50',        # Azul oscuro para texto - excelente contraste
    'text_light': '#6C757D',  # Gris para texto secundario
    'background': '#FFFFFF',  # Blanco para fondo
    'grid': '#DEE2E6',       # Gris muy claro para grillas
    'border': '#BDC3C7',     # Gris claro para bordes
    
    # Estados específicos para botones y elementos interactivos
    'hover': '#34495E',       # Azul oscuro para hover
    'active': '#2980B9',      # Azul medio para activo
    'disabled': '#95A5A6'     # Gris para deshabilitado
}

# Paletas predefinidas para diferentes tipos de gráficas
COLOR_PALETTES = {
    'spain_vs_europe': [STORYTELLING_COLORS['spain'], STORYTELLING_COLORS['europe']],
    'need_scale': [
        STORYTELLING_COLORS['applies_totally'],
        STORYTELLING_COLORS['applies_rather'], 
        STORYTELLING_COLORS['applies_partially'],
        STORYTELLING_COLORS['applies_rather_not'],
        STORYTELLING_COLORS['does_not_apply']
    ],
    'gender': [STORYTELLING_COLORS['female'], STORYTELLING_COLORS['male']],
    'positive_negative': [STORYTELLING_COLORS['need_work'], STORYTELLING_COLORS['dont_need_work']],
    'warning_levels': [
        STORYTELLING_COLORS['dont_need_work'],
        STORYTELLING_COLORS['warning'], 
        STORYTELLING_COLORS['danger']
    ]
}

# Configuración de layout estándar para todas las gráficas
STANDARD_LAYOUT = {
    'plot_bgcolor': STORYTELLING_COLORS['background'],
    'paper_bgcolor': STORYTELLING_COLORS['background'],
    'font': {
        'family': 'Arial, sans-serif', 
        'size': 12, 
        'color': STORYTELLING_COLORS['text']
    },
    'title': {
        'font': {
            'size': 18, 
            'color': STORYTELLING_COLORS['text'],
            'family': 'Arial, sans-serif'
        },
        'x': 0.5,
        'xanchor': 'center'
    },
    'legend': {
        'font': {
            'size': 12, 
            'color': STORYTELLING_COLORS['text'],
            'family': 'Arial, sans-serif'
        }
    }
}

# Configuración de ejes estándar
STANDARD_AXES = {
    'showgrid': True,
    'gridwidth': 1,
    'gridcolor': STORYTELLING_COLORS['grid'],
    'linecolor': STORYTELLING_COLORS['border'],
    'title_font': {
        'color': '#000000',  # Negro para máximo contraste
        'size': 14, 
        'family': 'Arial, sans-serif'
    },
    'tickfont': {
        'color': '#000000',  # Negro para máximo contraste
        'size': 11, 
        'family': 'Arial, sans-serif'
    }
}

def get_country_color(country_code):
    """
    Retorna el color apropiado para un país específico
    
    Args:
        country_code (str): Código del país (ej: 'ES', 'FR', etc.)
        
    Returns:
        str: Código de color hex
    """
    if country_code == 'ES':
        return STORYTELLING_COLORS['spain']
    else:
        return STORYTELLING_COLORS['europe']

def apply_standard_layout(fig, title=None, height=600, width=800):
    """
    Aplica el layout estándar a una figura de Plotly
    
    Args:
        fig: Figura de Plotly
        title (str): Título personalizado opcional
        height (int): Altura en píxeles
        width (int): Ancho en píxeles
        
    Returns:
        fig: Figura con layout actualizado
    """
    layout_update = STANDARD_LAYOUT.copy()
    layout_update['height'] = height
    layout_update['width'] = width
    
    if title:
        layout_update['title']['text'] = title
    
    fig.update_layout(**layout_update)
    fig.update_xaxes(**STANDARD_AXES)
    fig.update_yaxes(**STANDARD_AXES)
    
    return fig 