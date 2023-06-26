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
    if os.path.isfile("/"+contenido):
        file_size = os.path.getsize("/"+contenido)
        tamaños.append(file_size)
    else:
        tamaños.append(5)

print(tamaños)

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
