from pessoa import Pessoa
from animal import Animal

if __name__ ==  '__main__':
    print('INICIO')
    mae = Pessoa('Maria', 25)
    pai = Pessoa('Joao', 28)
    filho = Pessoa.recem_nascido('Marcos')

    print(pai.nome, pai.idade)
    print(filho.nome, filho.idade)

    pet1 = Animal.cria_cachorro('Toto')
    pet2 = Animal.cria_gato('Tobias')

    filho.adotar_pet(pet1, pet2)
    filho.chamar_pets()

    pai.inserir_endereco('Av. Prefeito Paulo', 123)
    pai.inserir_endereco('Rua Cristina Maria', 90)
    pai.listar_enderecos()
    print('\n')
    print(pai + mae)
    print(pai - mae)

    print('\n\n\n\n\n')
    print(repr(pai))
    print(repr(filho))