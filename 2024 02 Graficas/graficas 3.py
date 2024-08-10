from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Datos adicionales simulados para incremento y mejoras
cumplimiento_incremento = [75.74, 95.90, 70.86, 85.00, 92.00, 78.00]
meses_adicionales = ['Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre']

# Gráfica
plt.figure(figsize=(8, 6))
plt.bar(meses_adicionales, cumplimiento_incremento, color=['black', 'red', 'black', 'black', 'red', 'black'])
plt.title('Cumplimiento de Producción con Incremento y Mejoras')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()