class Pessoa:
    def __new__(cls, *args, **kwargs):
        print(f'Nascimento...')
        return super().__new__(cls)

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.__pets = []
        self.__enderecos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @classmethod
    def recem_nascido(cls, nome):
        return cls(nome, 0, )
    

    def adotar_pet(self, *animais):
        for animal in animais:
            if animal.pet:
                self.__pets.append(animal)

    def chamar_pets(self):
        for pet in self.__pets:
            print(f'{'Pega' if pet.especie == 'cachorro' else 'Vem'} {pet.nome}')


    def inserir_endereco(self, rua, numero):
        self.__enderecos.append(Endereco(rua, numero))


    def listar_enderecos(self):
        print('Enderecos:\n')
        for endereco in self.__enderecos:
            print(f'{endereco.rua}, {endereco.numero}')


    def __repr__(self):
        return f'{self.__class__.__name__}(nome={self.nome!r}, idade={self.idade!r}, pets={self.__pets!r}, enderecos={self.__enderecos!r})'

    def __add__(self, other):
        return f'{self.nome} se casou com {other.nome}.'

    def __sub__(self, other):
        return f'{self.nome} se separou de {other.nome}.'

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __repr__(self):
        return f'{self.__class__.__name__}(rua={self.rua!r}, numero={self.numero!r})'
