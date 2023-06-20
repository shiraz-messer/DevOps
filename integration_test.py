import requests
import pytest


def test_get_city_by_name():
    id_input = "Jerusalem"
    response = requests.get("http://localhost:80/en/{id_input}")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data["res"]
    assert "y" in data["res"]

    id_input = "חולון"
    response = requests.get("http://localhost:80/he/{id_input}")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data["res"]
    assert "y" in data["res"]


test_get_city_by_name()
