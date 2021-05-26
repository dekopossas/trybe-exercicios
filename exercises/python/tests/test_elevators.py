from elevators.elevador import Elevador
from elevators.elevador_2 import TerreoElevador

def test_elevador():
    # arrange
    elevador = Elevador()
    # act
    elevador.chamar(2)
    elevador.chamar(2)
    elevador.chamar(2)
    elevador.ir
    # assert
    assert elevador.localizar() == 2

def test_elevador_2():
    # arrange
    elevador = TerreoElevador()
    # act
    elevador.chamar(2)
    elevador.chamar(4)
    elevador.ir()
    elevador.ir()
    elevador.ir()
    assert elevador.localizar() == 0
    