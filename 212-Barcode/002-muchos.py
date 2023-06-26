import barcode
from barcode.writer import ImageWriter
import random
import os

try:
    os.mkdir("imagenes")
except:
    print("existe")

for i in range(0,100):
    codigo = random.randint(0,590123)
    codigoceros = str(codigo).zfill(12)
    ean = barcode.get_barcode_class('ean13')
    barcode_value = str(codigoceros)
    imagen = ean(barcode_value, writer=ImageWriter())

    archivo = imagen.save('imagenes/barcode'+str(codigoceros)+".png")
