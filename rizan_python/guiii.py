from tkinter import*
user=Tk() 
user.title("tommy")
lbl=Label(user,text="M R COMPANY",bg = "grey",fg = "black",font=(("palatino","20")))
lbl.place(x=20,y=20)
path =PhotoImage(file="C:/Users/Python/Downloads/porsche.png")
porsche_image = Label(user, image = path, width = 700, height = 600)
porsche_image.place(x = 1000,y = 1000)


path2 = PhotoImage(file = "C:/Users/Python/Downloads/graphic porsche.png")
porsche_image2 = Label(user,image = path2,width = 700,height = 500 )
porsche_image2.place(x = 300, y = 300)
user.geometry("500x500")
user.mainloop()
