import barcode
from barcode.writer import ImageWriter

ean = barcode.get_barcode_class('ean13')
barcode_value = '5901234123457'
imagen = ean(barcode_value, writer=ImageWriter())

archivo = imagen.save('barcode')
