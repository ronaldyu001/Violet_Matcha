from pydantic import BaseModel


class MatchaOrder(BaseModel):
    """
    Elements
    - orders: list of dict[ name, quantity ]
    - active: True if want to order matcha
    """
    orders: list[dict]
    active: bool
