import tkinter
from tkinter import *
def CALC():
    class cal:
        def __init__(self):
            self.root=Toplevel()
            self.root.title("Calculator")
            self.root.overrideredirect(1)
            self.root.geometry("550x680+100+0")
            self.root.resizable(0,0)
            self.root.configure(bg='black')
            i4=PhotoImage(file=r"C:\Users\hi\Downloads\frame2.png")
            i5=PhotoImage(file=r"C:\Users\hi\Downloads\frame3.png")
            i6=PhotoImage(file=r"C:\Users\hi\Downloads\lframe.png")
            f=Frame(self.root,background="#000131" ,height=80,width=700)
            f.pack(side=BOTTOM,pady=3)
            b4=Button(f,image=i5,border=0,bg="#5C5C5C",command=lambda: self.deg(self.root))
            b4.place(x=(550/2)-90,y=2)
            self.equation = ""
            self.Title=Label(self.root,width=25,height=2,text="CALCULATOR",font=("arial",30),bg='black',fg='white',relief="solid")
            self.Title.pack(side=TOP)
            self.label_result=Label(self.root,width=25,height=2,text="",font=("arial",30),bg='black',fg='white',relief="solid")
            self.label_result.place(x=-1,y=70)
            Button(self.root,text="C",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#000131",command=lambda:self.clear()).place(x=9,y=155)
            Button(self.root,text="/",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#022451",command=lambda:self.show("/")).place(x=145,y=155)
            Button(self.root,text="%",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#022451",command=lambda:self.show("%")).place(x=280,y=155)
            Button(self.root,text="*",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#671465",command=lambda:self.show("*")).place(x=412,y=155)
            Button(self.root,text="7",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("7")).place(x=9,y=240)
            Button(self.root,text="8",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("8")).place(x=145,y=240)
            Button(self.root,text="9",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("9")).place(x=280,y=240)
            Button(self.root,text="-",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#671465",command=lambda:self.show("-")).place(x=412,y=240)
            Button(self.root,text="4",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("4")).place(x=9,y=330)
            Button(self.root,text="5",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("5")).place(x=145,y=330)
            Button(self.root,text="6",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("6")).place(x=280,y=330)
            Button(self.root,text="+",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="white",bg="#671465",command=lambda:self.show("+")).place(x=412,y=330)
            Button(self.root,text="1",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("1")).place(x=9,y=417)
            Button(self.root,text="2",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("2")).place(x=145,y=417)
            Button(self.root,text="3",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("3")).place(x=280,y=417)
            Button(self.root,text="0",width=13, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show("0")).place(x=7,y=503)
            Button(self.root,text=".",width=6, height=1, font=("arial",25,"bold"),bd=1,fg="black",bg="#17b9f5",command=lambda:self.show(".")).place(x=280,y=503)
            Button(self.root,text="=",width=6, height=4, font=("arial",25,"bold"),bd=1,fg="white",bg="#671465",command=lambda:self.calculate()).place(x=412,y=407)
            self.root.mainloop()
        #def des(self):
        #    newwin.destroy()
        def deg(self,root):
            self.root.destroy()
        def show(self,value):
            self.equation+=value
            self.label_result.config(text=self.equation)
        def clear(self):
            self.equation=""
            self.label_result.config(text=self.equation)
        def calculate(self):
            result = ""
            if self.equation !="":
                try:
                    result=eval(self.equation)
                except:
                    result = "error"
                    self.equation=""
            self.label_result.config(text=result)
    cal()
if __name__=="__main__":
    CALC()