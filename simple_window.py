import tkinter
from tkinter.ttk import Button
window=tkinter.Tk()
window.title("edureka")
label=tkinter.Label(window, text="nidha salam",font=("Arial",40)).pack()
bt= Button (window,text="Enter")
bt.pack(side=tkinter.TOP)
window.mainloop()
