from cesar.cesar import encripta


def test_encripta_felipe_retorna_sryvcr():
    assert encripta('Felipe') == 'sryvcr'


def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espaços():
    resultado = encripta('e a')
    assert resultado[1] == ' '
