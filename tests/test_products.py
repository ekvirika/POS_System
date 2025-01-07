from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products", json={
        "unit_id": "unit1",
        "name": "Apple",
        "barcode": "1234567890",
        "price": 520
    })
    assert response.status_code == 201
    assert response.json()["product"]["name"] == "Apple"
