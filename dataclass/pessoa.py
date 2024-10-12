from dataclasses import asdict, astuple, dataclass, field


@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str
    enderecos: list[str] = field(default_factory=list)

    def __post_init__(self):
        print('POST INIT')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otavio')
    p1.nome_completo = 'Maria Helena Figueiredo'
    print(p1.nome_completo)

    print('##\n')

    lista_de_pessoas = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    lista_de_pessoas_ordenadas = sorted(lista_de_pessoas,
                                        reverse=False,
                                        key=lambda p: p.sobrenome)
    print(lista_de_pessoas_ordenadas)

    print(asdict(p1))
    print(astuple(p1))
