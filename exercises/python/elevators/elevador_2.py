from elevators.elevador import Elevador

class TerreoElevador(Elevador):
    def ir(self):
        """Volta pro terreio se estiver sem chamadas"""
        if not self._chamados:
            self._andar = 0
        else:
            super().ir() # metodo irado de falar q ta usando function base.