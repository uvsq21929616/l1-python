import tkinter as tk

racine = tk.Tk()
racine.title("tk")


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes
        r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256
mon_canvas = tk.Canvas(racine, background="black",
                       width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

bouton_aléatoire = tk.Button(text="Aléatoire", foreground="blue",
                             font="Times" "30", command="draw_pixel")
bouton_gris = tk.Button(text="Dégradé Gris", foreground="blue",
                        font="Times" "30")
bouton_2D = tk.Button(text="Dégradé 2D", foreground="blue",
                      font="Times" "30")


def draw_pixel(i, j, color):
    mon_canvas.create_rectangle(i-1, j-1, i+1,
                                j+1, fill="color")


bouton_aléatoire.grid(row=0, column=0)
bouton_gris.grid(row=1, column=0)
bouton_2D.grid(row=2, column=0)
mon_canvas.grid(row=0, column=1, rowspan=3)
racine.mainloop()
