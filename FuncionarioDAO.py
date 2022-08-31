from fastapi import APIRouter


router = APIRouter()

# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE

@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario(id: int):
    return {"msg": "get executado"}, 200

@router.post("/funcionario/{id}", tags=["funcionario"])
def post_funcionario(id: int):
    return {"msg": "post executado"}, 200

@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 201