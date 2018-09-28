# Busqueda binaria
"""
Optimiza las busquedas para tablas de grandes volumenes (millones
de filas) unicamente funciona con data numerica ordenada
"""


def b_search(numeros, n_to_find, low, high):
    """
    Este metodo recibe una lista de numeros y calcula su punto medio,
    si el numero situado en el punto medio es mayor al numero buscado, se vuelve a
    ejecutar el metodo pero poniedo como final "high" al punto medio

    Y si el numero situado en el punto medio es menor al numero buscado, vuelve a
    ejecutar el metodo pero poniendo como inicio "low" al punto medio

    :param numeros: Data numerica ordenada
    :param n_to_find: Numero que se desea buscar
    :param low: Desde donde empieza la data
    :param high: Hasta donde termina la data
    :return: True or False si es que encuentra el num o no
    """
    if low > high:
        """Si el low es mayor que el high significa
        que ya busco en toda la data y no encontró"""
        return False

    # calculando el punto medio
    mid = int((low + high) / 2)

    if numeros[mid] == n_to_find:
        """
        Si el numero coincide con el numero buscado retorna True, 
        sino seguira buscando y dividiendo la lista por la mitad
        superior o inferior segun corresponda
        """
        return True
    elif numeros[mid] > n_to_find:
        return b_search(numeros, n_to_find, low, mid - 1)
    else:
        return b_search(numeros, n_to_find, mid + 1, high)


# Listado de numeros de prueba (aqui van las millones de filas)
nums = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 38, 45, 49, 51, 60]
n_to_find = int(input("Que número quieres buscar: "))

r = b_search(nums, n_to_find, 0, len(nums) - 1)

# if r == true: el numero si existe
if r:
    print("el numero SI existe")
else:
    print("el numero NO existe")

