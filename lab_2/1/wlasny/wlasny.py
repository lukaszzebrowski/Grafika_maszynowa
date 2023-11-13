import numpy as np
from PIL import Image


def rysuj_ramki_w_obrazie(h, w, grubosc, odstep = 0):
    tab_obrazu = np.ones((h, w))
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

ramki = rysuj_ramki_w_obrazie(h=2000, w=2000, grubosc=5, odstep=5)
ramki.save("wlasny.bmp")
