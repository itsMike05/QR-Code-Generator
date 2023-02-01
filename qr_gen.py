# Importing libraries
import qrcode 

# Defining a function to generate the QR code

def generate_qrcode (url_to_convert):

    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRERT_M, 
        box_size = 10, 
        border = 4
    )

    qr.add_data(url_to_convert)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('qr_img.png')

# Calling the function

generate_qrcode('www.google.com')