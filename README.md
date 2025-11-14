# 📚 API de Livraria Pessoal

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**API RESTful para gerenciamento de biblioteca pessoal com autenticação JWT**

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#%EF%B8%8F-tecnologias) •
[Instalação](#-instalação) •
[Documentação](#-documentação-da-api) •
[Contribuir](#-contribuindo)

</div>

---

## 📖 Sobre o Projeto

Esta API foi desenvolvida como parte do meu processo de aprendizado em desenvolvimento **Back-end com Python**, implementando um sistema completo de gerenciamento de livros com autenticação segura baseada em **tokens JWT**. 

O projeto demonstra a aplicação de conceitos modernos de desenvolvimento de APIs, incluindo:

- ✅ Autenticação e autorização
- ✅ Validação de dados com Pydantic
- ✅ ORM com SQLAlchemy
- ✅ Documentação automática
- ✅ Boas práticas de segurança

## ✨ Funcionalidades

### 🔐 Sistema de Autenticação

- Registro de usuários com validação robusta
- Criptografia de senhas usando **PBKDF2-SHA256**
- Autenticação via **Token JWT** com tempo de expiração configurável
- Middleware de autenticação para rotas protegidas

### 📚 Gerenciamento de Livros

- CRUD completo (Create, Read, Update, Delete)
- Rotas públicas para consulta de livros
- Rotas protegidas para operações de escrita (POST, PUT, DELETE)
- Validação automática de dados com Pydantic

### 📝 Documentação Interativa

- Interface **Swagger UI** integrada
- Indicadores visuais de rotas protegidas 🔒
- Testagem de endpoints diretamente na documentação
- Alternativa **ReDoc** para documentação

## 🛠️ Tecnologias

<table>
  <tr>
    <td align="center" width="96">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
      <br>Python
    </td>
    <td align="center" width="96">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="48" height="48" alt="FastAPI" />
      <br>FastAPI
    </td>
    <td align="center" width="96">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="48" height="48" alt="SQLAlchemy" />
      <br>SQLAlchemy
    </td>
    <td align="center" width="96">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="48" height="48" alt="SQLite" />
      <br>SQLite
    </td>
  </tr>
</table>

### Core

- **[Python 3.10+](https://www.python.org/)** - Linguagem de programação
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e de alta performance
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[SQLAlchemy 2.0+](https://www.sqlalchemy.org/)** - ORM Python
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validação de dados

### Segurança

- **[Passlib](https://passlib.readthedocs.io/)** - Hashing de senhas
- **[Python-JOSE](https://python-jose.readthedocs.io/)** - JWT (JSON Web Tokens)
- **[Python-Multipart](https://andrew-d.github.io/python-multipart/)** - Suporte multipart/form-data

## 🚀 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

```bash
# Clone o repositório
git clone https://github.com/DiogoAbreu07/api-livraria-python.git
cd api-livraria-python

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn main:app --reload
```

### Acessar a Aplicação

- **API Base:** `http://127.0.0.1:8000`
- **Documentação (Swagger):** `http://127.0.0.1:8000/docs`
- **Documentação (ReDoc):** `http://127.0.0.1:8000/redoc`

## 📚 Documentação da API

### Autenticação

#### 📝 Registrar Usuário

```http
POST /usuarios
Content-Type: application/json
```

**Body:**
```json
{
  "username": "seu_usuario",
  "email": "seu_email@exemplo.com",
  "password": "sua_senha_segura"
}
```

#### 🔑 Login

```http
POST /login
Content-Type: application/x-www-form-urlencoded
```

**Body:**
```
username=seu_usuario&password=sua_senha_segura
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Livros

| Método | Endpoint | Descrição | Autenticação |
|:------:|----------|-----------|:------------:|
| `POST` | `/livros` | Adiciona um novo livro | 🔒 Sim |
| `GET` | `/livros` | Lista todos os livros | ✅ Não |
| `GET` | `/livros/{id}` | Obtém detalhes de um livro | ✅ Não |
| `PUT` | `/livros/{id}` | Atualiza um livro | 🔒 Sim |
| `DELETE` | `/livros/{id}` | Remove um livro | 🔒 Sim |

#### 📖 Adicionar Livro

```http
POST /livros
Authorization: Bearer {seu_token_jwt}
Content-Type: application/json
```

**Body:**
```json
{
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "ano": 2008,
  "genero": "Tecnologia"
}
```

## 🗂️ Estrutura do Projeto

```
api-livraria-python/
│
├── 📄 main.py              # Ponto de entrada da aplicação
├── 📄 models.py            # Modelos do banco de dados (SQLAlchemy)
├── 📄 schemas.py           # Schemas de validação (Pydantic)
├── 📄 auth.py              # Lógica de autenticação e JWT
├── 📄 database.py          # Configuração do banco de dados
├── 📄 requirements.txt     # Dependências do projeto
├── 📄 .env                 # Variáveis de ambiente (não versionado)
├── 📄 .gitignore          # Arquivos ignorados pelo Git
├── 📄 LICENSE             # Licença do projeto
└── 📄 README.md           # Documentação
```

## 🔐 Segurança

Este projeto implementa as seguintes práticas de segurança:

- 🔒 **Criptografia de senhas** com PBKDF2-SHA256
- 🎫 **Tokens JWT** com expiração configurável
- 🛡️ **Middleware de autenticação** para rotas protegidas
- ✅ **Validação rigorosa** de dados de entrada
- 🔑 **Variáveis de ambiente** para informações sensíveis

## 🎯 Roadmap

- [ ] Implementar paginação nos endpoints de listagem
- [ ] Adicionar filtros e busca avançada de livros
- [ ] Sistema de categorias e tags
- [ ] Upload de capas de livros
- [ ] Testes unitários e de integração
- [ ] Rate limiting para prevenir abuso
- [ ] Migração para PostgreSQL
- [ ] Containerização com Docker
- [ ] CI/CD com GitHub Actions

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Faça **push** para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/DiogoAbreu07">
        <img src="https://github.com/DiogoAbreu07.png" width="100px;" alt="Diogo Abreu"/><br>
        <sub>
          <b>Diogo Abreu</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

[![GitHub](https://img.shields.io/badge/GitHub-DiogoAbreu07-181717?style=for-the-badge&logo=github)](https://github.com/DiogoAbreu07)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-diogoabreuu-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/diogoabreuu)
## 💙 Agradecimentos

- Comunidade [FastAPI](https://fastapi.tiangolo.com/) pela excelente documentação
- Todos os desenvolvedores que contribuem para o ecossistema Python
- Você que está lendo isso! 😊

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela! ⭐**

Feito com 💙 e ☕ por [Diogo Abreu](https://github.com/DiogoAbreu07)

</div>
