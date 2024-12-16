n=int(input("Entrez la valeur du n (avec n>0):"))
while n<=0:
  n=int(input("Entrez la valeur du n (avec n>0):"))
s=float(0)
for i in range(1,n+1):
  s+=1/i # s= s+1/n
print("La somme du 1/1+1/2+...+1/n est:",s)