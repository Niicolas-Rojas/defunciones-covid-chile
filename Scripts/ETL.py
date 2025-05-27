import pandas as pd
from sqlalchemy import create_engine

# === Paso 1: Extracción ===
print("🔽 Extrayendo datos...")
archivo_csv = "../data/defunciones_covid19_2020_2024.csv"
df = pd.read_csv(archivo_csv, sep=";")


print(f"✅ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

# === Paso 2: Transformación ===
print("🔧 Transformando datos...")

# Lista de columnas que quieres eliminar explícitamente
columnas_a_eliminar = ['EDAD_TIPO', 'DIAG1', 'CAPITULO_DIAG1','GLOSA_CAPITULO_DIAG1','CODIGO_GRUPO_DIAG1','GLOSA_GRUPO_DIAG1','CODIGO_CATEGORIA_DIAG1','GLOSA_CATEGORIA_DIAG1','DIAG2']

# Elimina solo si existen en el DataFrame
df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns])
# Renombrar columnas para que no tengan espacios ni caracteres especiales, e igualmente que tengan un nombre en minusculas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w_]", "", regex=True)

# Eliminar columnas donde todos los valores son NaN
df = df.dropna(axis=1, how='all')

# Renombrar columnas a nombres mas intuitivos
df = df.rename(columns={'sexo_nombre': 'sexo'})
df = df.rename(columns={'edad_cant': 'edad'})
df = df.rename(columns={'codigo_subcategoria_diag1': 'cod_diagnostico1'})
df = df.rename(columns={'glosa_subcategoria_diag1': 'glosa_diagnostico1'})

#print(df.head())
print(f"✅ Transformación completada: {df.shape[0]} filas, {df.shape[1]} columnas")


# === ETAPA 3: Carga en base de datos PostGresql (Simulada de manera local con Docker) ===

# Parámetros de conexión
usuario = "admin"
password = "admin12345"
host = "localhost"
puerto = "5432"
basedatos = "defunciones_covid_db"

# Crea el motor de conexión
engine = create_engine(f"postgresql://{usuario}:{password}@{host}:{puerto}/{basedatos}")

# Carga el DataFrame en la tabla 'defunciones_covid'
df.to_sql("defunciones_covid", engine, if_exists="replace", index=False)

print("✅ Datos cargados exitosamente en PostgreSQL.")
