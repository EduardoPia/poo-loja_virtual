
from tkinter import *
from tkinter import ttk

# Crie uma janela principal
root = Tk()
root.title("Janela com Scrollbar")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for i in range(100):
    resultado = Label(second_frame, text = "Falha ao cadastrar")
    resultado.grid(row = i, column = i)

# Inicie a janela principal
root.mainloop()
