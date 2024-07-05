# Análisis Financiero con Derivadas en Python

Este proyecto realiza un análisis financiero utilizando derivadas a partir de datos de precios históricos de acciones. Utiliza técnicas de diferencias finitas para detectar tendencias y evaluar la volatilidad de los precios.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Datos](#ejemplo-de-datos)
- [Código de Análisis](#código-de-análisis)
- [Licencia](#licencia)

## Instalación

Para ejecutar este proyecto, necesitas tener Python instalado junto con las bibliotecas `pandas`, `numpy`, `matplotlib` y `chardet`. Puedes instalar estas bibliotecas utilizando pip:

```bash
pip install pandas numpy matplotlib chardet
```
##  Crear el Archivo CSV

import pandas as pd

# Crear un DataFrame con datos de ejemplo
data = {
    'Date': ['01/01/2024', '02/01/2024', '03/01/2024', '04/01/2024', '05/01/2024'],
    'Open': [150.00, 154.00, 153.00, 151.00, 152.00],
    'High': [155.00, 156.00, 157.00, 153.00, 158.00],
    'Low': [149.00, 152.00, 150.00, 148.00, 150.00],
    'Close': [154.00, 153.00, 151.00, 152.00, 157.00],
    'Volume': ['1,000,000', '1,200,000', '1,300,000', '1,100,000', '1,400,000']
}

df = pd.DataFrame(data)

# Guardar el DataFrame como un archivo CSV
df.to_csv('historical_stock_prices.csv', index=False, sep=';')

print("Archivo CSV creado exitosamente.")

## Código de Análisis
El código de análisis realiza las siguientes tareas:

-Detectar la codificación del archivo CSV.
-Leer el archivo CSV con la codificación detectada.
-Normalizar los nombres de las columnas.
-Convertir la columna de fechas a un objeto datetime.
-Eliminar filas con fechas no válidas.
-Verificar y eliminar datos faltantes.
-Graficar los precios de cierre.
-Calcular y graficar diferencias finitas para detectar tendencias.
-Suavizar los datos y aplicar diferencias finitas a los datos suavizados.
-Calcular y graficar la segunda derivada para evaluar la aceleración de los precios.
-Evaluar y graficar la volatilidad como la desviación estándar de las diferencias finitas.

![image](https://github.com/martinskerr/Calculo/assets/98781432/f5fc040f-f1f8-40a0-a2a3-8cd3b59f1b03)

![image](https://github.com/martinskerr/Calculo/assets/98781432/8a2d8101-fd6e-4aa6-b222-21298bd8dba7)

![image](https://github.com/martinskerr/Calculo/assets/98781432/779ec849-203a-41f2-a2ec-9c6de2d090cd)

![image](https://github.com/martinskerr/Calculo/assets/98781432/1729c915-132d-4b09-afe8-947b136ed4e9)




Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.

