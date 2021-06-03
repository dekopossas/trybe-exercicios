numeros = [1, 2, 2, 6, 6, 6, 6, 7, 10]

print(len(numeros))
def numero_que_aparece_um_quarto(numeros):
    contador = dict()
    quarto = len(numeros) / 4

    for numero in numeros:
        contador[numero] = contador.get(numero, 0) + 1

    print(contador)

    for numero, contagem in contador.items():
        if contagem >= quarto:
            return numero

resultado = numero_que_aparece_um_quarto(numeros)

print(resultado)