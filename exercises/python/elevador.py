
class Elevador:
    """Essa classe transforma uma variável em um elevador"""
    def __init__(self):
        self.andar = 0
        self.chamados = []

    def chamar (self, andar):
        """adiciona o andar chamado na lista de chamados"""
        self.chamados.append(andar)

    def ir(self):
        """Vai para o próximo andar da lista de chamados"""
        if self.chamados:
            self.andar = self.chamados[0]
            self.chamados = self.chamados[1:]

elevador_1 = Elevador()
elevador_2 = Elevador()

elevador_1.chamar(3)
elevador_1.chamar(4)
elevador_1.ir()

assert elevador_1.andar == 3
