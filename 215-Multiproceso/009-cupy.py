import cupy as cp

def calcula():
    numero = cp.float64(1.00000000034)
    for i in range(0, 1000000000):
        numero *= cp.float64(1.000000000055)
    print("hilo finalizado")


with cp.cuda.Device(0):
    calcula()
    calcula()
    calcula()
