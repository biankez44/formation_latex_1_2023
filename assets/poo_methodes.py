class Etoile:
    def __init__(self, masse, position, quantite_mouvement):
        self.masse = masse
        self.position = position
        self.quantite_mouvement = quantite_mouvement

    def effort(self, liste_etoiles):
            effort = [0,0,0]
            for e in liste_etoiles:
                    effort = [effort[i] + G*self.masse*e.masse*(e.position[i]-self.position[i])/dist2(self,e) for i in range(3)]
            return effort

    def deplacement_elem(self, pas, liste_etoiles):
            effort = self.effort(liste_etoiles)
            for i in range(3):
                    self.quantite_mouvement[i] += pas*effort[i]
                    self.position[i] += pas*self.quantite_mouvement[i]/self.masse