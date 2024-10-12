from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self, velocidade, vetor) -> str: ...

class Carro(Veiculo):
    def __init__(self, cor, marca):
        super().__init__()
        self._cor = cor
        self._marca = marca
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    def mover(self, velocidade, vetor='X'):
        return f'O carro se moveu no eixo {vetor} a {velocidade} km/h'



if __name__ == '__main__':
    carro = Carro('Vermelho', 'Ford')
    print(carro.marca, carro.cor)
    print(carro.mover(10))
