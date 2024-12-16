def getIndice(ch,e):
  ind=0
  for i in ch:
    ind+=1
    if i==e:
      return ind
    
  else:
    return -1
ch = input("Donner une chaîne de caractères : ")

indice = getIndice(ch, e)
print("L'indice positif de la première occurrence du caractère '{}' est : {}".format(e, indice))
