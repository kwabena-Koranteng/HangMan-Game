from tkinter import *
import random
global count
count=0
c=-1
letters=[]
mistakes=[]
elist=["hehe.png","aye.png","bruh.png"]
def destroy(p):
    p.destroy()
    namesec()
    return None
def destroy1(q):
    q.destroy()
def destroy2(k):
    k.destroy()
    namesec2()
    return None
def destroy4(entry,x):
    global name
    name=entry.get()
    x.destroy()
    namesec1()
def destroyk(a):
    a.destroy()
    namesec1()

def LoadWords():
    filename=open("words.txt","r")
    line=filename.readline()
    wordlist=line.split()
    print()
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)

def newpage():
    window=Tk()
    window.geometry("1920x1080")
    window.title("WORD GUESING GAME")
    window.configure(bg="White")
    return window

def button():
    a=newpage()
    welcc=PhotoImage(file="Wel.png")
    s=Label(master=a,image=welcc)
    s.place(x=20,y=20,relwidth=1,relheight=1)
    label=Label(master=a,text=" ",font=("",200),bg="white smoke")
    label.pack(side=LEFT)
    Button_1=Button(master=a,text="PLAY",font=("Cooper Black",50),command=lambda :destroy(a),bg="Orange red",fg="Snow").pack(side=LEFT)
    label1=Label(master=a,text=" ",font=(" ",200),bg="white smoke")
    label1.pack(side=RIGHT)
    Button_2=Button(master=a,text="QUIT",font=("Cooper Black",50),command=lambda :destroy1(a),bg="DodgerBlue2",fg="Snow").pack(side=RIGHT)
    mainloop()
    return a
def namesec():
    m=newpage()
    hangman=PhotoImage(file="zork.png")
    c=Label(master=m,image=hangman)
    c.place(x=20,y=20,relwidth=1,relheight=1)
    label2=Label(text="",font=("Cooper Black",50),bg="ghost white",fg="Black")
    label2.pack(side=TOP)
    label1=Label(text="PLEASE ENTER YOUR NAME",font=("Cooper Black",50),bg="white",fg="black")
    label1.pack(side=TOP)
    entry=Entry()
    entry.pack(side=TOP)
    button=Button(text="NEXT",font=("Cooper Black",20),command= lambda :destroy4(entry,m),bg="White")
    button.pack(side=TOP)
    mainloop()
def namesec1():
    e=newpage()
    l=Label(master=e)
    l.place(x=1450,y=50)
    man=PhotoImage(file="louder.png")
    c=Label(master=e,image=man)
    c.place(x=20,y=20,relwidth=1,relheight=1)
    label1=Label(text="Click on next to have fun",font=("Cooper Black",50),bg="white smoke")
    label1.place(x=550,y=600)
    button=Button(text="Next",font=("Cooper Black",20),command=lambda:destroy2(e),bg="DodgerBlue2")
    button.place(x=900,y=700)
    mainloop()
    
def checker(a):
        global c
        global letters
        global check
        global elist
        global f
        check=secretword.upper()
        #print(check)
        c=c+1
      
    
        if a in secretword.upper():
            while check.count(a):
                
                letters.insert(check.index(a),a)
                m=Label(text=str(a),font=("Cooper Black",20),width=4,height=2,bg="white",fg="black")
                m.place(x=480+101*check.index(a),y=358)
                check=check.replace(a,"1",1)
        else:
            mistakes.append(a)
        guess=True
        if len(mistakes)==4 or len(letters)==len(secretword.upper()):
            destroy1(f)
            submit()
        else:
            for i in range(len(mistakes)):
                button=Button(text="",font=("",20),bg="red")
                button.place(x=200+50*i,y=200)
                a=PhotoImage(file=elist[i])
                l.configure(image=a)
        try:
            
            mainloop()
        except AttributeError:
            print("")
            
def namesec2():
    global l
    global f
    f=newpage()
    l=Label(master=f)
    l.place(x=1450,y=50)
    label=Label(f,text="Guess the word, You have 4 tries",font=("Cooper Black",40),bg="white smoke",fg="Black")
    label.place(x=500,y=200)
    k="QWERTYUIOP"
    for i in k:
        button1=Button(f,text=i,font=("Cooper Black",20),bg="white",fg="black")
        button1.place(x=480+100*k.find(i),y=600)
        button1.configure(command=lambda x=button1["text"]:checker(x))
        
    s="ASDFGHJKL"
    for i in s:
        button2=Button(master=f,text=i,font=("Cooper Black",20),bg="white",fg="black")
        button2.place(x=530+100*s.find(i),y=700)
        button2.configure(command=lambda x=button2["text"]:checker(x))
    p="ZXCVBNM"
    for i in p:
        button3=Button(master=f,text=i,font=("Cooper Black",20),bg="white",fg="black")
        button3.place(x=590+100*p.find(i),y=800)
        button3.configure(command=lambda x=button3["text"]:checker(x))
     
    wordlist=LoadWords()
    global secretword
    secretword=random.choice(wordlist)
    #print(secretword)
    v=len(secretword)
    for norma in range(v):
        entry=Text(width=9,height=3,bg="white").place(x=480+101*norma,y=358)
        
    mainloop()
   
   
                
            
                                 
                
def submit():  
    k=newpage()
    m=0
    count=0
    for letter in secretword.upper():
        if letter in letters:
            m=m+1
            count=m
    count=count-len(mistakes)
    score=round(count/len(secretword)*100)
    if score<0:
        score=0
        man=PhotoImage(file="SMH-PNG.png")
        c=Label(master=k,image=man)
        c.place(x=20,y=20,relwidth=1,relheight=1)
    elif score >=20 and score<50:
        lol=PhotoImage(file="wada.png")
        q=Label(master=k,image=lol)
        q.place(x=20,y=20,relwidth=1,relheight=1)
    elif score >=50 and score <80:
        how=PhotoImage(file="Lucky.png")
        h=Label(master=k,image=how)
        h.place(x=20,y=20,relwidth=1,relheight=1)
        
    else:
        man=PhotoImage(file="YES.png")
        f=Label(master=k,image=man)
        f.place(x=20,y=20,relwidth=1,relheight=1)                     
    label=Label(master=k,text=str(name)+ " ," + " In total, you scored "+ str(score),font=("Cooper Black",20),bg="white smoke")
    label.pack(side=TOP)
    label=Label(master=k,text="",font=("",20),bg="white smoke").pack()
    label2=Label(master=k,text="The answer was " + str(secretword),font=("Cooper Black",20),bg="white smoke")
    label2.pack(side=TOP)
    button1=Button(master=k,text="Quit",font=("Cooper Black",50),command=lambda :destroy1(k),bg="red")
    button1.place(x=910,y=300)
    file=open("Leaderboard.txt","a")
    print(str(name) + "," + str(score),file=file)
    file=open("Leaderboard.txt","r")
    list=[]
    for i in file:
        list.append((i.replace("\n","")).split(","))
    file.close()
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j][1]>list[j+1][1]:
                list[j],list[j+1]=list[j+1],list[j]        
    file=open("Leaderboard.txt","w")
    for i in list:
        print(",".join(i),file=file)
    file.close()
        
    
    mainloop()
a=button()


    
a.mainloop()
