import plotly.express as px
import os

carpetas = []
padres = []
tamaños = []

def count_levels(route):
    print("La ruta es:"+str(route))
    levels = str(route).split('/')
    # Remove empty parts (e.g., leading/trailing slashes)
    levels = [level for level in levels if level]
    return len(levels)

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def recursivo(ruta):
    global profundidad
    contenidos = os.listdir(ruta)
    for contenido in contenidos:
        
        padres.append(ruta)
        if os.path.isfile(ruta+"/"+contenido):
            carpetas.append(ruta+contenido)
            file_size = os.path.getsize(ruta+"/"+contenido)
            tamaños.append(file_size)
        else:
            carpetas.append(ruta+contenido)
            file_size = get_folder_size(ruta+"/"+contenido)
            tamaños.append(file_size)
            if count_levels(ruta+"/"+contenido+"/") - profundidad <= 1: 
                recursivo(ruta+"/"+contenido+"/")

ruta = '/jv/'
profundidad = count_levels(ruta)

recursivo(ruta)

print(carpetas)
print(padres)
print(tamaños)

data = dict(
    character=carpetas,
    parent=padres,
    value=tamaños)
print(data)

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()
