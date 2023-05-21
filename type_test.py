from tkinter import *
import random
from tkinter import messagebox
window=Tk(className=" Typing Speed Test")
window.geometry("1000x650")
window.config(bg="black")
file1=open("words.txt","r")
words=file1.read().split("\n")
score=missed=count1=0
time=60
def giventime():
    global time,score,missed
    if time>0:
        time-=1
        timercount.configure(text=time)
        timercount.after(1000,giventime)
    else:
        startlabel.configure(text="Game Over! ")
        gameinstruction.configure(text="Typing Speed = {} wpm | Hit = {} | Miss= {} ".format(score-missed,score,missed))
        rr=messagebox.askokcancel("Game Over","Press Ok to Exit")
        if rr==True:
            exit()
    
def game(event):
    global score,missed
    if time==60:
        giventime()
    startlabel.configure(text="Continue...")
    gameinstruction.configure(text="Hit Enter after Typing the word")
    if wordentry.get()==labelforward["text"]:
        score+=1
        scorelabelcount.configure(text=score)
    else:
        missed+=1
    random.shuffle(words)
    labelforward.configure(text=words[0])
    wordentry.delete(0,END)

startlabel = Label(window,text='Typing Speed Test',font=('Impact',30),bg='black',fg='dark green')
startlabel.place(x=335, y=50)

labelforward = Label(window,text='Press enter to start',font=('arial',35),fg='green',bg="black")
labelforward.place(x=300, y=240)

scorelabel = Label(window,text='Your Score:',font=('arial',25),fg='light green',bg="black")
scorelabel.place(x=110, y=100)

scorelabelcount = Label(window,text=score,font=('arial',25),fg='light green',bg="black")
scorelabelcount.place(x=250, y=180)

labelfortimer = Label(window,text='Time Left:',font=('arial',25),fg='light green',bg="black")
labelfortimer.place(x=700, y=100)

timercount = Label(window,text=time,font=('arial',25),fg='light green',bg="black")
timercount.place(x=700, y=180)

gameinstruction = Label(window,text='Hit Enter After Typing The Word',font=('arial',15,'italic bold'),fg='white',bg="black")
gameinstruction.place(x=250, y=500)
wordentry = Entry(window, font=('arial',25,'italic bold'), bd=9, justify='center',bg="dark grey",fg="black")
wordentry.place(x=300, y=350)
wordentry.focus_set()
window.bind("<Return>",game)
mainloop()

