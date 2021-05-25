
class Elevador:
  """Essa classe transforma uma variável em um elevador"""
    def __init__(self):
        self.andar = 0
        self.chamados = []

    def chamar (andar):
        """adiciona o andar chamado na lista de chamados"""
        self.chamados.append(self, andar)

elevador_1:Elevador()
elevador_2:Elevador()

def ir():
    """Vai para o próximo andar da lista de chamados"""
    global chamados # usando variavel de fora do escopo
    global andar # usando variavel de fora do escopo
    if chamados:
        andar = chamados[0]
        chamados = chamados[1:]

chamar(2)
chamar(3)
chamar(0)

ir()
ir()

assert andar == 3
