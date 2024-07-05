import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chardet

# Detectar la codificación
with open('historical_stock_prices.csv', 'rb') as f:
    result = chardet.detect(f.read(10000))
encoding = result['encoding']
print(f"Detected encoding: {encoding}")

# Leer el archivo CSV con la codificación detectada
data = pd.read_csv('historical_stock_prices.csv', encoding=encoding, delimiter=';', on_bad_lines='skip', thousands='.', decimal=',')

# Imprimir los nombres de las columnas para verificar
print(data.columns)

# Intentar normalizar los nombres de las columnas
data.columns = data.columns.str.strip()

# Convertir la columna de fechas a un objeto datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')

# Eliminar filas con fechas no válidas
data = data.dropna(subset=['Date'])

# Verificar si las columnas tienen datos faltantes
print(data.isnull().sum())

# Llenar o eliminar filas con datos faltantes en la columna 'Close'
data = data.dropna(subset=['Close'])

# Extraer las columnas de interés
dates = data['Date']
prices = data['Close']

# Graficar los precios de las acciones
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label='Precio de Cierre')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.title('Precios Históricos de Acciones')
plt.legend()
plt.show()

# Función de diferencias finitas
def finite_difference(y, h):
    return (y[2:] - y[:-2]) / (2 * h)

# Calcular diferencias finitas para detectar la tendencia
h = 1  # Supongamos que los datos son diarios
price_diff = finite_difference(prices, h)
date_diff = dates[1:-1]

# Graficar la derivada de los precios
plt.figure(figsize=(10, 5))
plt.plot(date_diff, price_diff, label='Diferencia Finita de Precios')
plt.xlabel('Fecha')
plt.ylabel('Diferencia Finita')
plt.title('Detección de Tendencias en Precios de Acciones')
plt.legend()
plt.show()

# Función de suavizado de datos
def moving_average(y, window_size):
    return np.convolve(y, np.ones(window_size)/window_size, mode='valid')

# Suavizar los datos y aplicar diferencias finitas
window_size = 5
prices_smooth = moving_average(prices, window_size)
date_smooth = dates[(window_size-1)//2:-(window_size-1)//2]

price_diff_smooth = finite_difference(prices_smooth, h)
date_diff_smooth = date_smooth[1:-1]

# Graficar la derivada de los datos suavizados
plt.figure(figsize=(10, 5))
plt.plot(date_diff_smooth, price_diff_smooth, label='Diferencia Finita (Datos Suavizados)')
plt.xlabel('Fecha')
plt.ylabel('Diferencia Finita')
plt.title('Detección de Tendencias con Datos Suavizados en Precios de Acciones')
plt.legend()
plt.show()

# Cálculo de la segunda derivada para evaluar la aceleración de los precios
def second_finite_difference(y, h):
    return (y[2:] - 2 * y[1:-1] + y[:-2]) / (h ** 2)

price_accel = second_finite_difference(prices, h)
date_accel = dates[1:-1]

# Graficar la segunda derivada de los precios
plt.figure(figsize=(10, 5))
plt.plot(date_accel, price_accel, label='Segunda Derivada de Precios')
plt.xlabel('Fecha')
plt.ylabel('Segunda Derivada')
plt.title('Evaluación de la Aceleración de Precios')
plt.legend()
plt.show()

# Evaluar la volatilidad como la desviación estándar de las diferencias finitas
volatility = np.std(price_diff)

print(f"Volatilidad estimada de los precios: {volatility:.5f}")

# Graficar la volatilidad
plt.figure(figsize=(10, 5))
plt.plot(date_diff, np.abs(price_diff), label='Volatilidad (|Diferencia Finita|)')
plt.xlabel('Fecha')
plt.ylabel('Volatilidad')
plt.title('Evaluación de la Volatilidad de Precios')
plt.legend()
plt.show()
