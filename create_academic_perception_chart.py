import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


class AcademicPerceptionChart:
    def __init__(self):
        # Colores consistentes con el storytelling
        self.colors = {
            "spain": "#C41E3A",  # Rojo España
            "europe": "#003DA5",  # Azul Europa
            "positive": "#27AE60",  # Verde éxito
            "warning": "#F39C12",  # Naranja advertencia
            "neutral": "#7F8C8D",  # Gris neutral
            "light_blue": "#3498db",  # Azul claro
            "gradient": [
                "#E74C3C",
                "#F39C12",
                "#F1C40F",
                "#2ECC71",
                "#27AE60",
            ],  # Gradiente de rojo a verde
        }

    def load_data(self, file_path):
        """Cargar y explorar los datos del archivo Excel"""
        try:
            # Leer el archivo Excel
            df = pd.read_excel(file_path)
            print("Estructura de los datos:")
            print(f"Shape: {df.shape}")
            print(f"Columns: {df.columns.tolist()}")
            print("\nPrimeras filas:")
            print(df.head())
            print("\nTipos de datos:")
            print(df.dtypes)
            print("\nValores únicos por columna:")
            for col in df.columns:
                print(f"{col}: {df[col].unique()}")

            return df
        except Exception as e:
            print(f"Error cargando datos: {e}")
            return None

    def create_academic_perception_chart(self, df):
        """Crear gráfico de percepción académica basado en relación trabajo-estudio"""

        if df is None:
            print("No hay datos para procesar")
            return None

        # Identificar las columnas relevantes
        # Asumimos que hay una columna para relación trabajo-estudio y otra para percepción académica
        work_relation_col = None
        academic_perception_col = None

        for col in df.columns:
            if (
                "work" in col.lower()
                or "related" in col.lower()
                or "relation" in col.lower()
            ):
                work_relation_col = col
            elif (
                "performance" in col.lower()
                or "perception" in col.lower()
                or "assessment" in col.lower()
            ):
                academic_perception_col = col

        print(f"Columna relación trabajo: {work_relation_col}")
        print(f"Columna percepción académica: {academic_perception_col}")

        if work_relation_col and academic_perception_col:
            return self._create_correlation_chart(
                df, work_relation_col, academic_perception_col
            )
        else:
            # Si no podemos identificar las columnas, crear un gráfico genérico con los datos disponibles
            return self._create_generic_chart(df)

    def _create_correlation_chart(self, df, work_col, academic_col):
        """Crear gráfico de correlación específico"""

        # Preparar datos para el gráfico
        chart_data = (
            df.groupby([work_col, academic_col]).size().reset_index(name="count")
        )

        # Crear gráfico de barras apiladas
        fig = go.Figure()

        # Obtener valores únicos para crear el gráfico
        work_levels = sorted(df[work_col].unique())
        academic_levels = sorted(df[academic_col].unique())

        # Crear una barra para cada nivel de relación trabajo-estudio
        for i, work_level in enumerate(work_levels):
            data_subset = chart_data[chart_data[work_col] == work_level]

            fig.add_trace(
                go.Bar(
                    x=data_subset[academic_col],
                    y=data_subset["count"],
                    name=f"Relación trabajo-estudio: {work_level}",
                    marker_color=self.colors["gradient"][
                        i % len(self.colors["gradient"])
                    ],
                    opacity=0.8,
                )
            )

        # Configurar layout
        fig.update_layout(
            title={
                "text": "<b>Percepción Académica Personal según Relación Trabajo-Estudio</b><br><sub>España - Impacto del trabajo relacionado en la autoevaluación</sub>",
                "x": 0.5,
                "xanchor": "center",
                "font": {"size": 16, "color": "#2C3E50"},
            },
            xaxis_title="Percepción del Rendimiento Académico",
            yaxis_title="Número de Estudiantes",
            barmode="group",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font={"color": "#2C3E50"},
            showlegend=True,
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
            ),
            margin=dict(t=100, l=50, r=50, b=80),
        )

        # Estilo de ejes consistente con el storytelling
        fig.update_xaxes(
            showgrid=True, gridcolor="rgba(128,128,128,0.2)", linecolor="#dee2e6"
        )
        fig.update_yaxes(
            showgrid=True, gridcolor="rgba(128,128,128,0.2)", linecolor="#dee2e6"
        )

        return fig

    def _create_generic_chart(self, df):
        """Crear gráfico genérico con los datos disponibles"""

        # Usar las primeras dos columnas numéricas o categóricas
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=["object"]).columns

        if len(numeric_cols) >= 2:
            x_col, y_col = numeric_cols[0], numeric_cols[1]
        elif len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
            x_col, y_col = categorical_cols[0], numeric_cols[0]
        else:
            x_col, y_col = df.columns[0], df.columns[1]

        print(f"Usando columnas: {x_col} (x) y {y_col} (y)")

        # Crear gráfico de barras
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title="Percepción Académica Personal - Datos Disponibles",
            color_discrete_sequence=[self.colors["spain"]],
        )

        # Aplicar estilo consistente
        fig.update_layout(
            title={
                "text": "<b>Percepción Académica Personal según Relación Trabajo-Estudio</b><br><sub>España - Análisis de datos disponibles</sub>",
                "x": 0.5,
                "xanchor": "center",
                "font": {"size": 16, "color": "#2C3E50"},
            },
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1,
                xanchor="right",
                x=1,
                font={"color": "#000000"},
            ),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font={"color": "#2C3E50"},
            margin=dict(t=100, l=50, r=50, b=80),
        )

        # Estilo de ejes
        fig.update_xaxes(
            showgrid=True, gridcolor="rgba(128,128,128,0.2)", linecolor="#dee2e6"
        )
        fig.update_yaxes(
            showgrid=True, gridcolor="rgba(128,128,128,0.2)", linecolor="#dee2e6"
        )

        return fig

    def create_streamlit_optimized_chart(self, df):
        """Crear versión optimizada para Streamlit del gráfico"""

        fig = self.create_academic_perception_chart(df)

        if fig:
            # Optimizaciones para Streamlit
            fig.update_layout(
                height=500,  # Altura fija apropiada
                showlegend=True,
                legend=dict(
                    orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5
                ),
            )

        return fig


# Función principal para usar en el storytelling
def create_academic_perception_analysis(
    file_path="preprocessed_impact_by_job/E8_selfevaluation__s_performance_self_assessment__ES.xlsx",
):
    """Función principal para crear el análisis de percepción académica"""

    chart_creator = AcademicPerceptionChart()

    # Cargar datos
    df = chart_creator.load_data(file_path)

    if df is not None:
        # Crear gráfico
        fig = chart_creator.create_streamlit_optimized_chart(df)
        return fig, df
    else:
        return None, None


# Test del script
if __name__ == "__main__":
    fig, df = create_academic_perception_analysis()
    if fig:
        fig.show()
        print("Gráfico creado exitosamente")
    else:
        print("Error creando el gráfico")
