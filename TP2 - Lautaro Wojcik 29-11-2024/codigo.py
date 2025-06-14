import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

"""
necesito graficos almenos 3 no todos graficos de barras:
    un grafico pie marcando el porcentaje de respuestas ?
    arma mas popular
    frecuencia de ocurrencias de armas
"""

#Get the csv from drive
dataFrame = pd.read_csv("https://docs.google.com/spreadsheets/d/" + 
                        "11s09p5V1ZuJTbNWDgcquKHR4MMCUoa5hbKxJvVfpx5I" + 
                        "/export?format=csv")

#Subcategoria a
dataFrame["sub a"] = dataFrame["Armas de Alcance "]
dataFrame["sub a"] = dataFrame["sub a"].combine_first(dataFrame["Armas de Combate Cuerpo a Cuerpo "])
dataFrame["sub a"] = dataFrame["sub a"].combine_first(dataFrame["Armas Especializadas "])

#Subcategoria b
dataFrame["sub b"] = dataFrame["Armas Proyectiles "]
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas de Fuego "])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas de Energía (Futuristas)"])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Artillería y Explosivos "])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Proyectiles Aéreos "])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas Cortantes (Armas Afiladas)"])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas Contundentes (Armas de Golpe)"])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas Flexibles "])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas No Convencionales"])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas de Asedio (Históricas/Medievales)"])
dataFrame["sub b"] = dataFrame["sub b"].combine_first(dataFrame["Armas Nucleares y Biológicas "])

######################################################################## Arma mas popular
"""
tiposGeneralesDeArmasOcurrencias = dataFrame["sub b"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(tiposGeneralesDeArmasOcurrencias, labels=tiposGeneralesDeArmasOcurrencias.index, autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
plt.title("Popularidad de armas", fontsize=16)

plt.show()
"""
################################################################### En que dia se respondio mas a la encuesta
"""
#convert datetimes to dates
dataFrame["Marca temporal"] = dataFrame["Marca temporal"].apply(lambda x: x.split(" ")[0])
respuestasXDias = dataFrame["Marca temporal"].value_counts()
respuestasXDias = respuestasXDias.sort_index()

respuestasXDias.plot(kind="bar", color="skyblue")

plt.title("Respuestas por Dia", fontsize=16)
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Respuestas", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
######################################################################
"""
# Create a sunburst plot to represent the tree of responses
fig = px.sunburst(dataFrame, path=["Árbol de Clasificación de Armas ", "sub a", "sub b"], title="Distribuicion de respuestas")
fig.update_traces(textinfo="label+value", textfont=dict(size=18)) 
fig.show()
"""