#########################################
# groupe BI 2
# Guillaume EMERDJIAN
# Victor DE BAETS
# Léa OSTER
# Maxime BOUAMRA
# https://github.com/uvsq22107719/projet_1
#########################################

### Import des librairies

import tkinter as tk

### Définitions des constantes

# Hauteur du canevas
HAUTEUR = 600
# Largeur du canevas
LARGEUR = 600

### Définitions des variables globales

### Définitions des Fonctions


### Programme principal


# Définition des widgets
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, width = LARGEUR, heigh = HAUTEUR)
bouton = tk.Button(racine, text="Configuration aléatoire")

# Placement des widgets
canvas.grid(column=0, row=0)
bouton.grid(column=0, row=1)



# Boucle principale
racine.mainloop()


taille =int(input("taille de la matrice"))
mat=[]
for i in range(taille):
    ligne=[]
    for j in range(taille):
        value = input("entier")
        if '.' not in value:
            ligne.append(int(value))

    mat.append(ligne)

print(mat)