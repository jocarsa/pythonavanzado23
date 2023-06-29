import multiprocessing

nucleos = multiprocessing.cpu_count()

for i in range(nucleos):
    print("voy a usar un núcleo")

def calcula():
    numero = 1.00000000034
    for i in range(0,100000000):
        numero *= 1.000000000055
    print("hilo finalizado")

calcula()
calcula()
calcula()
calcula()

