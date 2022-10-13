# Mayus F10
def subsequence_occurrences(string_big: str, string_small: str, replace_movements: int) -> int:
    """
    Given a certain limit for replace movements and two strings, find the number of occurrences of the second string
    into the first, given the fact that certain replacements are available to maximize the answer

    :param string_big: The String which is traversed
    :param string_small: The subsequence string
    :param replace_movements: The limit for replacement movements to max the number of occurrences
    :return: The number of occurrences of the
    """
    all_chars = list(dict.fromkeys(string_small.split())) # Para el caso donde el string_small sea del mismo caracter dos veces, ej: 'aa'
    len_big = len(string_big)

    build = {char: [0 for _ in range(len_big)] for char in all_chars} # Diccionario para saber a que caracter nos referimos
    counter = {char: 0 for char in all_chars} # Same as above

    for i in all_chars:
        for j in range(len_big):
            build[i][j] = 1 if string_big[j] == i else 0
        counter[i] = sum(build[i])

    # El indice del caracter mas a la derecha es con string.rindex(caracter)
    # El indice del caracter mas a la izquierda es con string.index(caracter)

    # TODO diseñar los casos
    # TODO diseñar el reemplazo
    # TODO diseñar el llamado a la función (probablemente sea volver a llamarla pero con el string cortado[a:b] siendo a o b el ultimo indice cambiado

    return 0


if __name__ == '__main__':
    from sys import stdin as sin

    input1 = sin.readline()
    input2 = sin.readline()
    input3 = int(sin.readline())
    subsequence_occurrences(input1, input2, input3)
