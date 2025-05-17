
# 🖼️ Plataforma Web de Filtros com PIL

## 📌 Descrição

Esta é uma aplicação web desenvolvida com **Flask** e **Pillow (PIL)** que permite ao usuário **enviar uma imagem** e aplicar diferentes filtros de processamento, como:

- Negativo
- Mediana
- Gaussiano
- Filtro personalizado (realce de bordas)

As imagens processadas podem ser visualizadas lado a lado com a original e baixadas com um clique.

---

## 🚀 Como usar

### 1. Clone o repositório (ou baixe os arquivos)
```bash
git clone https://github.com/Marcondes05/CG-7-P-Trabalho01.git
cd CG-7-P-Trabalho01

```

### 2. Crie e ative o ambiente virtual

**Linux/macOS:**
```bash
python3 -m venv env
source env/bin/activate
```

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install flask pillow
```

### 4. Estrutura do Projeto

```
.
├── app.py                  # Aplicação principal Flask
├── filtros.py              # Lógica de processamento de imagem
├── static/
│   ├── uploads/            # Imagens enviadas
│   ├── processed/          # Imagens com filtro
│   └── style.css           # Estilos da página
├── templates/
│   └── index.html          # Página HTML principal
└── README.md               # Este arquivo
```


### 5. Execute o servidor Flask
```bash
python app.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pillow (PIL)](https://python-pillow.org/)

---

## 💡 Melhorias Futuras

- Adicionar novos filtros (ex: preto e branco, sépia, pixelização)
- Suporte a múltiplas imagens por vez
- Deploy em nuvem (Heroku, Render, etc.)
- Histórico de imagens processadas por sessão

---

## 👤 Autor

Desenvolvido por **Marcondes**.  
Sinta-se à vontade para contribuir ou sugerir melhorias! 🚀
