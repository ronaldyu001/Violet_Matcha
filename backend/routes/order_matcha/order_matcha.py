from fastapi import APIRouter
import logging

from services.order_matcha.order_matcha import order_matcha
from models.MatchaOrder.MatchaOrder import MatchaOrder


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


router = APIRouter()

@router.post("/order_matcha")
def order_matcha_route( orders: MatchaOrder ):
    logging.info("Ordering matcha")

    try:
        order_matcha(orders=orders.orders) if orders.active else None
        return {"success": True, "error": None}

    except Exception as err:
        logging.info(f"Error ordering: {repr(err)}")
        return {"success": False, "error": err}

