from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe Abstrata """

    def prepare(self) -> None:
        """ Template Method """

        self.hook_before_add_igredients()
        self.add_igredients()
        self.hook_after_add_igredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_igredients(self) -> None:
        ...

    def hook_after_add_igredients(self) -> None:
        ...

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando a pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo a pizza.')

    @abstractmethod
    def add_igredients(self) -> None:
        ...

    @abstractmethod
    def cook(self) -> None:
        ...


class HomemadePizza(Pizza):
    def hook_before_add_igredients(self) -> None:
        print('Antes de adicionar igredientes.')

    def add_igredients(self) -> None:
        print(f'{self.__class__.__name__}: Adicionando ovo, queijo e tomate.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cozinhando por 45min.')


class ChickenPizza(Pizza):
    def hook_after_add_igredients(self) -> None:
        print('Depois de adicionar igredientes.')

    def add_igredients(self) -> None:
        print(f'{self.__class__.__name__}: Adicionando queijo e frango.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cozinhando por 50min.')


if __name__ == '__main__':
    homemade = HomemadePizza()
    homemade.prepare()

    print()

    chicken = ChickenPizza()
    chicken.prepare()
