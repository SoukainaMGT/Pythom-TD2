def saisir_liste_chaine(n):
  liste=list([])
  for i in range(1,n+1):
    ch=str(input("Entrez le chaine du charactére d'indice i:"))
    liste.append(ch)
  return liste