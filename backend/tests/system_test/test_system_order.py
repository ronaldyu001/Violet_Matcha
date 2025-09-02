import pytest
import requests

def test_order():
    payload = {
        "orders": [
            {"name": "test_1", "quantity": 2},
            {"name": "test_2", "quantity": 3},
            {"name": "test_3", "quantity": 4},
            {"name": "test_4", "quantity": 5}
        ],
        "active": True
    }

    response = requests.post(
        url="http://localhost:8000/api/order_matcha",
        headers={"Content-Type": "application/json"},
        json=payload
    )

    assert response.status_code == 200
    print(response.json())