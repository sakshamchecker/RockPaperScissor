from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar
import random
import smtplib
from win import window
scorec=0
scorep=0

def ron():
    val='Rock'
    user_val.set(val)
    print('imhere')
def pa():
    val='Paper'
    user_val.set(val)
def sc():
    val='Scissor'
    user_val.set(val)
def play():
    global scorec
    global scorep
    # global rounden
    r=int(rounden.get())
    print(r)
    # print(scorep+scorec)
    if scorep+scorec < r:
        final.set('Game In Progress')
        a=user_val.get()
        a=a[0].lower()
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
                result.set('Player wins')
                scorep+=1
                score_p.set(scorep)
            elif a[0] == b[0]:
                result.set('Draw')
            else:
                result.set('Computer wins')
                scorec+=1
                score_c.set(scorec)
        if scorep+scorec ==r:
            if scorep>scorec:
                final.set('Player Wins')
            else:
                final.set('Computer Wins')

def cle():
    global scorec
    global scorep
    user_val=''
    res=''
    user_en.delete(0,'end')
    result_entry.delete(0,'end')
    cc_entry.delete(0,'end')
    scorec=0
    scorep=0
    final_dis.delete(0,'end')
    scorec_dis.delete(0,'end')
    scorep_dis.delete(0,'end')
    mail_in.delete(0,'end')
def mail():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('samplemail@domain.com','password')
    message=f'Computer Score is {scorec} and Player Score is {scorep}'
    rec=str(maili.get())
    s.sendmail('samplemail@domain.com',rec,message)
    s.close()



ro=Label(window,text='Number of Rounds',width=14,bg='black',fg='white')
ro.grid(column=0,row=0,padx=20,pady=20)
rounden=DoubleVar()
round_en=Entry(window,textvariable=rounden,width=20)
round_en.grid(column=1,row=0,pady=20,padx=20)
round_en.delete(0,'end')

user_in=Label(window,text='User',bg='black',fg='white',width=14)
user_in.grid(column=0,row=1,pady=20,padx=20)

user_val=StringVar()
rock=Button(window,text='Rock',bg='blue',fg='white',width=14,command=ron)
rock.grid(column=1,row=1,padx=20,pady=20)
paper=Button(window,text='Paper',bg='blue',fg='white',width=14,command=pa)
paper.grid(column=2,row=1,padx=20,pady=20)
scissor=Button(window,text='Scissor',bg='blue',fg='white',width=14,command=sc)
scissor.grid(column=3,row=1,padx=20,pady=20)
play=Button(window,text='Play',bg='red',fg='white',width=14,command=play)
play.grid(column=0,row=2,padx=20,pady=20)

result_label=Label(window,text='Result',bg='black',fg='white',width=14)
result_label.grid(column=0,row=3,padx=20,pady=20)
result=StringVar()
result_entry= Entry(window,textvariable=result,width=20)
result_entry.grid(column=1,row=3,padx=20,pady=20)
result_entry.delete(0,'end')

user_en=Entry(window,textvariable=user_val,width=20)
user_en.grid(column=1,row=2,pady=20,padx=20)
cc=StringVar()
cc_entry= Entry(window,textvariable=cc,width=20)
cc_entry.grid(column=2,row=2,padx=20,pady=20)
cc_entry.delete(0,'end')

clr=Button(window,text='RESTART',bg='red',fg='white',width=14,command=cle)
clr.grid(column=3,row=2,padx=20,pady=20)

scorep_lbl=Label(window,text='PlayerScore',bg='black',fg='white',width=14)
scorep_lbl.grid(column=0,row=4,pady=20,padx=20)
score_p=StringVar()
scorep_dis= Entry(window,textvariable=score_p,width=20)
scorep_dis.grid(column=1,row=4,pady=20,padx=20)
scorep_dis.delete(0,'end')

scorec_lbl=Label(window,text='ComputerScore',bg='black',fg='white',width=14)
scorec_lbl.grid(column=0,row=5,pady=20,padx=20)
score_c=StringVar()
scorec_dis= Entry(window,textvariable=score_c,width=20)
scorec_dis.grid(column=1,row=5,pady=20,padx=20)
scorec_dis.delete(0,'end')

final_lbl=Label(window,text='FINAL',bg='black',fg='white',width=20)
final_lbl.grid(column=0,row=5,padx=20,pady=20)
final=StringVar()
final_dis=Entry(window,textvariable=final,width=14)
final_dis.grid(column=2,row=5,padx=20,pady=20)
final_dis.delete(0,'end')

maili=StringVar()
mail_in=Entry(window,textvariable=maili,width=14)
mail_in.grid(column=0,row=6,pady=20,padx=20)
mail_in.delete(0,'end')
mail_button=Button(window,text='MAIL',bg='red',fg='white',width=14,command=mail)
mail_button.grid(column=1,row=6,pady=20,padx=20)

window.mainloop()