import numpy as np
from PIL import Image
from random import randint


def rysuj_ramki_rgb_w_obrazie(h, w, grubosc, odstep = 0):
    tab_rgb = np.full((h, w, 3), [0, 0, 0], dtype=np.uint8)
    start = 0
    while start < min(h, w) / 2:
        kolor_r = randint(0, 256)
        kolor_g = randint(0, 256)
        kolor_b = randint(0, 256)
        for i in range(start, h - start):
            if start + grubosc < h:
                for j in range(start, grubosc + start):
                    tab_rgb[i][j] = [kolor_r, kolor_g, kolor_b]
                for j in range(w - grubosc - start, w - start):
                    tab_rgb[i][j] = [kolor_r, kolor_g, kolor_b]
        for i in range(start, w - start):
            if start + grubosc < w:
                for j in range(start, grubosc + start):
                    tab_rgb[j][i] = [kolor_r, kolor_g, kolor_b]
                for j in range(h - grubosc - start, h - start):
                    tab_rgb[j][i] = [kolor_r, kolor_g, kolor_b]
        if odstep == 0:
            tab = tab_rgb.astype(np.uint8)
            return Image.fromarray(tab)
        else:
            start += odstep + grubosc
        tab = tab_rgb.astype(np.uint8)
    tab = tab_rgb.astype(np.uint8)
    return Image.fromarray(tab)

ramki_rgb = rysuj_ramki_rgb_w_obrazie(h=320, w=480, grubosc=20, odstep=20)
ramki_rgb_negatyw = Image.fromarray(255 - np.asarray(ramki_rgb))
ramki_rgb.save("obraz2_2.png")
ramki_rgb.save("obraz2_2.jpg")
ramki_rgb_negatyw.save("obraz2_2N.png")
ramki_rgb_negatyw.save("obraz2_2N.jpg")
