from abc import ABC, abstractmethod
import enum


class VeiculosEnum(enum.Enum):
    LUXO = enum.auto()
    POPULAR = enum.auto()
    MOTO = enum.auto()


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


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: VeiculosEnum) -> Veiculo:
        match tipo:
            case VeiculosEnum.LUXO:
                return CarroLuxo()

            case VeiculosEnum.POPULAR:
                return CarroPopular()

            case VeiculosEnum.MOTO:
                return Moto()

        assert 0, 'Veículo não existe'


if __name__ == '__main__':

    carro_luxo = VeiculoFactory.get_carro(VeiculosEnum.LUXO)
    carro_luxo.buscar_cliente()

    carro_popular = VeiculoFactory.get_carro(VeiculosEnum.POPULAR)
    carro_popular.buscar_cliente()

    moto = VeiculoFactory.get_carro(VeiculosEnum.MOTO)
    moto.buscar_cliente()
