import numpy as np
from PIL import Image

def rysuj_ramki_w_obrazie(tab_obrazu, grubosc, odstep = 0):
    h, w = tab_obrazu.shape
    start = 0
    while start < min(h, w) / 2:
        for i in range(start, h - start):
            if start + grubosc < h:
                for j in range(start, grubosc + start):
                    tab_obrazu[i][j] = 0
                for j in range(w - grubosc - start, w - start):
                    tab_obrazu[i][j] = 0
        for i in range(start, w - start):
            if start + grubosc < w:
                for j in range(start, grubosc + start):
                    tab_obrazu[j][i] = 0
                for j in range(h - grubosc - start, h - start):
                    tab_obrazu[j][i] = 0
        if odstep == 0:
            tab = tab_obrazu.astype(bool)
            return Image.fromarray(tab)
        else:
            start += odstep + grubosc
    tab = tab_obrazu.astype(bool)
    return Image.fromarray(tab)

image = Image.open("inicjaly.bmp")
tablica_obrazu = np.asarray(image, dtype=bool) * 1

ramki5 = rysuj_ramki_w_obrazie(tablica_obrazu, grubosc=5)
ramki10 = rysuj_ramki_w_obrazie(tablica_obrazu, grubosc=10)

ramki5.save("ramka5.bmp")
ramki10.save("ramka10.bmp")