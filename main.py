##=================================================##
## @author Santiago Zuñiga, Mauren Rivera          ##
##=================================================##

import time
from random import randint
from concurrent.futures import ProcessPoolExecutor
from tests import *
from findMaxDifference import findMaxDifference, findMaxDifferenceDC


def getPercentages(i):
    """Obtiene la cantidad de números aleatorios necesarios para una secuencia

    Args:
        i (integer): Índice a comparar

    Returns:
        integer: La cantidad de números necesarios a generar
    """
    if i <= 29_000:
        return 100
    elif i <= 29_700:
        return 500
    elif i <= 29_900:
        return 1000
    elif i <= 29_950:
        return 5000
    elif i <= 29_975:
        return 15000
    else:
        return 30000


def loadTestCases(inFile="test_cases.in", outFile="test_cases.out"):
    """Carga en la clase Test los datos de prueba y sus respectivos datos esperados

    Args:
        inFile (str, optional):  Nombre archivo de casos entrada. Defaults to "test_cases.in".
        outFile (str, optional): Nombre archivo de resultados. Defaults to "test_cases.out".

    Returns:
        Test: Una instancia de la clase Test con las pruebas y resultados
    """
    t = Test()
    with open(inFile, "r") as fileIn, open(outFile, "r") as fileOut:
        fileIn.readline()  # ignore header
        for test, result in zip(fileIn, fileOut):
            case = [float(i) for i in test.split()]
            l = result.split()
            index = int(l[0])
            result = float(l[1])
            t.add(case, index, result)
    return t


def genRandomSequences(number, high=1000):
    """Generar secuencias aleatorias

    Args:
        number (integer): Longitud de la secuencia a generar
        high (int, optional): Tope de generación. Defaults to 1000.

    Returns:
        list: Secuencia con datos aleatiorios de tamaño number
    """
    return [randint(-high, high) for _ in range(number)]


def run(func, case):
    """Ejecuta el algotirmo con el caso solicitado

    Args:
        func (function): Algoritmo que se desea ejecutar
        case (list): Secuencia para ejecutar el algoritmo

    Returns:
        float: Tiempo de ejecución del algoritmo
    """
    t = time.time()
    func(case)
    return time.time()-t


def parallel(func, n=30_000):
    """Wrapper para paralelizar algoritmos

    Args:
        func (function): Algoritmo a ejecturaar
        n (integer, optional): número de ejecuciones a realizar. Defaults to 30_000.

    Returns:
        list: Lista de tamaño ñ con los tiempos de ejecución
    """
    l = []
    for i in range(n):
        l.append(run(func, genRandomSequences(getPercentages(i))))
        print(f"{func.__name__}, {i}")
    return l


def execute():
    """Paraleliza algoritmos y guarda en disco la comparación
    """
    t1 = ProcessPoolExecutor().submit(parallel, findMaxDifference)
    t2 = ProcessPoolExecutor().submit(parallel, findMaxDifferenceDC)

    with open('out.txt', "w") as file:
        for iterF, dvF in zip(t1.result(), t2.result()):
            file.write(f"{iterF} {dvF}\n")


def main():
    """Función Main, donde se ejecuta las 2 situaciones solicitadas
    """
    # 1ro
    execute()

    # 2do
    t = loadTestCases()
    t.test(findMaxDifference)
    t.test(findMaxDifferenceDC)


if __name__ == '__main__':
    main()
