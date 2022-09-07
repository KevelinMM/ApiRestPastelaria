from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Produto(BaseModel):
    codigo: int = None
    nome: str
    descricao: str
    foto: bool = None
    valor_unitario: float

# Criar os endpoints de produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    return {"msg": "get executado", "id": id}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int, f: Produto):
    return {"msg": "post executado", "id": id, "nome": f.nome, "descricao": f.descricao}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, f: Produto):
    return {"msg": "put executado", "id": id, "nome": f.nome, "descricao": f.descricao}, 201

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado", "id": id}, 201