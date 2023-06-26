import plotly.express as px
import os

ruta = '/'

contenidos = os.listdir(ruta)
print(contenidos)
carpetas = []
padres = []
tamaños = []

for contenido in contenidos:
    carpetas.append(contenido)
    padres.append("/")
    tamaños.append(5)


data = dict(
    character=carpetas,
    parent=padres,
    value=tamaños)

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()
