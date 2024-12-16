s=int(0)
e10=int(0)
e5=int(0)
e1=int(0)
prix=int(input("Entrez le prix du achats un par un en euros(terminée par 0):"))
while prix!=0:
  s+=prix
  prix=int(input("Entrez le prix du achats un par un en euros(terminée par 0):"))
print("La somme a payée en euros est:",s)
paye=int(input("Entrez le payement en euros:"))
s-=paye
while s!=0:
  if s>10:
    s-=10
    e10+=1
  elif s>5:
    s-=5
    e5+=1
  else:
    e1=s
    s=0
print(f"votre remise est: {e10} 10 Euros, {e5} 5 Euros, {e1} 1 Euro")