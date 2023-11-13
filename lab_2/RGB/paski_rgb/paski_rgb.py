import numpy as np
from PIL import Image
from random import randint


def rysuj_paski_rgb(h, w, grubosc):
    tab_rgb = np.full((h, w, 3), [0, 0, 0], dtype=np.uint8)
    start = 0

    while start < max(h, w):
        kolor_r = randint(0, 256)
        kolor_g = randint(0, 256)
        kolor_b = randint(0, 256)
        for i in range(0, h):
            if start + grubosc <= w:
                for j in range(start, grubosc + start):
                    tab_rgb[i][j] = [kolor_r, kolor_g, kolor_b]
        start += grubosc
    tab = tab_rgb.astype(np.uint8)
    return Image.fromarray(tab)


paski_rgb = rysuj_paski_rgb(h=320, w=480, grubosc= 20)
paski_rgb_negatyw = Image.fromarray(255 - np.asarray(paski_rgb))
paski_rgb.save("obraz2_1.png")
paski_rgb.save("obraz2_1.jpg")
paski_rgb_negatyw.save("obraz2_1N.png")
paski_rgb_negatyw.save("obraz2_1N.jpg")