import multiprocessing
import time
from PIL import Image


imagen = Image.open("josevicenteresumen.jpg")
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

##if __name__ == '__main__':
##    procesos = []
##    for _ in range(nucleos):
##        proceso = multiprocessing.Process(target=calcula)
##        procesos.append(proceso)
##        proceso.start()
##
##
##    for proceso in procesos:
##        proceso.join()


despues = int(time.time())
print(despues-antes)









