"""Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
elementos que se encuentran en A o en B, o en ambos."""

A= {55,22,33,44,11}
B= {11,22,33,44,55,66,77}

print(A | B)


"""Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
elementos que se encuentran en A y en B"""

A={98,78,63,45,73}
B={73,45,63,78,98}

print(A & B)

"""Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
conjunto de los elementos que se encuentran en A o en B, pero no en ambos"""

A={25,36,89,14,27}
B={14,27,36,89,25,99,100}

print(A.symmetric_difference(B))


"""Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
un subconjunto de otro conjunto, B"""

A={'frutilla','manzana','pera','mandarina','banana'}
B={'manzana','pera','mandarina'}

print(A.issubset(B))

"""Dados un conjunto, A, escribe un programa en Python que imprima el número de
elementos del conjunto."""

A={2,6,9,5,7,2,3,78,95,63,10,32,45,67,89,100}

print(len(A))
