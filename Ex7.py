n=int(input("entrez le nombre du chevaux partants:"))
p=int(input("entrez le nombre du chevaux joués:"))
x=float(1)
y=float(1)
for i in range(n-p+1,n+1):
  x*=i
  y*=i
for i in range(1,p+1):
  y/=i
print(f"Dans l'ordre: une chance sur {x} de gagner ")
print(f"Dans le désordre: une chance sur {y} de gagner ")