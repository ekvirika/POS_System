# from fastapi.testclient import TestClient
#
# from app.main import app
#
# client = TestClient(app)
#
# def test_get_sales_report():
#     response = client.get("/sales")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["n_receipts"] == 0
#     assert data["revenue"] == 0
