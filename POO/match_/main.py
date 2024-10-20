from dataclasses import dataclass, field


def registra_operacao_texto(operacao_texto):
    match operacao_texto.split():
        case ['credito' | 'cred', *valores_str] if len(valores_str) > 0:
            for valor in [int(valor_str.replace(',', ''))
                          for valor_str in valores_str
                          if valor_str.replace(',', '').isdigit()]:

                print(f'Operação de crédito de {valor} reais')

        case ['debito' | 'deb', *valores_str] if len(valores_str) > 0:
            for valor in [int(valor_str.replace(',', ''))
                          for valor_str in valores_str
                          if valor_str.replace(',', '').isdigit()]:

                print(f'Operação de débito de {valor} reais')

        case _:
            print('Operação inválida.')


# registra_operacao_texto('credito 12 14 5')
# registra_operacao_texto('debito 70 8 4 5 6')
# registra_operacao_texto('credito de 50, 5 e 70 reais')
# registra_operacao_texto('deb de 500 e 7 reais')


@dataclass
class Operacao():
    tipo: str
    valores: list[int] = field(default_factory=list)


def registra_operacao(operacao: Operacao):
    match operacao:
        case Operacao(tipo='credito' | 'cred', valores=[_, *_]):
            for valor in operacao.valores:
                print(f'Operação de crédito de {valor} reais')

        case Operacao(tipo='debito' | 'deb', valores=[_, *_]):
            for valor in operacao.valores:
                print(f'Operação de débito de {valor} reais')

        case _:
            print('Operação Inválida.')


operacao = Operacao('deb', [1, 2])
registra_operacao(operacao)
