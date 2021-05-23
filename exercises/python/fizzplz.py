"""Pede um número para o usuário"""
from fizzbuzz import fizzbuzz


def pedir_numero():
    """Pede numero e retorna fizzbuzz"""
    try:
        return int(input("Digite um número inteiro por favor: "))
    except ValueError:
        return pedir_numero()


numero = pedir_numero()
results = fizzbuzz(numero)
print(results)
