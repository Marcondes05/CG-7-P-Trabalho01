import os
from flask import Flask, render_template, request, redirect, url_for
from filtros import aplicar_filtro  # Função para aplicar o filtro de imagem

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração dos diretórios de upload e processamento
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Cria as pastas se ainda não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Rota principal que aceita GET e POST
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']          # Obtém o arquivo enviado
        filtro = request.form['filtro']        # Obtém o filtro escolhido no formulário

        if file:
            # Caminho completo onde o arquivo será salvo
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(caminho_imagem)

            # Aplica o filtro e obtém o caminho da imagem processada
            imagem_processada = aplicar_filtro(caminho_imagem, filtro, app.config['PROCESSED_FOLDER'])

            # Renderiza a página com as imagens e o filtro aplicado
            return render_template('index.html',
                                   original_image=url_for('static', filename='uploads/' + file.filename),
                                   processed_image=url_for('static', filename='processed/' + os.path.basename(imagem_processada)),
                                   filtro_aplicado=filtro)  # <- Passa o nome do filtro para a template

    # Se for GET ou não houve imagem enviada ainda
    return render_template('index.html')

# Roda o servidor Flask em modo debug
if __name__ == '__main__':
    app.run(debug=True)
