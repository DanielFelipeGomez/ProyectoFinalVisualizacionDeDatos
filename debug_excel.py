import pandas as pd
from storytelliing_charts import PreprocessedDatasetsName

# Leemos el archivo con diferentes parámetros
print('=== Leyendo sin parámetros adicionales ===')
df = pd.read_excel(PreprocessedDatasetsName.WORK_MOTIVE_AFFORD_STUDY.value)
print(f'Shape: {df.shape}')
print(f'Columns: {df.columns.tolist()}')
print(f'Primeras 10 filas:')
print(df.head(10))

print('\n=== Leyendo con header=None ===')
df_no_header = pd.read_excel(PreprocessedDatasetsName.WORK_MOTIVE_AFFORD_STUDY.value, header=None)
print(f'Shape: {df_no_header.shape}')
print(f'Primeras 10 filas:')
print(df_no_header.head(10))

print('\n=== Looking at specific rows ===')
df_rows = pd.read_excel(PreprocessedDatasetsName.WORK_MOTIVE_AFFORD_STUDY.value, header=None, nrows=15)
for i, row in df_rows.iterrows():
    print(f'Row {i}: {row.tolist()}') 