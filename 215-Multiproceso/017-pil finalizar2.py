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

def invierte(datos):
    listalocal = []
    for dato in datos:
        dato = (255-dato[0],255-dato[1],255-dato[2])
        listalocal.append(dato)
    print("inversión finalizada")
    return listalocal


if __name__ == '__main__':
    procesos = []
    for sublista in sublistas:
        proceso = multiprocessing.Process(target=invierte(sublista))
        procesos.append(proceso)
        proceso.start()
    semaforo = len(procesos)

    for proceso in procesos:
        proceso.join()
        print("el semaforo vale:"+str(semaforo))
        semaforo -= 1
        print("Un nucleo ha terminado pero el semaforo no ha acabado")
        if semaforo == 0:
            print("el proceso ha finalizado")
            union = []
            for sublista in sublistas:    
                union.extend(invierte(sublista))

            print("union:")

            imagen.putdata(pixeles)
            imagen.show()
            despues = int(time.time())
            print(despues-antes)









