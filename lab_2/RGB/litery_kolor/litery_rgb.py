import numpy as np
from PIL import Image
from random import randint

def konwertuj_rgb(tab_obrazu):
    for i in range(tab_obrazu.shape[0]):
        for j in range(tab_obrazu.shape[1]):
            if np.array_equal(tab_obrazu[i][j], [1, 1, 1]):
                tab_obrazu[i][j] = [255, 255, 255]
            else:
                tab_obrazu[i][j] = [0, 0, 0]
    return tab_obrazu

def rysuj_paski_rgb(inicjaly_rgb, grubosc):
    start = 0
    while start < min(inicjaly_rgb.shape[0], inicjaly_rgb.shape[1]):
        kolor_r = randint(0, 256)
        kolor_g = randint(0, 256)
        kolor_b = randint(0, 256)
        for i in range(0, inicjaly_rgb.shape[1]):
            if start + grubosc <= inicjaly_rgb.shape[0]:
                for j in range(start, grubosc + start):
                    if np.array_equal(inicjaly_rgb[j][i], [0, 0, 0]):
                        inicjaly_rgb[j][i] = [kolor_r, kolor_g, kolor_b]
        start += grubosc
    return inicjaly_rgb


image = Image.open("inicjaly.bmp")

image_array = np.array(image, dtype=np.uint8)
image_rgb = np.stack((image_array, image_array, image_array), axis=-1)

obraz_rgb = Image.fromarray(rysuj_paski_rgb(konwertuj_rgb(image_rgb), 2))

obraz_rgb.save("inicjaly_jpg.jpg")
obraz_rgb.save("inicjaly_png.png")





