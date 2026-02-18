from pydantic import BaseModel, Field

class RetornoResponse(BaseModel):
  mensagem: str = Field(description="Exemplo de Mensagem", default='Valor Default')
  cod_retorno: int = Field()