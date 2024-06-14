from tkinter import *
from tkinter import messagebox
def gg():
    def new_task():
        new = Toplevel()
        new.geometry('550x200+93+0')
        new.overrideredirect(1)
        new.config(background="#2e3c7b")
        e = Entry(new, textvariable=t1,background="black",foreground="yellow")
        e.pack(pady=20)
        b = Button(new, text='Add Task', command=lambda: geti(new))
        b.pack(pady=10)

    def geti(new):
        t = t1.get()
        if t == "":
            messagebox.showwarning('Error', 'Task cannot be empty!')
        else:
            var = BooleanVar() 
            c = Checkbutton(chat_area, text=t, variable=var, bg="black", fg="yellow", selectcolor="#2e3c7b")
            chat_area.config(state=NORMAL)
            chat_area.window_create(END, window=c)
            chat_area.insert(END, '\n') 
            chat_area.config(state=DISABLED)
            dic.append((t, var, c)) 
        new.destroy()  

    def delete_task():
        if not dic:
            messagebox.showwarning('Error', 'No tasks created that can be deleted')
        else:
            try:
                for task, vari, c in dic[:]:
                    if vari.get():
                        c.destroy()
                        dic.remove((task, vari, c))
            except:
                if not any(vari.get() for _, vari, _ in dic):
                    messagebox.showwarning('Error', 'No tasks selected to be deleted')
    def deg():
        root.destroy()

    root = Toplevel()
    root.title("ChatBot")
    root.geometry("550x680+100+0")
    root.resizable(0, 0)
    root.overrideredirect(1)
    root.config(background="#2e3c7b")

    dic = []
    t1 = StringVar()

    chat_area = Text(root, state=DISABLED, width=80, height=20, wrap=WORD, background="black", foreground="yellow")
    chat_area.pack(padx=10, pady=10)

    b1 = Button(root, text='New Task', command=new_task,background="purple",foreground="white")
    b1.pack(pady=10)

    b2 = Button(root, text='Delete Task', command=delete_task,background="purple",foreground="white")
    b2.pack(pady=10)

    i5 = PhotoImage(file=r"C:\Users\hi\Downloads\frame3.png")
    b4 = Button(root, image=i5, border=0, bg="#5C5C5C", command=lambda: deg())
    b4.pack(side=BOTTOM, pady=10)

    root.mainloop()
