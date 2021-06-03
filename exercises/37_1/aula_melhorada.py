numeros = [1, 2, 2, 6, 6, 6, 6, 7, 10]

print(len(numeros))
def numero_que_aparece_um_quarto(numeros):
    contador = dict()

    for numero in numeros:
        contador[numero] = contador.get(numero, 0) + 1

    print(contador)

    numero_mais_frequente = None
    maior_contagem = 0

    for numero, contagem in contador.items():
        if contagem > maior_contagem:
            numero_mais_frequente = numero
            maior_contagem = contagem

    return numero_mais_frequente

resultado = numero_que_aparece_um_quarto(numeros)

print(resultado)