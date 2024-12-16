def estVoyelle(c):
  if c=="A" or c=="E" or c=="I" or c=="O" or c=="U" or c=="Y" or c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="y":
    return True
  else:
    return False
ch=str(input("Entrez une phrase:"))
c=0
for i in ch:
  if estVoyelle(i)==True:
    c+=1
print(f"Le nombre du voyelles dans cette phrase est {c}")