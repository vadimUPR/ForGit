from tkinter import *
import random
#from pynput import keyboard

window=Tk()
window.title("Виселица")
window.geometry("700x200")

listsl=["абориген","самосвал","переход","таможня","компьютер","черновик","микроскоп","человек","небоскрёб"]

listpop=[0]           #количество попыток
listlet=[]            #все буквы слова
listletsh=[]          #открытые и неоткрытые буквы слова    
listCRS=[1,4]          #начальное позиционное значение букв
listzakr=[]            #закрытые буквы
setprob=set([])          #уже введённые буквы

""""""
def clicked():
    leng=len(listlet)
    lblvig.configure(text="Ещё не выиграл")
    kolzv=0
    allword=""
    newwzap=""
    word=txtN.get()  
    txtN.delete(0,END)
    lensl=len(word)

    if not(word in setprob):
        for i in range(0,leng):
            allword+=listlet[i]
            if listletsh[i]=="*":
                kolzv+=1
        if kolzv>0:
            if listpop[0]<7:
                kolzv=0
                if word!="" and listpop[0]<7:
                    if word==allword:
                        kolzv=0
                        for i in range(leng):
                            listletsh[i]=listlet[i]
                    listCRS[0]+=1  
                    listpop[0]+=1
                    lblvtr.configure(text="Использовано опыток: "+ str(listpop[0]))
                    setprob.add(word)
                    lblvod.configure(text=setprob)
                    for i in range(1,listpop[0]+1):
                        lblvod.grid(column=listCRS[0],row=listCRS[1])
                newword=""
                ww=word
                for i in range(leng):
                    newword+=listletsh[i]
                    print(newword)
                newwzap=""
                for i in range(leng):
                    if newword[i]=="*" and ww==listlet[i]:
                        newwzap+=ww
                        listletsh[i]=ww
                    else:
                        newwzap+=newword[i]
                    
                for i in range(0,leng):
                    if listletsh[i]=="*":
                        kolzv+=1
                if kolzv==0:
                    lblvig.configure(text="Ты выиграл!")
                    listpop[0]=0
                lblword.configure(text=newwzap)
            else:
                lblvig.configure(text="Ты проиграл!")
                
        else:
            lblvig.configure(text="Ты уже выиграл!")
            listpop[0]=0
    else:
        lblvig.configure(text="Уже было!")

def startvibor(word):
    word=str(word)
    leng=len(word)
    print(leng)
    del listlet[:]
    del listletsh[:]
    del listzakr[:]

    for i in range(0,leng):
        listlet.append(word[i])
        print(listlet[i])
    for i in range(0,leng):
        listletsh.append(listlet[i])
        print(listletsh[i])

    kolzakr=0
    while kolzakr<4:
        rand=int((random.random()*100)//10)
        print(rand)
        if rand>=0 and rand<leng:
            listzakr.append(listletsh[rand])
            listletsh[rand]="*"
            kolzakr+=1
    word=""
    for i in range(leng):
        print(listletsh[i])
        word+=listletsh[i]
    return word
    
def newgame():
    txtN.delete(0,END)

    zagad=""
    zagad=random.choice(listsl)

    setprob.clear()
    lblvig.configure(text="Ещё не выиграл")

    del listpop[:]
    listpop.append(0)

    lblword.configure(text="                            ")
    lblword.configure(text=startvibor(zagad))
   
zagad=random.choice(listsl)
zagadsave=zagad
zagad=startvibor(zagad)

lblpriv=Label(window, text="Сыграем в игру! Отгадай слово, которое я загадал.")         
lblpriv.grid(column=0, row=0) 

lblpriv1=Label(window, text="Вводи в текстовое поле букву или всё слово, но помни, у тебя всего 7 попыток.")         
lblpriv1.grid(column=0, row=1) 

lblvtr=Label(window, text="Использовано опыток: "+ str(listpop[0]))
lblvtr.grid(column=1,row=1)

txtN=Entry(window,width=15)                    
txtN.grid(column=0, row=2)

btn=Button(window, text="Ввод", command=clicked)
btn.grid(column=1,row=2)


lblword=Label(window, text=zagad)
lblword.grid(column=0,row=3)

lblvodd=Label(window, text="Уже введены: ")
lblvodd.grid(column=0,row=4)

lblvig=Label(window, text="Ещё не выиграл")
lblvig.grid(column=0,row=5)

btnng=Button(window,text="New game",command=newgame)
btnng.grid(column=1,row=5)

lblvod=Label(window, text="")


window.mainloop()