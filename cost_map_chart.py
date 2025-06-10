import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def read_cost_dataset():
    """Lee el dataset de costes mensuales por país"""
    try:
        # Leer el archivo Excel de costes
        df = pd.read_excel("preprocessed_excels/E8_costs_all_total__all_students__all_contries.xlsx")
        return df
    except Exception as e:
        print(f"Error leyendo dataset de costes: {e}")
        return None


def generate_europe_cost_heatmap():
    """
    Genera un mapa de calor interactivo de Europa mostrando los costes mensuales por país
    
    Returns:
        plotly.graph_objects.Figure: Mapa de calor interactivo de Europa
    """
    
    # Leer datos
    df = read_cost_dataset()
    
    if df is None or df.empty:
        print("No se pudieron cargar los datos de costes")
        return None
    
    try:
        # Mapeo de códigos de países de 2 letras a códigos ISO-3 para el mapa
        country_iso_mapping = {
            'AT': 'AUT',  # Austria
            'BE': 'BEL',  # Belgium
            'BG': 'BGR',  # Bulgaria
            'HR': 'HRV',  # Croatia
            'CY': 'CYP',  # Cyprus
            'CZ': 'CZE',  # Czech Republic
            'DK': 'DNK',  # Denmark
            'EE': 'EST',  # Estonia
            'FI': 'FIN',  # Finland
            'FR': 'FRA',  # France
            'DE': 'DEU',  # Germany
            'GR': 'GRC',  # Greece
            'HU': 'HUN',  # Hungary
            'IS': 'ISL',  # Iceland
            'IE': 'IRL',  # Ireland
            'IT': 'ITA',  # Italy
            'LV': 'LVA',  # Latvia
            'LT': 'LTU',  # Lithuania
            'LU': 'LUX',  # Luxembourg
            'MT': 'MLT',  # Malta
            'NL': 'NLD',  # Netherlands
            'NO': 'NOR',  # Norway
            'PL': 'POL',  # Poland
            'PT': 'PRT',  # Portugal
            'RO': 'ROU',  # Romania
            'SK': 'SVK',  # Slovakia
            'SI': 'SVN',  # Slovenia
            'ES': 'ESP',  # Spain
            'SE': 'SWE',  # Sweden
            'CH': 'CHE',  # Switzerland
            'GB': 'GBR',  # United Kingdom
            'TR': 'TUR',  # Turkey
            'AZ': 'AZE',  # Azerbaijan
            'GE': 'GEO',  # Georgia
            'AM': 'ARM'   # Armenia
        }
        
        # Mapeo de códigos ISO-3 a nombres completos para display
        iso_to_country_names = {
            'AUT': 'Austria', 'BEL': 'Belgium', 'BGR': 'Bulgaria', 'HRV': 'Croatia',
            'CYP': 'Cyprus', 'CZE': 'Czech Republic', 'DNK': 'Denmark', 'EST': 'Estonia',
            'FIN': 'Finland', 'FRA': 'France', 'DEU': 'Germany', 'GRC': 'Greece',
            'HUN': 'Hungary', 'ISL': 'Iceland', 'IRL': 'Ireland', 'ITA': 'Italy',
            'LVA': 'Latvia', 'LTU': 'Lithuania', 'LUX': 'Luxembourg', 'MLT': 'Malta',
            'NLD': 'Netherlands', 'NOR': 'Norway', 'POL': 'Poland', 'PRT': 'Portugal',
            'ROU': 'Romania', 'SVK': 'Slovakia', 'SVN': 'Slovenia', 'ESP': 'Spain',
            'SWE': 'Sweden', 'CHE': 'Switzerland', 'GBR': 'United Kingdom', 'TUR': 'Turkey',
            'AZE': 'Azerbaijan', 'GEO': 'Georgia', 'ARM': 'Armenia'
        }
        
        # Preparar los datos según la estructura real del archivo
        # El archivo tiene las primeras 2 filas como headers, empezar desde la fila 2
        df_data = df.iloc[2:].copy()  # Saltar las filas de encabezado
        
        # Usar las columnas 'Country' (códigos de país) y 'All students' (costes)
        df_processed = df_data[['Country', 'All students']].copy()
        df_processed.columns = ['Country_Code', 'Monthly_Cost']
        
        # Limpiar datos nulos y convertir costes a numérico
        df_processed = df_processed.dropna()
        df_processed['Monthly_Cost'] = pd.to_numeric(df_processed['Monthly_Cost'], errors='coerce')
        df_processed = df_processed.dropna()  # Eliminar filas con costes no numéricos
        
        # Agregar códigos ISO-3 basado en los códigos de 2 letras
        df_processed['ISO3'] = df_processed['Country_Code'].map(country_iso_mapping)
        df_processed['Country_Name'] = df_processed['ISO3'].map(iso_to_country_names)
        
        # Filtrar países que tienen código ISO (países europeos principalmente)
        df_processed = df_processed.dropna(subset=['ISO3'])
        
        print(f"Países procesados: {len(df_processed)}")
        print("Muestra de datos procesados:")
        print(df_processed.head())
        
        # Crear el mapa de calor
        fig = go.Figure(data=go.Choropleth(
            locations=df_processed['ISO3'],
            z=df_processed['Monthly_Cost'],
            locationmode='ISO-3',
            colorscale=[
                [0.0, '#d0f0c0'],   # Verde muy claro
                [0.2, '#a8e6a3'],   # Verde claro
                [0.4, '#fddc9b'],   # Amarillo suave
                [0.6, '#ffb347'],   # Naranja medio
                [0.8, '#ff8c00'],   # Naranja fuerte
                [1.0, '#ff4500']    # Rojo intenso
            ],
            text=df_processed['Country_Name'],
            hovertemplate='<b>%{text}</b><br>' +
                         'Coste mensual: €%{z:,.0f}<br>' +
                         '<extra></extra>',
            colorbar=dict(
                title=dict(text="Coste Mensual (€)", font=dict(size=14)),
                tickfont=dict(size=12)
            )
        ))
        
        # Configurar el layout para enfocar Europa
        fig.update_layout(
            title={
                'text': 'Costes Mensuales de Estudiantes Universitarios en Europa',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18, 'family': 'Arial, sans-serif', 'color': '#2C3E50'}
            },
            geo=dict(
                scope='europe',
                resolution=50,
                showframe=False,
                showcoastlines=True,
                projection_type='natural earth',
                bgcolor='rgba(0,0,0,0)',
                showland=True,
                landcolor='#F8F9FA',
                showocean=True,
                oceancolor='#E3F2FD',
                showcountries=True,
                countrycolor='#CCCCCC'
            ),
            height=600,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family="Arial, sans-serif", size=12, color="#2C3E50")
        )
        
        # Añadir anotación con información clave
        spain_data = df_processed[df_processed['Country_Code'] == 'ES']
        spain_cost = spain_data['Monthly_Cost'].iloc[0] if not spain_data.empty else None
        avg_cost = df_processed['Monthly_Cost'].mean()
        
        annotation_text = f"Promedio Europeo: €{avg_cost:,.0f}"
        if spain_cost:
            annotation_text += f"<br>España: €{spain_cost:,.0f}"
        
        fig.add_annotation(
            text=annotation_text,
            xref="paper", yref="paper",
            x=0.02, y=0.98,
            showarrow=False,
            font=dict(size=12, color="#2C3E50"),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="#CCCCCC",
            borderwidth=1
        )
        
        return fig
        
    except Exception as e:
        print(f"Error creando mapa de costes: {e}")
        return None


def get_cost_statistics():
    """
    Obtiene estadísticas clave de los costes mensuales
    
    Returns:
        dict: Diccionario con estadísticas clave
    """
    df = read_cost_dataset()
    
    if df is None or df.empty:
        return {"error": "No se pudieron cargar los datos"}
    
    try:
        # Mapeo de códigos ISO-3 a nombres completos
        iso_to_country_names = {
            'AUT': 'Austria', 'BEL': 'Belgium', 'BGR': 'Bulgaria', 'HRV': 'Croatia',
            'CYP': 'Cyprus', 'CZE': 'Czech Republic', 'DNK': 'Denmark', 'EST': 'Estonia',
            'FIN': 'Finland', 'FRA': 'France', 'DEU': 'Germany', 'GRC': 'Greece',
            'HUN': 'Hungary', 'ISL': 'Iceland', 'IRL': 'Ireland', 'ITA': 'Italy',
            'LVA': 'Latvia', 'LTU': 'Lithuania', 'LUX': 'Luxembourg', 'MLT': 'Malta',
            'NLD': 'Netherlands', 'NOR': 'Norway', 'POL': 'Poland', 'PRT': 'Portugal',
            'ROU': 'Romania', 'SVK': 'Slovakia', 'SVN': 'Slovenia', 'ESP': 'Spain',
            'SWE': 'Sweden', 'CHE': 'Switzerland', 'GBR': 'United Kingdom', 'TUR': 'Turkey',
            'AZE': 'Azerbaijan', 'GEO': 'Georgia', 'ARM': 'Armenia'
        }
        
        country_iso_mapping = {
            'AT': 'AUT', 'BE': 'BEL', 'BG': 'BGR', 'HR': 'HRV', 'CY': 'CYP', 'CZ': 'CZE',
            'DK': 'DNK', 'EE': 'EST', 'FI': 'FIN', 'FR': 'FRA', 'DE': 'DEU', 'GR': 'GRC',
            'HU': 'HUN', 'IS': 'ISL', 'IE': 'IRL', 'IT': 'ITA', 'LV': 'LVA', 'LT': 'LTU',
            'LU': 'LUX', 'MT': 'MLT', 'NL': 'NLD', 'NO': 'NOR', 'PL': 'POL', 'PT': 'PRT',
            'RO': 'ROU', 'SK': 'SVK', 'SI': 'SVN', 'ES': 'ESP', 'SE': 'SWE', 'CH': 'CHE',
            'GB': 'GBR', 'TR': 'TUR', 'AZ': 'AZE', 'GE': 'GEO', 'AM': 'ARM'
        }
        
        # Usar la misma lógica de procesamiento que en generate_europe_cost_heatmap
        df_data = df.iloc[2:].copy()  # Saltar las filas de encabezado
        
        df_processed = df_data[['Country', 'All students']].copy()
        df_processed.columns = ['Country_Code', 'Monthly_Cost']
        
        # Limpiar datos nulos y convertir costes a numérico
        df_processed = df_processed.dropna()
        df_processed['Monthly_Cost'] = pd.to_numeric(df_processed['Monthly_Cost'], errors='coerce')
        df_processed = df_processed.dropna()
        
        # Agregar nombres de países
        df_processed['ISO3'] = df_processed['Country_Code'].map(country_iso_mapping)
        df_processed['Country_Name'] = df_processed['ISO3'].map(iso_to_country_names)
        df_processed = df_processed.dropna(subset=['ISO3'])
        
        # Estadísticas generales
        stats = {
            'promedio_europa': df_processed['Monthly_Cost'].mean(),
            'mediana_europa': df_processed['Monthly_Cost'].median(),
            'coste_minimo': df_processed['Monthly_Cost'].min(),
            'coste_maximo': df_processed['Monthly_Cost'].max(),
            'pais_mas_barato': df_processed.loc[df_processed['Monthly_Cost'].idxmin(), 'Country_Name'],
            'pais_mas_caro': df_processed.loc[df_processed['Monthly_Cost'].idxmax(), 'Country_Name'],
            'total_paises': len(df_processed)
        }
        
        # Estadísticas específicas de España si está disponible
        spain_data = df_processed[df_processed['Country_Code'] == 'ES']
        if not spain_data.empty:
            spain_cost = spain_data['Monthly_Cost'].iloc[0]
            stats['coste_espana'] = spain_cost
            stats['diferencia_con_promedio'] = spain_cost - stats['promedio_europa']
            
            # Ranking de España
            spain_rank = (df_processed['Monthly_Cost'] > spain_cost).sum() + 1
            stats['ranking_espana'] = spain_rank
        
        return stats
        
    except Exception as e:
        print(f"Error calculando estadísticas: {e}")
        return {"error": str(e)} 