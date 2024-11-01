import numpy as np
import matplotlib.pyplot as plt


media = 10 
desviacion_estandar = 2 

var = desviacion_estandar ** 2
mu = np.log((media ** 2) / np.sqrt(var + media ** 2))
sigma = np.sqrt(np.log(var / media ** 2 + 1))


tiempos_espera = np.random.lognormal(mu, sigma, 50)


print("Tiempos de espera generados (minutos):", tiempos_espera)


media_espera = np.mean(tiempos_espera)
mediana_espera = np.median(tiempos_espera)
maximo_espera = np.max(tiempos_espera)
minimo_espera = np.min(tiempos_espera)

print(f"\nEstadísticas de los tiempos de espera:")
print(f"Media: {media_espera:.2f} minutos")
print(f"Mediana: {mediana_espera:.2f} minutos")
print(f"Máximo: {maximo_espera:.2f} minutos")
print(f"Mínimo: {minimo_espera:.2f} minutos")


plt.hist(tiempos_espera, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Tiempos de Espera en el Mostrador de Servicio')
plt.xlabel('Tiempo de espera (minutos)')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()