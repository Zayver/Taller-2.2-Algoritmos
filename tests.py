from math import isclose
class UnitTest:
    """Clase tipo estructura para almacenar los casos de prueba
    """
    
    __slots__ = 'sequence', 'index', 'result'

    def __init__(self, sequence, index, result):
        self.sequence = sequence
        self.index = index
        self.result = result

    def __str__(self):
        return f"[{self.sequence}, {self.index}, {self.result}]"


class Test:
    """Clase que contiene todas las pruebas cargadas desde el módulo main
    """
    __slots__ = 'tests'

    def __init__(self):
        self.tests = list()

    def add(self, case, index, result):
        self.tests.append(UnitTest(case, index, result))

    def __getitem__(self, key):
        return self.tests[key]

    def test(self, func):
        for case in self.tests:
            a, b = func(case.sequence), case.result
            assert (isclose(a, b))