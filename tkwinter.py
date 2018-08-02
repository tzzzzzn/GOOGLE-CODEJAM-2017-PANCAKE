import tkinter as t
p=t.Tk()
p.title("demo")
p.geometry("500x500")
#label
title=t.Label(text='hello world this is my app',font=("Times New Roman",25))
title.grid(column=10,row=0)
#grid
button=t.Button(text='click me',bg="red")
button.grid(column=10,row=1)
#entry
entryfeild=t.Entry(width=30)
entryfeild.grid(column=10,row=2)
textfeild=t.Text(master=p,height=10,width=30)
textfeild.grid(column=10,row=4)
p.mainloop()
