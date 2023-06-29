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
    piscina = multiprocessing.Pool(processes=6)
    piscina.apply_async(calcula)
    piscina.close()
    piscina.join()

