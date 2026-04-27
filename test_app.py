# Funções matemáticas simples para teste
def soma(a, b): 
    return a + b

def subtracao(a, b): 
    return a - b

# Teste 1: Soma Positiva
def test_soma_positivos():
    assert soma(2, 3) == 5

# Teste 2: Soma Negativa
def test_soma_negativos():
    assert soma(-1, -1) == -2

# Teste 3: Subtração
def test_subtracao():
    assert subtracao(5, 2) == 3

# Teste 4: Lógica Básica
def test_verdadeiro():
    assert True == True

# Teste 5: Validação de Texto
def test_texto():
    assert "GitHub" in "GitHub Actions"
