from fastapi.testclient import TestClient

def test_create_outcome(client: TestClient):
    response = client.post("/outcomes/", json={
        "learner_id": 1,
        "item_id": 1,
        "status": "passed"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "passed"
    assert "id" in data

def test_get_outcomes(client: TestClient):
    client.post("/outcomes/", json={"learner_id": 1, "item_id": 1, "status": "passed"})
    
    response = client.get("/outcomes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_outcome_by_id(client: TestClient):
    create_resp = client.post("/outcomes/", json={
        "learner_id": 1, 
        "item_id": 2, 
        "status": "failed"
    })
    created_id = create_resp.json()["id"]

    response = client.get(f"/outcomes/{created_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "failed"

def test_get_non_existent_outcome(client: TestClient):
    response = client.get("/outcomes/999999")
    assert response.status_code == 404