class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self) -> None:
        print('INIT')
        self.tema = 'Dark'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Light'
    print(as1.tema)
    as2 = AppSettings()
    print(as2.tema)
