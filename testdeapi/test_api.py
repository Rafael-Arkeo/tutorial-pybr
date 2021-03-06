from fastapi.testclient import TestClient
from http import HTTPStatus
from api_pedidos.api import app
import pytest





def testsaude():
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK


def test_quando_verificar_integridade_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"


def test_quando_verificar_integridade_deve_conter_informacoes():
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {"status": "ok",}