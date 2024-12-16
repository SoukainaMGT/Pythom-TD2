z1={}

z1["x"]=int(input("Entrez le partie réel:"))
z1["y"]=int(input("Entrez le partie imaginaire:"))

def somme_complexe(z1,z2):
  z3={}
  z3["x"]=z1["x"]+z2["x"]
  z3["y"]=z1["y"]+z2["y"]
  return z3

def produit_complexe(z1,z2):
  z3={}
  z3["x"]=z1["x"]*z2["x"]-z1["y"]*z2["y"]
  z3["y"]=z1["x"]*z2["y"]+z1["y"]*z2["x"]
  return z3

def affiche(z):
  x=z["x"]
  y=z["y"]
  print(f"{x}+{y}i")