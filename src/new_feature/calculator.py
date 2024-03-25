class NotANumberException(Exception):
    pass


class Calculator:
    def __init__(self):
        print("hello this is the instance")

    def sum(self, a, b):
        if type(b) is not int:
            raise NotANumberException()
        return a - b


