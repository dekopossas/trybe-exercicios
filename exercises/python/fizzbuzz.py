"""Fizz buzz com python"""


def fizzbuzz(numero):
    """Recebe um numero, retorna fizz, buzz, fizzbuzz ou o numero"""
    if (numero % 3 == 0) and (numero % 5 == 0):
        return "fizzbuzz"
    if numero % 5 == 0:
        return "buzz"
    if numero % 3 == 0:
        return "fizz"
    return str(numero)

def fizzbuzz_on(limit):
    """Aplica o fizzbuzz ate o numero passado no parametros"""
    for numero in range(1, limit + 1):
        print(fizzbuzz(numero))


assert fizzbuzz(3) == "fizz"
assert fizzbuzz(5) == "buzz"
assert fizzbuzz(15) == "fizzbuzz"
assert fizzbuzz(4) == "4"
