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
