n=int(input("Entrez la valeur du n (avec n>0):"))
while n<=0:
  n=int(input("Entrez la valeur du n (avec n>0):"))
s=float(0)
for i in range(1,n+1):
  s+=1/i/i
else:
  s=s/n
print("La somme a l'ordre n est:",s)