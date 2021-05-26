from abc improt ABC, abstractmethod


class Elevador:
    """Essa classe transforma uma variável em um elevador"""
    def __init__(self):
        self._andar = 0
        self._chamados = []

    def chamar (self, andar):
        """adiciona o andar chamado na lista de chamados"""
        self._chamados.append(andar)

    def ir(self):
        """Vai para o próximo andar da lista de chamados"""
        if self._chamados:
            self._andar = self._chamados[0]
            self._chamados = self._chamados[1:]

    def localizar(self):
        """ Indica o andar do elevador"""
        return self._andar
