import qrcode
import os

try:
    os.mkdir("qrs")
except:
    print("ya existe")

nombres = ['Jose Vicente','Jose','Mariana','Ana','Raul','Rodrigo','Henry']

for nombre in nombres:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
        )

    datos = "https://jocarsa.com"

    qr.add_data(datos)
    qr.make(fit=True)

    imagen = qr.make_image(fill_color="black", back_color="white")
    #imagen.show()
    imagen.save("qrs/qrcode-"+nombre+".png")
