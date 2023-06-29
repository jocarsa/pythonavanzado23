import multiprocessing
import time
from PIL import Image


imagen = Image.open("josevicenteresumen2.jpg")
pixeles = list(imagen.getdata())

print(len(pixeles))

sublistas = [pixeles[i:i+int(len(pixeles)/6)] for i in range(0, len(pixeles), int(len(pixeles)/6))]

print(len(sublistas))

for sublista in sublistas:
    print(len(sublista))

antes = int(time.time())
nucleos = multiprocessing.cpu_count()

for i in range(nucleos):
    print("voy a usar un núcleo")

def calcula():
    numero = 1.00000000034
    for i in range(0,100000000):
        numero *= 1.000000000055
    print("hilo finalizado")

def invierte(datos):
    listalocal = []
    for dato in datos:
        dato = (255-dato[0],255-dato[1],255-dato[2])
        listalocal.append(dato)
    print("inversión finalizada")
    return listalocal

union = []
for sublista in sublistas:    
    union.extend(invierte(sublista))

print("union:")


print(len(union))
for i in range(0,len(pixeles)):
    pixeles[i] = union[i]


imagen.putdata(pixeles)
imagen.show()



despues = int(time.time())
print(despues-antes)









