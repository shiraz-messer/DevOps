from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/he/גבעת שמואל/")
    assert response.status_code == 200
    assert response.json() == {"res": {"x": 32.0781, "y": 34.8489}}

    response = client.get("/en/Jerusalem")
    assert response.status_code == 200
    assert response.json() == {"res": {"x": 31.7833, "y": 35.2167}}


test_read_main()
