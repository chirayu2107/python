import qrcode


data = "https://www.primevideo.com/"

# Generate a QR code
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each QR code "box" (adjust as needed)
    border=4,     # Border size (adjust as needed)
)

qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it
img.save("qrcode.png")  # Save to a file
img.show()  # Display in default image viewer


