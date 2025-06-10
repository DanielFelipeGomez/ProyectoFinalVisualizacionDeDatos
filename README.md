# Proyecto Final de la asignatura de Visualización de Datos
## Autor: Daniel Felipe Gomez Aristizabal


### Descripción

En este repositorio presento una aplicación interactiva de Streamlit en la que he creado un storytelling donde analizo la realidad de los estudiantes europeos que necesitan trabajar para costear sus estudios, con especial foco en España.

### Tecnologías utilizadas

- Streamlit
- Plotly
- Pandas
- Numpy
- Matplotlib
- OpenPyXL

### Estructura del repositorio

#### assets

En este directorio se encuentran las imagenes utilizadas en el storytelling, además de los logos institucionales de la Universidad Oberta de Catalunya y de EUROSTUDENT.

#### data

En este repositorio se encuentran los excels utilizados para el storytelling, además de los excels sin procesar de cada una de las categorias que se evaluaron en la ronda 8 de la encuesta EUROSTUDENT.

#### modules

En este directorio se encuentran los modulos utilizados para el storytelling, cada modulo tiene su propia carpeta y dentro de cada carpeta se encuentran los archivos necesarios para el funcionamiento de cada modulo.

#### storytelling.py

En este archivo se encuentra el storytelling principal, donde se importan los modulos y se crea la aplicación interactiva. He añadido algunso estilos css para mejorar la estética de la aplicación.

#### requirements.txt

En este archivo se encuentran las dependencias necesarias para el funcionamiento de la aplicación.

### Instalación

Para instalar las dependencias necesarias para el funcionamiento de la aplicación, se puede utilizar el archivo requirements.txt.

```bash
pip install -r requirements.txt
```

Seguidamente, se puede ejecutar la aplicación con el siguiente comando:

```bash
streamlit run storytelling.py
```

### Bibliografía

- EUROSTUDENT: https://www.eurostudent.eu/
- Ronda 8 de la encuesta EUROSTUDENT: https://database.eurostudent.eu/drm/

### Créditos

- Trabajo realizado por Daniel Felipe Gómez Aristizábal con fines académicos, 
como parte de la asignatura Visualización de Datos del Máster Universitario en Ciencia de Datos de la UOC.

### Licencia

Este trabajo está bajo la licencia MIT.
