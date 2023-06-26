import plotly.express as px
import os

ruta = '/xampp'

contenidos = os.listdir(ruta)
print(contenidos)
carpetas = []
padres = []
tamaños = []

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

for contenido in contenidos:
    carpetas.append(contenido)
    padres.append(ruta)
    if os.path.isfile(ruta+"/"+contenido):
        file_size = os.path.getsize(ruta+"/"+contenido)
        tamaños.append(file_size)
    else:
        file_size = get_folder_size(ruta+"/"+contenido)
        tamaños.append(file_size)

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
