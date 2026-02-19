from fastapi import APIRouter, Body, HTTPException, Depends

from src.controller.category_controller import CategoryController

category_router = APIRouter(prefix="/categories", tags=["Categories"])

category = CategoryController()

@category_router.get(
  "",
  summary="List Categories",
  description="Endpoint to list all categories"
)(category.list_categories)