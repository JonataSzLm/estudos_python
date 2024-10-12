from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        nome = None
        for k in kwargs:
            if k == 'nome':
                nome = kwargs[k]
        
        if not nome and len(args) > 0:
            nome = args[0]

        print(f'O numero {self.phone} esta recebendo uma ligacao{f' de {nome}' if nome else ''}...')
        return True if nome else False

call = CallMe('123456789')
retorno = call(nome='Jose')
call2 = CallMe('7894561347')
retorno2 = call2('Maria')
call3 = CallMe('5448687347')
retorno3 = call3()
print(retorno, retorno2, retorno3)