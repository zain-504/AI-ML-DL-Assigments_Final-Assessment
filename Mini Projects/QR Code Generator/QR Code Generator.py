# import qrcode 

# data = input("Enter Text or URL for QR Code: ")
# filename = input("Please Enter the Name of your File: ")

# qr = qrcode.make(data)

# qr.save(filename + ".png")

# print("QR Code generated successfully!")
# print("Thank You for using My_QR Code.apk")


# QR Code Generator in Python

import qrcode

# Take input from user
data = input("Enter text or URL for QR Code: ")

# Create QR Code
qr = qrcode.make(data)

# Save QR Code image
qr.save("my_qrcode.png")

print("QR Code generated successfully!")
print("Saved as my_qrcode.png")