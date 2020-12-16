import tkinter as tk

racine = tk.Tk()
racine.title("un titre")
label = tk.Label(racine,text="Un texte dans ma fenêtre",font=("helvetica","6"))
label.grid()

racine.mainloop()
