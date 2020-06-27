import re
import pyperclip
import random
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from PIL import ImageTk,Image
def copy():
    pyperclip.copy(text.get("1.0","end"))
def getvals(a,a1):
    n=int(a.get())
    mx=int(a1.get())
    a2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':','1','2','3','4','5','6','7','8','9','0']
    arr=[]
    for i in range(0,n):
        k =  random.randint(8,mx)
        s=""
        for j in range (0,k):
            c = random.choice(a2)
            s = s+c
        if (s.islower()):
            s = s.capitalize()
        if (any(i.isdigit() for i in s)==False):
            s = s[:-1]
            s = s + "1"
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
        if(regex.search(s) == None):
            s = s[:-1]
            s = s + "#" 
        arr.append(s)
    for i in arr:
        text.insert(END,str(i)+"\n")
tk = Tk()
icon = PhotoImage(file='icon.png')
tk.call('wm', 'iconphoto',tk._w, icon)
tk.title("Password Generator")
tk.geometry("450x700")
tk.maxsize(450,700)
tk.minsize(450,700)
lbl = Label(text="        ")
lbl.grid(row=0,column=0)
lbl = Label(text="        ")
lbl.grid(row=0,column=1)
lbl1 = Label(text = "PASSWORD GENERATOR", font="none 18 bold underline")
lbl1.grid(row=1,column=2)
lbl = Label(text="        ")
lbl.grid(row=2,column=1)
lbl = Label(text="        ")
lbl.grid(row=3,column=1)
lbl1 = Label(text = "Enter number of Passwords you want", font="none 10 bold")
lbl1.grid(row=4,column=2)
lbl = Label(text="        ")
lbl.grid(row=5,column=0)
a = IntVar()
x = Entry(tk,textvariable=a ,width= 45)
x.grid(row=6,column=2)
lbl = Label(text="        ")
lbl.grid(row=7,column=0)
lbl2 = Label(text = "Enter maximum length of the password ( min is 8 )", font="none 10 bold")
lbl2.grid(row=8,column=2)
lbl = Label(text="        ")
lbl.grid(row=9,column=0)
a1= IntVar()
y = Entry(tk,textvariable=a1 ,width = 45)
y.grid(row=10,column=2)
lbl = Label(text="        ")
lbl.grid(row=11,column=0)
lbl = Label(text="        ")
lbl.grid(row=12,column=0)
style = Style()
style.configure('W.TButton', font =
               ('calibri', 14, 'bold'), 
                foreground = 'red', background = "yellow") 
btn=Button(text="GET PASSWORDS!!",command=lambda:getvals(a,a1), style= 'W.TButton').grid(row=13,column=2)
lbl = Label(text="        ")
lbl.grid(row=14,column=0)
lbl = Label(text="        ")
lbl.grid(row=15,column=0)
lbl2 = Label(text="Generated Passwords:")
lbl2.place(x=84,y=320)
f1= Frame(height=20,width=30)
f1.grid(row=16,column=2)
text= ScrolledText(master = f1,width = 30,height = 20,wrap= WORD)
text.pack(padx=10, pady=10, fill=BOTH, expand=True)
text.grid(row=16,column=2)
Button(text="COPY", command=copy).place(x=254,y=340)
tk.mainloop()
