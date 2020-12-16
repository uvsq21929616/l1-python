import tkinter as tk


b = int(input("taille de l'image"))


racine = tk.Tk()
racine.title("mon dessin")


CANVAS_WIDTH = b
CANVAS_HEIGHT = b
mon_canvas = tk.Canvas(racine, background="black", width=CANVAS_WIDTH,
                       height=CANVAS_HEIGHT)


def circle_blue():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="blue")


def circle_green():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="green")


def circle_black():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="black")


def circle_yellow():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="yellow")


def circle_magenta():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="magenta")


def circle_red():
    centre_x = b/2
    centre_y = b/2
    mon_canvas.create_oval(centre_x - c, centre_y - c,
                           centre_x + c, centre_y + c,
                           fill="red")


c = int(b/2)

while c > 6:
    if c % 60 == 0:
        circle_red()
    elif c % 60 == 10:
        circle_magenta()
    elif c % 60 == 20:
        circle_yellow()
    elif c % 60 == 30:
        circle_black()
    elif c % 60 == 40:
        circle_green()
    elif c % 60 == 50:
        circle_blue()
    c -= 10


mon_canvas.grid(row=0, column=0)
racine.mainloop()
