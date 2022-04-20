repertoire={
    "thomas" : "0625456905",
    "sebastien" : "0780685851",
    "pierre": "0625849637",
    'henri': '0497853475',
    "paul" : "0687953412",
}
info=input("cherché: ")

def ajout_contact():
    name = input("nom du contact:")
    num= input("numero du contact: ")
    repertoire[name]=num
    return repertoire

def supr_contact(information,dico):
    del dico[information]
    print(dico)
    return "contact suprimer"

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

def recherche(info):
    if info > "0" and info<="9999999999":
        for cle,value in repertoire.items():
            if value == info:
                print(info+"est le num de"+cle)
                return cle
        return "Pas de contact a ce numero."
    else:
        num = repertoire.get(info)
        if num==None:
            return "Pas de contact a ce nom."
        else:
            print("le numero de "+info+" est "+num)
            return num

##def modifier(repertoire, info):
##    quoi=input("suprimer ou modifier: ")
##    if quoi =="suprimer":
##        del repertoire[recherche(info)]
##        return repertoire
##    else:
##        return "ok"


