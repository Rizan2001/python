from tkinter import*
from tkinter import ttk
meta = Tk()
meta.title("Welcome to Threads")
meta.geometry("350x200")

lbl = Label(meta, text ="THREADS FROM META", font=(("normal","20")),bg = "black",fg ="white")
lbl.place(x = 30, y = 30)
path = PhotoImage(file="C:/Users/PYTHON/Downloads/tds 1.png")
label_image = Label(meta, image = path, width = 400, height = 400)
label_image.place(x = 390,y = 1)
path2 = PhotoImage(file="C:/Users/PYTHON/Downloads/tds 3.png")
label_image = Label(meta,image = path2, width = 600, height = 400)
label_image.place(x = 290,y = 290)
path3 = PhotoImage(file="C:/Users/PYTHON/Downloads/tds 5.png")
label_image = Label(meta,image = path3, width = 700, height = 500 )
label_image.place(x = 240,y = 550)

def clicked():
    print("i am clicked")
btn = Button(meta,text="loggin", command = clicked)
btn.place(x = 570, y = 330)
entry = Entry(meta)
entry.place(x = 530,y = 580)
entry1 = Entry(meta)
entry1.place(x = 530,y = 630)
meta.mainloop()





