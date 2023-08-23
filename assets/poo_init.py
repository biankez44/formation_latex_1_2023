class Etoile:
    def __init__(self, masse, position, quantite_mouvement):
				# __init__ est la fonction qui permet d'initialiser notre objet
        self.masse = masse
        self.position = position
        self.quantite_mouvement = quantite_mouvement


etoile1 = Etoile(10, [0, 0, 0], [0, 0, 0])

print(etoile1.masse) # Renvoie la masse de etoile1 (ici 10)