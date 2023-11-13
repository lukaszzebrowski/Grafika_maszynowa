from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint
from time import time
# plt.switch_backend('TkAgg')

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

def odkoduj(image1, image2):
    tab_image1 = np.array(image1)
    tab_image2 = np.array(image2)
    odkodowana = np.ones(tab_image2.shape, dtype=np.uint8)

    for i in range(tab_image1.shape[0]):
        for j in range(tab_image2.shape[1]):
            if np.array_equal(tab_image1[i][j], tab_image2[i][j]):
                odkodowana[i][j] = 0
            else:
                odkodowana[i][j] = 255
    reultat = Image.fromarray(odkodowana)
    return reultat


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")
    plt.show()

def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

diff = Image.open("diff.png")

statystyki(diff)

rysuj_histogram_RGB(diff)
print("*" * 100)

counter = 1
for i in range(0, 21, 5):
    start = time()
    zlicz_suma, procent_suma = zlicz_roznice_suma_RGB(diff, i)
    zlicz_srednia, procent_srednia = zlicz_roznice_srednia_RGB(diff, i)
    print(f"liczba niepasujących pikseli z funkcji zlicz_roznice_suma_RGB()\n "
          f"wywołanej z współczynnikiem {i}: {zlicz_suma}")
    print(f"procent niepasujących pikseli z funkcji zlicz_roznice_suma_RGB()\n "
          f"wywołanej z współczynnikiem {i}: {procent_suma}")
    print(f"liczba niepasujących pikseli z funkcji zlicz_roznice_srednia_RGB()\n "
          f"wywołanej z współczynnikiem {i}: {zlicz_srednia}")
    print(f"procent niepasujących pikseli z funkcji zlicz_roznice_srednia_RGB()\n "
          f"wywołanej z współczynnikiem {i}: {procent_srednia}")

    print(f"Pętla nr. {counter}: Czas: {round(time() - start, 2)}")
    counter += 1
    print("*" * 100)

image = Image.open("obraz.jpg")
print("Obraz oryginalny")
statystyki(image)

print('*' * 100)

for i in range(1, 6):
    image.save(f"obraz{i}.jpg")
    image = Image.open(f"obraz{i}.jpg")

image = Image.open("obraz.jpg")
image4 = Image.open("obraz4.jpg")
image5 = Image.open("obraz5.jpg")

print("Obraz po 4 zapisach")
statystyki(image4)

print('*' * 100)
print("Obraz po 5 zapisach")
statystyki(image5)


porownaj(image4, image5)

zakodowany = Image.open("zakodowany2.bmp")
oryginal = Image.open("jesien.jpg")

odkoduj(zakodowany, oryginal).save("kod2.bmp")




