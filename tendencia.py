import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la serie temporal
np.random.seed(0)  # Para reproducibilidad
n_points = 100
x = np.linspace(0, 10, n_points)
trend = 2 * x + 1  # Tendencia lineal
noise = np.random.normal(0, 1, n_points)
y = trend + noise

# Graficar la serie temporal
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Datos con Ruido')
plt.plot(x, trend, label='Tendencia Subyacente', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.title('Serie Temporal con Tendencia Lineal y Ruido')
plt.show()

#Aplicaremos diferencias finitas para detectar la tendencia en los datos ruidosos.

def finite_difference(y, h):
    """
    Calcula la primera derivada usando diferencias finitas.
    """
    return (y[2:] - y[:-2]) / (2 * h)

# Calcular diferencias finitas
h = x[1] - x[0]  # Supongamos que los datos están equiespaciados
dy = finite_difference(y, h)
dx = x[1:-1]

# Graficar la derivada de la serie temporal
plt.figure(figsize=(10, 5))
plt.plot(dx, dy, label='Diferencias Finitas')
plt.axhline(2, color='red', linestyle='--', label='Tendencia Derivada Esperada')
plt.xlabel('Tiempo')
plt.ylabel('Diferencia Finita (Aproximación de Derivada)')
plt.legend()
plt.title('Detección de Tendencias mediante Diferencias Finitas')
plt.show()


#Aplicaremos diferencias finitas para detectar la tendencia en los datos ruidosos.

def moving_average(y, window_size):
    return np.convolve(y, np.ones(window_size)/window_size, mode='valid')

# Suavizar los datos
window_size = 5
y_smooth = moving_average(y, window_size)
x_smooth = x[(window_size-1)//2:-(window_size-1)//2]

# Calcular diferencias finitas en datos suavizados
dy_smooth = finite_difference(y_smooth, h)
dx_smooth = x_smooth[1:-1]

# Graficar la derivada de los datos suavizados
plt.figure(figsize=(10, 5))
plt.plot(dx_smooth, dy_smooth, label='Diferencias Finitas (Datos Suavizados)')
plt.axhline(2, color='red', linestyle='--', label='Tendencia Derivada Esperada')
plt.xlabel('Tiempo')
plt.ylabel('Diferencia Finita (Aproximación de Derivada)')
plt.legend()
plt.title('Detección de Tendencias con Datos Suavizados')
plt.show()



"""
Generación de Datos Sintéticos:

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

"""