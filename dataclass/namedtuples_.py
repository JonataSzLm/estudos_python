# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
# as_espadas = Carta('A', '♠️')
# print(as_espadas)
# print(as_espadas.valor)
# print(as_espadas.naipe)

# print(as_espadas._field_defaults)
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_copas = Carta('A', '♥️')
print(as_copas)
