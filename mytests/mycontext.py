class MyContextManager:
    def __enter__(self):
        print('ENTER')
        return 1234
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')


with MyContextManager() as algo:
    print('WITH', algo)