# 📚 API de Livraria Pessoal (Projeto de Portfólio)

Uma API RESTful completa para gerenciar uma coleção de livros, construída com Python, FastAPI e SQLAlchemy como parte do meu aprendizado em desenvolvimento back-end.

**Status do Projeto:** Concluído ✔️

---

## 🚀 Sobre o Projeto

Este projeto é o primeiro de uma série para meu portfólio de Desenvolvedor Back-end. O objetivo foi construir uma API 100% funcional que implementa todas as operações de um **CRUD (Create, Read, Update, Delete)**.

A API permite criar, listar, buscar por ID, atualizar e deletar livros de um banco de dados SQLite.

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI:** Para a construção da API (rotas, validação, documentação).
* **Pydantic:** Para validação e "contratos" de dados (schemas).
* **SQLAlchemy:** Para o ORM (Object-Relational Mapping) e comunicação com o banco.
* **SQLite:** Banco de dados leve e local.
* **Uvicorn:** Servidor ASGI para rodar a aplicação.

## ✨ Features (Funcionalidades)

* [x] **Create:** `POST /livros` - Adiciona um novo livro.
* [x] **Read (All):** `GET /livros` - Lista todos os livros.
* [x] **Read (One):** `GET /livros/{id}` - Busca um livro específico por ID.
* [x] **Update:** `PUT /livros/{id}` - Atualiza um livro existente.
* [x] **Delete:** `DELETE /livros/{id}` - Deleta um livro.
* [x] **Documentação Automática:** Acesso em `/docs` (Swagger UI).

---

## 🏁 Como Executar (Localmente)

Siga os passos abaixo para rodar o projeto na sua máquina.

**1. Clone o repositório:**
```bash
git clone https://github.com/DiogoAbreu07/api-livraria-python.git
cd api-livraria-python
```

**2. Crie e ative o ambiente virtual (venv):**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Rode o servidor:**
```bash
uvicorn main:app --reload
```

**5. Acesse a API:**
* **Servidor rodando em:** `http://127.0.0.1:8000`
* **Documentação Interativa (Swagger):** `http://127.0.0.1:8000/docs`

---

## 📋 Endpoints da API

Abaixo está um resumo dos endpoints disponíveis:

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/livros` | Cria um novo livro. |
| `GET` | `/livros` | Lista todos os livros. |
| `GET` | `/livros/{livro_id}` | Busca um livro por ID. |
| `PUT` | `/livros/{livro_id}` | Atualiza um livro por ID. |
| `DELETE` | `/livros/{livro_id}`| Deleta um livro por ID. |