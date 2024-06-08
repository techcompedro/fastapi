from fastapi import FastAPI
from pydantic import BaseModel

bdlivros = {
    1: {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "preço": 25.99},
    2: {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "preço": 19.90},
    3: {"titulo": "A Montanha Mágica", "autor": "Thomas Mann", "preço": 12.50},
    4: {"titulo": "1984", "autor": "George Orwell", "preço": 9.99},
    5: {"titulo": "O Apanhador no Campo de Centeio", "autor": "J.D. Salinger", "preço": 15.75},
    6: {"titulo": "Moby Dick", "autor": "Herman Melville", "preço": 11.25},
    7: {"titulo": "A Divina Comédia", "autor": "Dante Alighieri", "preço": 8.99},
    8: {"titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski", "preço": 13.50},
    9: {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "preço": 10.75},
    10: {"titulo": "O Grande Gatsby", "autor": "F. Scott Fitzgerald", "preço": 16.99}
}

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    preco: float
    disponibilidade: bool

app = FastAPI()
@app.get("/")
def MostrarInfos():
    return {
        "mensagem": "api de livros",
        "versao": "1.0"
    }
@app.get("/livros/")
def MostrarTodosLivros():
    return bdlivros

@app.get("/livros/{id}")
def mostrarumlivro(id: int):
    try:
        return {
            "livro": bdlivros[id],
            "StatusCode": 200
        }
    except:
        return {
            "livro": "livro não encontrado",
            "StatusCode": 404
        }