def test_sales_report(test_app):
    # Create two receipts and close them
    for _ in range(2):
        receipt_response = test_app.post("/receipts")
        receipt_id = receipt_response.json()["receipt"]["id"]
        test_app.patch(f"/receipts/{receipt_id}", json={"status": "closed"})

    # Get sales report
    response = test_app.get("/sales")
    assert response.status_code == 200
    assert response.json()["sales"]["n_receipts"] == 2
