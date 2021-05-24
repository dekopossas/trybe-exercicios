"""Pede um número para o usuário"""
from fizzbuzz import fizzbuzz
import sys


def pedir_numero():
    """Pede numero e retorna fizzbuzz"""
    try:
        resposta = input("Digite um número inteiro por favor: ")
    except KeyboardInterrupt:
        print("\n deixa quieto")

    try:
        return int(resposta)
    except ValueError:
        print("número invalido")
        return pedir_numero()


numero = pedir_numero()
results = fizzbuzz(numero)
print(results)
