import tkinter as tk


racine = tk.Tk()
racine.tilte("mon dessin")

bouton_cercle = tk.Button(racine, text="cercle")
bouton_carre = tk.Button(racine, text="carré")
bouton_croix = tk.Button(racine, text="croix")
bouton_couleur = tk.Button(racine, text="choisir une couleur")

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background="black", width= CANVAS_WIDTH, height=CANVAS_HEIGHT)

bouton_cercle.grid(row=1, column=0)
bouton_carre.grid(row=2, column=0)
bouton_croix.grid(row=3, column=0)
bouton_couleur.grid(row=0, column=1)

