from fastapi import APIRouter

from .expedientes_routes import router as expediente_router

# Router V1
router_v1 = APIRouter(prefix='/v1')

# Agregamos al router v1 las rutas definidas
router_v1.include_router(expediente_router, tags=['Expedientes'])