from tkinter import *
from time import strftime

app = Tk()
relogio = Label(app, font='helvetica 120 bold', text= strftime('%H:%M:%S'))
relogio.pack()

def tempo():
    agora = strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tempo)

tempo()
app.mainloop()

