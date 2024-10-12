class Animal:
    def __init__(self, especie, nome = None, pet = False):
        self._especie = especie
        self._nome = nome
        self._pet = pet

    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self, valor):
        self._especie = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def pet(self):
        return self._pet
    
    @pet.setter
    def pet(self, valor):
        self._pet = valor

    @classmethod
    def cria_cachorro(cls, nome):
        return cls('cachorro', nome, True)
    
    @classmethod
    def cria_gato(cls, nome):
        return cls('gato', nome, True)
    
    def __repr__(self):
        return f'{self.__class__.__name__}(especie={self.especie!r},nome={self.nome!r},pet={self.pet!r})'