from fastapi.testclient import TestClient
from app.main import app
from app.domain.auth_strategy import AuthStrategy
import pytest

client = TestClient(app)

def test_login_with_jwt():
    response = client.post("login", json={
        "username": "JohnDoe",
        "password": "123456",
        "method": "jwt"
    })

    assert response.status_code == 200
    assert response.json()["token"] == "jwt-token-for-JohnDoe"

def test_login_with_session():
    response = client.post("/login", json={
        "username": "JohnDoe",
        "password": "123456",
        "method": "session"
    })

    assert response.status_code == 200
    assert response.json()["token"] == "session-cookie-for-JohnDoe"

def test_login_with_invalid_user():
    response = client.post("/login", json={
        "username": "NoUsuario",
        "password": "1234",
        "method": "jwt"
    })
    assert response.status_code == 401

def test_login_invalid_password():
    response = client.post("/login", json={
        "username": "JohnDoe",
        "password": "1234",
        "method": "jwt"
    })
    assert response.status_code == 401

def test_login_invalid_method():
    response = client.post("/login", json={
        "username": "JohnDoe",
        "password": "123456",
        "method": "otro"
    })
    assert response.status_code == 400

def test_auth_strategy_abstract_method_call():
    with pytest.raises(TypeError):
        AuthStrategy()