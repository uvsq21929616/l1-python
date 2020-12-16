import tkinter as tk
import random as rd


def draw_circle():
    centre_x = rd.randint(51, CANVAS_WIDTH - 51)
    centre_y = rd.randint(51, CANVAS_HEIGHT - 51)

    mon_canvas.create_oval(centre_x - 50, centre_y - 50,
                           centre_x + 50, centre_y + 50, fill=couleur_courante)


def draw_square():
    centre_x = rd.randint(51, CANVAS_WIDTH - 51)
    centre_y = rd.randint(51, CANVAS_HEIGHT - 51)

    mon_canvas.create_rectangle(centre_x - 50, centre_y - 50,
                                centre_x + 50, centre_y + 50,
                                fill=couleur_courante)


def draw_cross():
    centre_x = rd.randint(51, CANVAS_WIDTH - 51)
    centre_y = rd.randint(51, CANVAS_HEIGHT - 51)

    mon_canvas.create_line(centre_x - 50, centre_y, centre_x + 50, centre_y,
                           fill=couleur_courante)
    mon_canvas.create_line(centre_x, centre_y - 50, centre_x, centre_y + 50,
                           fill=couleur_courante)


def choisir_couleur():
    global couleur_courante
    couleur_courante = input("choisir une couleur\n")


racine = tk.Tk()
racine.title("mon dessin")

bouton_cercle = tk.Button(racine, text="cercle", command=draw_circle)
bouton_carre = tk.Button(racine, text="carré", command=draw_square)
bouton_croix = tk.Button(racine, text="croix", font="helvetica" "30",
                         command=draw_cross)
bouton_couleur = tk.Button(racine, text="choisir une couleur",
                           command=choisir_couleur)

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH,
                       height=CANVAS_HEIGHT, borderwidth=5,
                       relief="raised")

bouton_cercle.grid(row=1, column=0)
bouton_carre.grid(row=2, column=0)
bouton_croix.grid(row=3, column=0)
bouton_couleur.grid(row=0, column=1)
mon_canvas.grid(row=1, column=1, rowspan=3)

racine.mainloop()
