# 📁 Datos de Defunciones por COVID-19 en Chile

Este archivo contiene el dataset oficial de defunciones asociadas a COVID-19 en Chile entre los años 2020 y 2025.

## 📚 Fuente

- Plataforma de Datos Abiertos del Gobierno de Chile
- URL directa: [https://datos.gob.cl/dataset/defunciones-por-covid19](https://datos.gob.cl/dataset/defunciones-por-covid19)
- Última actualización: mayo 2025

## 📄 Archivo incluido

- `defunciones_covid19_2020_2024.csv`: archivo CSV separado por punto y coma (`;`), codificado en `ISO-8859-1`.

## ℹ️ Notas

- El archivo fue utilizado como base para el proceso ETL que carga los datos en PostgreSQL.
- Columnas innecesarias o sensibles fueron eliminadas en el script `ETL.py`.
- Las edades fueron agrupadas en rangos durante la visualización.

