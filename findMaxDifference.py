from math import inf
def findMaxDifference(S):
    """Algoritmo para encontrar la máxima iésima-diferencia en una secuencia. Secuencia donde debe
    tener todos elementos con el operador + y - definido

    Args:
        S (list): Secuencia para ejecutar el algoritmo

    Returns:
        number: Máxima iésima-diferencia encontrada por el algoritmo
    """
    maxDiff = -inf
    for index in range(0, len(S)):
        countLeft = 0
        countRight = 0
        for l in range(index-1, -1, -1):
            countLeft += S[l]
        for h in range(index+1, len(S)):
            countRight += S[h]

        diff = countLeft - countRight

        if diff > maxDiff:
            maxDiff = diff
    return maxDiff


def countMaxDifference(S, q):
    """Contar las diferencias dado un pivote

    Args:
        S (list): Secuencia para realizar el conteo
        q (integer): pivote, por donde se cuenta hacia la derecha o izquiera la diferencia

    Returns:
        number: Diferencia entre la izquierda del pivote q y la derecha sin exluyéndolo
    """
    countLeft = 0
    countRight = 0
    for l in range(q-1, -1, -1):
        countLeft += S[l]
    for h in range(q+1, len(S)):
        countRight += S[h]
    return countLeft-countRight


def findMaxDifferenceAux(S, low, high):
    """Wrapper para el algoritmo de dividir y vencer 'findMaxDifferenceDC'

    Args:
        S (list): secuencia a realizar el algoritmo
        low (integer): Límite inferior
        high (integer): Límite superior

    Returns:
        number: Máxima diferencia de la secuencia S
    """
    if high <= low:
        return countMaxDifference(S, low)
    else:
        q = (low+high)//2
        left = findMaxDifferenceAux(S, low, q)
        right = findMaxDifferenceAux(S, q+1, high)
        return max(left, right)


def findMaxDifferenceDC(S):
    """Algoritmo tipo dividir y vencer para encontrar la máxima iésima-diferencia. Secuencia donde debe
    tener todos elementos con el operador + y - definido

    Args:
        S (list): Secuencia para realizar el algoritmo

    Returns:
        number: Máxima iésima-diferencia encontrada por el algoritmo
    """
    return findMaxDifferenceAux(S, 0, len(S)-1)