# Importing libraries
import qrcode 
from tkinter import *
from tkinter import filedialog


# GUI
screen = Tk()
title = screen.title("QR Code Generator")
canvas = Canvas(screen, width = 800, height = 600)
canvas.pack()




# Defining a function to generate the QR code
def generate_qrcode (url_to_convert):

    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRECT_M, 
        box_size = 10, 
        border = 4
    )

    qr.add_data(url_to_convert)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('qr_img.png')


# Rendering GUI
screen.mainloop()

# Calling the function to generate the image
# generate_qrcode('www.google.com')