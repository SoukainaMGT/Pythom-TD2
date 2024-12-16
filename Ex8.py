def longueur_chaine(ch):
  c=0
  for i in ch:
    c+=1
  return c

ch=input("Entrer une chaine de caractères :")
print("la longeur de la chaine est:", longueur_chaine(ch))