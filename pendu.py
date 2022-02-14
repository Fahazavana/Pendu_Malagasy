# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:49:05 2020

@author: Lucien
"""

info_about ="Created on Sat May 16 10:49:05 2020 \nBy Lucien\nFacebook : http://www.facebook.com/rjlucien.aina"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random  import choice


def init() :
    essais.set(10)
    nbr_lettre.set(0)
    cacher.set("Maka teny iray")
    txt1.set("Isan' ny andrana : %s"%essais.get())
    txt2.set("Mitady teny misy litera %s Ianao"%nbr_lettre.get())
    mots.set("")
    sary = tk.PhotoImage(file = "img_0.png")
    photo.config(image = sary)
    photo.image = sary


def erreur() :
    messagebox.showinfo("Fampahafantarana"," Mampidira litera ao anatin' ny : \"A...Z\" na \"a...z\"")    

def popup():
    txt_pt.set("Point : "+str(point.get()))
    popup= tk.Toplevel()
    popup.resizable(width=False, height=False)
    popup.geometry("250x100")
    popup['bg']="black"
    popup.title('Fampahafantarana')
    tk.Message(popup,fg="white",bg="black",width = "220",justify="center",text=msg.get()+"\n Le mots cherché est :\n "+mots.get()).pack()
    tk.Button(popup, text='Ok', command=popup.destroy).pack(padx=10, pady=5)
    popup.transient(main) 	  # Réduction popup impossible 
    popup.grab_set()		  # Interaction avec fenetre main impossible
    main.wait_window(popup)
    tirage.configure(state="active")
    entre.configure(state="disabled")
    init()
    



def masque(**args):
    n=len(mots.get())
    takona=""
    for j in range(n):
        takona=takona+"*"
    cacher.set(takona)

    
def tirer(*args):
    """
        Tirage d 'un mots dans data
    """
    tire= choice(data)
    tire=tire[0:len(tire)-1]
    mots.set(tire)
    masque()
    nbr_lettre.set(len(tire))
    txt2.set("Mitady teny misy litera %s Ianao"%nbr_lettre.get())
    tirage.configure(state="disabled")
    entre.configure(state="active")
    
def valider(*args):
    enter = saisie.get().upper()
    saisie.delete(0,len(enter))
    i=0
    if len(enter)!=1:
        while (ord(enter[i]) not in range(65,91)) and (i<len(enter)-1) :
            print(i,enter[i])
            i+=1        
    if (ord(enter[i]) not in range(65,91)) :
        erreur()
    else :
        enter=enter[i]
        check(enter)
        if (mots.get()==cacher.get()) :
            point.set(point.get()+2)
            msg.set("Nandresy ianao (+Isa 2)")
            sary = tk.PhotoImage(file = "nandresy.png")
            photo.config(image = sary)
            photo.image = sary

            popup()
        else :
            if essais.get()== 0 :
                msg.set("Resy Ianao (- Isa 1)")
                popup()
                     
    
def check(lettre):
    n = len(mots.get())
    teny = mots.get()
    takona = cacher.get()
    if (lettre in teny) and not (lettre in takona) :
        for i in range(n):
            if lettre==teny[i]:
                tmp1=takona[:i] ## selection jusqu' a la i-1 ème lettre
                tmp2=takona[i+1:]  ## selection de la  i ème lettre jusqu a la fin
                takona=tmp1+lettre+tmp2
        cacher.set(takona)
    else:
        nom_image = "img_"+str(10 -essais.get())+".png"
        essais.set(essais.get()-1)
        sary = tk.PhotoImage(file = nom_image)
        photo.config(image=sary)
        photo.image = sary
        txt1.set("Isan' ny andrana : %s"%essais.get())

def survey(*arg):
    tmp = entry_var.get()
    if (len(tmp)>0) and (len(mots.get())!=0):
        entre.configure(state="active")
    else :
        entre.configure(state="disabled")
        
def test(*args):
    if (len(entry_var.get())!=0) and (len(mots.get())!=0) :
        valider()
    else :
        pass




# =============================================================================
# fenetre principale
# =============================================================================

pendu = tk.Tk()
pendu.title('"Pendu" Malagasy')
point = tk.IntVar()
point.set(0)
pendu.resizable(width=False, height=False)
mots =  tk.StringVar()
msg = tk.StringVar()
nbr_lettre = tk.IntVar()
cacher = tk.StringVar()
txt1 = tk.StringVar()
txt2 = tk.StringVar()
essais = tk.IntVar()


onglet = ttk.Notebook(pendu)
onglet.pack()
o_pendu = ttk.Frame(onglet)
o_pendu.pack()
o_about = ttk.Frame(onglet)
o_about.pack()
onglet.add(o_pendu, text = 'Hilalao')
onglet.add(o_about,text = 'Mombamomba')
info = tk.Message(o_about, text = info_about, width = 300, justify = "center")
info.pack()


main = tk.Frame(o_pendu, bg = "black")
    


# =============================================================================
# Affichage
# =============================================================================
cadre0 = tk.Frame(main)
cadre0.grid(column =0,sticky ="n")
txt_pt = tk.StringVar()
txt_pt.set("Isa : "+str(point.get()))
pt_lab = tk.Label(cadre0, textvariable = txt_pt,bg="black",fg="white")
pt_lab.pack()



cadre1 = tk.Frame(main)
cadre1['bg']="black"
tirage = tk.Button(cadre1, text = "Haka teny iray", command = tirer)
tirage.grid(row = 1, column = 1,pady=5,sticky = "n")


lab1 = tk.Label(cadre1, textvariable= txt1,bg= "black",fg="white")
lab1.grid(row=2, column = 1,pady=5)



lab2 = tk.Label(cadre1,bg= "black",fg="white",  textvariable= txt2)
lab2.grid(row=3,column = 1,pady=5)


labCacher = tk.Label(cadre1, textvariable = cacher,bg= "black",font=("Consolas",20,"bold"),fg="white")
labCacher.grid(row=4,column = 1,pady=5)

# =============================================================================
# Saisie des données
# =============================================================================
entry_var = tk.StringVar()

entre = tk.Button(cadre1,text = "Alefao" ,state="disabled", command = valider )
saisie = tk.Entry(cadre1, width="6",textvariable = entry_var )
saisie.bind("<Return>",test)
entry_var.trace("w",survey)
saisie.grid(row=5, column = 1,pady=5)
entre.grid(row = 6,column = 1,pady=5)
saisie.focus_force()

cadre1.grid(row=1, column=1)


cadre2 = tk.Frame(main,border = 5)
cadre2['bg']="black"


sary = tk.PhotoImage(file = "img_0.png", )
image_p = tk.Canvas(cadre2,width = 120,height = 129)

photo = tk.Label(image_p, image = sary)
photo.place(x=0, y =0)

cadre2.grid(row = 1,column=2, sticky ="n")
image_p.pack()
init()
main.pack()
# =============================================================================
# Chargement des donner
# =============================================================================
data=[]
for teny in open("dico_mg.txt"):
    data.append(teny)

pendu.mainloop()


