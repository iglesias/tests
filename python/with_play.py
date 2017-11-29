# Small toy program with with block and custom context manager.

class CustomContextManager:
    def __enter__(self):
        print('Entering')

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting')

with CustomContextManager() as ccm:
    print(type(ccm))
