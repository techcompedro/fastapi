from fastapi import FastAPI
from pydantic import BaseModel

bdlivros = {}
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    preco: float
    disponibilidade: bool

app = FastAPI()
@app.get("/")
def mostrarinfos():
    return {
        "mensagem": "api de livros",
        "versao": "1.0"
    }
@app.get("/livros/")
def MostrarTodosLivros():
    return bdlivros

