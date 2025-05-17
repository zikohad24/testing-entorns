from calculadora import suma, resta

def test_suma():
    assert suma(2, 3) == 6  


def test_resta():
    assert resta(5, 3) == 2
