from PIL import Image, ImageFilter

# Filtro negativo
def filtro_negativo(img):
    matriz = img.load()
    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            pixel = (
                255 - matriz[i, j][0],
                255 - matriz[i, j][1],
                255 - matriz[i, j][2]
            )
            matriz[i, j] = pixel
    return img

# Filtro escala de cinza
def filtro_escala_cinza(img):
    matriz = img.load()
    largura, altura = img.size
    for i in range(largura):
        for j in range(altura):
            media = sum(matriz[i, j]) // 3
            pixel = (media, media, media)
            matriz[i, j] = pixel
    return img

# Filtro mediana
def filtro_mediana(img):
    return img.filter(ImageFilter.MedianFilter(size=3))

# Filtro gaussiano
def filtro_gaussiano(img, radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))
