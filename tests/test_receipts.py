def test_create_receipt(test_app):
    response = test_app.post("/receipts")
    assert response.status_code == 201
    assert response.json()["receipt"]["status"] == "open"
    assert response.json()["receipt"]["total"] == 0

def test_add_product_to_receipt(test_app):
    # Create a unit
    unit_response = test_app.post("/units", json={"name": "კგ"})
    unit_id = unit_response.json()["unit"]["id"]

    # Create a product
    product_response = test_app.post(
        "/products",
        json={
            "unit_id": unit_id,
            "name": "Apple",
            "barcode": "1234567890",
            "price": 520,
        },
    )
    product_id = product_response.json()["product"]["id"]

    # Create a receipt
    receipt_response = test_app.post("/receipts")
    receipt_id = receipt_response.json()["receipt"]["id"]

    # Add product to receipt
    response = test_app.post(
        f"/receipts/{receipt_id}/products",
        json={"id": product_id, "quantity": 2},
    )
    assert response.status_code == 201
    assert response.json()["receipt"]["total"] == 1040

def test_close_receipt(test_app):
    # Create a receipt
    receipt_response = test_app.post("/receipts")
    receipt_id = receipt_response.json()["receipt"]["id"]

    # Close receipt
    response = test_app.patch(f"/receipts/{receipt_id}", json={"status": "closed"})
    assert response.status_code == 200

    # Verify receipt is closed
    response = test_app.get(f"/receipts/{receipt_id}")
    assert response.status_code == 200
    assert response.json()["receipt"]["status"] == "closed"
