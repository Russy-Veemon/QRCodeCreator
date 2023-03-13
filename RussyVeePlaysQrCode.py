import qrcode

website_link = 'https://www.youtube.com/channel/UC9Yu2R8AtrllEXStKfGrdFg'

# Next, we want to create an instance of qrcode. Since it's a Python library, we can call the package constructor to create a qrcode object, customized to our specifications.

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

# The version parameter is an integer from 1 to 40 that controls the size of the QR code.
# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be.

# As an exercise, try taking in these parameters as input, and explaining to the user how to set this up, so they can create the QR code to their own specifications.
# something to add to another app so that it is easy to get

qr.add_data(website_link)
qr.make()

# save this created QR code in an img pillow object using qr.make_image():

img = qr.make_image(fill_color = 'black', back_color = 'white')
# Setting the line color fill_color to black.
# Setting the background color back_color to white.

img.save('youtube_qr.png')
# storing the file onto the machine