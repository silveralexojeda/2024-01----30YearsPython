from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Ajuste de regresión lineal
X = np.arange(len(meses)).reshape(-1, 1)
y = np.array(cumplimiento).reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Gráfica
plt.figure(figsize=(8, 6))
plt.bar(meses, cumplimiento, color=['black', 'red', 'black'])
plt.plot(meses, y_pred, color='blue', linestyle='--')
plt.title('Cumplimiento de Producción con Regresión Lineal')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()

from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame

# Convertir los datos a un DataFrame para ARIMA
df = DataFrame(cumplimiento, columns=['Cumplimiento'], index=meses)

# Ajuste del modelo ARIMA
model = ARIMA(df, order=(1, 0, 0))
model_fit = model.fit()

# Predecir los próximos valores
forecast = model_fit.forecast(steps=3)

# Gráfica
plt.figure(figsize=(8, 6))
plt.bar(meses, cumplimiento, color=['black', 'red', 'black'])
plt.plot(meses + ['Julio', 'Agosto', 'Septiembre'], list(cumplimiento) + list(forecast), marker='o', linestyle='--', color='blue')
plt.title('Cumplimiento de Producción con Proyección ARIMA')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()

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

