import time
from tkinter import *
from PIL import Image,ImageTk
import random
def RPS():
    class rp:
        def __init__(self):
            root= Toplevel()
            root.resizable(0,0)
            root.overrideredirect(1)
            root.wm_attributes("-transparent","#c1dde1")
            i=PhotoImage(file=r"C:\Users\hi\Downloads\forsest.png")
            i4=PhotoImage(file=r"C:\Users\hi\Downloads\frame2.png")
            i5=PhotoImage(file=r"C:\Users\hi\Downloads\frame3.png")
            i6=PhotoImage(file=r"C:\Users\hi\Downloads\lframe.png")
            l=Label(root,image=i)
            l.place(x=-2,y=-2)
            root.geometry("550x680+100+0")
            f=Frame(root,background="#000131" ,height=80,width=700)
            f.pack(side=BOTTOM,pady=3)
            b4=Button(f,image=i5,border=0,bg="#5C5C5C",command=lambda: deg(root))
            b4.place(x=(550/2)-90,y=2)
            def des():
                newwin.destroy()
            def deg(root):
                root.destroy()   
            class RPS:
                def __init__(self,re,b):
                    self.result=re
                    self.H=b
                    self.H.destroy()
                    self.result.destroy()
                    self.choice_s=Label()
                    self.choice_r=Label()
                    self.H=Label()
                    self.count1=0
                    self.count2=0
                    ii=PhotoImage(file=r"C:\Users\hi\Downloads\frame4.png")
                    self.img_sci=PhotoImage(file=r"C:\Users\hi\Downloads\scissors.png")
                    self.img_rock=PhotoImage(file=r"C:\Users\hi\Downloads\rock.png")
                    self.img_paper=PhotoImage(file=r"C:\Users\hi\Downloads\paper.png")
                    f2=Label(root,image=ii,border=0)
                    f2.pack(side=TOP,pady=80)
                    self.pane=Frame(root,bg="#000131")
                    self.pane.place(x=80,y=100)
                    self.rock_b= Button(self.pane,image=self.img_rock,width=100,height=100,border=0,command=self.giver2,bg="#000131")
                    self.rock_b.pack(side=LEFT,padx=10)
                    self.paper_b= Button(self.pane,image=self.img_paper,width=100,height=100,borderwidth=0,command=self.giver3,bg="#000131")
                    self.paper_b.pack(side=LEFT,padx=20)
                    self.scissor_b= Button(self.pane,image=self.img_sci,width=100,height=100,borderwidth=0,command=self.giver,bg="#000131")
                    self.scissor_b.pack(side=LEFT,padx=20)
                    self.pane1=Frame(root,bg="#000131")
                    self.pane1.place(x=90,y=300)
                    self.q=Label(root,text="LIVES:").place(x=50,y=20)
                    self.h=Label(root,text="SCORE").place(x=446,y=20)
                    self.pane2=Frame(root,bg="#000131")
                    self.pane2.place(x=360,y=300)
                    self.f=True
                    self.Game()
                    self.pane2.destroy()
                    self.rock_b.destroy()
                    self.paper_b.destroy()
                    self.scissor_b.destroy()
                    f2.destroy()
                    self.pane.destroy()
                    self.pane1.destroy()
                    self.pane3=Frame(root,background="#000131")
                    self.pane3.place(x=220,y=320)
                    self.H=Button(self.pane3,text="Restart",command=lambda:RPS(self.result,self.pane3),font=("",20),border=0,fg="yellow",bg="#000131")
                    self.H.pack(side=RIGHT,padx=10)
                def Disp(self,v,l,m):
                    v=v
                    x=l
                    y=m
                    a=Label(root,text=v)
                    a.place(x=x,y=y)
                    root.update()
                def Timer(self):
                    for tim in range(5,-1,-1):
                        if tim==1:
                            self.choice_s.destroy()
                        countd= Label(root, text=tim,bg="#000131",fg="yellow",font=("",20))
                        countd.place(x=270,y=320)
                        root.update()
                        time.sleep(0.5)
                def giver(self):
                    self.choice_r.destroy()
                    self.choice_r= Label(self.pane1,image=self.img_sci,bg="#000131",width=100,height=100)
                    self.choice_r.pack(side=TOP)
                    self.game=1
                    self.f=False
                def giver2(self):
                    self.choice_r.destroy()
                    self.choice_r= Label(self.pane1,image=self.img_rock,width=100,bg="#000131",height=100)
                    self.choice_r.pack(side=TOP)
                    self.game=2
                    self.f=False
                def giver3(self):
                    self.choice_r.destroy()
                    self.choice_r= Label(self.pane1,image=self.img_paper,width=100,height=100,bg="#000131")
                    self.choice_r.pack(side=TOP)
                    self.game=3
                    self.f=False
                def g_check(self,lifes,score):
                    if (self.game==self.game_c):
                        score=score+5
                    elif (self.game==1 and self.game_c==3 or self.game==2 and self.game_c==1 or self.game==3 and self.game_c==2):
                        score=score+10
                    elif(self.game==3 and self.game_c==1 or self.game==1 and self.game_c==2 or self.game==2 and self.game_c==3):
                        lifes=lifes-2
                    else:
                        lifes=lifes-1
                    return [lifes,score]
                def gcp(self):
                    val=random.choice([1,2,3])
                    if val==1:
                        self.choice_s= Label(self.pane2,image=self.img_sci,width=100,height=100,bg="#000131")
                        self.choice_s.pack(side=TOP)
                        self.game_c=1
                    elif val==2:
                        self.choice_s= Label(self.pane2,image=self.img_rock,width=100,height=100,bg="#000131")
                        self.choice_s.pack(side=TOP)
                        self.game_c=2
                    elif val==3:
                        self.choice_s= Label(self.pane2,image=self.img_paper,width=100,height=100,bg="#000131")
                        self.choice_s.pack(side=TOP)
                        self.game_c=3
                def Game(self):
                
                    stre= True
                    lifes=6
                    score=0
                    self.result=Label(root,text="")
                    while (stre):
                        self.Timer()
                        self.gcp()
                        if self.f:
                            self.game=10
                        [lifes,score]=self.g_check(lifes,score)
                        if lifes<1:
                            stre=False
                        self.Disp(lifes /2,90,20)
                        self.Disp(score,490,20)
                    self.result.config(text="You Lose",font=("",40),bg="#000131",fg="yellow")
                    self.result.place(x=180,y=500)
            def ste(stre):
                stre=True
                print(stre)
            r=Label()
            f=Label()
            RPS(re=r,b=f)
            root.mainloop()
    rp()
if __name__=="__main__":
    RPS()