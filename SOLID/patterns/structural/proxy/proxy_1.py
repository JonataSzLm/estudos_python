from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    """ Subject Interface """

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        ...

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        ...


class User(IUser):
    """ Real Subject """

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {
            'cpf': '111.111.111-11',
            'rg': 'AB111222444'
        }


class UserProxy(IUser):
    """ Proxy """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: User
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    luiz = UserProxy('Luiz', 'Otavio')

    print(luiz.firstname)
    print(luiz.lastname)

    # 6 Segundos
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # Responde instantaneamente
    print('CACHED DATA')
    for i in range(50):
        print(luiz.get_addresses())
