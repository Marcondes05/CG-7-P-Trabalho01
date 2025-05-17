from PIL import Image, ImageFilter, ImageOps
import os

def aplicar_filtro(caminho_imagem, filtro, pasta_saida):
    """
    Aplica um filtro de imagem com base na opção escolhida.

    Parâmetros:
    - caminho_imagem: caminho da imagem original
    - filtro: tipo de filtro a aplicar ('negativo', 'mediana', 'gaussiano', 'personalizado')
    - pasta_saida: pasta onde a imagem processada será salva

    Retorna:
    - caminho completo da imagem processada
    """

    # Abre a imagem original
    img = Image.open(caminho_imagem)

    # Define o nome do arquivo de saída com o nome do filtro aplicado
    nome_saida = os.path.basename(caminho_imagem).split('.')[0] + f'_{filtro}.png'
    caminho_saida = os.path.join(pasta_saida, nome_saida)

    # Aplica o filtro correspondente
    if filtro == 'negativo':
        # Inverte as cores (necessário converter para RGB antes)
        img = ImageOps.invert(img.convert('RGB'))

    elif filtro == 'mediana':
        # Aplica filtro da mediana (reduz ruídos)
        img = img.filter(ImageFilter.MedianFilter(size=3))

    elif filtro == 'gaussiano':
        # Aplica desfoque gaussiano com raio 5
        img = img.filter(ImageFilter.GaussianBlur(radius=5))

    elif filtro == 'personalizado':
        # Aplica um filtro de detecção de bordas com kernel definido
        kernel = ImageFilter.Kernel(
            (3, 3),
            [-1, -1, -1,
             -1, 8, -1,
             -1, -1, -1],
            scale=1
        )
        img = img.filter(kernel)

    # Salva a imagem modificada na pasta de saída
    img.save(caminho_saida)

    # Retorna o caminho da imagem processada
    return caminho_saida
