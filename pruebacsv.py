import pandas as pd

# Crear un DataFrame con datos de ejemplo
# data = {
#     'Date': ['01/01/2024', '02/01/2024', '03/01/2024', '04/01/2024', '05/01/2024'],
#     'Open': [150.00, 154.00, 153.00, 151.00, 152.00],
#     'High': [155.00, 156.00, 157.00, 153.00, 158.00],
#     'Low': [149.00, 152.00, 150.00, 148.00, 150.00],
#     'Close': [154.00, 153.00, 151.00, 152.00, 157.00],
#     'Volume': ['1,000,000', '1,200,000', '1,300,000', '1,100,000', '1,400,000']
# }

# df = pd.DataFrame(data)

# # Guardar el DataFrame como un archivo CSV
# df.to_csv('historical_stock_prices.csv', index=False, sep=';')

# print("Archivo CSV creado exitosamente.")

# Leer el archivo CSV creado
df_read = pd.read_csv('historical_stock_prices.csv', delimiter=';')

# Mostrar el contenido del DataFrame leído
print(df_read)