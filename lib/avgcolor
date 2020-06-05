from PIL import Image
def avg_color(img):
    pixels = list(img.getdata())

    r = 0
    g = 0
    b = 0

    for i in pixels:
        r += i[0]
        g += i[1]
        b += i[2]

    size = img.width * img.height
    avg_r = int(r / size)
    avg_g = int(g / size)
    avg_b = int(b / size)

    return (avg_r, avg_g, avg_b)
