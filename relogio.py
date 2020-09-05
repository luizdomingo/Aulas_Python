from tkinter import *
from time import strftime

app = Tk()
app.geometry("200x70")
app.title('Relógio Do Maldini')
app.resizable(False, False)
# relogio = Label(app, font='Helvetica 30 bold', text=strftime('%H:%M:%S'))
# relogio.pack()
btn = Button(app, font='Arial 30 bold', text=strftime('%H:%M:%S'))
btn.pack()


# def tempo():
#     agora = strftime('%H:%M:%S')
#     if agora != relogio['text']:
#         relogio['text'] = agora
#     relogio.after(100, tempo)


def tempo1():
    agora1 = strftime('%H:%M:%S')
    if agora1 != btn['text']:
        btn['text'] = agora1
    btn.after(100, tempo1)


# tempo()
tempo1()
app.mainloop()
