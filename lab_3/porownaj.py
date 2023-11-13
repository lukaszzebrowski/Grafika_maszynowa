import numpy as np
from PIL import Image

def pozyskaj_r(image):
    r = image[:, :, 0]
    return r

def pozyskaj_g(image):
    g = image[:, :, 1]
    return g

def pozyskaj_b(image):
    b = image[:, :, 2]
    return b

def porownaj(image1, image2):
    tab_image1 = np.array(image1)
    tab_image2 = np.array(image2)

    counter_r = 0
    counter_g = 0
    counter_b = 0

    if tab_image1.shape != tab_image2.shape:
        print("Tablice obrazów różnią się rozmiarem")
    else:
        for i in range(tab_image1.shape[0]):
            for j in range(tab_image2.shape[1]):
                if pozyskaj_r(tab_image1)[i][j] == pozyskaj_r(tab_image2)[i][j]:
                    continue
                else:
                    counter_r += 1
                if pozyskaj_g(tab_image1)[i][j] == pozyskaj_g(tab_image2)[i][j]:
                    continue
                else:
                    counter_g += 1
                if pozyskaj_b(tab_image1)[i][j] == pozyskaj_b(tab_image2)[i][j]:
                    continue
                else:
                    counter_b += 1

        print(f"Ilość różnic w r: {counter_r}")
        print(f"Ilość różnic w g: {counter_g}")
        print(f"Ilość różnic w b: {counter_b}")