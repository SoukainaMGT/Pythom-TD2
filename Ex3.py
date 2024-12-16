n = int(input("Entrez un nombre compris entre 10 et 20: "))
while n < 10 or n > 20:
    if n > 20:
        print("Plus petit !")
    else:
        print("Plus grand !")
    n = int(input("Entrez un nombre compris entre 10 et 20: "))

print("Merci, vous avez entré un nombre valide :", n)