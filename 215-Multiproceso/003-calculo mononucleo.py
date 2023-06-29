import multiprocessing

nucleos = multiprocessing.cpu_count()

for i in range(nucleos):
    print("voy a usar un núcleo")

numero = 1.00000000034

for i in range(0,1000000000):
    numero *= 1.000000000054

print("ya he acabado")
