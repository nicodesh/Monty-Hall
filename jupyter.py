# Voici les lignes à exécuter dans Jupyter Notebook
# Le Notebook doit être ouvert / enregistré dans le même dossier que le module montyhall.py

%matplotlib inline
from montyhall import MontyHall

my_monty_hall = MontyHall()
my_monty_hall.plot_compare(1000)
my_monty_hall.plot_linearity([1000, 10000, 20000, 50000, 80000, 100000, 100000])