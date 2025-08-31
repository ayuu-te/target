import qrcode as qr
img = qr.make("https://www.udemy.com/course/full-stack-ai-with-python/learn/lecture/52004391#overview")
img.save("qrcode.png")