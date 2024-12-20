from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): ...

    @abstractmethod
    def add_firstname(self, firstname): ...

    @abstractmethod
    def add_lastname(self, lastname): ...

    @abstractmethod
    def add_age(self, age): ...

    @abstractmethod
    def add_phone(self, phone): ...

    @abstractmethod
    def add_address(self, phone): ...


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder: UserBuilder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder._result

    def with_addresses(self, firstname, lastname, address):
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder._result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Luiz', 'Otavio', 30)
    user2 = user_director.with_addresses('João', 'Silva', 'Av. Brasil')
    print(user1)
    print(user2)
