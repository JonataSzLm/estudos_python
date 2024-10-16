# class Multiplicar:
#     def __init__(self, func):
#         self.func = func
#         self._multiplier = 10

#     def __call__(self, *args, **kwargs):
#         result = self.func(*args, *kwargs)
#         return result * self._multiplier

# @Multiplicar
# def calc(x, y):
#     return x + y

# print(calc(5,2))

class Multiplicar:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def __call__(self, func):
        def interna(*args, **kwargs):
            result = func(*args, *kwargs)
            return result * self._multiplier
        return interna

@Multiplicar(5)
def calc(x, y):
    return x + y

print(calc(5,2))