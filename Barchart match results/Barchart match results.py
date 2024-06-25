#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Barchart 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read .csv
datos = pd.read_csv(r'C:\Users\josea\Desktop\ANALISIS CALAVERA Y ABR\VISUALIZACIONES\CLASIFICACION_2ANDALUZA.csv', delimiter=';')

# Seaborn configuration and chart creation
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plotting stacked bars manually with matplotlib
plt.bar(datos['Equipos'], datos['Ganados'], color='lightgreen', label='Ganados', width=0.5)
plt.bar(datos['Equipos'], datos['Empatados'], color='lightyellow', label='Empatados', bottom=datos['Ganados'], width=0.5)
plt.bar(datos['Equipos'], datos['Perdidos'], color='lightcoral', label='Perdidos', bottom=datos['Ganados'] + datos['Empatados'], width=0.5)

# Config labels and chart desing
plt.xlabel('Equipos')
plt.ylabel('Cantidad de partidos Jugados')
plt.title('Resultados de los partidos de cada equipo')
plt.xticks(rotation=45, ha='right')
plt.yticks(range(1, 16))
plt.legend()
plt.tight_layout()
plt.show()

