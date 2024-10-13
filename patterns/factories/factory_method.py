from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: ...


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de popular está buscando o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('A moto está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        ...

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        match tipo:
            case 'luxo':
                return CarroLuxo()

            case 'popular':
                return CarroPopular()

            case 'moto':
                return Moto()

        raise ValueError('Veículo não existe')
        # assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        match tipo:
            case 'popular':
                return CarroPopular()

        raise ValueError('Veículo não existe')
        # assert 0, 'Veículo não existe'


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_zona_sul = ['popular']

    print('Zona Norte:\n')
    for i in range(5):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print('\n\nZona Sul:\n')
    for i in range(5):
        carro2 = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
