# 🖼️ Aplicador de Filtros de Imagem com Flask

Este projeto é uma aplicação web simples feita com **Flask** que permite ao usuário enviar uma imagem e aplicar diversos filtros de processamento digital.

Filtros disponíveis:
- Negativo
- Mediana
- Gaussiano
- Escala de Cinza
- Preto & Branco

---

## 🚀 Como executar o projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```
> **Obs:** Caso não tenha um arquivo `requirements.txt`, instale manualmente:
```bash
pip install flask pillow numpy
```

### 4. Execute a aplicação:
```bash
python app.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Como testar

1. Acesse a interface web pelo navegador.
2. Clique em **"Escolher arquivo"** e selecione uma imagem do seu computador.
3. Escolha um filtro no menu suspenso.
4. Clique em **"Aplicar Filtro"**.
5. A imagem original e a imagem com o filtro aplicado serão exibidas lado a lado.
6. Você pode **baixar a imagem processada** clicando no botão de download.

---

## 📁 Estrutura de Pastas

```
├── app.py
├── filtros.py
├── static
│   ├── uploads          # Imagens enviadas
│   ├── processed        # Imagens processadas
│   └── style.css        # Estilo da interface
├── templates
│   └── index.html       # Página principal
└── README.md
```

---

## 📌 Requisitos
- Python 3.7+
- Flask
- Pillow
- NumPy

---

## 📄 Licença
Este projeto é livre para uso acadêmico e educacional.
