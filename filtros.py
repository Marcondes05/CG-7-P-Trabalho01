from PIL import Image, ImageFilter, ImageChops
import numpy as np
import random
import math

# Filtro negativo
def filtro_negativo(img):
    matriz = img.load()
    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            pixel = ((255 - matriz[i,j][0]), (255 - matriz[i,j][1]), (255 - matriz[i,j][2]))
            matriz[i,j] = pixel
    return img

# Filtro escala de cinza
def filtro_escala_cinza(img):
    matriz = img.load()
    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            media = int((matriz[i,j][0] + matriz[i,j][1] + matriz[i,j][2]) / 3)
            pixel = (media, media, media)
            matriz[i,j] = pixel
    return img

# Filtro preto e branco
def filtro_preto_branco(img):
    matriz = img.load()
    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            media = int((matriz[i,j][0] + matriz[i,j][1] + matriz[i,j][2]) / 3)
            if media < 128:
                pixel = (0, 0, 0)
            else:
                pixel = (255, 255, 255)
            matriz[i,j] = pixel
    return img

# Filtro mediana
def filtro_mediana(img):
    return img.filter(ImageFilter.MedianFilter(size=3))

# Filtro gaussiano
def filtro_gaussiano(img, radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))
