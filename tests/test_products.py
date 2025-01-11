def test_create_product(test_app):
    # Create a unit first
    unit_response = test_app.post("/units", json={"name": "კგ"})
    unit_id = unit_response.json()["unit"]["id"]

    # Create a product
    response = test_app.post(
        "/products",
        json={
            "unit_id": unit_id,
            "name": "Apple",
            "barcode": "1234567890",
            "price": 520,
        },
    )
    assert response.status_code == 201
    product = response.json()["product"]
    assert product["name"] == "Apple"
    assert product["barcode"] == "1234567890"
    assert product["price"] == 520
    assert product["unit_id"] == unit_id


def test_create_duplicate_product(test_app):
    # Create a unit
    unit_response = test_app.post("/units", json={"name": "კგ"})
    unit_id = unit_response.json()["unit"]["id"]

    # Create a product
    test_app.post(
        "/products",
        json={
            "unit_id": unit_id,
            "name": "Apple",
            "barcode": "1234567890",
            "price": 520,
        },
    )

    # Attempt to create the same product
    response = test_app.post(
        "/products",
        json={
            "unit_id": unit_id,
            "name": "Apple",
            "barcode": "1234567890",
            "price": 520,
        },
    )
    assert response.status_code == 409
    assert "already exists" in response.json()["error"]["message"]


def test_read_product(test_app):
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

    # Read the product
    response = test_app.get(f"/products/{product_id}")
    assert response.status_code == 200
    product = response.json()["product"]
    assert product["name"] == "Apple"
    assert product["barcode"] == "1234567890"
    assert product["price"] == 520
    assert product["unit_id"] == unit_id


def test_read_nonexistent_product(test_app):
    response = test_app.get("/products/999")
    assert response.status_code == 404
    assert "does not exist" in response.json()["error"]["message"]


def test_list_products(test_app):
    # Create a unit
    unit_response = test_app.post("/units", json={"name": "კგ"})
    unit_id = unit_response.json()["unit"]["id"]

    # Create multiple products
    product_1 = {
        "unit_id": unit_id,
        "name": "Apple",
        "barcode": "1234567890",
        "price": 520,
    }
    product_2 = {
        "unit_id": unit_id,
        "name": "Orange",
        "barcode": "0987654321",
        "price": 300,
    }
    test_app.post("/products", json=product_1)
    test_app.post("/products", json=product_2)

    # List products
    response = test_app.get("/products")
    assert response.status_code == 200
    products = response.json()["products"]
    assert len(products) == 2
    assert any(p["name"] == "Apple" for p in products)
    assert any(p["name"] == "Orange" for p in products)


def test_update_product(test_app):
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

    # Update product price
    response = test_app.patch(f"/products/{product_id}", json={"price": 550})
    assert response.status_code == 200

    # Verify the update
    response = test_app.get(f"/products/{product_id}")
    product = response.json()["product"]
    assert product["price"] == 550


def test_update_nonexistent_product(test_app):
    response = test_app.patch("/products/999", json={"price": 550})
    assert response.status_code == 404
    assert "does not exist" in response.json()["error"]["message"]
