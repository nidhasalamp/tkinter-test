import tkinter
from tkinter.ttk import Button
window=tkinter.Tk()
window.title("edureka")
tkinter.Label(window, text="nidha salam",font=("Arial",40)).pack()
tkinter.Label(window, text="raniya",font=("Arial",40)).pack()
tkinter.Label(window, text="nameer",font=("Arial",40)).pack()
bt= Button (window,text="Enter")
bt.pack(side=tkinter.TOP)
window.mainloop()
