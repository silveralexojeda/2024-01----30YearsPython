import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import ipywidgets as widgets
from IPython.display import display

# Datos de cumplimiento de producción
meses = ['Abril', 'Mayo', 'Junio']
cumplimiento = [75.74, 95.90, 70.86]

# Añadir valores de cumplimiento a la serie de datos
cumplimiento.extend([85.00, 92.00, 78.00])
meses.extend(['Julio', 'Agosto', 'Septiembre'])

# Datos de incumplimiento redondeado a 2 dígitos
incumplimiento = [round(100 - x, 2) for x in cumplimiento]

def plot_graph(option):
    if option == 'Regresión Lineal':
        plt.figure(figsize=(10, 6))
        X = np.arange(len(meses)).reshape(-1, 1)
        y = np.array(cumplimiento).reshape(-1, 1)
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)
        
        bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
        plt.plot(meses, y_pred, color='blue', linestyle='--')

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        plt.title('Cumplimiento de Producción con Regresión Lineal y Valores Adicionales')
        plt.xlabel('Mes')
        plt.ylabel('Cumplimiento (%)')
        plt.grid(True)
        plt.show()

    elif option == 'Proyección ARIMA':
        plt.figure(figsize=(10, 6))
        df = DataFrame(cumplimiento, columns=['Cumplimiento'], index=meses)
        model = ARIMA(df, order=(1, 0, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=3)
        
        bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
        plt.plot(meses + ['Octubre', 'Noviembre', 'Diciembre'], list(cumplimiento) + list(forecast), marker='o', linestyle='--', color='blue')

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        plt.title('Cumplimiento de Producción con Proyección ARIMA y Valores Adicionales')
        plt.xlabel('Mes')
        plt.ylabel('Cumplimiento (%)')
        plt.grid(True)
        plt.show()

    elif option == 'Incremento y Mejoras':
        plt.figure(figsize=(10, 6))
        bars = plt.bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        plt.title('Cumplimiento de Producción con Incremento y Mejoras y Valores Adicionales')
        plt.xlabel('Mes')
        plt.ylabel('Cumplimiento (%)')
        plt.grid(True)
        plt.show()

    elif option == 'Todas':
        fig, axs = plt.subplots(3, 1, figsize=(10, 18))
        
        # Gráfica 1: Regresión Lineal
        X = np.arange(len(meses)).reshape(-1, 1)
        y = np.array(cumplimiento).reshape(-1, 1)
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)
        
        bars = axs[0].bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
        axs[0].plot(meses, y_pred, color='blue', linestyle='--')

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            axs[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            axs[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        axs[0].set_title('Cumplimiento de Producción con Regresión Lineal y Valores Adicionales')
        axs[0].set_xlabel('Mes')
        axs[0].set_ylabel('Cumplimiento (%)')
        axs[0].grid(True)

        # Gráfica 2: Proyección ARIMA
        df = DataFrame(cumplimiento, columns=['Cumplimiento'], index=meses)
        model = ARIMA(df, order=(1, 0, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=3)
        
        bars = axs[1].bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])
        axs[1].plot(meses + ['Octubre', 'Noviembre', 'Diciembre'], list(cumplimiento) + list(forecast), marker='o', linestyle='--', color='blue')

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            axs[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            axs[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        axs[1].set_title('Cumplimiento de Producción con Proyección ARIMA y Valores Adicionales')
        axs[1].set_xlabel('Mes')
        axs[1].set_ylabel('Cumplimiento (%)')
        axs[1].grid(True)

        # Gráfica 3: Incremento y Mejoras
        bars = axs[2].bar(meses, cumplimiento, color=['black', 'red', 'black', 'black', 'red', 'black'])

        for bar, cump, incump in zip(bars, cumplimiento, incumplimiento):
            axs[2].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{cump}%', ha='center', va='bottom', color='white')
            axs[2].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{incump}%', ha='center', va='bottom', color='black')

        axs[2].set_title('Cumplimiento de Producción con Incremento y Mejoras y Valores Adicionales')
        axs[2].set_xlabel('Mes')
        axs[2].set_ylabel('Cumplimiento (%)')
        axs[2].grid(True)

        plt.tight_layout()
        plt.show()

# Crear el widget de selección
select = widgets.Dropdown(
    options=['Regresión Lineal', 'Proyección ARIMA', 'Incremento y Mejoras', 'Todas'],
    value='Regresión Lineal',
    description='Gráfica:',
)

# Mostrar la gráfica inicial y configurar la función de actualización
plot_graph(select.value)
widgets.interact(plot_graph, option=select)
