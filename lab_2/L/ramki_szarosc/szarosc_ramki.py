import numpy as np
from PIL import Image


def rysuj_szare_ramki_w_obrazie(h, w, grubosc, odstep = 0, odcien = 0):
    tab_obrazu = np.full((h, w), 255, dtype=np.uint8)
    start = 0
    odcien = np.uint8(odcien)
    while start < min(h, w) / 2:
        for i in range(start, h - start):
            if start + grubosc < h:
                for j in range(start, grubosc + start):
                    tab_obrazu[i][j] = odcien
                for j in range(w - grubosc - start, w - start):
                    tab_obrazu[i][j] = odcien
        for i in range(start, w - start):
            if start + grubosc < w:
                for j in range(start, grubosc + start):
                    tab_obrazu[j][i] = odcien
                for j in range(h - grubosc - start, h - start):
                    tab_obrazu[j][i] = odcien
        if odstep == 0:
            tab = tab_obrazu.astype(np.uint8)
            return Image.fromarray(tab)
        else:
            start += odstep + grubosc
        tab = tab_obrazu.astype(np.uint8)
    tab = tab_obrazu.astype(np.uint8)
    return Image.fromarray(tab)

ramki_szare = rysuj_szare_ramki_w_obrazie(h=320, w=480, grubosc=20, odstep=20, odcien=80)
ramki_szare_negatyw = Image.fromarray(255 - np.asarray(ramki_szare))
ramki_szare.save("obraz1_2.png")
ramki_szare_negatyw.save("obraz1_2N.png")

