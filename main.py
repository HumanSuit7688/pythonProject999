from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Progressbar
from tkinter import ttk
window = Tk()
window.title("Welcome to app")
window.geometry('450x300')

def clicked():
    # res = f"Hello, {combo.get()}"
    # lbl.configure(text=f"Good\n {res}")
    lbl.configure(text=selected.get())

lbl = Label(window, text='Hello', font=('Arial Bold', 30))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10, )
txt.grid(column=1, row=0)

btn = Button(window, text='CLICK!!!', bg='black', fg='orange', command=clicked)
btn.grid(column=0, row=10)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, 'Text')
combo.current(0)
combo.grid(column=2, row=0)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='выбрать', var=chk_state)
chk.grid(column=3)

selected = IntVar()

rad1 = Radiobutton(window, text='Python', value=1, variable=selected)
rad2 = Radiobutton(window, text='C++', value=2, variable=selected)
rad3 = Radiobutton(window, text='Java', value=3, variable=selected)
rad1.grid(column=0, row=20)
rad2.grid(column=1, row=20)
rad3.grid(column=2, row=20)

style = ttk.Style()
style.theme_use('default')
style.configure('red.Horizontal.TProgresbar', background='red')
bar = Progressbar(window, length=200, style='red.Horizontal.TProgresbar')
bar.pack()
bar.grid(column=0, row=30)



window.mainloop()