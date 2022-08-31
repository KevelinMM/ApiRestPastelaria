from fastapi import FastAPI

import FuncionarioDAO
import ClienteDAO

app = FastAPI()

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)