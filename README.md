# 🛒 Lista de Compras — Django App

Um aplicativo web simples para gerenciar sua lista de compras, desenvolvido com **Python + Django**.  
Permite adicionar, editar, excluir e marcar itens como comprados, com uma interface moderna feita em **Bootstrap 5**.

---

## 🚀 Funcionalidades

- ✅ Adicionar novos itens à lista  
- ✏️ Editar itens existentes  
- 🗑️ Excluir itens  
- 🛍️ Mover itens entre a lista e o carrinho  
- 🌙 Tema escuro com design responsivo
- ↕️ Ordenação/filtro de ordem alfabética e por odem de criação.
- 💾 Banco de dados SQLite (local) ou PostgreSQL (produção)

---

## 🧱 Tecnologias Utilizadas

- **Python 3.12+**  
- **Django 5.2**  
- **Bootstrap 5**  
- **Whitenoise** (para servir arquivos estáticos em produção)  
- **Gunicorn** (servidor WSGI de produção)  
- **Render.com** (deploy gratuito)  

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/Rennan1/lista-compras.git
cd lista-compras/projeto
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Inicie o servidor local
```bash
python manage.py runserver
```

> O app estará disponível em: http://127.0.0.1:8000/

---

## 🗃️ Estrutura do Projeto

```
lista-compras/
├── manage.py
├── requirements.txt
├── lista_compras/         # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── compras/               # Aplicativo principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── index.html
│       ├── adicionar_item.html
│       ├── editar_item.html
│       └── excluir_item.html
└── static/
    └── img/
```

---

## 🧩 Banco de Dados

Por padrão o projeto usa **SQLite3** para desenvolvimento.  
Para produção, ele detecta automaticamente o `DATABASE_URL` (por exemplo no Render) e usa **PostgreSQL**.

---

## 🌐 Deploy no Render

1. Faça login no [Render.com](https://render.com)  
2. Conecte seu repositório GitHub  
3. Configure as variáveis de ambiente:
   ```
   DEBUG=False
   SECRET_KEY=uma-chave-secreta
   DATABASE_URL=postgres://...
   ```
4. Deploy automático será feito via `gunicorn lista_compras.wsgi`

---

## 👨‍💻 Autor

**Rennan Oliveira**  

---

## 🎥 Demonstração (GIF)

![Demonstração do fluxo](media/demo.gif)
