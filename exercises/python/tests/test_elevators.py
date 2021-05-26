from elevators.elevator import Elevator
from elevators.terreo import TerreoElevador

def test_elevador():
    # arrange
    elevador = Elevator()
    # act
    elevador.chamar(2)
    elevador.chamar(2)
    elevador.chamar(2)
    elevador.ir
    # assert
    assert elevador.localizar() == 2
