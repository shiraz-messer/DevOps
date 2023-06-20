from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/Jerusalem")
    assert response.status_code == 200
    assert response.json() == {"res": {"wrote": True}}

    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.json() == {"res": {"wrote": False}}

    response = client.get("/log/log")
    assert response.status_code == 200


test_read_main()
