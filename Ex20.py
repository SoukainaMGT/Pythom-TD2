liste_des_stagaires=[]
liste_des_matières=[]
list_des_notes=[]

n_stagaires=int(input("Entrez le nombre du stagaires:"))
for i in range(1,n_stagaires+1):
    stagaire={}
    stagaire["CodeInscription"]=int(input(f"Entrez le code d'inscription du stagaire {i}:"))
    stagaire["Nom"]=str(input(f"Entrez le nom du stagaire {i}:"))
    stagaire["Prénom"]=str(input(f"Entrez le prénom du stagaire {i}:"))
    stagaire["Adresse"]=str(input(f"Entrez l'adresse du stagaire {i}:"))
    stagaire["Filière"]="TDI"
    liste_des_stagaires.append(stagaire)

n_matières=int(input("Entrez le nombre du matières:"))
for i in range(1,n_matières+1):
    matière={}
    matière["CodeMatière"]=i
    matière["NomMatière"]=str(input(f"Entrez le nom du matière {i}:"))
    matière["Coefficient"]=int(input(f"Entrez le coefficient du matière {i}:"))
    while matière["Coefficient"]<1 or matière["Coefficient"]>5:
        matière["Coefficient"]=int(input("Le coefficient doit etre entre 1 et 5:"))
    liste_des_matières.append(matière)

for i in liste_des_stagaires:
    for j in liste_des_matières:
        note={}
        note["CodeInscription"]=i["CodeInscription"]
        note["CodeMatière"]=j["CodeMatière"]
        note["note"]=int(input(f"Entrez le note du stagarire {note['CodeInscription']} dans le matière {note['CodeMatière']}:"))
        while note["note"]<0 or note["note"]>20:
            note["note"]=int(input("Le note doit etre compris entre 0 et 20:"))
        list_des_notes.append(note)

list_des_notes_totale=[]
note_du_majorant=0
for stagaire in liste_des_stagaires:
    note_totale={}
    note_totale["CodeInscription"]=stagaire["CodeInscription"]
    note_totale["note"]=0
    for matière in liste_des_matières:
        for note in list_des_notes:
            if note["CodeInscription"]==stagaire["CodeInscription"]:
                if note["CodeMatière"]==matière["CodeMatière"]:
                    note_totale["note"]+=matière["Coefficient"]*note["note"]
    if note_totale["note"]>note_du_majorant or note_du_majorant==0:
        note_du_majorant=note_totale["note"]
    list_des_notes_totale.append(note_totale)
for note_totale in list_des_notes_totale:
    if note_totale["note"]==note_du_majorant:
        print(f"Le majorant du class est l'etudiant avec code d'inscription {note_totale['CodeInscription']} et le note totale {note_totale['note']}")

CodeInscription_Chercher=int(input("Entrez le code d'inscription du stagaire d'ou en cherche le bulletin des notes:"))

for matière in liste_des_matières:
    for note in list_des_notes:
        if note["CodeInscription"]==CodeInscription_Chercher:
            if note["CodeMatière"]==matière["CodeMatière"]:
                print(f"Le note du matière {note['CodeMatière']} est {note['note']}")

list_des_moyennes=[]
for stagaire in liste_des_stagaires:
    moyenne={}
    moyenne["CodeInscription"]=stagaire["CodeInscription"]
    moyenne["note"]=0
    for matière in liste_des_matières:
        for note in list_des_notes:
            if note["CodeInscription"]==stagaire["CodeInscription"]:
                if note["CodeMatière"]==matière["CodeMatière"]:
                    moyenne["note"]+=matière["Coefficient"]*note["note"]
    moyenne["note"]/=len(liste_des_matières)
    list_des_moyennes.append(moyenne)
for moyenne in list_des_moyennes:
    print(f"Le stagaire avec code d'inscription {moyenne['CodeInscription']} a le moyenne {moyenne['note']}")