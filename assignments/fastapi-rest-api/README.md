# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir uma API REST completa usando o framework FastAPI do Python. Você criará endpoints para gerenciar uma biblioteca de livros, implementando operações CRUD (Create, Read, Update, Delete) e aprendendo conceitos fundamentais de desenvolvimento de APIs.

## 📝 Tasks

### 🛠️	Configuração do Ambiente e API Básica

#### Description
Configure um projeto FastAPI do zero e crie sua primeira API com endpoints básicos. Você instalará as dependências necessárias, criará a estrutura inicial do projeto e implementará endpoints de saúde da aplicação.

#### Requirements
Completed program should:

- Instalar FastAPI e Uvicorn usando pip
- Criar um arquivo `main.py` com a aplicação FastAPI
- Implementar um endpoint GET `/` que retorna uma mensagem de boas-vindas
- Implementar um endpoint GET `/health` que retorna o status da API
- Executar a aplicação localmente na porta 8000
- Acessar a documentação automática em `/docs`

### 🛠️	Implementar CRUD para Gerenciamento de Livros

#### Description
Desenvolva um sistema completo de gerenciamento de livros implementando todos os métodos HTTP necessários. Você criará um modelo de dados para livros e implementará endpoints para criar, listar, buscar, atualizar e deletar livros.

#### Requirements
Completed program should:

- Criar um modelo Pydantic para Livro com campos: id, título, autor, ano_publicacao, isbn
- Implementar endpoint POST `/books` para criar novos livros
- Implementar endpoint GET `/books` para listar todos os livros
- Implementar endpoint GET `/books/{book_id}` para buscar um livro específico
- Implementar endpoint PUT `/books/{book_id}` para atualizar um livro
- Implementar endpoint DELETE `/books/{book_id}` para remover um livro
- Usar uma lista em memória para armazenar os dados
- Implementar tratamento de erros com códigos HTTP apropriados (404, 400, etc.)
- Validar dados de entrada usando Pydantic
- Retornar respostas JSON estruturadas para todos os endpoints