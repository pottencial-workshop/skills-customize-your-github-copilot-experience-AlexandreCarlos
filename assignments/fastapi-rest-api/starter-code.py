"""
FastAPI REST API - Starter Code
Biblioteca de Livros

Este arquivo contém a estrutura básica para começar a desenvolver
uma API REST com FastAPI para gerenciar uma biblioteca de livros.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Criar instância da aplicação FastAPI
app = FastAPI(
    title="Biblioteca API",
    description="API REST para gerenciar uma biblioteca de livros",
    version="1.0.0"
)

# Modelo Pydantic para Livro
class Book(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int
    isbn: str

class BookCreate(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
    isbn: str

class BookUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    ano_publicacao: Optional[int] = None
    isbn: Optional[str] = None

# Lista em memória para armazenar os livros
books_db: List[Book] = []
next_id = 1

# TODO: Implementar endpoint GET / (boas-vindas)


# TODO: Implementar endpoint GET /health (status da API)


# TODO: Implementar endpoint POST /books (criar livro)


# TODO: Implementar endpoint GET /books (listar todos os livros)


# TODO: Implementar endpoint GET /books/{book_id} (buscar livro por ID)


# TODO: Implementar endpoint PUT /books/{book_id} (atualizar livro)


# TODO: Implementar endpoint DELETE /books/{book_id} (deletar livro)


# Função para executar a aplicação
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)