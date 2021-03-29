import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('MY DATA')
qr.make(fit=True)
# YOU CAN CHANGE THE COLORS IF YOU WANT
img = qr.make_image(fill_color="black", back_color="white")
img.save('1.png')
