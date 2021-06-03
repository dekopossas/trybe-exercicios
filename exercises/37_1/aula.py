numeros = [1, 2, 2, 6, 6, 6, 6, 7, 10]

print(len(numeros))

contador = dict()

for numero in numeros:
    contador[numero] = contador.get(numero, 0) + 1

print(contador)

numero_mais_frequente = None
maior_contagem = 0

for numero, contagem in contador.item():
    if contagem > maior_contagem:
        numero_mais_frequente = numero
        maior_contagem = contagem

print(numero_mais_frequente)