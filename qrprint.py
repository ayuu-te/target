import qrcode
from PIL import Image
# img = qrcode.make("https://www.udemy.com/course/full-stack-ai-with-python/learn/lecture/52004391#overview")
# img.save("qrcode.png")
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://www.udemy.com/course/full-stack-ai-with-python/learn/lecture/52004391#overview")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("qrcode.png")