numeros = [1, 2, 2, 6, 6, 6, 6, 7, 10]

print(len(numeros))

contador = dict()

for numero in numeros:
    contador[numero] = contador.get(numero, 0) + 1

for numero, contagem in contador.item():
    if contagem > maior_contagem:
        maior_numero = numero
        maior_contagem = contagem

print(contador)