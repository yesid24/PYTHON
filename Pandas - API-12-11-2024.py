import pandas as pd
import matplotlib.pyplot as plt

# Crear el diccionario
dict_ = {'a': [11, 41, 31], 'b': [12, 22, 32]}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(dict_)

# Graficar los datos
df.plot(kind='bar')
plt.xlabel('Índice')
plt.ylabel('Valores')
plt.title('Gráfico de barras')
plt.show()

