from tkinter import *
from tkinter import messagebox

fenetre=Tk()

fenetre.title('Contacts')
fenetre.minsize(width=350, height=75)
fenetre.config(pady=20)


repertoire={
    "thomas" : "0625456905",
    "sebastien" : "0780685851",
    "pierre": "0625849637",
    'henri': '0497853475',
    "paul" : "0687953412",
}

label=Label(fenetre,text="Nom ou numéros: ")

def recherche():
    info=entree.get()
    print(info)
    if info > "0" and info<="9999999999":
        for cle,value in repertoire.items():
            if value == info:
                print(info+" est le num de "+cle)
                messagebox.showinfo("Contact", info+" est le numéro de "+cle)
                return cle
        return "Pas de contact a ce numero.", messagebox.showerror("Error","Pas de contact a ce numero.")
    else:
        num = repertoire.get(info)
        if num==None:
            return "Pas de contact a ce nom.", messagebox.showerror("Error","Pas de contact a ce nom.")
        else:
            print("le numero de "+info+" est "+num)
            messagebox.showinfo("Contact", "Le numéro de "+info+" est "+num)
            return num

entree=Entry(fenetre,width=30)

recherche_button=Button(fenetre, text="Chercher", command=recherche)

def ajout_contact():
    name = ajout_entree_nom.get()
    num= ajout_entree_num.get()
    if num < "0600000000":
        return "Numéro incorrect.", messagebox.showerror("Error","Numéro incorrect.")
    else:
        repertoire[name]=num
        messagebox.showinfo("Success","contact ajouté avec succès")
        return repertoire,


ajout_label=Label(fenetre,text="Ajouter un contact")
nom_ajout_label=Label(fenetre,text="Nom: ")
ajout_entree_nom=Entry(fenetre, width=10)
num_ajout_label=Label(fenetre,text="Numéros: ")
ajout_entree_num=Entry(fenetre, width=10)
ajout_button=Button(fenetre, text="Ajouter", command=ajout_contact)

def supr_contact():
    information=supr_entree_nom.get()
    del repertoire[information]
    print(repertoire)
    return "contact suprimer",messagebox.showinfo("Success","contact suprimer avec succès")

supr_label=Label(fenetre,text="Supprimer un contact")
nom_supr_label=Label(fenetre,text="Nom: ")
supr_entree_nom=Entry(fenetre, width=10)
supr_button=Button(fenetre, text="Supprimer", command=supr_contact)


def affiche():
    liste=[]
    for cle,value in repertoire.items():
        liste.append([cle,value])
    messagebox.showinfo("Contacts",liste)
    print(liste)
    return(liste)

affiche_button=Button(fenetre, text="Afficher contacts", command=affiche)



label.pack()
entree.pack()
recherche_button.pack()
ajout_label.pack(pady=20)
nom_ajout_label.pack()
ajout_entree_nom.pack()
num_ajout_label.pack()
ajout_entree_num.pack()
ajout_button.pack()

supr_label.pack(pady=20)
nom_supr_label.pack()
supr_entree_nom.pack()
supr_button.pack()

affiche_button.pack(pady=20)

















##print(supr_contact(info,repertoire))


##def recherche_contact():
##    name = input("nom du contact: ")
##    num = repertoire.get(name)
##    if num==None:
##        return "Pas de contact a ce nom."
##    else:
##        return "le numero de "+name+" est "+num
##
##def recherche_num():
##    num=input("numero du contact: ")
##    for cle,value in repertoire.items():
##        if value == num:
##            return cle
##    return "Pas de contact a ce numero."



##def modifier(repertoire, info):
##    quoi=input("suprimer ou modifier: ")
##    if quoi =="suprimer":
##        del repertoire[recherche(info)]
##        return repertoire
##    else:
##        return "ok"


fenetre.mainloop()