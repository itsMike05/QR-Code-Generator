# Importing libraries
import qrcode 
from tkinter import *
from tkinter import filedialog


def selectPath():
    path = filedialog.askdirectory()
    path_label.config(text = path)
    


# Defining a function to generate the QR code
def generateQRcode ():
    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRECT_M, 
        box_size = 10, 
        border = 4
    )
    
    url = link_field.get()
    create_path = path_label.cget("text")
    
    
    qr.add_data(url)
    qr.make(fit = True)
    # img = qr.make_image(fill_color = "black", back_color = "white")
    # img.save("qr_img.png")
    


# GUI
screen = Tk()
title = screen.title("QR Code Generator")
canvas = Canvas(screen, width = 600, height = 600)
canvas.pack()

# Logo

app_logo = PhotoImage(file = "logo.png")
app_logo = app_logo.subsample(1, 1)
canvas.create_image(300, 100, image = app_logo)

# Target link field 

link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter a link to convert: ", font = "Arial, 15")
canvas.create_window(300, 240, window = link_label)
canvas.create_window(300, 280, window = link_field)

# Selecting the image path with a select_button

path_label = Label(screen, text = "Choose a path for your image", font = "Arial, 15")
select_path_button = Button(screen, text = "Open File Explorer", command = selectPath)

canvas.create_window(300, 360, window = path_label)
canvas.create_window(300, 400, window = select_path_button)

# Create the QR code Button

create_button = Button(screen, text = "Generate QR Code", command = generateQRcode)

# Rendering GUI
screen.mainloop()

# Calling the function to generate the image
# generateQRcode('www.google.com')