import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )

datos = "Mastermedia"

qr.add_data(datos)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.show()
#imagen.save("qrcode.png")
