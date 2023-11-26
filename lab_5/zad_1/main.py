from PIL import Image


def put_initials(image, initials_image, m, n, color):
    w, h = initials_image.size
    for i in range(h):
        for j in range(w):
            if initials_image.getpixel((j, i)) == 255:
                pass
            else:
                image.putpixel((m + j, n + i), color)

    return image


image_original = Image.open("obraz.jpg")
initials = Image.open("inicjaly.bmp")

image_copy = image_original.copy()

image_w, image_h = image_original.size

initials_w, initials_h = initials.size

image_initials = put_initials(image_original, initials, image_w - initials_w, image_h - initials_h, (255, 0, 0))
image_initials.save("obraz1.bmp")
