import qrcode

data = "https://github.com/dipson54"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("dipson54.png")
