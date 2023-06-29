import multiprocessing

nucleos = multiprocessing.cpu_count()

for i in range(nucleos):
    print("voy a usar un núcleo")
