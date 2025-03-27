from fastapi import APIRouter
from api.v1 import route_passenger
from api.v1 import route_cashier
from api.v1 import route_common
api_router = APIRouter()
api_router.include_router(route_common.router,prefix="", tags=["Common_route"])
api_router.include_router(route_passenger.router,prefix="", tags=["Passnger_route"])
api_router.include_router(route_cashier.router,prefix="", tags=["Cashier_route"])

