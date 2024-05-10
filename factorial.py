#!/usr/bin/python3
import sys


def factorielle(n):
    if n < 0:
        raise ValueError(
            "La factorielle n'est pas définie pour les nombres négatifs")
    resultat = 1
    while n > 1:
        resultat *= n
        n = n - 1
    return resultat


if len(sys.argv) != 2:
    print("Utilisation : python3 nom_du_script.py <nombre>")
    sys.exit(1)

try:
    nombre = int(sys.argv[1])
    resultat = factorielle(nombre)
    print(resultat)
except ValueError:
    print("Erreur : Veuillez fournir un entier valide en tant qu'entrée")
    sys.exit(1)
