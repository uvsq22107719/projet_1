#########################################
# groupe BI 2
# Guillaume EMERDJIAN
# Victor DE BAETS
# Lhéa OSTER
# Maxime BOUAMRA
# https://github.com/uvsq22107719/projet_1
#########################################

### Import des librairies

import tkinter as tk
import random

### Définitions des constantes

# Hauteur du canevas
HAUTEUR = 600
# Largeur du canevas
LARGEUR = 600

### Définitions des variables globales

taille = 3

### Définitions des fonctions



### Programme principal


# Définition des widgets
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, width = LARGEUR, heigh = HAUTEUR)
bouton = tk.Button(racine, text="Configuration aléatoire")

# Placement des widgets
canvas.grid(column = 0, row = 0)
bouton.grid(column = 0, row = 1)


# Boucle principale
racine.mainloop()



mat = []
ligne = []
cpt = taille
while cpt > 0:
    mat.append(random.sample(range(1,10), taille))
    cpt -= 1
print(mat)