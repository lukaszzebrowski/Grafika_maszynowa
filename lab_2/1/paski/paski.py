import numpy as np
from PIL import Image


def rysuj_paski_w_obrazie(h, w, grubosc, odstep = 10):
    tab_obraz = np.ones((h, w))
    start = 0
    while start < max(h, w):
        for i in range(0, h):
            if start + grubosc < w:
                for j in range(start, grubosc + start):
                    tab_obraz[i][j] = 0
        start += odstep + grubosc
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)


paski = rysuj_paski_w_obrazie(h=320, w=480, grubosc=20, odstep=20)
paski.save("paski.png")
