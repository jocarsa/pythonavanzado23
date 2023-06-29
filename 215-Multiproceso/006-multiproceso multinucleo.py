import multiprocessing

nucleos = multiprocessing.cpu_count()

for i in range(nucleos):
    print("voy a usar un núcleo")

def calcula():
    numero = 1.00000000034
    for i in range(0,1000000000):
        numero *= 1.000000000055
    print("hilo finalizado")

if __name__ == '__main__':
    procesos = []
    for _ in range(nucleos):
        proceso = multiprocessing.Process(target=calcula)
        procesos.append(proceso)
        proceso.start()


    for proceso in procesos:
        proceso.join()

