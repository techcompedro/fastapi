from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float


bancodados = {
    1:{
        "nome": "pizza",
        "preço": 29.90
    },
    2:{
        "nome": "lasanha",
        "preço": 9.90
    },
    3:{
        "nome": "salgado",
        "preço": 4.00
    }
}


app = FastAPI()
#roda princinpal de apresentação
@app.get("/")
def apresencao():
    return {
        "mensagem": "olá mundo",
        "statusCode": 200
    }
@app.get("/{nome}")
def saudacao(nome):
    return {
        "mensagem": f"olá {nome}!",
        "statusCode": 200
    }
@app.get("/produto/")
def mostratodosprodutos():
    return bancodados

@app.get("/produto/{idproduto}")
def mostrarumproduto(idproduto):
    try:
        if bancodados[idproduto]:
            return {
                "produto": bancodados[idproduto],
                "statusCode": 200
            }


    except:
        return {
            "produto": "não encontrado",
            "statusCode": 404
        }

@app.post("/produotos/cadastrar/")
def cadastrarproduto(item: Produto):
    id = len(bancodados)+1
    bancodados[id]= item
    listadeprodutos = bancodados.values()
    for produto in listadeprodutos:
        if produto['nome'] == item.nome:
            return {
                "mensagem": "produto já cadastrado",
                "statusCodee": 400
            }
        else :
            bancodados[id]= item
            return {
                "mensagem": "item criado com sucesso",
                "produto": item,
                "statusCode": 200
                }


@app.delete("/produtos/excluir{id}")
def excluirproduto(id):
    bancodados.pop(id)
    return {
        "mesagem": "produto excluido",
        "idproduto": id,
        "StatusCode": 200
    }


