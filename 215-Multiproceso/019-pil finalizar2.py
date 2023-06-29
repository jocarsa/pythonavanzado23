import multiprocessing
import time
from PIL import Image


imagen = Image.open("josevicenteresumen2.jpg")
pixeles = list(imagen.getdata())

print(len(pixeles))

nucleos = multiprocessing.cpu_count()*10
sublistas = [pixeles[i:i+int(len(pixeles)/nucleos)] for i in range(0, len(pixeles), int(len(pixeles)/nucleos))]

print(len(sublistas))

for sublista in sublistas:
    print(len(sublista))

antes = int(time.time())

union = []
for i in range(nucleos):
    print("voy a usar un núcleo")


def invierte(datos):
    global union
    listalocal = []
    for dato in datos:
        dato = (255-dato[0],255-dato[1],255-dato[2])
        listalocal.append(dato)
    print("inversión finalizada")
    #return listalocal
    union.extend(listalocal)


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

            imagen.putdata(union)
            imagen.show()
            despues = int(time.time())
            print(despues-antes)









