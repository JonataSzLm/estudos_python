from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self) -> None:
        ...

    def base_class_method(self):
        print('Metodo da classe abstrata...')

    @abstractmethod
    def operation1(self) -> None:
        ...

    @abstractmethod
    def operation2(self) -> None:
        ...


class ConcreteClass1(Abstract):
    def hook(self):
        print('Hook utilizado.')

    def operation1(self) -> None:
        print('Operação 1 concluída')

    def operation2(self) -> None:
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self) -> None:
        print('Operação 1 concluída (de maneira diferente)')

    def operation2(self) -> None:
        print('Operação 2 concluída (de maneira diferente)')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()
