import tkinter as tk


def dessine_pixel_rouge(event):
    coordonnee_x = event.x
    coordonnee_y = event.y
    mon_canvas.create_rectangle(coordonnee_x, coordonnee_y, coodronnee_x+1, coordonnee_y+1)
    

racine = tk.Tk()
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
mon_canvat = tk.Canvas(racine, background="black", width= CANVAS_WIDTH, height = CANVAS_HEIGHT)
mon_canvas.grid()

mon_canvas.Bind("<Button1>", )