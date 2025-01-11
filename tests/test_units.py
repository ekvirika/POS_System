def test_create_unit(test_app):
    response = test_app.post("/units", json={"name": "კგ"})
    assert response.status_code == 201
    assert response.json()["unit"]["name"] == "კგ"

def test_create_duplicate_unit(test_app):
    test_app.post("/units", json={"name": "კგ"})
    response = test_app.post("/units", json={"name": "კგ"})
    assert response.status_code == 409
    assert "already exists" in response.json()["error"]["message"]

def test_read_unit(test_app):
    response = test_app.post("/units", json={"name": "ცალი"})
    unit_id = response.json()["unit"]["id"]

    response = test_app.get(f"/units/{unit_id}")
    assert response.status_code == 200
    assert response.json()["unit"]["name"] == "ცალი"

def test_read_nonexistent_unit(test_app):
    response = test_app.get("/units/999")
    assert response.status_code == 404
    assert "does not exist" in response.json()["error"]["message"]
