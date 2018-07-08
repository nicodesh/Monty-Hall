import matplotlib.pyplot as plt
import numpy as np

class MontyHall():
    """ Classe représentant une partie de Monty Hall. """
        
    def _play(self, strategy, rounds):
        """ Fonction privée pour lancer une partie de Monty Hall.
        
        Cette fonction est appelée uniquement par les autres fontions de la classe.
        
        Args:
            strategy (Int): 0 pour la stratégie "Garder", 1 pour la stratégie "Changer"
            rounds (Int): nombre de coups devant être joués
            
        """

        # Porte gagnante (ndarray)
        porte_gagnante = np.random.randint(1,4, size=(1,rounds))

        # Porte candidat (ndarray)
        porte_candidat = np.random.randint(1,4, size=(1,rounds))

        # Détermine la porte restante
        def first_round(porte_gagnante, porte_candidat):

            if (porte_gagnante == porte_candidat):
                portes = [1,2,3]
                portes.remove(porte_gagnante)
                porte = portes[np.random.randint(0,2)]
                return porte

            else:
                return porte_gagnante

        # Vectorisation de la fonction
        v_first_round = np.vectorize(first_round)

        # Génération du troisième ndarray qui contient la porte restante
        porte_restante = v_first_round(porte_gagnante, porte_candidat)

        # Choix du ndarray final modélisant le choix du candidat
        if (strategy == 1):
            porte_finale = porte_restante

        elif (strategy == 0):
            porte_finale = porte_candidat

        # Détermination du gain ou de la perte
        def final_round(porte_finale, porte_gagnante):

            if (porte_finale == porte_gagnante):
                return 1
            else:
                return 0

        # Vectorisation de la fonction
        v_final_round = np.vectorize(final_round)

        # Génération du ndarray final avec la liste des résultats
        results = v_final_round(porte_finale, porte_gagnante)
        
        # Attribution des chiffres dans des attributs en fonction de la stratégie
        if (strategy == 1):
            self.changer_results = results
            self.changer_sum = np.sum(results)
            self.changer_percent = self.changer_sum / rounds
            
        elif (strategy == 0):
            self.garder_results = results
            self.garder_sum = np.sum(results)
            self.garder_percent = self.garder_sum / rounds
        
        # Retourne la somme des gains
        return np.sum(results)
            
    def plot_linearity(self, the_array):
        """ Plot la linéarité avec un nuage de points.
        
        Chaque entrée du tableau passé en argument représente un nombre
        de coups joués. Les coups sont joués avec les deux stratégies et
        sont conservés dans deux tableau distincts.
        Ensuite, les deux tableaux de résultats sont plottés avec des points.
        
        Args:
            the_array (array): tableau donnant la liste du nombre de coups à jouer.
        
        """
        
        # Renvoie le nombre de gains sur le total des rounds demandés dans l'array
        def play_array(rounds, strategy):
            return self._play(strategy, rounds)
        
        # Vectorisation de la fonction
        v_play_array = np.vectorize(play_array, excluded=['strategy'])
        
        # Génération des deux tableaux de résultats
        garder_array = v_play_array(the_array, strategy=0)
        changer_array = v_play_array(the_array, strategy=1)
        
        # Plot des deux tableaux
        
        figure = plt.figure()
        plot = plt.scatter(the_array, garder_array)
        plot = plt.scatter(the_array, changer_array)
        
    def plot_compare(self, rounds):
        """ Plot la comparaison entre la stratégie Changer et Garder.
        
        Args:
            rounds (int): Nombre de rounds à comparer
            
        """
        
        # Lance une partie en stratégie "changer"
        self._play(1, rounds)
        
        # Lance une partie en stratégie "garder"
        self._play(0, rounds)
        
        # Plot les résultats
        figure = plt.figure()
        plot = plt.bar(
                        [1,2],
                        [
                            self.garder_sum,
                            self.changer_sum,
                        ],
                        tick_label=["Keep", "Change"]
                    )