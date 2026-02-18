from typing import Optional
from pydantic import BaseModel, Field

class CategoryModel(BaseModel):
  name_category: str = Field(..., description="Nome da Categoria")
  description_category: str = Field(..., description="Descrição da Categoria")
  cod_category: int = Field(..., description="Código da Categoria")