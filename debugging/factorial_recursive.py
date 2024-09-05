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


if __name__ == "__main__":
    try:
        # Vérifier si un argument est passé
        if len(sys.argv) < 2:
            raise ValueError(
                "Erreur : Veuillez fournir un nombre entier en argument.")

        # Convertir l'argument en entier
        n = int(sys.argv[1])

        # Vérifier que l'entier est non négatif
        if n < 0:
            raise ValueError(
                "Erreur : Le nombre doit être un entier non négatif.")

        # Calculer et afficher le factoriel
        f = factorial(n)
        print(f)

    except ValueError as e:
        print(e)
