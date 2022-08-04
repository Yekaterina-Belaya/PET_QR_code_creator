import qrcode
import qrcode.image.pil

data = "https://i.pinimg.com/564x/80/5d/a9/805da9797b22f037b7e4f7d56b47e7df.jpg"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = "blue", back_color = "white")

#img = qrcode.make(data)

img.save("C:/Users/belos/Desktop/бэк/my_qrcode_styled.png")