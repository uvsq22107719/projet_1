#########################################################
# Groupe BI TD2                                         #
# Guillaume EMERDJIAN                                   #
# Victor DE BAETS                                       #
# Léa OSTER                                             #
# Maxime BOUAMRA                                        #
# https://github.com/uvsq22107719/projet_1_tas_de_sable #
#########################################################

### Import des librairies

import tkinter as tk
import random

### Définitions des constantes

HAUTEUR = 1000 # Hauteur du canevas
LARGEUR = 1000 # Largeur du canevas

### Définitions des variables globales

taille = 100 # Taille de la matrice
print("Taille de la matrice :", taille)

### Définitions des fonctions

# Configuration courante
def config_courante():
    """Crée la matrice de départ, sans sable"""
    mat = []
    for i in range(taille):
        l = [0 for i in range(taille)]
        mat.append(l)
    creer_grille(mat)
    return(mat)

# Configuration aléatoire
def config_aleatoire():
    """Crée une matrice aléatoire selon la taille définie et avec des chiffres allant de 0 à 10"""
    mat = [] # Réinitialise la matrice déjà existante
    for i in range(taille):
        l = [random.randint(0,10) for i in range(taille)]
        mat.append(l)
    print("Matrice aléatoire :\n", mat)
    creer_grille(mat)
    return(mat)

def config_predef_1():
    """Active le mode de création de grille"""
    mat = [] # Réinitialise la matrice déjà existante
    if taille == 100:
        mat_predef = open("mat_predef.txt", "r")
        for ligne in mat_predef:
            mat = ligne
    print("Matrice prédéfinie 1 :\n")
    creer_grille(mat)
    return(mat)

# Création de la grille
def creer_grille(mat):
    """Crée des rectangles à partir de la matrice générée"""
    for ligne in range(len(mat)): # Chaque ligne de la matrice
        for chiffre in range(len(mat[ligne])): # Chaque chiffre des lignes de la matrice
            if mat[ligne][chiffre] == 0: # Si le chiffre est 0, couleur blanche (pas de sable)
                # Taille des rectangles = LARGEUR/taille
                # activeoutline = "red" : bordure rouge si le rectangle est visé avec la souris
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#FFFFFF") # Pas de sable, blanc
            elif mat[ligne][chiffre] == 1: # Si le chiffre est 1, couleur qui se rapproche du jaune
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#FFFBC8") # Couleurs : code hexadécimal
            elif mat[ligne][chiffre] == 2:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#FFF796")
            elif mat[ligne][chiffre] == 3:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#FFF364")
            elif mat[ligne][chiffre] == 4: # Chiffre 4 : couleur jaune. Dernier chiffre où le sable est stable
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "yellow") # Dernier niveau stable, jaune
            elif mat[ligne][chiffre] == 5: # Chiffre 5 : instable, dégradé vers le noir
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#C8B800")
            elif mat[ligne][chiffre] == 6:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#968A00")
            elif mat[ligne][chiffre] == 7:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#645C00")
            elif mat[ligne][chiffre] == 8:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#4B4500")
            elif mat[ligne][chiffre] == 9:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#322F00")
            else:
                canvas.create_rectangle((chiffre * (LARGEUR/taille), ligne * (LARGEUR/taille)),((chiffre + 1) * (LARGEUR/taille), (ligne + 1) * (LARGEUR/taille)), activeoutline = "red", fill = "#000000") # Beaucoup de sable, noir


### Programme principal

# Définition des widgets
racine = tk.Tk()
racine.title("Tas de sable")
canvas = tk.Canvas(racine, width = LARGEUR, height = HAUTEUR)
config_courante() # Création de la grille de départ, sans sable
bouton1 = tk.Button(racine, text = "Configuration aléatoire", command = config_aleatoire) # Bouton "Configuration aléatoire" qui génère une matrice aléatoire et crée la grille
#bouton2 = tk.Button(racine, text = "Configuration prédéfinie", command = config_predef_1) # Bouton "Configuration prédéfinie" qui génère une matrice prédéfinie et crée la grille
#bouton3 = tk.Button(racine, text = "Configuration personnalisée", command = config_perso) # Bouton "Configuration personnalisée" qui permet de créer une matrice et crée la grille

# Placement des widgets
canvas.grid(column = 1, row = 0, rowspan = 3)
bouton1.grid(column = 0, row = 0)
#bouton2.grid(column = 0, row = 1)
#bouton3.grid(column = 0, row = 2)

# Boucle principale
racine.mainloop()