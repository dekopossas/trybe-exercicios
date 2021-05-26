from elevators.elevador import Elevador

class MemoriaElevador(Elevador):
    def __init__(self, memoria):
        self.memoria = memoria
        super().__init__()
        