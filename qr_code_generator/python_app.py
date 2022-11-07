# install all the libraries needed
# create funcation that collects a text and converts it to qrcode 
# save the qrcode as an image 
# run the funcation 

import qrcode

def generete_grcode(text):
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", black_color="white")
    img.save("qrimg.png")


url = input("Enter the website: ")
generete_grcode(str(url))
