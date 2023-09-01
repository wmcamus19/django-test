from PIL import Image
from pyzbar.pyzbar import decode

# Load the QR code image
qr_code_image = Image.open("test.png")

# Decode the QR code
decoded_objects = decode(qr_code_image)

# Extract and print the data
for obj in decoded_objects:
    print("Data:", obj.data.decode("utf-8"))
    print("Type:", obj.type)
