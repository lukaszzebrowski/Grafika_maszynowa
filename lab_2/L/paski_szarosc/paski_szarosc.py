import numpy as np
from PIL import Image


def rysuj_szare_paski(h, w, grubosc):
    tab_obrazu = np.zeros((h, w), dtype=np.uint8)
    start = 0
    odcien = np.uint8(255)
    while start < max(h, w):
        for i in range(0, h):
            if start + grubosc <= w:
                for j in range(start, grubosc + start):
                    tab_obrazu[i][j] = odcien
        start += grubosc
        if odcien < 0:
            odcien = np.uint8(255)
        else:
            odcien = np.uint8(odcien - max(h, w) // grubosc)
    tab = tab_obrazu.astype(np.uint8)
    return Image.fromarray(tab)

ramki_szare = rysuj_szare_paski(h=320, w=480, grubosc= 20)
ramki_szare_negatyw = Image.fromarray(255 - np.asarray(ramki_szare))
ramki_szare.save("obraz1_1.png")
ramki_szare_negatyw.save("obraz1_1N.png")
