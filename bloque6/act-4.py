def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    if cadena[0] == cadena[-1]:
        return es_palindromo(cadena[1:-1])
    return False

entrada = "reconocer"
print(es_palindromo(entrada))