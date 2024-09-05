#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calcule le factoriel d'un nombre entier donné.

    Parameters:
    n (int): Le nombre entier pour lequel calculer le factoriel. 
             Doit être un entier non négatif.

    Returns:
    int: Le factoriel du nombre donné. Si n est 0, retourne 1 car 0! = 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Calcul du factoriel du nombre passé en argument depuis la ligne de commande
f = factorial(int(sys.argv[1]))
print(f)
