def trier_liste_chaine(L,n):
  c=1
  while c!=0:
    c=0
    for i in range(0,n-1):
      if L[i]>L[i+1]:
        L[i],L[i+1]=L[i+1],L[i]
        c+=1
  return(L)