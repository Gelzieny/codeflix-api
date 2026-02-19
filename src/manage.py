from fastapi import FastAPI
from starlette.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from starlette.responses import RedirectResponse

from src.routes import category_router
from src.core.postgre_conexao import ConexaoPostgres


app = FastAPI(
  title="Codeflix API",
  description="""
    API para gerenciamento de conteúdo de streaming, incluindo filmes e séries, com funcionalidades de CRUD, autenticação e 
    integração com bancos de dados relacionais.
  """,
  version="1.0.0"
)

app.include_router(category_router)

# --- Rota de Redirecionamento da Raiz para a Documentação ---
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True

@app.get("/healthz", tags=["Health"])
async def health_check():
  return ConexaoPostgres().teste()
