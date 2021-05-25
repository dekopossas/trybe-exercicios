andar = 0
chamados = []

def chamar (andar):
    """adiciona o andar chamado na lista de chamados"""
    chamados.append(andar)

def ir():
    """Vai para o próximo andar da lista de chamados"""
    global chamados # usando variavel de fora do escopo
    global andar # usando variavel de fora do escopo
    if chamados:
        andar = chamados[0]
        chamados = chamados[1:]

chamar(2)
chamados.append(2)
chamados = [2]

andar = 3
ir()
andar = chamados[0]
