class MyError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    raise exception_


try:
    levantar()

except MyError as error:
    print(error)