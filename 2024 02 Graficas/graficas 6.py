import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Añadir valores de cumplimiento a la serie de datos
cumplimiento.extend([85.00, 92.00, 78.00])
meses.extend(['Julio', 'Agosto', 'Septiembre'])

# Datos de incumplimiento
incumplimiento = [100 - x for x in cumplimiento]

# Ajuste de regresión lineal
X = np.arange(len(meses)).reshape(-1, 1)
y = np.array(cumplimiento).reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
plt.plot(meses, y_pred, color='blue', linestyle='--')

# Añadir etiquetas de cumplimiento e incumplimiento
for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

plt.title('Cumplimiento de Producción con Regresión Lineal y Valores Adicionales')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()



from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Añadir valores de cumplimiento a la serie de datos
cumplimiento.extend([85.00, 92.00, 78.00])
meses.extend(['Julio', 'Agosto', 'Septiembre'])

# Datos de incumplimiento
incumplimiento = [100 - x for x in cumplimiento]

# Convertir los datos a un DataFrame para ARIMA
df = DataFrame(cumplimiento, columns=['Cumplimiento'], index=meses)

# Ajuste del modelo ARIMA
model = ARIMA(df, order=(1, 0, 0))
model_fit = model.fit()

# Predecir los próximos valores
forecast = model_fit.forecast(steps=3)

# Gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
plt.plot(meses + ['Octubre', 'Noviembre', 'Diciembre'], list(cumplimiento) + list(forecast), marker='o', linestyle='--', color='blue')

# Añadir etiquetas de cumplimiento e incumplimiento
for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

plt.title('Cumplimiento de Producción con Proyección ARIMA y Valores Adicionales')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()





# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Añadir valores de cumplimiento a la serie de datos
cumplimiento.extend([85.00, 92.00, 78.00])
meses.extend(['Julio', 'Agosto', 'Septiembre'])

# Datos de incumplimiento
incumplimiento = [100 - x for x in cumplimiento]

# Gráfica
plt.figure(figsize=(10, 6))
bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])

# Añadir etiquetas de cumplimiento e incumplimiento
for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

plt.title('Cumplimiento de Producción con Incremento y Mejoras y Valores Adicionales')
plt.xlabel('Mes')
plt.ylabel('Cumplimiento (%)')
plt.grid(True)
plt.show()
