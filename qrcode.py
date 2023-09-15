import qrcode


data = "https://github.com/chirayu2107"

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  
    border=4,     # Border size
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")  # Save to a file
img.show()
