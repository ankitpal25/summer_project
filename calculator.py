from tkinter import *

#to allow only certain certain values to be entered in entry box
def valid(inp):
    if inp!="" and inp[-1] in ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","%","."]:
        return True
    elif inp=="": return True
    else: return False

def allow():
    if ent_res.get() in ["+",".","*","-","%","","/"]:
        ent_res.delete(0,END)
    elif(ent_res.get()[-1] in ["+",".","*","-","%","/"] and ent_res.get()[-2] in ["+",".","*","-","%","/"] and len(ent_res.get())>2):
        put=ent_res.get()[:-2]
        put=put+ent_res.get()[-1]
        ent_res.delete(0,END)
        ent_res.insert(0,put)

#to highlight the button whose key is pressed on keyboard and also to call for "=" event
def fun(event):
    
    if "ERROR" in ent_res.get():
        ent_res.delete(0,END)

    if event.char=="=":
        res(event)
    if event.char in ["0","1","2","3","4","5","6","7","8","9","c"]:
        if event.char=="c":
            val.set("")
        globals()['b'+event.char].config(state=ACTIVE)
        root.after(100,lambda:globals()['b'+event.char].config(state=NORMAL))
    if event.char==".":
             bdec.config(state=ACTIVE)
             root.after(100,lambda:bdec.config(state=NORMAL))
    if event.char=="-":
             bsub.config(state=ACTIVE)
             root.after(100,lambda:bsub.config(state=NORMAL))
    if event.char=="+":
             badd.config(state=ACTIVE)
             root.after(100,lambda:badd.config(state=NORMAL))
    if event.char=="/":
             bdiv.config(state=ACTIVE)
             root.after(100,lambda:bdiv.config(state=NORMAL))
    if event.char=="%":
             bper.config(state=ACTIVE)
             root.after(100,lambda:bper.config(state=NORMAL))
    if event.char=="*":
             bmul.config(state=ACTIVE)
             root.after(100,lambda:bmul.config(state=NORMAL))
    allow()

#Enter or = key event functionality to get the answer:         
def res(event):
    br.config(state=ACTIVE)
    root.after(100,lambda:br.config(state=NORMAL))
    try:
        if "%" in val.get():
                v1=eval(val.get()[:val.get().find("%")])
                v2=eval(val.get()[val.get().find("%")+1:])
                v=v1*v2/100
        else:
                v=eval(val.get())
        if "." in str(v):
            if int((str(v))[str(v).find(".")+1:])==0:
                v=int(v)
        ent_res.delete(0,END)
        ent_res.insert(0,str(v))
    except ZeroDivisionError:
            val.set("ERROR")
            vi=val.get()
            ent_res.delete(0,END)
            ent_res.insert(0,vi)
    except:
        pass
    reg=root.register(valid)
    ent_res.config(validate="key",validatecommand=(reg,"%P"))

#Backspace button flash (function on its own)
def clear(event):
    if(ent_res.get()=="ERROR"):
        ent_res.delete(0,END)
    bs.config(state=ACTIVE)
    root.after(100,lambda:bs.config(state=NORMAL))

#what to do on clicking on the buttons on calculator
def click(event):
    global val
    text=event.widget.cget("text")
    if "ERROR" in ent_res.get():
        ent_res.delete(0,END)
    if text=="=":
        try:
            if "%" in val.get():
                v1=eval(val.get()[:val.get().find("%")])
                v2=eval(val.get()[val.get().find("%")+1:])
                v=v1*v2/100
            else:
                v=eval(val.get())
            if "." in str(v):
             if int((str(v))[str(v).find(".")+1:])==0:
                v=int(v)
            ent_res.delete(0,END)
            ent_res.insert(0,str(v))
        except ZeroDivisionError:
            val.set("ERROR")
            vi=val.get()
            ent_res.delete(0,END)
            ent_res.insert(0,vi)
        except:
            pass
    elif  text=="c":
        val.set("")
    elif text=="←":
        if(ent_res.get()=="ERROR"):
          ent_res.delete(0,END)
        if val.get()!="":
            val.set(val.get()[:-1])
    else:
        temp=val.get()
        ent_res.delete(0,END)
        ent_res.insert(0,temp+text)
    allow()
    reg=root.register(valid)
    ent_res.config(validate="key",validatecommand=(reg,"%P"))

#setting up root window and designing it 
root=Tk()
root.title("Calculator")
root.geometry("255x290+100+100")
# root.iconbitmap("C:\\Users\\Asus\\Downloads\\Tkinter Project Simple Calculator.zip\\Tkinter Project Simple Calculator\\favicon.ico")
root.resizable(False,False)
root.config(bg="#17161b")

#dynamic string which changes itself with the text entered in Entry Box 
val=StringVar()
val.set("")

#designing entry box
ent_res=Entry(root,textvar=val,font=("Calibri",20),bg="#303030",fg="white",borderwidth=0,highlightthickness=2)
ent_res.focus()# puts cursor on box at start of the app
ent_res.config(highlightbackground = "#606060", highlightcolor= "#505050")
ent_res.pack(fill=X, padx=10,pady=10)

#buttons on the keyboard

bc=Button(root,text="c",font=("Arial",15,"bold"),fg="white",bg="#3697f5",bd=1,width=4,height=1)
bc.place(x=10,y=60)
bc.bind("<Button-1>",click)#<Button-1> is actually the left click button on mouse

bdec=Button(root,text=".",font=("Arial",15,"bold"),fg="black",bg="#fad11b",bd=1,width=4,height=1)
bdec.place(x=70,y=60)
bdec.bind("<Button-1>",click)

bper=Button(root,text="%",font=("Arial",15,"bold"),fg="black",bg="#fad11b",bd=1,width=4,height=1)
bper.place(x=130,y=60)
bper.bind("<Button-1>",click)

badd=Button(root,text="+",font=("Arial",15,"bold"),fg="white",bg="#c77f14",bd=1,width=4,height=1)
badd.place(x=190,y=105)
badd.bind("<Button-1>",click)

b1=Button(root,text="1",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b1.place(x=10,y=105)
b1.bind("<Button-1>",click)

b2=Button(root,text="2",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b2.place(x=70,y=105)
b2.bind("<Button-1>",click)

b3=Button(root,text="3",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b3.place(x=130,y=105)
b3.bind("<Button-1>",click)

bsub=Button(root,text="-",font=("Arial",15,"bold"),fg="white",bg="#c77f14",bd=1,width=4,height=1)
bsub.place(x=190,y=150)
bsub.bind("<Button-1>",click)

b4=Button(root,text="4",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b4.place(x=10,y=150)
b4.bind("<Button-1>",click)

b5=Button(root,text="5",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b5.place(x=70,y=150)
b5.bind("<Button-1>",click)

b6=Button(root,text="6",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b6.place(x=130,y=150)
b6.bind("<Button-1>",click)

bmul=Button(root,text="*",font=("Arial",15,"bold"),fg="white",bg="#c77f14",bd=1,width=4,height=1)
bmul.place(x=190,y=195)
bmul.bind("<Button-1>",click)

b7=Button(root,text="7",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b7.place(x=10,y=195)
b7.bind("<Button-1>",click)

b8=Button(root,text="8",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b8.place(x=70,y=195)
b8.bind("<Button-1>",click)

b9=Button(root,text="9",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b9.place(x=130,y=195)
b9.bind("<Button-1>",click)

bdiv=Button(root,text="/",font=("Arial",15,"bold"),fg="white",bg="#c77f14",bd=1,width=4,height=1)
bdiv.place(x=190,y=240)
bdiv.bind("<Button-1>",click)

b0=Button(root,text="0",font=("Arial",15,"bold"),fg="white",bg="#2a2d36",bd=1,width=4,height=1)
b0.place(x=10,y=240)
b0.bind("<Button-1>",click)

br=Button(root,text="=",font=("Arial",15,"bold"),fg="white",bg="#196926",bd=1,width=9,height=1)
br.place(x=70,y=240)
br.bind("<Button-1>",click)

bs=Button(root,text="←",font=("Arial",15,"bold"),fg="white",bg="#02a18b",bd=1,width=4,height=1)
bs.place(x=190,y=60)
bs.bind("<Button-1>",click)

root.bind("<Key>",fun)
root.bind("<BackSpace>",clear)
root.bind("<Return>",res)

reg=root.register(valid)
ent_res.config(validate="key",validatecommand=(reg,"%P"))

root.mainloop()