import tkinter as tk
from tkinter import colorchooser


def collect_color(k):
    c_code = colorchooser.askcolor(title="Select color")
    buttons[k].config(bg=c_code[1])


my_w = tk.Tk()
my_w.geometry("410x250")  # Size of the window

n = 200  # number of buttons
i = 0  # row
j = 5  # column
buttons = []
for k in range(n):
    e = tk.Button(my_w, text=k, height=2, width=2, command=lambda k=k: collect_color(k))
    e.grid(row=i, column=j, padx=1, pady=1)
    buttons.append(e)
    j = j + 1
    if j % 5 == 0:
        i = i + 1
        j = 0
my_w.mainloop()  # Keep the window open
