import numpy as np
from PIL import Image


def odstep():
    print("-" * 30)


print("Wczytanie obrazka.")
picture = Image.open("../lab_2/1/ramka/inicjaly.bmp")

print("Informacje o obrazie:\n")
print("Tryb:", picture.mode)
print("Format:", picture.format)
print("Rozmiar:", picture.size)

odstep()

print("Wczytywanie obrazu do tablicy oraz pobieranie informacji o tablicach.")

picture_data = np.asarray(picture)

odstep()

print("Informacje o tablicy obrazu.\n")

print("Typ danych tablicy:", picture_data.dtype)
print("rozmiar tablicy:", picture_data.shape)
print("liczba elementow:", picture_data.size)
print("wymiar tablicy:", picture_data.ndim)
print("rozmiar wyrazu tablicy:", picture_data.itemsize)
print("Wartość piksela o współrzędnych [50, 30):", picture_data[30][50])
print("Wartość piksela o współrzędnych [90, 40):", picture_data[40][90])
print("Wartość piksela o współrzędnych [99, 0):", picture_data[0][99])

odstep()

print("Zmiana typu bool na int.")
picture_data_int = np.asarray(picture_data) * 1

odstep()

print("Tworzenie i zapisywanie do pliku.")

plik = "inicjaly.txt"

with open(plik, "w") as inicjaly_txt:
    for i in range(picture_data.shape[0]):
        for j in range(picture_data.shape[1]):
            inicjaly_txt.write(str(picture_data_int[i][j]) + " ")
        inicjaly_txt.write("\n")

odstep()

print("Informacje o tablicy wczytanej jako bool_.\n")

tablica_bool = np.loadtxt(plik, dtype=np.bool_)
print("Typ danych tablicy:", tablica_bool.dtype)
print("rozmiar tablicy:", tablica_bool.shape)
print("liczba elementow:", tablica_bool.size)
print("wymiar tablicy:", tablica_bool.ndim)
print("rozmiar wyrazu tablicy:", tablica_bool.itemsize)

print("Porównianie tablicy inicjaly.bmp z wczytaną tablicą jako bool z inicjaly.txt: ")

if picture_data.dtype == tablica_bool.dtype:
    print("picture_data_jpg.dtype == tablica_bool.dtype: ", True)
else:
    print("picture_data_jpg.dtype == tablica_bool.dtype: ", False)
if picture_data.shape == tablica_bool.shape:
    print("picture_data_jpg.shape == tablica_bool.shape: ", True)
else:
    print("picture_data_jpg.shape == tablica_bool.shape: ", False)
if picture_data.size == tablica_bool.size:
    print("picture_data_jpg.size == tablica_bool.size: ", True)
else:
    print("picture_data_jpg.size == tablica_bool.size: ", False)
if picture_data.ndim == tablica_bool.ndim:
    print("picture_data_jpg.ndim == tablica_bool.ndim: ", True)
else:
    print("picture_data_jpg.ndim == tablica_bool.ndim: ", False)
if picture_data.itemsize == tablica_bool.itemsize:
    print("picture_data_jpg.itemsize == tablica_bool.itemsize: ", True)
else:
    print("picture_data_jpg.itemsize == tablica_bool.itemsize: ", False)

odstep()

print("Informacje o tablicy wczytanej jako uint8.\n")

tablica_unit8 = np.loadtxt(plik, dtype=np.uint8)
print("Typ danych tablicy:", tablica_unit8.dtype)
print("rozmiar tablicy:", tablica_unit8.shape)
print("liczba elementow:", tablica_unit8.size)
print("wymiar tablicy:", tablica_unit8.ndim)
print("rozmiar wyrazu tablicy:", tablica_unit8.itemsize)

print("Porównianie tablicy inicjaly.bmp z wczytaną tablicą jako unit8 z inicjaly.txt: ")

if picture_data.dtype == tablica_unit8.dtype:
    print("picture_data_jpg.dtype == tablica_unit8.dtype: ", True)
else:
    print("picture_data_jpg.dtype == tablica_unit8.dtype: ", False)
if picture_data.shape == tablica_unit8.shape:
    print("picture_data_jpg.shape == tablica_unit8.shape: ", True)
else:
    print("picture_data_jpg.shape == tablica_unit8.shape: ", False)
if picture_data.size == tablica_unit8.size:
    print("picture_data_jpg.size == tablica_unit8.size: ", True)
else:
    print("picture_data_jpg.size == tablica_unit8.size: ", False)
if picture_data.ndim == tablica_unit8.ndim:
    print("picture_data_jpg.ndim == tablica_unit8.ndim: ", True)
else:
    print("picture_data_jpg.ndim == tablica_unit8.ndim: ", False)
if picture_data.itemsize == tablica_unit8.itemsize:
    print("picture_data_jpg.itemsize == tablica_unit8.itemsize: ", True)
else:
    print("picture_data_jpg.itemsize == tablica_unit8.itemsize: ", False)

odstep()

print("Tworzenie obrazu na podstawie tablicy unit8")

tablica_bmp = Image.fromarray(tablica_unit8)
tablica_bmp.show()
