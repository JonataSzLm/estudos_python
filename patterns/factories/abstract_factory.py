from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: ...


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: ...


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da zona norte está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro de popular da zona norte está buscando o cliente...')


class MotoZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('A moto da zona norte está buscando o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da zona sul está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro de popular da zona sul está buscando o cliente...')


class MotoZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('A moto da zona sul está buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        ...

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        ...

    @staticmethod
    @abstractmethod
    def get_moto() -> VeiculoPopular:
        ...


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto() -> VeiculoPopular:
        return MotoZS()


class Filiais:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory]:
            print('')
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            print('')
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            print('')
            moto = factory.get_moto()
            moto.buscar_cliente()
            print('--------------\n')


if __name__ == '__main__':
    filiais = Filiais()
    filiais.busca_clientes()
