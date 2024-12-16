n=int(input("Entrez un nombre n (avec n>0):"))
while n<=0:
  n=int(input("Entrez un nombre n (avec n>0):"))
f=int(1)
for i in range(1,n+1):
  f=f*i
print("le factorielle du n est:",f)