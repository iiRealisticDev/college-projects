from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=19)
frm.grid()
ttk.Label(frm, text="Hello World!", width=10).grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy, width=20).grid(column=1, row=0)
# position the label and button in the frame
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.rowconfigure(0, weight=1)
root.mainloop()