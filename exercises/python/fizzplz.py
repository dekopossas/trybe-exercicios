"""Pede um número para o usuário"""
from fizzbuzz import fizzbuzz


def pedir_numero():
    """Pede numero e retorna fizzbuzz"""
    resposta = input("Digite um número inteiro por favor: ")
    try:
        return int(resposta)
    except ValueError:
        print("número invalido")
        return pedir_numero()


numero = pedir_numero()
results = fizzbuzz(numero)
print(results)
