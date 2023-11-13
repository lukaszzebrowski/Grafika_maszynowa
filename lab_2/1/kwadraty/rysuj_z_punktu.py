import numpy as np
from PIL import Image

def kwadraty(h, w, h_start, w_start):
    tab_obrazu = np.ones((h, w))
    h, w = tab_obrazu.shape
    for i in range(h_start, -1, -1):
        for j in range(w_start, -1, -1):
            tab_obrazu[i][j]=0
    for i in range(h_start, h):
        for j in range(w_start, w):
            tab_obrazu[i][j]=0
    tab = tab_obrazu.astype(bool)
    return Image.fromarray(tab)

figury = kwadraty(h=320, w=480, h_start=50, w_start= 100)
figury.save("rysuj_z_punktu.png")
