from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

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