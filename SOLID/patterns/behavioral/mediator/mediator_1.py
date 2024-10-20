from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        ...

    @abstractmethod
    def direct(self, msg: str) -> None:
        ...


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        ...

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        ...


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'From: {colleague.name} -> To: All\n{msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'From: {sender.name} -> To: {receiver_obj[0].name}\n{msg}'
        )


if __name__ == '__main__':
    chat = Chatroom()

    joao = Person('João', chat)
    jose = Person('José', chat)
    maria = Person('Maria', chat)
    elis = Person('Elis', chat)

    chat.add(joao)
    chat.add(jose)
    chat.add(maria)
    chat.add(elis)

    joao.broadcast('Olá pessoal!')
    maria.broadcast('Opa.')

    jose.send_direct('Maria', 'Olá Maria, tudo bem?')
    maria.send_direct('José', 'Oi, bem e você?')
