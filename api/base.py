from fastapi import APIRouter
from api.v1 import route_passenger
from api.v1 import route_cashier
from api.v1 import route_common
from api.v1 import route_flight
from api.v1 import route_ship
from api.v1 import route_ticket
api_router = APIRouter()
api_router.include_router(route_common.router,prefix="", tags=["Common_route"])
api_router.include_router(route_passenger.router,prefix="", tags=["Passnger_route"])
api_router.include_router(route_cashier.router,prefix="", tags=["Cashier_route"])
api_router.include_router(route_flight.router,prefix="", tags=["Flight_route"])
api_router.include_router(route_ship.router, prefix="", tags=["Ship_route"])
api_router.include_router(route_ticket.router, prefix="", tags=["Ticket_route"])