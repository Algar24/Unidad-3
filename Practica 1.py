import numpy as np
import matplotlib.pyplot as plt
n = 20  
p = 0.70  


dias = 7
pedidos_satisfechos = np.random.binomial(n, p, dias)


print("Pedidos satisfechos por día:", pedidos_satisfechos)


plt.bar(range(1, dias + 1), pedidos_satisfechos, color='skyblue')
plt.title('Número de Pedidos Satisfechos por Día')
plt.xlabel('Día de la Semana')
plt.ylabel('Número de Pedidos Satisfechos')
plt.xticks(range(1, dias + 1))
plt.ylim(0, n) 
plt.axhline(y=np.mean(pedidos_satisfechos), color='r', linestyle='--', label='Media')
plt.legend()
plt.show()