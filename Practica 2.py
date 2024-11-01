import numpy as np
import matplotlib.pyplot as plt


lambda_llegada = 1 / 15  
duracion_dia = 12 * 60  


tiempos_entre_llegadas = np.random.exponential(1 / lambda_llegada, duracion_dia)


tiempos_acumulados = np.cumsum(tiempos_entre_llegadas)


tiempos_acumulados = tiempos_acumulados[tiempos_acumulados <= duracion_dia]


print("Tiempos entre llegadas (minutos):", tiempos_entre_llegadas)
print("Tiempos acumulados de llegada (minutos):", tiempos_acumulados)


plt.plot(tiempos_acumulados, marker='o', linestyle='-', color='skyblue')
plt.title('Tiempos Acumulados de Llegada de Vehículos Eléctricos')
plt.xlabel('Número de Llegadas')
plt.ylabel('Tiempo Acumulado (minutos)')
plt.axhline(y=duracion_dia, color='r', linestyle='--', label='12 Horas')
plt.legend()
plt.grid()
plt.show()