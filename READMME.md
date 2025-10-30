# API de Livraria Pessoal (com Autenticação JWT)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-red?style=for-the-badge&logo=sqlalchemy)](https://www.sqlalchemy.org/)

API RESTful desenvolvida como parte do meu aprendizado em desenvolvimento Back-end com Python. O projeto implementa um sistema de gerenciamento de livros com autenticação de usuários baseada em Token JWT.

## Status do Projeto
Projeto Concluído (Versão 2.0)

## 🚀 Features

* [x] **Autenticação de Usuários**:
    * [x] Cadastro (`POST /usuarios`) com validação e criptografia de senha (PBKDF2-SHA256).
    * [x] Login (`POST /login`) com geração de Token JWT.
* [x] **CRUD de Livros Protegido**:
    * [x] `POST`, `PUT`, `DELETE` de livros são rotas protegidas que exigem um Token JWT válido.
    * [x] `GET` (leitura) de livros são rotas públicas.
* [x] **Documentação Automática**: Geração de documentação interativa (Swagger UI) com "cadeados" 🔒 para rotas protegidas.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework:** FastAPI
* **Servidor:** Uvicorn
* **ORM:** SQLAlchemy
* **Banco de Dados:** SQLite
* **Validação de Dados:** Pydantic
* **Segurança:** `passlib` (para hash de senhas) e `python-jose` (para Tokens JWT)
* **Dependências Extras:** `python-multipart`, `bcrypt` (ou `pbkdf2_sha256`)

## 📦 Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/DiogoAbreu07/api-livraria-python.git](https://github.com/DiogoAbreu07/api-livraria-python.git)
    cd api-livraria-python
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```bash
    uvicorn main:app --reload
    ```

5.  **Acesse a API:**
    * **Documentação (Swagger):** `http://127.0.0.1:8000/docs`

## 📖 Endpoints da API

A documentação completa pode ser acessada em `/docs`.

### Autenticação

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/usuarios` | Cadastra um novo usuário. |
| `POST` | `/login` | Faz login e retorna um Token JWT. |

### Livros

| Método | Rota | Descrição | Protegido? |
| :--- | :--- | :--- | :--- |
| `POST` | `/livros` | Adiciona um novo livro. | **Sim** 🔒 |
| `GET` | `/livros` | Lista todos os livros. | Não |
| `GET` | `/livros/{livro_id}` | Obtém um livro pelo seu ID. | Não |
| `PUT` | `/livros/{livro_id}` | Atualiza um livro existente. | **Sim** 🔒 |
| `DELETE` | `/livros/{livro_id}` | Deleta um livro pelo seu ID. | **Sim** 🔒 |