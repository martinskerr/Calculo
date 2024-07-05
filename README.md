#Generación de Datos Sintéticos: Tendencia.py
Se generan n_points datos con una tendencia lineal y ruido aleatorio.
Se grafica la serie temporal con la tendencia subyacente.
Aplicación de Diferencias Finitas:

Se define una función finite_difference para calcular la primera derivada usando diferencias finitas centrales.
Se aplican diferencias finitas a los datos ruidosos y se grafica la aproximación de la derivada.
Suavizado de Datos (Opcional):

Se define una función moving_average para suavizar los datos usando un promedio móvil.
Se aplican diferencias finitas a los datos suavizados y se grafica la aproximación de la derivada de los datos suavizados.

1. Diferencias Finitas Aproximan Bien la Tendencia Subyacente
La aplicación de diferencias finitas a la serie temporal original con ruido mostró que las diferencias finitas pueden aproximar la derivada de la función subyacente. Sin embargo, el ruido en los datos afecta la precisión de esta aproximación.
2. El Suavizado de Datos Mejora la Precisión
Al suavizar los datos originales utilizando un promedio móvil, se observa una mejora significativa en la precisión de la aproximación de la derivada.
La derivada calculada a partir de los datos suavizados se acerca más a la tendencia derivada esperada (en este caso, una constante de 2, que es la pendiente de la tendencia lineal subyacente).
3. Importancia del Tamaño del Paso (h)
El tamaño del paso 
ℎ
h es crucial en el cálculo de diferencias finitas. En este ejemplo, 
ℎ
h se calcula a partir de los datos equiespaciados.
Un tamaño de paso adecuado es esencial para equilibrar la precisión y la estabilidad numérica.
4. Visualización de Datos Ayuda a Entender Resultados
La visualización de los resultados, tanto de los datos originales como de los suavizados, proporciona una comprensión clara de cómo el ruido afecta a la derivada y cómo el suavizado puede mitigar este efecto.
Los gráficos ayudan a comparar visualmente la diferencia entre las derivadas calculadas y la tendencia derivada esperada.
5. Limitaciones y Consideraciones
Ruido en Datos: Los datos ruidosos afectan negativamente la precisión de las diferencias finitas. Es crucial considerar técnicas de suavizado o filtrado de datos para mejorar la precisión.
Ventanas de Suavizado: La elección del tamaño de la ventana de suavizado (en este caso, 5) puede influir en los resultados. Ventanas demasiado grandes pueden suavizar excesivamente, perdiendo detalles importantes, mientras que ventanas demasiado pequeñas pueden no eliminar suficiente ruido.
Conclusión General
Las diferencias finitas son una herramienta poderosa para la detección de tendencias en series temporales. 
Aunque el ruido en los datos puede afectar la precisión, técnicas de suavizado como el promedio móvil pueden mejorar significativamente los resultados. 
La correcta elección del tamaño del paso y de la ventana de suavizado es crucial para obtener resultados precisos y útiles. 
Este enfoque puede ser aplicado a diversos campos donde el análisis de tendencias es importante, como la economía, la ingeniería y las ciencias naturales.

# Análisis Financiero con Derivadas en Python: Finanzas.py & pruebacsv.py

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

