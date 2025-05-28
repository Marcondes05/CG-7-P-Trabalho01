import os
from flask import Flask, render_template, request, url_for
from filtros import *

app = Flask(__name__)

# Configuração das pastas
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Cria as pastas se não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Mapeamento dos nomes dos filtros para as funções correspondentes
FILTROS_DISPONIVEIS = {
    'negativo': filtro_negativo,
    'mediana': filtro_mediana,
    'gaussiano': filtro_gaussiano,
    'cinza': filtro_escala_cinza,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        filtro = request.form['filtro']
        if file and filtro in FILTROS_DISPONIVEIS:
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(caminho_imagem)

            img = Image.open(caminho_imagem).convert('RGB')
            img_processada = FILTROS_DISPONIVEIS[filtro](img.copy())

            nome_saida = os.path.splitext(file.filename)[0] + f'_{filtro}.png'
            caminho_saida = os.path.join(app.config['PROCESSED_FOLDER'], nome_saida)
            img_processada.save(caminho_saida)

            return render_template('index.html',
                                   original_image=url_for('static', filename='uploads/' + file.filename),
                                   processed_image=url_for('static', filename='processed/' + nome_saida),
                                   filtro_aplicado=filtro)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
