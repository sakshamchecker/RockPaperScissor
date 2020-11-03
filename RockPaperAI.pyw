from tkinter import Tk,Button,Label,StringVar,Entry
import random
from win import window
def ro():
    val='r'
    user_val.set(val)
def pa():
    val='p'
    user_val.set(val)
def sc():
    val='s'
    user_val.set(val)
def play():
    a=user_val.get()
    c = random.randint(0, 2)
    if c == 0:
        b = 'r'
        cc.set('Computer-Rock')
    elif c == 1:
        b = 'p'
        cc.set('Computer-Paper')
    else:
        b = 's'
        cc.set('Computer-Scissor')
    if (a[0] == 'r' or a[0] == 'p' or a[0] == 's') and (b[0] == 'r' or b[0] == 'p' or b[0] == 's'):
        if (a[0] == 'r' and b[0] == 's') or (a[0] == 'p' and b[0] == 'r') or (a[0] == 's' and b[0] == 'p'):
            res.set('Player wins')
        elif a[0] == b[0]:
            res.set('Draw')
        else:
            res.set('Computer wins')
    else:
        res.set('Retry')
def cle():
    user_val=''
    res=''
    res_entry.delete(0,'end')
    cc_entry.delete(0,'end')
user_in=Label(window,text='User',bg='black',fg='white',width=14)
user_in.grid(column=0,row=0,pady=20,padx=20)

user_val=StringVar()
rock=Button(window,text='Rock',bg='blue',fg='white',width=14,command=ro)
rock.grid(column=1,row=0,padx=20,pady=20)
paper=Button(window,text='Paper',bg='blue',fg='white',width=14,command=pa)
paper.grid(column=2,row=0,padx=20,pady=20)
scissor=Button(window,text='Scissor',bg='blue',fg='white',width=14,command=sc)
scissor.grid(column=3,row=0,padx=20,pady=20)
play=Button(window,text='Play',bg='red',fg='white',width=14,command=play)
play.grid(column=0,row=1,padx=20,pady=20)

res=StringVar()
res_entry= Entry(window,textvariable=res,width=20)
res_entry.grid(column=1,row=1,padx=20,pady=20)
res_entry.delete(0,'end')

cc=StringVar()
cc_entry= Entry(window,textvariable=cc,width=20)
cc_entry.grid(column=2,row=1,padx=20,pady=20)
cc_entry.delete(0,'end')

clr=Button(window,text='RESTART',bg='red',fg='white',width=14,command=cle)
clr.grid(column=3,row=1,padx=20,pady=20)
window.mainloop()