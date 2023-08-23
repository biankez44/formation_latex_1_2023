def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(addition(1, 2, 3)) # Affiche 6

def afficher_noms(**kwargs):
    for nom, age in kwargs.items():
        print(f"{nom} a {age} ans")

afficher_noms(Alice=25, Bob=30, Claire=27)
# Affiche :
# Alice a 25 ans
# Bob a 30 ans
# Claire a 27 ans