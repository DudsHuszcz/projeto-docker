from app import app, soma, subtracao

# Teste 1: Verifica se o site está online
def test_hello_route():
    response = app.test_client().get('/')
    assert response.status_code == 200

# Teste 2: Verifica a frase do site
def test_conteudo_route():
    response = app.test_client().get('/')
    assert b"Professor" in response.data

# Teste 3: Verifica soma positiva
def test_soma_positivos():
    assert soma(2, 3) == 5

# Teste 4: Verifica soma negativa
def test_soma_negativos():
    assert soma(-1, -1) == -2

# Teste 5: Verifica subtração
def test_subtracao():
    assert subtracao(5, 2) == 3
